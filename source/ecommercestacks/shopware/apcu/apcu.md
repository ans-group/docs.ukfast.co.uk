# APCu

### Version Check

You can check the version of APCu installed with the command:

```bash
~]# rpm -qa | grep -i apcu
php-pecl-apcu-5.1.17-1.el7.remi.7.2.x86_64
```

### Module Check

You can confirm the module has been loaded:

```bash
~]# php -m | grep -i APCu
apcu
```

### Flush APCu

#### Service Reload

You can flush APCu with a reload of the PHP-FPM service, always run a configuration test before reloading

```bash
~]# php-fpm -t
[19-Aug-2019 08:48:54] NOTICE: configuration file /etc/php-fpm.conf test is successful
~]# systemctl reload php-fpm
```

#### PHP Function

You can also clear APCu using the PHP function:

```php
<?php
 if (extension_loaded('apcu')) {
    echo "APCu cache: " . apcu_clear_cache() . "\n";
 }
?>
```

### APCu settings

We use the following `sed` to change the default settings of APCu on our Shopware stacks:

```bash
sed -i 's/;apc.shm_size=32M/apc.shm_size=512M/g' /etc/php.d/*apcu.ini
```

```eval_rst
  .. title:: Shopware APCu
  .. meta::
     :title: Shopware APCu | ANS Documentation
     :description: A guide to using APCu on our Shopware optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Shopware, APCu, eCommerce
```
