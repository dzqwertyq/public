import paramiko
#from os import getcwd
import datetime
import traceback
from re import sub
from time import sleep

#params Synology
synHost = 'ipaddr'
synUser = 'LOGIN'
synSecret = 'PWD'
synPort = 22
#params ESXI
esxiHost = 'ippaddr'
esxiUser = 'PWD'
esxiSecret = 'LOGIN'
esxiPort = 22
vmExcludeName = 'EatonSrv'
log_path = "C:\\Program Files (x86)\\Eaton\\IntelligentPowerProtector\\configs\\actions\\"

#wait time to shutdown VMs sec
waittime = 60

def logWrite(logStr="*****"):
    now = datetime.datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    str = now +': '+logStr + '\n'
    paramFile = log_path+'esxi_log.txt'
    file = open(paramFile, 'a')
    file.write(str)
    file.close()

def sshExecCmd(ssh_connection, cmd, log_cmd_text="", debug_param=False):
    if log_cmd_text=="":
        log = "Execute: " + cmd
        logWrite(log)
    else:
        log = "Execute: " + log_cmd_text
        logWrite(log)
    stdin, stdout, stderr = ssh_connection.exec_command(cmd)
    data = stdout.read() + stderr.read()
    data = data.decode()
    log = "Execute response: " + data
    logWrite(log)
    if debug_param==True:
        print(data)
    return data

def ssh_connect(addr, uname, pwd, port, disable_alg=False):
    log = "Connecting: "+addr
    logWrite(log)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if disable_alg:
            ssh.connect(hostname=addr, username=uname, password=pwd, port=22,
                        banner_timeout=10,auth_timeout=10, disabled_algorithms={'keys': ['rsa-sha2-256', 'rsa-sha2-512']})
        else:
            ssh.connect(hostname=addr, username=uname, password=pwd, port=22)
        log = "Connected: " + addr
        logWrite(log)
        return ssh
    except Exception as e:
        log = ('Error: ' + traceback.format_exc())
        logWrite(log)
        #raise e
        return 0

###Script
logWrite()
logWrite("started shutdown script")

#Synology
ssh = ssh_connect(synHost, synUser, synSecret, synPort, True)
if ssh == 0:
    logWrite("Destination host is unreachable via ssh")
else:
    cmd = 'echo '+synSecret+' | sudo -S shutdown'
    cmd_log = 'echo pwd | sudo -S shutdown'
    sshExecCmd(ssh, cmd, cmd_log)
    ssh.close()
    logWrite("connection closed")

#ESXi VMs
ssh = ssh_connect(esxiHost, esxiUser, esxiSecret, esxiPort, False)
if ssh == 0:
    logWrite("Destination host is unreachable via ssh")
else:
    cmd = 'esxcli vm process list | grep -e "Display Name" -e "World ID"' # grep -e "Display Name" -e "World ID"
    vmsData = sshExecCmd(ssh, cmd)
    #get worldId`s for VMs from response
    vmsData = sub("^\s+|\n|\r|\s+$", '', vmsData)
    vmsData = vmsData.split("   ")
    vmsIdList = []
    i = 0
    for str in vmsData:
        if i == 0:
            str = str.split(":")
            vmID = str[1].strip()
        if i == 1:
            str = str.split(":")
            vmName = str[1].strip()
            if vmName != vmExcludeName:
                vmsIdList.append(vmID)
            i = -1
            vmID=''
            vmName=''
        i = i+1

    for vmID in vmsIdList:
        logWrite("VM soft shutdown: "+vmID)
        cmd = 'esxcli vm process kill --type=soft --world-id='+vmID #–type = [soft, hard, force]
        sshExecCmd(ssh, cmd)

    #if not offline yet - wait 2 min try to shutdown hard
    logWrite("wait...")
    sleep(waittime)
    logWrite("run...")
    for vmID in vmsIdList:
        logWrite("VM hard shutdown: "+vmID)
        cmd = 'esxcli vm process kill --type=hard --world-id='+vmID #–type = [soft, hard, force]
        sshExecCmd(ssh, cmd)

#wait 2 min and shutdown ESXI host
logWrite("wait...")
sleep(waittime)
logWrite("run...")
sshExecCmd(ssh, '/sbin/shutdown.sh && /sbin/poweroff')
