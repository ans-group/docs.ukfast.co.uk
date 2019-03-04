# Installing MySQL

`MySQL` is somewhat infamous for being the number one hobbyist database whilst also being the world's second most widely used (overtaken only by SQLite and its prolific usage on Android/Apple devices).

## Installation

### CentOS 5 & 6

Use yum to install `MySQL`:

```console
  yum install mysql-server
```

Set `MySQL` to start on boot:

```console
  chkconfig mysqld on
```

Finally, start `MySQL`:

```console
  service mysqld start
```

### CentOS 7

`MySQL` on CentOS 7 must be installed via the community repo.

Download and install the RPM from the community repo:

```console
  wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
  yum install mysql-community-release-el7-5.noarch.rpm
```

Run a yum update to allow the repo to become available.

```console
  yum update
```

Now it can be yum installed:

```console
  yum install mysql-server
```

Enable `MySQL` to start on boot:

```console
  systemctl enable mysqld
```

Finally, start `MySQL`:

```console
  systemctl start mysqld
```

### Secure Installation

Finally, to finish the installation and review some security features of `MySQL`, run the secure installation command:

```console
  mysql_secure_installation
```

## Configuration

The MySQL configuration file is usually located in the following location:

```console
  /etc/my.cnf
```

There are many guides on how to 'tune' MySQL on the internet, most of which contain conflicting, misleading or even damaging information. Any guide that claims to have 'the best' `my.cnf` layout should be treated with suspicion. For a guide on a few of the more common steps, please do check out our [MySQL Troubleshooting and Tuning](/operatingsystems/linux/mysql/troubleshooting.html) guide.

While these guides can help with some common issues and configurations, they are no substitute for consulting an experienced DBA who can optimize for your application and solution, especially if your application is not standard off-the-shelf software.

```eval_rst
  .. meta::
     :title: Installing MySQL in Linux | UKFast Documentation
     :description: A guide to installing MySQL on Linux
     :keywords: ukfast, linux, mysql, database, install, centos, cloud, lamp, server, virtual