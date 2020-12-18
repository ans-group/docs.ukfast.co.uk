# Linux Database Servers

```eval_rst
   .. title:: DR | Linux Database Server Backups
   .. meta::
      :title: DR | Linux Database Server Backups | UKFast Documentation
      :description: Information on how to backup your Linux Database servers
```  

Database servers tend to keep a lot of things in memory, so seeing as we're taking file level backups you've got quite a high chance of taking inconsistent/corrupt backups.

To get around this it's sensible to try and get a consistent dump of your databases written to disk before your backups run. This has the added bonus of being easily compressible, saving you space in your backup quota in the long run.

In most cases, a simple MySQL dump using the `mysqldump` command should suffice, but if this causes disruption for your application then a more complex solution such as Percona's `XtraBackup` product. Both are covered below.

## mysqldump

MySQL comes bundled with the mysqldump utility in pretty much all instances, so it should already be installed on your system.

To create a dump of all your databases, run the following command:

```eval_rst
.. note::
   Dump files can be quite large, so it's worth using `df -h` to check that you've got enough space on the partition you're going to use.
```

```bash
  mysqldump --all-databases > /var/alldb.sql
```

If you have a username and password on your database server then you'll need to adjust the command like so:

```bash
  mysqldump -uUSERNAME -pPASSWORDGOESHERE --all-databases > /var/alldb.sql
```

You can omit the password from the command line and just leave `-p` on it's own to get an interactive password prompt if you prefer.

Further information on mysqldump and it's various flags can be found using `man mysqldump` or on the [MySQL documentation site](https://dev.mysql.com/doc/refman/5.1/en/mysqldump.html)


## XtraBackup

XtraBackup is a product from Percona, made to allow 'hot' backups of your database, meaning that there should be no locking involved.

Installing it will require the percona repo on CentOS:

```console   
   [percona]
   name = CentOS $releasever - Percona
   baseurl=http://repo.percona.com/centos/$releasever/os/$basearch/
   enabled = 0
```

Put that in a file called `/etc/yum.repos.d/percona.repo` and then install the xtrabackup utilities with following command:

```console
  yum install xtrabackup --enablerepo=percona
```

Once this is installed, you can create a full backup of your data directory by executing the `innobackupex` command with a directory, like so:

```console
  innobackupex /var/dumps/
```

## Automating dumps

As with most things on linux, the best way to automate one of the above is to use `cron`.

Our guide on cron can be found [here](/operatingsystems/linux/basics/cron), but as an example, here are both the methods laid out as cron jobs that would run at 10pm each night:

```bash
   0 22 * * * mysqldump -uroot -pMySuperLongPassword --all-databases > /var/dumps/alldb-`date`.sql
```
```bash
   0 22 * * * innobackupex /var/dumps/
```

Those cron jobs can be added to your standard crontab, accessible via the command `crontab -e` or `crontab -u someuser -e`.

```eval_rst
.. note::   
   Note that in the above mysqldump cron job, the command `date` is backticked into the command to create a different dump file/directory for each day to ensure that they don't overwrite the previous days dump.

   If this method is used, it will require manual intervention occasionally to go in and clear out old dump files to free up space.

   Innobackupex will create its own timestamped directories by default.
```

## Scripting the dump

If you'd like to run innodbex nightly and automatically clean up old backups, add the following script to your server, changing sections as necessary.

```bash
   #!/bin/bash
   #Backup MySQL DBs onto FS to then be sweeped up by file system backups.

   #Create the dump directory if not already present, permissions set as user that runs the script
   [ ! -d /var/dump/ ] && mkdir /var/dump

   #Run the backup, won't lock innodb, but will lock myisam
   innobackupex --user=backup --password=password --no-timestamp /var/dump/$(date +%d%m%y)
   innobackupex --apply-log /var/dump/$(date +%d%m%y)

   #Clean up backups older than 5 days
   find /var/dump/ -mtime +5 -exec rm {} \;
```

This can then be ran nightly as a cron job as mentioned in the previous section.

## Next steps

Once you're confident that you have consistent backups using one of the above two methods, you should now be good to follow the :doc:`Setting backup exclusions</dr-ha/ukfast_backup/backup_schedule>` guide to exclude `/var/lib/mysql` (or wherever else you may keep your data directory) from your backup run to save some space.
