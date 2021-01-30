# Installing MySQL

`MySQL` is somewhat infamous for being the number one hobbyist database whilst also being the world's second most widely used (overtaken only by SQLite and its prolific usage on Android / Apple devices).

## Installation

MySQL is available from the standard repositories on CentOS and can be installed with the following command:

CentOS 5 & 6:

```console
yum install mysql-server
```

CentOS 7:

```console
yum install mariadb-server
```

This will also install the MySQL command line client to allow you to interact with the new MySQL server.

## Set MySQL to always start on boot

CentOS 5 & 6:

```console
chkconfig mysqld on
```

CentOS 7:

```console
systemctl enable mariadb
```

## Start your MySQL server

CentOS 5 & 6:

```console
service mysqld start
```

CentOS 7:

```console
systemctl start mariadb
```

## Configuration

The MySQL configuration file is usually located in the following location:

```console
/etc/my.cnf
```

There are many guides on how to 'tune' MySQL on the internet, most of which contain conflicting, misleading or even damaging information. Any guide that claims to have 'the best' `my.cnf` layout should be treated with suspicion. For a guide on a few of the more common steps, please do check out our [MySQL Troubleshooting and Tuning](/operatingsystems/linux/mysql/troubleshooting) guide.

While these guides can help with some common issues and configurations, they are no substitute for consulting an experienced DBA who can optimise for your application and solution, especially if your application is not standard off-the-shelf software.

```eval_rst
  .. title:: Installing MySQL in Linux
  .. meta::
     :title: Installing MySQL in Linux | UKFast Documentation
     :description: A guide to installing MySQL on Linux
     :keywords: ukfast, linux, mysql, database, install, centos, cloud, lamp, server, virtual
```
