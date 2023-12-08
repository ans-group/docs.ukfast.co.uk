# FastDesk Backup Policies

UKFast FastDesk backups are based on enterprise grade Commvault technology and software. Backups are handled in two ways. They are either VM Level or File Level.

```eval_rst
.. note::

  The backup and recovery system uses agents to interface with file systems and applications to facilitate the transfer of data from production systems to the protected environment.

```
## VM Level Backups

VM Level backups are done at the VM container level, rather than OS level. This is done by the backup software liaising with your VMware environment to take an incremental backup. An incremental backup contains only data that is new or has changed since the last backup, regardless of the type. On average, incremental backups consume far less media and place less of a burden on resources than full backups.

To ensure a consistent copy of the virtual machine is taken, a snapshot is taken of the VM first. This begins a quiesce operation against the VM to commit any data waiting to be written to the disk and directs any new writes to a temporary file (called a delta file). This allows the backup application to backup the disk whilst no changes are being made, whilst the VM is still online and running. Once the backup has completed, a consolidation process is started to move any of the writes to the temporary delta file back into the virtual disks of the VM.

## File Level Backups

File level backups are backups that are done at the Operating System level, through a backup agent installed on the server. Running a file level backup backs up all directories and files in scope of the backup. This allows us to back up and restore individual files and folders.

## Individual User Data

For individual users, their home drives (`appdata`, `desktop`, `my documents`, `downloads`, `etc.`) are currently file-level meaning the entire VM does not need to be restored and we are able to go back and restore files. The only caveat to this is the size of the folders in question. If the folder/file size is very large, we may recommend completing a VM level restore instead as the File Level restores are much slower. For the user's home drives, this is currently done using incremental backups at the end of each day between 12am and 4am. A synthetic full back up is taken on the 7th day.

Synthetic full backups consolidate the data from the latest full backup or synthetic full backup together with any subsequent incremental backups into one archive file, instead of reading and backing up data directly from the client computer. Since synthetic full backups do not back up data from the client computer, this operation imposes no load on the client computer. The backups are then stored for 28 days.

## DB/File/App Server Data

For DB/File/App servers, this is a VM level backup so it is backing up the entire VM meaning if we needed to restore then it would be the entire VM. The policy for this is the same as the File Level ones where an incremental backup is taken once a day (between 10pm and 4am) and a full back up is then taken on the 7th day.

## Microsoft SQL Data

SQL backups will be managed via a maintenance plan, but the onus is on the customer to ensure SQL maintenance plans are working effectively. The customer will select a location on the VM, and SQL will write to it however often and store it as a `.bak` file. As stated above, UKFast will back up the VM. We would recommend that SQL backups are set to finish by 12am. This will make sure the backups finish before the VM is then backed up later (From around 12am - 4am).

```eval_rst
.. note::

  If you require a deviation from any of polices above, please contact the FastDesk support team on 0800 923 0617.

```

```eval_rst
   .. title:: Backup Policy | FastDesk: Backup Policies Documentation
   .. meta::
      :title: FastDesk Backup Policies | ANS Documentation
      :description: Guide on the different FastDesk Backup Policies
      :keywords: FastDesk, Citrix, ukfast, VDI, Citrix Receiver, Windows, Workspace Application, File, Change, VM, Web, Portal, Commvault, SQL
```
