# How to Perform Common Administrative Tasks in MongoDB

## Connecting to the Shell

To connect to the `MongoDB` shell, simply type `mongo` as a `sudo` user.

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

To exit the shell, type `exit`

## Connecting with Authentication

To connect to the `MongoDB` shell with a specific user, use the following syntax

```bash
[root@~]# mongo -u YOURUSER -p --authenticationDatabase admin
```

## Creating a database

If a database does not exist, MongoDB will automatically create the database when you try to use it.

```bash
> use authors
switched to db authors
```

Though the database doesn't officially exist until you insert data, as below.

```bash
> show dbs
admin    0.000GB
config   0.000GB
local    0.000GB
> db.authors.insert({ authorname: "Ursula K. Le Guin"})
WriteResult({ "nInserted" : 1 })
> show dbs
authors 0.000GB
admin   0.000GB
config  0.000GB
local   0.000GB
> db.authors.find()
{ "_id" : ObjectId("5f60a43e73116436bea8c0a4"), "authorname" : "Ursula K. Le Guin" }
```

## Enabling Remote Access

```eval_rst
.. warning:: Always ensure that the bind address for MongoDB is restricted on your firewall.
```

To connect to `MongoDB` from a remote location, you will need to ensure that the bind address is amended to your required IP Address.

* As a `sudo` user, edit the `MongoDB` configuration file to specify the bind address. In this example, we are binding this to `12.34.56.78`.

```bash
[root@ ~]# vi /etc/mongod.conf
# network interfaces
net:
  port: 27017
  bindIp: 127.0.0.1,12.34.56.78
# Enter 0.0.0.0,:: to bind to all IPv4 and IPv6 addresses or, alternatively, use the net.bindIpAll setting.
```

* Restart the service

```bash
[root@]# systemctl restart mongod
```

```eval_rst
.. note:: You may also need to ensure that port 27017 is open to your required location on your software firewall. This falls outside the scope of this tutorial.
```

## Changing the Assigned Port

```eval_rst
.. warning:: Always ensure that the assigned port for MongoDB is restricted on your firewall.
```

To change the `MongoDB` to something non-standard, away from `27017`, you will need to edit your `MongoDB` configuration file:

* As a `sudo` user, edit the `MongoDB` configuration file to specify your new port number.

```bash
[root@ ~]# vi /etc/mongod.conf
# network interfaces
net:
#  port: 27017
  port: 27018
```

* Restart the service

```bash
[root@]# systemctl restart mongod
```

```eval_rst
.. note:: You may also need to ensure that port ``27017`` is open to your required location on your software firewall. This falls outside the scope of this tutorial.
```

## Troubleshooting

### Error Logging

`MongoDB` logs to the following file upon startup and shutdown, and so is a good place to start when diagnosing startup errors.

```bash
/var/log/mongodb/mongod.log
```

### Permissions

Typically, file ownership and permissions can trip up a MongoDB installation. Be sure to check that the `MongoDB` data directory is owned by the `mongod` user.

```bash
[root@ ~]# stat /var/lib/mongo
  File: '/var/lib/mongo'
  Size: 4096            Blocks: 8          IO Block: 4096   directory
Device: fd02h/64770d    Inode: 669         Links: 4
Access: (0755/drwxr-xr-x)  Uid: (  977/  mongod)   Gid: (  971/  mongod
```

If this is not owned by the `mongod` user, you can correct this with the following command as a `sudo` user.

```bash
[root@ ~]# chown -R mongod: /var/lib/mongo
```

If using `SELinux` in **enforcing mode**, you will need to ensure that the correct `SELinux` policy is set using the following documentation
* [MongoDB SELinux configuration](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/index.html#configure-selinux)

```eval_rst
  .. title:: MongoDB | How to Perform Common Administrative Tasks in MongoDB
  .. meta::
     :title: How to Perform Common Administrative Tasks in MongoDB | UKFast Documentation
     :description: How to Perform Common Administrative Tasks in MongoDB
     :keywords: mongodb, admin, shell, howto, guide, tutorial
```
