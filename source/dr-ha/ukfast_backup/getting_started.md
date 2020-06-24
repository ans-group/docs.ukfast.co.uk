# Getting Started

UKFast Backup can be managed by selecting the server you want to manage within [MyUKFast](https://www.ukfast.co.uk/myukfast.html) and selecting "Backup" from the tab menu.

![connect](files/backup_overview.png)

**Overview** provides information on your total, used and available backup quota and provides quick access to perform a full restore.

**Running jobs** is only visible when a backup or restore job is currently being processed.

```eval_rst
.. warning::
  Please note that Windows backups must wait for a system state to run on the client before files will begin to process, this often takes up to 20 minutes.
```

## Default includes and excludes

UKFast Backup comes pre-configured with a default backup schedule which includes all data from mounted disks and excludes certain temporary files and log files including:

* Linux includes
  * `/`


* Linux excludes
  * `/proc`
  * `/sys`
  * `/tmp`
  * `/var/tmp`


* Windows includes
  * `[A-Z]:/`


* Windows excludes
  * `[A-Z]:/System Volume Information`
  * `[A-Z]:/$recycle bin`
  * `hiberfil`
  * `[A-Z]:/pagefile.sys`
  * `[A-Z]:/Windows/Temp`
  * `[A-Z]:/Windows/Installer`

You can create additional rules within the [backup schedule](/dr-ha/ukfast_backup/backup_schedule.html).

```eval_rst
  .. title:: Getting started with UKFast Backup
  .. meta::
     :title: Getting started with UKFast Backup | UKFast Documentation
     :description: Managing UKFast Backup through MyUKFast
     :keywords: ukfast, backup, files, folders, recovery
