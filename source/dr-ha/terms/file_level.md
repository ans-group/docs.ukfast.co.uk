# File Level Backups

File level backups are backups that are done at the Operating System level, through a backup agent installed on the server.

Running a file level backup backs up all directories and files in scope of the backup.

For Windows servers, by default this utilises VSS to access and backup files that are in use and locked by users or the operating system. VSS is used as part of the System State backup also, which is taken as part of a file level backup. The System State backup is the portion of the backup that backups up essential parts of the Windows Operating system if a bare metal restore was required. This includes elements of Windows such as boot files, system files and the registry.

```eval_rst
   .. title:: File Level Backups
   .. meta::
      :description: File Level Backups | UKFast Documentation
      :keywords: ukfast, backups, terminology, commvault, bacula, dpm
```