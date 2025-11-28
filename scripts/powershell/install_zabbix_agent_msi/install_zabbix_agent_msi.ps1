$ifInstalled = Get-Service -name 'zabbix agent*'
$msiexec = 'msiexec.exe'
$run_path = $MyInvocation.MyCommand.Path | Split-Path -Parent

$install_path = 'C:\Program Files\Zabbix Agent 2\'
$agentName  = 'zabbix_agent2-6.4.8-windows-amd64-openssl.msi'
$configName = 'zabbix_agent2.conf'

$agentF = $run_path+'\'+$agentName
$confF = $run_path+'\'+$configName
#additional scripts if needed
$scrF1  =$run_path+'\cputemp.ps1'
$scrF2  =$run_path+'\ssd870.ps1'
$scrF3  =$run_path+'\ssd970.ps1'


if ($ifInstalled -eq $null)
{
#install
$mkdir = Test-Path -Path $install_path
if ($mkdir -ne $true){New-Item -Path $install_path -ItemType Directory}
Copy-Item -Path $agentF -Destination $install_path
#additional scripts if needed
Copy-Item -Path $scrF1 -Destination $install_path
Copy-Item -Path $scrF2 -Destination $install_path
Copy-Item -Path $scrF3 -Destination $install_path

$installArg = '/i "C:\Program Files\Zabbix Agent 2\zabbix_agent2-6.4.8-windows-amd64-openssl.msi" server=SERVERADDR sport=10050 iport=10050 serveractive=SERVERADDR rmtcmd=0 /qn'
Start-Process -FilePath $msiexec -ArgumentList $installArg -Wait
Start-Sleep -s 5
Stop-Service -Name 'Zabbix Agent*'
Copy-Item -Path $confF -Destination $install_path
Start-Sleep -s 1
Start-Service -Name 'Zabbix Agent*' 
}
else 
{
#stop service and update config file
Stop-Service -Name 'Zabbix Agent*'
Copy-Item -Path $confF -Destination $install_path
Start-Sleep -s 1
Start-Service -Name 'Zabbix Agent*'
}
#check if install file exist -> rm
$install_path=$install_path+$agentName
$instFile = Test-Path -Path $install_path
if ($instFile -eq $true){Remove-Item $install_path}
