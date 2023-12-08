# Service Management on CentOS 6

On a Linux server, a service is an application that is capable of running in the background performing some task or other. This guide will detail the `SysVinit` system and how you can manage services with it.

To keep in the scope of this tutorial as part of a [Linux basics](/operatingsystems/linux/basics/index) series, we'll only be covering two of the most common services you'll come across when managing a Linux web server, `Apache` and `MySQL`

Our main tool for interacting with services on Linux is fairly straight forward: `service`

The syntax for common tasks is fairly self explanatory and takes the following format:

```bash
service {servicename} {command}
```

Below are a few sections on common tasks with some examples.

As a broad rule, all service management should be carried out as the `root` user, so make sure you're logged into that account or have access to one with `sudo`.

## Starting services

The argument to start a service is simply `start`, so using the structure above with the `httpd` (Red Hat distributions use this name for Apache) we get the following command:

```bash
service httpd start
```

This will return some content letting you know if the service started successfully or not before dropping you back to your prompt ready to enter more commands:

```console
[root@94 ~]# service httpd start
Starting httpd:                                            [  OK  ]
[root@94 ~]#
```

If the service failed to start, it may give you information on why it failed to start or it may simply say `FAILED`:

```console
[ukfastsupport@94 ~]$ service httpd start
Starting httpd: (13)Permission denied: make_sock: could not bind to address [::]:80
(13)Permission denied: make_sock: could not bind to address 0.0.0.0:80
no listening sockets available, shutting down
Unable to open logs
                                                            [FAILED]
[ukfastsupport@94 ~]$
```

The above example was actually fairly descriptive, letting us know that the user we were using didn't have necessary permission to start the service, but don't be surprised if you get little to no information. Such is the joy of Linux. Learning to diagnose why services won't/can't start is beyond the scope of this article but will be covered elsewhere in our documentation in the future.

## Stopping services

Similar to our `start` commands above, to stop a services we can just use `stop` instead. This time we'll use MySQL in our example, which has the service name `mysqld`:

```bash
service mysqld stop
```

Again, similar to start, you'll usually get some amount of feedback to let you know that the service has stopped successfully:

```console
[root@94 ~]# service mysqld start
Starting mysqld:                                           [  OK  ]
[root@94 ~]#
```

## Restarting services

You may have an idea on what command will be needed to restart a service by now. We'll be needing the `restart` argument:

```bash
service httpd restart
```

This will give a combined bit of output as it stops and then starts the service:

```console
[root@94 ~]# service httpd restart
Stopping httpd:                                            [  OK  ]
Starting httpd:                                            [  OK  ]
[root@94 ~]#
```

## Checking the status of services

It's sometimes useful to see if a service is running or not, and it may not be immediately apparent, so most (but not all) services implement the `status` argument:

```console
[root@94 ~]# service httpd status
httpd (pid  17462) is running...
```

Above, we can see that Apache is up and running quite happily (or at least the service is)

```console
[root@94 ~]# service mysqld status
mysqld is stopped
```

Whilst the output varies from service to service, it's usually fairly clear if the service is running or not.

You can sometimes even get some information on if the service was stopped cleanly or crashed:

```console
[root@94 ~]# service mysqld status
mysqld dead but subsys locked
```

## Starting services on boot

One of the most important tasks regarding services is making sure they start automatically, as you don't want to have to log in after every reboot and start them manually.

The command for this is `chkconfig` on Red Hat/CentOS systems.

Usage is fairly simple. To start Red Hat at boot, we'd use the following command:

```bash
chkconfig httpd on
```

To stop MySQL from starting at boot, we could use the inverse:

```bash
chkconfig mysqld off
```

Unlike the `service` command above, `chkconfig` doesn't give any output to the command, but we can check what is configured to start on a normal boot using the following, slightly more convoluted, command:

```bash
chkconfig --list|grep '3:on'
```

This will likely generate quite a lot of output as there are a fair few services that start automatically, but looking down the left hand side you should be able to see that in the following example Red Hat is configured to start at boot but `MySQL` isn't:

```console
[root@94 ~]# chkconfig --list|grep '3:on'
auditd          0:off   1:off   2:on    3:on    4:on    5:on    6:off
crond           0:off   1:off   2:on    3:on    4:on    5:on    6:off
httpd           0:off   1:off   2:on    3:on    4:on    5:on    6:off
ip6tables       0:off   1:off   2:on    3:on    4:on    5:on    6:off
iptables        0:off   1:off   2:on    3:on    4:on    5:on    6:off
lvm2-monitor    0:off   1:on    2:on    3:on    4:on    5:on    6:off
messagebus      0:off   1:off   2:on    3:on    4:on    5:on    6:off
netfs           0:off   1:off   2:off   3:on    4:on    5:on    6:off
network         0:off   1:off   2:on    3:on    4:on    5:on    6:off
rsyslog         0:off   1:off   2:on    3:on    4:on    5:on    6:off
sendmail        0:off   1:off   2:on    3:on    4:on    5:on    6:off
sshd            0:off   1:off   2:on    3:on    4:on    5:on    6:off
sysstat         0:off   1:on    2:on    3:on    4:on    5:on    6:off
udev-post       0:off   1:on    2:on    3:on    4:on    5:on    6:off
```

```eval_rst
   .. title:: Service Management on CentOS 6
   .. meta::
      :title: Service Management on CentOS 6 | ANS Documentation
      :description: Information on how to manage services on CentOS 6
```
