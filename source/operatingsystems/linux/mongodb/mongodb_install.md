# How to Install MongoDB Community Edition on CentOS 7

`MongoDB 4.4` is the latest stable release, so in this tutorial we will add the `MongoDB` package repository for 4.4.

```eval_rst
.. note:: As package versions do change, please adjust the repository version accordingly as to your requirements.
```
## Configuring the Repository

As a `sudo` user, create a file for the `MongoDB` repository within the `/etc/yum.repos.d` directory, and add the following content.

```bash
[root@ ~]# cat > /etc/yum.repos.d/mongodb.repo
[mongodb]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc
```

## Installing the Packages

As a `sudo` user, use `yum` to install `mongodb-org`. This will pull in a few different packages for administering the `MongoDB` service.

```bash
[root@ ~]# yum install mongodb-org
...
Installing:
 mongodb-org
Installing for dependencies:
 mongodb-org-mongos
 mongodb-org-server
 mongodb-org-shell
 mongodb-org-tools
```

## Starting the Service

Set this to start on boot and start the service with the `systemd` `--enable now` flag

```bash
[root@ ~]# systemctl enable --now mongod
[root@ ~]# systemctl status mongod
...
Jul 05 11:43:32 server.novalocal mongod[15786]: child process started successfully, parent exiting
Jul 05 11:43:32 server.novalocal systemd[1]: Started MongoDB Database Server.
```

Test this is running by entering the `mongo` shell.

```bash
[root@~]# mongo
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("2d22b941-8fbf-4fe3-99ed-a52678e22097") }
MongoDB server version: 4.4.1
---
...
>
```

Next, you should create an **admin** user to administrate your MongoDB service and secure the installation.

```eval_rst
  .. title:: MongoDB | How to Install MongoDB Community Edition on CentOS 7
  .. meta::
     :title: How to Install MongoDB Community Edition on CentOS 7 | ANS Documentation
     :description: How to Install MongoDB Community Edition on CentOS 7
     :keywords: mongodb, install, howto, guide, tutorial
```
