# MySQL Command Line Basics

In this tutorial, we will cover the basics of MySQL command line. MySQL CLI is a client for accessing the MySQL server daemon and will allow you to access, retrieve and modify your databases and users through your Linux server.

It is available through the base CentOS and Ubuntu repositories. The commands below will help you browse through your databases and look at your users.

## Access MySQL through your shell

Once you have logged into your server through SSH using a client like PuTTY, use the command below to access the MySQL CLI. This will require you to know the credentials for the user you are using.

```bash
mysql -u root -p
```


Once logged in your should see something like the following prompt.

```console
  Welcome to the MySQL monitor.  Commands end with ; or \g.
  Your MySQL connection id is 479
  Server version: 5.1.73-14.12 Percona Server (GPL), Release 14.12, Revision 624

  Copyright (c) 2009-2013 Percona LLC and/or its affiliates
  Copyright (c) 2000, 2013, Oracle and/or its affiliates. All rights reserved.

  Oracle is a registered trademark of Oracle Corporation and/or its
  affiliates. Other names may be trademarks of their respective
  owners.

  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

  mysql>
```


## View Database and Tables

You should now be able to view your databases and tables. This can be done use the commands below.

```sql
SHOW DATABASES;
```

You can also use a database from the list of databases available to you.


```sql
USE database_wp;
```

This will show the following information.

```console
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql>
```

Here you can view your tables and even run queries.

```sql
SHOW TABLES;
```

Here is an example query from a Magento database, where we are checking the current base URL:

```sql
SELECT * FROM core_config_data WHERE path LIKE '%base%url%';
```

### Users and GRANTS

You can also view your users. All of the users that are available on your MySQL install will be shown using the command below.

```sql
SELECT user, host FROM mysql.user;
```

MySQL users have 2 parts: `username` and `host`, usually written as `'username'@'host'`. `username` is self-explanatory. `host` defines where that user is allowed to connect from. For example, `'dbuser'@'123.123.123.123'`, which will allow `dbuser` to connect from the IP address `123.123.123.123`, or `'root'@'localhost'` means the `root` user, connecting from the local server only.

Note that this means you could have 2 users with the same `username`, as long as they have different hosts. So `'dbuser'@'123.123.123.123'` and `'dbuser'@'111.111.111.111'` can both exist on the same server.

A thing to note here is that the `root@localhost` user is NOT the same as `root@127.0.0.1`! MySQL (and Linux in general) treats sockets differently to TCP/IP connections unless there is an alias associated with it. You can read more about this by using the link to the [official MySQL documentation](https://dev.mysql.com/doc/refman/5.5/en/can-not-connect-to-server.html).

You can also view grants for an individual user using the command below.

```console
  mysql> SHOW GRANTS for root@localhost;
  +---------------------------------------------------------------------+
  | Grants for root@localhost                                           |
  +---------------------------------------------------------------------+
  | GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION |
  +---------------------------------------------------------------------+
  1 row in set (0.00 sec)
```

For more tips on managing users and databases, please do check out our [Managing Databases and Users](/operatingsystems/linux/mysql/managing_databases_users) guide.

```eval_rst
  .. title:: MySQL command line basics
  .. meta::
     :title: MySQL command line basics | UKFast Documentation
     :description: A basic guide to using the MySQL command line in Linux
     :keywords: ukfast, mysql, database, command, line, basics, tutorial, guide, linux, centos
```
