# MariaDB Installation

`MariaDB` is a fork of `MySQL` and so the two are very similar. Notable users of MySQL include Wikipedia, WordPress.com and Google.

## Installation

### CentOS 6

Before `MariaDB` can be installed on CentOS 6, the repository will first need adding. Create the below file:

```console
  vi /etc/yum.repos.d/MariaDB.repo
```

Now paste the below into the file and save edits:

```console
  [mariadb]
  name = MariaDB
  baseurl = http://yum.mariadb.org/10.1/centos6-amd64
  gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
  gpgcheck=1
```

`MariaDB` can now be yum installed:

```console
  yum install MariaDB-server MariaDB-client
```

Set the service to start on boot:

```console
  chkconfig mysqld on
```

Finally, start `MariaDB`:

```console
  service mysqld restart
```


### CentOS 7

Installing `MariaDB` is much easier on CentOS 7, as the package can just be yum installed:

```console
  yum install mariadb-server
```

Enable the service to start on boot:

```console
  systemctl enable mariadb
```

Finally, start the service:

```console
  systemctl start mariadb
```

## Secure Installation Command

Finally, to finish the installation and review some security features of `MySQL`, run the secure installation command:

```console
  mysql_secure_installation
```

