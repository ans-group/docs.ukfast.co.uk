# Installing MySQL

`MySQL` is somewhat infamous for being the number one hobbyist database whilst also being the world's second most widely used (overtaken by SQLite and it's prolific usage on Android/Apple devices).

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

This will also install the mysql command line client to allow you to interact with the new mysql server.

Set mysql to start on boot with:

CentOS 5 & 6:

```console
  chkconfig mysqld on
```

CentOS 7:

```console
  systemctl enable mariadb
```

Then start it up with the following:

CentOS 5 & 6:

```console
  service mysqld start
```

CentOS 7:

```console
  systemctl start mariadb
```

Configuration

The MySQL configuration file is located in the following location:

```console
  /etc/my.cnf
```

There are many guides on how to 'tune' mysql on the internet, most of which contain conflicting, misleading or even damaging information and any guide that claims to have 'the best' `my.cnf` layout should be treated with suspicion.

That said, there are tools out there that can be used to make reasoned guesses about what configuration you may want to run, such as the following wizard from Percona:

<https://tools.percona.com/wizard>  (requires registration)

or the following perl script that checks your system resources and spits out a list of reccomended tweaks:

<http://mysqltuner.pl>

```eval_rst
.. warning::
   Neither of the above links are maintained by or related to UKFast and all content is used at your own discretion.
```
