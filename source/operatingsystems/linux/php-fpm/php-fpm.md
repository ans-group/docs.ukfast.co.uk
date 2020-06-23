# PHP-FPM

### Error Log
The error log for the PHP-FPM service is:

```bash
/var/log/php-fpm/error.log
```

### Conf File
The main configuration file for PHP-FPM is:

```bash
/etc/php-fpm.conf
```

This file has an include to /etc/php-fpm.d/*.conf:

```bash
~]# grep include /etc/php-fpm.conf
include=/etc/php-fpm.d/*.conf
```

### Domain Error Log
The error log for your domain is located just outside of the document root:

```bash
/var/www/vhosts/domain.com/domain.com-phpfpm-error.log
```

This error log should be reviewed regularly as you may see PHP errors in this file.

### Domain Conf File
The PHP-FPM configuration pool for your domain is located in /etc/php-fpm.d/

```bash
/etc/php-fpm.d/domaincom.conf
```

```eval_rst
  .. title:: PHP-FPM | UKFast Documentation
  .. meta::
     :title: PHP-FPM | UKFast Documentation
     :description: A guide to using PHP-FPM
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, PHP-FPM, eCommerce, Shopware

