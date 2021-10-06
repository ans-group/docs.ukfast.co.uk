# Magento2 Optimised Stack Troubleshooting Guide

This is the typical process we will following when troubleshooting issues on a Magento2 website.

## Traffic Flow

The first step is to perform a traffic flow on the domain in question. This ensures we are working on the correct server(s) that the website is hosted on.

We can do this using the dig command to determine the IP address(s) of the domain:

```console
user@server:~$ dig a ukfast.net +short
185.181.199.249
```

Now we have the IP address of the domain(s) we can perform a `whois` to find out what network that IP address(es) belong to:
```console
user@server:~$ whois 185.181.199.249 | grep -i netname
netname:        DDOSX
```

If the IP address belongs to a CDN we will need to find out the origin IP address from that CDN. Alternatively if we suspect a server of being the origin IP address we can SSH into that server and review incoming traffic like so:

```console
root@server:~# lsof -nP -iTCP:80,443 -sTCP:ESTABLISHED
nginx     18951   nginx   21u  IPv4 2713655406      0t0  TCP 172.22.132.163:443->185.181.199.249:16308 (ESTABLISHED)
nginx     18952   nginx   21u  IPv4 2713692171      0t0  TCP 172.22.132.163:443->185.181.199.249:18928 (ESTABLISHED)
nginx     18952   nginx   24u  IPv4 2713692613      0t0  TCP 172.22.132.163:443->185.181.199.249:19653 (ESTABLISHED)
```
You may need to run this command a few times to capture incoming traffic. This command will provide the IP addresses `(From the above example: 185.181.199.249)` connected to the server over ports 80 and 443. You can now perform a `whois` on these IP addresses to see which CDN provider they belong to.

You can also check the web services access logs to ensure traffic is going to the server in question. Typically the access logs are located in `/var/nginx/log/ukfast.net-access.log`. We can use the `tail` command to monitor the access log and the grep command to filter to our query string:

```console
root@server:~# tail -f /var/log/nginx/ukfast.net-access.log | grep trafficflow
```

Submit a request to the website with a query string of `trafficflow`:

```console
user@server:~$ curl -IL ukfast.net?trafficflow
```

If you see the request with your `tail -f` command when you know that you're on the correct server.

## Who is logged in and what are they doing?
The `w` command is an effective tool to see if anyone else is logged into the same server and what they are doing. This command also provides the load of the server and the number of days since the server was rebooted:
```console
root@server:~# w
 10:56:37 up 777 days,  2:08,  1 user,  load average: 0.01, 0.04, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
centos   pts/1    10.0.0.21        09:50    5.00s  0.03s  0.08s sshd: centos [priv]
```

## Who has been logged in?
You can also check to see who was logged into the server with the `last` command:

```console
root@server:~# last -ai | tac | tail
centos   pts/1        Tue Aug  3 15:19 - 20:28  (05:09)     10.0.0.21
centos   pts/1        Wed Aug  4 09:29 - 10:04  (00:34)     10.0.0.21
centos   pts/1        Wed Aug 11 09:50   still logged in    10.0.0.21
```

## Disk Space
Ensure that the disks are not full with the `df` command:

```console
root@server:~# df -h
Filesystem                   Size  Used Avail Use% Mounted on
devtmpfs                      48G     0   48G   0% /dev
tmpfs                         48G   54M   48G   1% /dev/shm
tmpfs                         48G  1.8M   48G   1% /run
tmpfs                         48G     0   48G   0% /sys/fs/cgroup
/dev/mapper/vg_main-lv_root   40G   19G   19G  51% /
/dev/sda1                    976M  143M  767M  16% /boot
/dev/drbd0                   183G  153G   22G  88% /nfsshare
tmpfs                        9.5G     0  9.5G   0% /run/user/1000
```

If any partition is full or running out of space we recommend using 'ncdu' to review the largest files/directories within that partition.

## Resource Check - [Atop](/operatingsystems/linux/basics/atop.html)
Atop is a useful command to review what processes are consuming the most memory, disk or CPU.

To review `realtime` data with a 1 second refresh use the command:
```console
root@server:~# atop -af 1
```
Once on the atop screen you can filter and arrange the data, here are some handy examples:

```console
Figures shown for active processes:
  'm'  - memory details
  'd'  - disk details
  'c'  - full command line per process

Sort list of processes in order of:
  'C'  - cpu activity
  'M'  - memory consumption
  'D'  - disk activity

Accumulated figures:
  'p'  - total resource consumption per program (i.e. same process name)

Process selections (keys shown in header line):
  '/'  - focus on specific command line string (regular expression)
````

To review data from the past:
```bash
atop -r /var/log/atop/atop_20210808
```

### Logs

When issues occur on a Linux/Ubuntu system a helpful message is (sometimes but not exclusively) printed to the application error log. Commonly these are found in respective paths below.

#### Magento2 Log Location:
Magento2 will capture errors and store them in files within the report directly located:

```bash
/var/www/vhosts/example.com/htdocs/var/report
```

If you're having an issue and there is no files generated in the report directory then review the `exception.log` and `system.log` files within `var/log`.

```bash
/var/www/vhosts/example.com/htdocs/var/log
```
Typically we look to review the following logs:

exception.log <br>
system.log


#### PHP-FPM error log location:

Default error logs: /var/log/`php-fpm`/error.log <br>
Site error logs: /var/www/vhosts/example.com/logs/`example.com-phpfpm-error.log`

Multi instance default error logs: /var/opt/`remi`/`$MUTLIPHPVERSION`/log/`php-fpm`/error.log <br>
Multi instance site error logs: /var/www/vhosts/example.com/logs/example.com-`phpfpm-error$PHPVERSION`.log

#### `Nginx` log location

Site access logs:
```bash
/var/www/vhosts/example.com/logs/$DOMAIN-access.log
```
Or
```bash
/var/log/nginx/example.com-access.log
```

Site error logs:
```bash
/var/www/vhosts/example.com/logs/example.com-error.log
```
Or
```bash
/var/log/nginx/example.com-error.log
```

#### MySQL error log

You can find the location of the `mysql` logs using the following command:
```bash
~]# mysql -e "SHOW VARIABLES LIKE 'log_error'"
+---------------+---------------------+
| Variable_name | Value               |
+---------------+---------------------+
| log_error     | /var/log/mysqld.log |
+---------------+---------------------+
```

#### Elasticsearch error log

The typical Elasticsearch log location is here:
```bash
/var/log/elasticsearch/elasticsearch.log
```

#### Server Logs

You can check for server errors here:

```bash
/var/log/messages
/var/log/crash
/var/log/dmesg
```

#### Varnish Logs

Varnish logs are not written by default. In order to get the log data you will need to run the following command:

```bash
varnishlog >> /tmp/varnishlogoutput.txt
```

How to check what is listening on the port:

```bash
~]# lsof -i:80
nginx   14405 nginx   10u  IPv4 44183735      0t0  TCP *:http (LISTEN)
```

```bash
netstat -l

```

### Command to check `Nginx` access logs:

```bash
grep "`date +%d/%b/%Y`" /var/log/nginx/example.com-access.log | awk '{print $1, $5,$6, $7,$9 $11}' | awk -F\" '{print $1,$2,$3}' | awk '{print $1,$3,$4,$5}' | sort | uniq -c | sort -gr | head -n 20
```

The most common cause of server slow down is one or more processes consuming a large amount of the system resources. The easiest way to view the current usage of resources is to use the utility `top`. `top` allows you to view CPU utilisation, Memory usage, Disk activity, Tasks and Load Average. Many of these are quite self explanatory and percentages to show usage. Load Average is representative of the queue of instructions on the CPU, this should ideally remain below 1.

There are several variations on the `top` utility however those are not covered in this section.

# Common Magento2 issues

## PHP-FPM Max Children Reached

### `Centos`
You can check for Max Children using the following command:

```bash
grep -iR "max_children" /var/log/php-fpm/error.log
```

If the site is displaying a 502 then you might need to test and restart `php-fpm`:

```bash
php-fpm -t && systemctl php-fpm
```

### `Centos` - PHP-FPM Additional Instance
You can check for Max Children using the following command:
```bash
grep -iR "max_children" /var/log/php-fpm/error.log
```
If the site is displaying a 502 then you might need to test and restart `php-fpm` (Example for PHP 7.4):

```bash
/opt/remi/php74/root/sbin/php-fpm && systemctl status php74-php-fpm
```

### Ubuntu
You can check for Max Children using the following command:
```bash
grep -iR "max_children" /var/log/php7.4-fpm.log
```
If the site is displaying a 502 then you might need to test and restart `php-fpm`:

```bash
php-fpm7.4 -t && systemctl php-fpm
```

## Database Deadlocks

You can get the engine status of MySQL using the following command:
```bash
mysql -e "SHOW ENGINE INNODB STATUS;"
```
This will identify if there has been a deadlock

## Varnish 503

You can check the health of the application using the following command:

```bash
~]# varnishadm backend.list
200
Backend name   Admin    Probe    Health
boot.default   probe    10/10    healthy
```

This is the typical configuration for the healthcheck:
https://docs.ukfast.co.uk/ecommercestacks/magento/magento2/varnish/varnish.html#health-check

## Permissions
Make sure the owner and group of the document root is `"websiteuser:websiteuser"`. You can find the user and group from the PHP-FPM configuration pool file.

### Find files not owned by `"websiteuser"`
```bash
find /var/www/vhosts/sitename.co.uk/htdocs/ -! -user websiteuser
```

If this command returns any output you will need to review the files and or directories and possible change the owner and group.

### To change the ownership you can run the following command:

```bash
chown -R websiteuser:websiteuser /var/www/vhosts/sitename.co.uk/htdocs/
```

Further permission advice can be found here:

https://docs.ukfast.co.uk/ecommercestacks/magento/magento2/permissionguide.html

```eval_rst
  .. title:: Magento 2 Troubleshooting
  .. meta::
     :title: Magento 2 Troubleshooting | UKFast Documentation
     :description: A guide to troubleshoot errors
     :keywords: ukfast, linux, nginx, varnish, php-fpm, install, centos, ubuntu, cloud, server, virtual, Magento2, security, eCommerce
```
