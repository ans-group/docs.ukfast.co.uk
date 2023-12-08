# How to Backup MySQL / MariaDB Databases

Ensuring your databases are safely and consistently backed up is vital.

UKFast offer "MySQL aware backups" with `Commvault` that allow for "Point-in-Time" backups and restores. However, if you wish to take your own database backups (e.g. for development) there are a few different methods to achieve this, depending on your needs.

## MySQL dumps

By far the most commonly used tool, `mysqldump` can be invoked on the command line. This method is easily configurable, but does *not* take a **hot copy** of the database.

```eval_rst
.. warning::

   Always ensure you have enough disk space available before creating a database dump
```
### Single Database

Basic example

```bash
mysqldump yourdatabase > yourdatabase.sql
```

With additional dump options (if you don't know if a database has events / routines, please use this)

```bash
mysqldump --events --routines yourdatabase > yourdatabase.sql
```
When disk space is low, you can pipe `mysqldump` output straight into a compressed file. As the output is basically text, you should see a sizeable reduction.

```bash
mysqldump yourdatabase | gzip > yourdatabase.sql.gz
```

#### Useful options
* `--host=host_name`, `-h remote_host`
  * The default host is `localhost`, but you can use this flag to specify a *remote host*.
* `--single-transaction`
  * Issues a `START TRANSACTION` statement before dumping data, for consistency. Turns off `lock-tables`, and is only useful for InnoDB tables
* `--quick`
  * On by default, forces `mysqldump` to retrieve table rows one at a time and dump straight to `stdout`, instead of buffering to memory.
* `--events --routines`
  * mysqldump dumps triggers along with tables, as these are part of the table definition. However, stored procedures, views, and events are not, and need extra parameters to be recreated explicitly
* `--lock-tables`
  * For MyISAM tables, this will prevent writes to the database during the dump.

```eval_rst
.. warning::

   Please note that ``MyISAM`` tables will lock during a database dump by default

```

### Multiple Databases

```bash
mysqldump --all-databases > all_databases.sql
```
### Scripting

Should you wish to script this, here is an example loop. This takes each database, dumps it to an example directory, then compresses it, names it and dates it.

The `nice` command adjusts the CPU priority of the process, defaulting to `10` without a flag. CPU priority ranges from `-20` (highest) to `19` (lowest), so here we are making the dump less disruptive to other processes.

```bash
for i in $(echo 'SHOW DATABASES;' | mysql | grep -v '^Database$')
do mysqldump --events --triggers $i | nice gzip > /root/mysqldumps/$i-`/bin/date +%Y.%m.%d.%a`.sql.gz
done
```

As an example, with file level backups you could keep a rolling 7 days worth of backups of each database by appending your script with the following command.

```bash
find /root/mysqldumps/ -type f -name "*.sql.gz" -mtime +7 -delete
```

```eval_rst
.. note::

   More information on the ``mysqldump`` command can be found in the official documentation:

   - https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html

```

## Percona XtraBackup

`Percona XtraBackup`

### Compatibility

XtraBackup can back up `InnoDB`, `XtraDB` & `MyISAM` tables from the following packages

* MySQL (`5.1`, `5.5`, `5.6`, `5.7` & `8.0`*)
* Percona Server

### Full backup

Percona have some detailed documentation on how to use XtraBackup [here](https://www.percona.com/doc/percona-xtrabackup/2.4/backup_scenarios/full_backup.html), but there are three main stages of the process:

* Create the backup

```bash
xtrabackup --backup --target-dir=/path/to/backup/
```

This takes a **hot copy** of the databases, so results in no locks/downtime.

* Prepare the backup

```bash
xtrabackup --prepare --target-dir=/path/to/backup/
```

This step is *vital** as it ensures the data is *point-in-time consistent*

* Restore from the backup

  * Copy the files into an *empty* data directory

```bash
rsync -avrP /path/to/backup/ /var/lib/mysql/
```

  * Check the data is owned by `mysql:mysql`, and then start up your database service

## Mariabackup

`Mariabackup` is a fork of `Percona XtraBackup` and should be used when **MariaDB 10.1+** is installed (more common on CentOS7 servers).

This backup service supports **Data-at-Rest Encryption** and **InnoDB Page Compression**.

### Installation

* Install the repo

```eval_rst
.. note::

   You will need to match the exact version of your MariaDB server or it will not backup.
```

```bash
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash -s -- --mariadb-server-version=10.2
```

```console
[info] Repository file successfully written to /etc/yum.repos.d/mariadb.repo.
[info] Adding trusted package signing keys...
[info] Successfully added trusted package signing keys.
```

* Install Mariabackup

```bash
yum install MariaDB-backup*
```

### Full Backup

* Create the backup

```bash
mariabackup --backup --target-dir=/path/to/backup/
```

This takes a **hot copy** of the databases, so results in no locks/downtime.

* Prepare the backup

```bash
mariabackup --prepare --target-dir=/path/to/backup/
```

```eval_rst
.. note::

   More information on **Mariabackup** can be found in the official MariaDB documentation

   - https://mariadb.com/kb/en/mariabackup-overview

```

```eval_rst
  .. title:: MySQL | How to Backup MySQL / MariaDB Databases
  .. meta::
     :title: MySQL | How to Backup MySQL / MariaDB Databases | ANS Documentation
     :description: A guide for taking consistent database backups on a Linux server
     :keywords: ukfast, linux, mysql, mysqldump, xtrabackup, mariabackup, backups, server, guide, tutorial
```
