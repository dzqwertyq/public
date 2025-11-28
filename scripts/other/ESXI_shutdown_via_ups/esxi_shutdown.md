# esxi_shutdown
Script to shutdown standalone ESXi host.
Script must be placed on VM (managing-VM) on managed host.
Login via ssh (host SSH must be on).
After loging script will search for VMs, filter VM by name in param "vmExcludeName", and shutdown SOFT all VMs, excluding filtered one.
After 1 min wait it will search for VMs, filter VM by name in param "vmExcludeName", and shutdown HARD all VMs (if any), excluding filtered one.
After 1 min host will be powered off.
Tested with ESXi 6.7.

For personal usage added shutdown of Synology NAS.
Login via SSH, then poweroff Synology.
Synology SSH must be on.

Connection params placed inside py file.