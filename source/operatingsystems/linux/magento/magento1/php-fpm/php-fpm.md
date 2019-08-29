# PHP-FPM

### Domain Error Log
The error log for your domain is located just outside of the document root:

```bash
/var/www/vhosts/magentodomain.com/magentodomain.com-phpfpm-error.log
```

This error log should be reviewed regularly as you may see PHP errors in this file.

### Domain Conf File
The PHP-FPM configuration pool for your domain is located in /etc/php-fpm.d/

```bash
/etc/php-fpm.d/magentodomaincom.conf
```

### PHP-FPM Error Log
The error log for the PHP-FPM service is:

```bash
/var/log/php-fpm/error.log
```

### PHP-FPM Conf File
The main configuration file for PHP-FPM is:

```bash
/etc/php-fpm.conf
```

This file has an include to /etc/php-fpm.d/*.conf:

```bash
~]# grep include /etc/php-fpm.conf
include=/etc/php-fpm.d/*.conf
```

```eval_rst
  .. meta::
     :title: Magento PHP-FPM | UKFast Documentation
     :description: A guide to using PHP-FPM on our Magento optimised stacks
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, PHP-FPM

