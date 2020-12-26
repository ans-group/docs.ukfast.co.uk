# VM Level Backups
If you have a virtualised environment with backups, there is a good chance you are using VM level backups.

This means backups are done at the VM container level, rather than OS level.

This is done by the backup software liaising with your Hyper-V or VMWare environment to backup the virtual machine disks and configuration files of the VMs in scope of the backup.

To ensure a consistent copy of the virtual machine is taken, a snapshot (in VMWare) or a checkpoint (in Hyper-V) is taken of the VM first.

This begins a quiesce operation against the VM to commit any data waiting to be written to the disk and directs any new writes to a temporary file (called a delta file). This allows the backup application to backup the disk whilst no changes are being made, whilst the VM is still online and running.

Once the backup has completed, a consolidation process is started to move any of the writes to the temporary delta file back into the virtual disks of the VM.