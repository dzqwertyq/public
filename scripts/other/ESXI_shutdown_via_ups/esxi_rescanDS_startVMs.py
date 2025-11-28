import paramiko
import datetime
import traceback
from re import sub
from time import sleep
from wakeonlan import send_magic_packet

# params Synology
synHost = 'ipaddr'
synUser = 'sysadmin'
synSecret = 'PWD'
synPort = 22
# params ESXI
esxiHost = 'ipaddr'
esxiUser = 'root'
esxiSecret = 'PWD'
esxiPort = 22
vmStartNames = '"Veeam|SQL"'
log_path = "C:\\Program Files (x86)\\Eaton\\IntelligentPowerProtector\\configs\\actions\\"

# wait time to start VMs after ds rescan, sec
waittime = 60
# wait before powerOn next VM, sec
powerOnDelay = 20

def logWrite(logStr="*****"):
    now = datetime.datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    str = now + ': ' + logStr + '\n'
    paramFile = log_path + 'esxi_log.txt'
    file = open(paramFile, 'a')
    file.write(str)
    file.close()

def sshExecCmd(ssh_connection, cmd, log_cmd_text="", debug_param=False):
    if log_cmd_text == "":
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
    if debug_param == True:
        print(data)
    return data

def ssh_connect(addr, uname, pwd, port, disable_alg=False):
    log = "Connecting: " + addr
    logWrite(log)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if disable_alg:
            ssh.connect(hostname=addr, username=uname, password=pwd, port=22,
                        banner_timeout=10, auth_timeout=10,
                        disabled_algorithms={'keys': ['rsa-sha2-256', 'rsa-sha2-512']})
        else:
            ssh.connect(hostname=addr, username=uname, password=pwd, port=22)
        log = "Connected: " + addr
        logWrite(log)
        return ssh
    except Exception as e:
        log = ('Error: ' + traceback.format_exc())
        logWrite(log)
        # raise e
        return 0

def check_synology():
    ssh = ssh_connect(synHost, synUser, synSecret, synPort, True)
    if ssh == 0:
        logWrite("Destination host is unreachable via ssh")
        return (0)
    else:
        return (1)

def rescanDataStore(ssh):
    cmd = 'esxcli storage core adapter rescan -a'
    sshExecCmd(ssh, cmd)
    logWrite("datastore rescan done... wait 60 sec...")
    sleep(waittime)

def powerOnVMs(ssh, vmStartNames=""):
    delim = '":"'
    cmd = "vim-cmd vmsvc/getallvms | sed -e '1d' -e 's/ \[.*$//' | awk '$1 ~ /^[0-9]+$/ {print $1" + delim + "substr($0,8,80)}' | grep -i -E " + vmStartNames
    VMSData = sshExecCmd(ssh, cmd)
    VMSData = sub("^\s+|\n|\r|\s+$", '', VMSData)
    VMSData = VMSData.split(" ")
    vmsIdList = []
    for str in VMSData:
        if str != '':
            str = str.split(":")
            vmsIdList.append(str[0].strip())

    for vmId in vmsIdList:
        cmd = "vim-cmd vmsvc/power.on " + vmId
        sshExecCmd(ssh, cmd)
        sleep(powerOnDelay)

###Script
logWrite()
logWrite("script started, check if Synology is up...")

# Synology
ssh = check_synology()
while ssh == 0:
    send_magic_packet('90.09.d0.21.d0.f9')
    logWrite("send_magic_packet('90.09.d0.21.d0.f9')")
    sleep(waittime)
    ssh = check_synology()
    logWrite("Sleep 60 sec...")

logWrite("Synology online, try to connect ESXi and start VMs...")
ssh = ssh_connect(esxiHost, esxiUser, esxiSecret, esxiPort, False)

rescanDataStore(ssh)
powerOnVMs(ssh, vmStartNames)
# if not started, try to start
rescanDataStore(ssh)
powerOnVMs(ssh, vmStartNames)
