# Restoring databases from a file based MySQL Backup

You've just requested a restore for one of your databases, and the UKFast team have just provided you with a restore on your server with a physical filepath, or if not a client, you've otherwise restored a copy of your MySQL datadir.

In this example, this will be in the form of `/var/restore33030948/var/lib/mysql`.


## Where do you start?

The first place you need to look at is the `my.cnf` file. This is going to be in `/etc/my.cnf` and will show all your MySQL configuration parameters. Here is an example of what a basic `my.cnf` looks like.

```console
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

The only thing you need to look in here is the datadir variable. In this case, your databases are all located in `/var/lib/mysql`.

For some type of databases, such as `MyISAM` databases, you can just use the individual databases within this folder and replace them in your datadir.

But for other type of databases, like `InnoDB` databases, you will need to create a second instance of MySQL. This is a simple process, and the step by step guide below will help you spin up a second instance of MySQL in no time.

## Second instance of MySQL

Use the vi editor on your SSH console and access the my.cnf using the command below.

```bash
  vi /etc/my.cnf
```

Now add the line below after pressing `i`. This puts your editor into edit mode. Copy the block below.

```console
  [mysqld1]
  socket=/var/run/mysqld/mysqld1.sock
  port=23306
  user=mysql
  basedir=/usr
  pid-file=/var/run/mysqld/mysqld1.pid
  datadir=/home/restore/var/lib/mysql
  log-error=/var/log/mysqld.log
  #innodb_force_recovery=6
```

Make sure the datadir in your block is the directory the UKFast support team have provided you.

Save the document by pressing `Esc` on your keyboard and then the following keys `:wq!`. Press `Enter`.



## Starting the instance

Type the command below in your SSH console to start this instance

```bash
  mysqld_multi start 1
```

Once started, type the command below to see if the instance is running.

```bash
  mysqld_multi report
```

It should show the following information

```console
  mysqld_multi report
  Reporting MySQL servers
  MySQL server from group: mysqld1 is not running
```



## Time to get the SQL dump out

Use the command below to get a working MySQL dump out.

```bash
  mysqldump -S /var/run/mysqld/mysqld1.sock -u root -p yourdatabase > yourdatabase.sql
```



## You're all done now, time to cleanup

Stop the second instance using the command below.

```bash
  mysqld_multi stop 1
```

And now you can use yourdatabase.sql to restore your database.

## Import a database dump

Once you have your database dump you will need to import this dump into MySQL. To do this, you will need to enter the below command.

```mysql -u root -p yourdatabase < yourdatabase.sql```

```eval_rst
  .. title:: Restoring databases from a MySQL backup file | UKFast Documentation
  .. meta::
     :title: Restoring databases from a MySQL backup file | UKFast Documentation
     :description: A guide to restoring a database from a MySQL backup file
     :keywords: ukfast, linux, mysql, database, backup, dump, restore, recovery, security, cloud
