# Connecting to MySQL via SSH

In Linux, the most commonly used method of connecting to MySQL is by using the `mysql` command within the command line interface.
You are unable to do that on a server using Plesk, however. When you type `mysql` and hit enter you will be greeted with an Access Denied message.

## Version >11

On Plesk Versions newer than 11, you can gain access to MySQL by running the following command.

``#
plesk db
``
Once you run that command, you will be put into the MySQL console which looks like the below:

``#
plesk db
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1172
Server version: 5.5.60-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [psa]>
``

## Version <11

On Plesk Versions older than 11, you will be unable to use both `mysql` and `plesk db` to connect to MySQL via the CLI.
To get into the MySQL Console, run the following command:

``#
mysql -uadmin -p`cat /etc/psa/.psa.shadow`
``

If you experience any issues with any of the methods above, please do not hesitate to get in touch with our support team.
Want to gain access via another method such as MySQL Workbench but encountering issues? Please raise a request with our support team who will assist and advise accordingly.

```eval_rst
  .. title:: Connecting to MySQL on Plesk via CLI
  .. meta::
     :title: Connecting to MySQL on Plesk via CLI | UKFast Documentation
     :description: A guide to connecting to MySQL on Plesk via CLI
     :keywords: ukfast, plesk, mysql, plesk db, linux, cli, command, mariadb
