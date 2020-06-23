# Reset MySQL Root Password

## skip-grant-tables

The first step to resetting a lost MySQL root password, is to restart your MySQL server with this variable set:
 - skip-grant-tables

You can do this, by editing the MySQL configuration file usually found here:
```console
/etc/my.cnf
```

As per the below, add "skip-grant-tables" to your MySQL config:
```console
[mysqld]
skip-grant-tables
```

Now that this has been set, you can restart MySQL:
```console
[root@dev-01 ~]# systemctl restart mysql
[root@dev-01 ~]#

[root@dev-01 ~]# mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.3.18-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

## Updating The Password

Now that MySQL is running with "skip-grant-tables", you can update the password with this command:
```console
UPDATE mysql.user SET Password=PASSWORD('password_here') WHERE User='root';
```

```console
MariaDB [(none)]> UPDATE mysql.user SET Password=PASSWORD('NEW-PASSWORD') WHERE User='root';
Query OK, 4 rows affected (0.002 sec)
Rows matched: 4  Changed: 4  Warnings: 0
```

Now run "FLUSH PRIVILEGES;":
```
MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.003 sec)
```

You can now remove the flag from "/etc/my.cnf", and restart MySQL:
```
[root@dev-01 ~]# systemctl restart mysql
[root@dev-01 ~]#
```


```eval_rst
  .. title:: MySQL command line basics | UKFast Documentation
  .. meta::
     :title: MySQL command line basics | UKFast Documentation
     :description: A basic guide to using the MySQL command line in Linux
     :keywords: ukfast, mysql, database, command, line, basics, tutorial, guide, linux, centos