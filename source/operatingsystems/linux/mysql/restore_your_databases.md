# Restoring databases from a file based MySQL Backup

This article will provide the steps need to restore a database using a physical file path when a `.sql` file is not available.

For this guide, the file path is `/home/restore/var/lib/mysql`.

Using the given path, you will create a second instance of MySQL. This second instance of MySQL will be used to dump out copy of the database and create a `.sql` file which you can then import.

## Create A Second Instance

First edit the `/etc/my.cnf` file to include a new block called `[mysql1]` for the second instance. Here is an example of what a basic `my.cnf` looks like.

```ini
  [mysqld]
  datadir=/var/lib/mysql
  socket=/var/lib/mysql/mysql.sock
  user=mysql
  # Disabling symbolic-links is recommended to prevent assorted security risks
  symbolic-links=0

  [mysqld_safe]
  log-error=/var/log/mysqld.log
  pid-file=/var/run/mysqld/mysqld.pid
```

Using a text editor, add the following `[mysql1]` block to the end of the `/etc/my.cnf`. Make sure to update the `datadir` with the file path of the database:

```bash
  $ vi /etc/my.cnf
```

```ini
  [mysqld1]
  datadir=/home/restore/var/lib/mysql
  socket=/var/lib/mysql/mysqld1.sock
  pid-file=/var/lib/mysql/mysqld1.pid
  port=23306
  user=mysql
```

## Start The Second Instance

Type the command below in your SSH console to start this instance

```bash
mysqld_multi start 1
```

Once started, type the command below to see if the instance is running.

```bash
mysqld_multi report
```

```console
Reporting MySQL servers
MySQL server from group: mysqld1 is running
```

If it is not running, use the log file `/var/lib/mysql/mysqld_multi.log` to debug.

## Dump Out The Database

```eval_rst
.. warning::

   Always ensure you have enough disk space available before creating a database dump
```

Check that the database you require is in the second instance of MySQL and contains the tables you are expecting:

```bash
mysql -S /var/lib/mysql/mysqld1.sock
```

```sql
  MariaDB [(none)]> show databases;
  +--------------------+
  | Database           |
  +--------------------+
  | information_schema |
  | mysql              |
  | performance_schema |
  | example_db         |
  +--------------------+
  4 rows in set (0.00 sec)
```

```sql
  MariaDB [(none)]> use example_db;
  Database changed

  MariaDB [example_db]> show tables;
  +---------------------+
  | Tables_in_example_db|
  +---------------------+
  | employees           |
  | products            |
  | orders              |
  +---------------------+
  1 row in set (0.00 sec)
```

Provided the data is as expected, back into SSH and dump out the individual database:

```bash
mysqldump -S /var/lib/mysql/mysqld1.sock -u root -p example_db > example_db.sql
```

Check the exported `.sql` file contains expected data:

```bash
less example_db.sql
```

## Cleanup

Now you have successfully imported the database, cleanup the second instance using the command below.

```bash
mysqld_multi stop 1
```

## Import a database dump

Now you have a `.sql` file you can follow [import your database guide](/operatingsystems/linux/mysql/import_database) for more information.

```eval_rst
  .. title:: Restoring databases from a MySQL backup file
  .. meta::
     :title: Restoring databases from a MySQL backup file | ANS Documentation
     :description: A guide to restoring a database from a MySQL backup file
     :keywords: ukfast, linux, mysql, database, backup, dump, restore, recovery, security, cloud
```
