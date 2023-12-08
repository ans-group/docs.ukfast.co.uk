# Linux Log Files

If you are experiencing issues with either your site or server, server logs can provide an insight into what may be causing these issues. Each service running on the server will have their own specific log file. Most logs for Linux can be found in the `/var/log/` directory.

In this directory we can see an example list of what you might expect to see in `/var/log/`:

```bash
[root@UKFast ~]# ls -l /var/log
```

```console
total 40308
drwxr-xr-x. 2 root   root       4096 Jul  1  2019 anaconda
drwxr-xr-x  2 root   root       4096 Jan 22 00:00 atop
drwx------. 2 root   root       4096 Jan 22 17:16 audit
-rw-------  1 root   root          0 Jan 13 03:23 boot.log
-rw-------  1 root   utmp   17139072 Jan 22 19:21 btmp
drwxr-xr-x. 2 chrony chrony     4096 Apr 12  2018 chrony
-rw-------  1 root   root     157324 Jan 12 17:38 cloud-init.log
-rw-------  1 root   root      24557 Jan 22 19:01 cron
-rw-r--r--  1 root   root      33396 Jan 12 17:37 dmesg
-rw-r--r--  1 root   root      32301 Nov 16 13:49 dmesg.old
-rw-r--r--  1 root   root     293168 Jan 22 19:21 lastlog
-rw-------  1 root   root          0 Jan 19 03:23 maillog
-rw-------  1 root   root        112 Jan  4 20:36 maillog-20200105
-rw-------  1 root   root      26892 Jan 22 19:21 messages
-rw-------  1 root   root     250235 Jan 19 03:01 messages-20200119
drwxr-xr-x. 2 ntp    ntp        4096 Apr 13  2018 ntpstats
-rw-------  1 root   root   13183804 Jan 22 19:21 secure
-rw-------  1 root   root    1737474 Jan 19 03:22 secure-20200119
drwxr-xr-x. 2 root   root       4096 Nov 16 13:50 tuned
-rw-rw-r--  1 root   utmp      53376 Jan 22 19:21 wtmp
-rw-------  1 root   root        261 Jan 21 21:44 yum.log
-rw-------  1 root   root       6125 Dec 12 10:04 yum.log-20200101
```

In this guide we will look into the main log files that can be used for troubleshooting. We will also look into panel specific logs such as cPanel and Plesk.

## General Logs

Usually the first point to an investigation will be in the `messages` and `secure` logs. These contain general, but useful information which could help confirm issues such as a hung task timeout, or out of memory issue.

* CentOS: `/var/log/messages`
* Ubuntu: `/var/log/syslog`

General messages and log in attempts. A useful log for diagnosing kernel panics and out of memory issues.

```bash
[root@UKFast ~]# cat /var/log/messages
```

```console
kernel: Out of memory: Kill process 9163 (mysqld) score 511 or sacrifice child
kernel: Killed process 9163, UID 27, (mysqld) total-vm:2457368kB, anon-rss:816780kB, file-rss:4kB
```

* CentOS: `/var/log/secure`
* Ubuntu: `/var/log/auth.log`

Contains the login attempts for SSH. Useful to check for hacking attempts or unauthorised logins.

```bash
[root@UKFast ~]# cat /var/log/secure
```

```console
sshd[2343]: Accepted publickey for ukfast from <ip address> port 56239 ssh2
sshd[2343]: pam_unix(sshd:session): session opened for user ukfast by (uid=0)
```

## Mail Server Logs

If you are experiencing issues with emails or would like to track an email then the mail log file is a great diagnostic tool. It's useful for tracking emails that have been sent or received.

* `/var/log/maillog`

```bash
[root@UKFast ~]# cat /var/log/maillog
```

```console
Jan 12 17:38:40 ukfast postfix/local[3142]: EF76E22A55: to=<root@ukfast>, orig_to=<root>, relay=local, delay=680510, delays=680510/0.01/0/0.01, dsn=2.0.0, status=sent (delivered to mailbox)
Jan 12 17:38:40 ukfast postfix/qmgr[3113]: EF76E22A55: removed
```

If your mail server is cPanel, this is likely to be using Exim as a Mail Transfer Agent (MTA). Exim will record errors, incoming and outgoing emails to `/var/log/exim_mainlog`

## MySQL/MariaDB Logs

You can check MySQL logging is enabled by running the following in MySQL:

```bash
mysql> show variables like '%log%';
```

The usual log file for MySQL general messages and errors is `/var/log/mysqld.log`

This can be useful when diagnosing why the MySQL service will not start, an example could include a full partition.

## Web Server Logs

The location of your web server logs will be dependant on the web service currently running.

* `/var/log/httpd/` - Directory for Apache server logs.

   The main logs in this directory are `error_log` and `access_log`. Many errors in regards to your web service can be found here. The access logs can be used to search for suspicious requests and reviewing incoming traffic.

* `/var/log/nginx/` - Directory for NGINX server logs.

   The main logs in this directory are `error.log` and `access.log`. Each site configured can have their own individual log file: `domain.error.log`.

* `/var/log/php-fpm/error.log` - Directory for PHP-RPM logs.

   If your web server is running PHP-FPM, this will be the log to diagnose any PHP issues. For example, you may be able to diagnose certain limit issues such as `max_children`:

```bash
[root@UKFast ~]# grep "children" /var/log/php-fpm/error.log
```

```console
WARNING: [pool domain] server reached pm.max_children setting (50), consider raising it
```

## cPanel Logs

* cPanel access logs for WHM, cPanel, and webmail - `/usr/local/cpanel/logs/access_log`
* General cPanel and WHM errors - `/usr/local/cpanel/logs/error_log`
* User's activities while they are logged into the cPanel account - `/usr/local/cpanel/logs/session_log`
* Exim Mail Transfer Agent - `/var/log/exim_mainlog`
* A domain's access and error logs directory - `/home/domain/logs/`
* PHP-FPM logs, replacing `<v>` for PHP version - `/opt/cpanel/ea-php<v>/root/usr/var/log/php-fpm/error.log`

## Plesk Logs

Plesk also has additional log locations and logs for its own services.

* General Plesk error log - `/var/log/sw-cp-server/error_log` and `/var/log/sw-cp-server/sw-engine.log`
* Plesk Access log - `/var/log/plesk/httpsd_access_log`
* Panel log - `/var/log/plesk/panel.log`
* A domain's access and error logs directory- `/var/www/vhosts/system/domain.com/logs/`
* PHP-FPM logs, replacing `<v>` for PHP version - `/var/log/plesk-php<v>-fpm/error.log`

```eval_rst
  .. title:: Linux Log Files
  .. meta::
     :title: Linux Log Files | ANS Documentation
     :description: Guidance on where to find important Linux logs
     :keywords: linux, logs, ukfast, secure, plesk, cpanel, messages
```
