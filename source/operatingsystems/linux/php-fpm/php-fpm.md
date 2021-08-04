# `PHP-FPM`

### Error Log

The error log for the `PHP-FPM` service is:

```bash
/var/log/php-fpm/error.log
```

### Config File

The main configuration file for `PHP-FPM` is:

```bash
`/etc/php-fpm.conf`
```

This file has an include to `/etc/php-fpm.d/*.conf`:

```ini
~]# grep include /etc/php-fpm.conf
include=/etc/php-fpm.d/*.conf
```

### Domain Error Log

The error log for your domain is located just outside of the document root:

```bash
/var/www/vhosts/domain.com/domain.com-phpfpm-error.log
```

This error log should be reviewed regularly as you may see `PHP` errors in this file.

### Domain Config File

The `PHP-FPM` configuration pool for your domain is located in `/etc/php-fpm.d/`

```bash
/etc/php-fpm.d/domaincom.conf
```
### Enable Core Dumps

Sometimes your application may generate a `SIGSEGV` error or similar. Within PHP-FPM, all we will see is a 502 error message. Enabling core dumps can help to debug these issues further.

If you need to enable core dumps you can run the below command:
```bash
echo '/tmp/core-%e.%p' > /proc/sys/kernel/core_pattern echo 0 > /proc/sys/kernel/core_uses_pid ulimit -c unlimited
```

Then set the `rlimit_core` directive in `/etc/php-fpm.d/domain.conf` to unlimited:
```bash
`rlimit_core = unlimited`
`sysctl fs.suid_dumpable=2`
```
Core dumps should be able to generate now. We will need debug software to read them:
```
`debuginfo-install php-fpm --enablerepo=remi,epel`
`yum install gdb`
```

Then run this to read a file where '2393' is the number at the end of the dump:
```
`gdb -x gdbCommands.txt   /usr/sbin/php-fpm /tmp/coredump-php-fpm.2393`
`bt`
```

```eval_rst
  .. title:: PHP-FPM
  .. meta::
     :title: PHP-FPM | UKFast Documentation
     :description: A guide to using PHP-FPM
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, PHP-FPM, eCommerce, Shopware
```
