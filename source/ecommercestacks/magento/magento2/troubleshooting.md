# Troubleshooting

### Example of a Good Ticket Format

When raising a ticket the most important aspect to keep in mind is to be informative and comprehensive whilst remaining concise.

Engineers need to know:

* Domain or IP address of the server.
* A short description of the issue.
* Any error messages produced when encountering the issue
* When did the issue start? Has this happened before?

### Collecting the right information

Dig the domain to find out the origin IP:

```bash
 dig a domain +short
```

Now we have the IP address of the domain(s) we can perform a whois to find out what network that IP address(es) belong to:
```bash
 whois ip | grep -i netname
```
### Atop

Atop is a useful command to review what actions are consuming the most memory, disk or load.

Here are a few commands you can look at to get started. To review realtime data, please use the follow command:
```bash
atop -af 1
```

To look at data from the past:
```bash
atop -r
atop -r /var/log/atop/atop_20210808
```

To review transactions consuming the most disk:
```bash
atop -afd 1
```

To review transactions consuming the most memory:
```bash
atop -afm 1
```

To see what services are consuming the most load:
```bash
atop -afp 1
```

Now we know what server this is related to we can work on reviewing the logs to work out what error is occuring.

### --- Logs ---

When issues occur on a Linux system a helpful message is (sometimes but not exclusively) printed to the application error log. Commonly these are found in respective paths below.

### Magento Log Location:
```bash
/var/www/vhosts/example.com/htdocs/var/log
```
Typically we look to review the following logs:

execption.log <br>
system.log

The report location path is below:
```bash
/var/www/vhosts/example.com/htdocs/var/report
```

### PHP-FPM error log location:

Default error logs: /var/log/php-fpm/error.log <br>
Site error logs: /var/www/vhosts/example.com/logs/example.com-phpfpm-error.log

Multi instance default error logs: /var/opt/remi/$MUTLIPHPVERSION/log/php-fpm/error.log <br>
Multi instance site error logs: /var/www/vhosts/example.com/logs/example.com-phpfpm-error$PHPVERSION.log

### Nginx log location

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

### MySQL error log

You can find the location of the mysql logs using the following command:

~]# mysql -e "SHOW VARIABLES LIKE 'log_error'"
+---------------+---------------------+
| Variable_name | Value               |
+---------------+---------------------+
| log_error     | /var/log/mysqld.log |
+---------------+---------------------+

### Elasticsearch error log

The typical elasticsearch log location is here:
```bash
/var/log/elasticsearch/elasticsearch.log
```

### Server Logs

You can check for server errors here:

```bash
/var/log/messages
/var/log/crash
/var/log/dmesg
```

### Varnish Logs

Varnish logs are not writeen by default. In order to get the log data you will need to run the following command:

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

### Command to check Nginx access logs:

```bash
grep "`date +%d/%b/%Y`" /var/log/nginx/example.com-access.log | awk '{print $1, $5,$6, $7,$9 $11}' | awk -F\" '{print $1,$2,$3}' | awk '{print $1,$3,$4,$5}' | sort | uniq -c | sort -gr | head -n 20
```

The most common cause of server slow down is one or more processes consuming a large amount of the system resources. The easiest way to view the current usage of resources is to use the utility `top`. `top` allows you to view CPU utilisation, Memory usage, Disk activity, Tasks and Load Average. Many of these are quite self explanatory and percentages to show usage. Load Average is representative of the queue of instructions on the CPU, this should ideally remain below 1.

There are several variations on the `top` utility however those are not covered in this section.

### Common issues

#### Max Children Reached

#### Centos
You can check for Max Children using the following command:

grep -iR "max_children" /var/log/php-fpm/error.log

If the site is displaying a 502 then you might need to test and restart php-fpm:

```bash
php-fpm -t && systemctl php-fpm
```

#### Centos Multi Instance
You can check for Max Children using the following command:

grep -iR "max_children" /var/log/php-fpm/error.log

If the site is displaying a 502 then you might need to test and restart php-fpm (Example for PHP 7.4):

```bash
/opt/remi/php74/root/sbin/php-fpm && systemctl status php74-php-fpm
```

#### Ubuntu
You can check for Max Children using the following command:

grep -iR "max_children" /var/log/php7.4-fpm.log

If the site is displaying a 502 then you might need to test and restart php-fpm:

```bash
php-fpm7.4 -t && systemctl php-fpm
```

### Database Deadlocks

You can get the engine status of MySQL using the following command:

mysql -e "SHOW ENGINE INNODB STATUS;"

This will identify if there has been a deadlock

### Varnish 503

You can check the health of the application using the following command:

```bash
~]# varnishadm backend.list
200
Backend name   Admin    Probe    Health
boot.default   probe    10/10    healthy
```

This is the typical configuration for the healthcheck:
https://docs.ukfast.co.uk/ecommercestacks/magento/magento2/varnish/varnish.html#health-check

### Permissions

Make sure the ownership for the data with the document root is "websiteuser:websiteuser"

To change the ownership you can run the following command:

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
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security, eCommerce
```
