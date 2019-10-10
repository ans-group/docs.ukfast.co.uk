# APCu

### Version Check
You can check the version of OPcache installed with the command:

```bash
~]# php -v | grep -i opcache
    with Zend OPcache v7.2.19, Copyright (c) 1999-2018, by Zend Technologies
```

### Module Check
You can confirm the module has been loaded:

```bash
~]# php -m | grep -i opcache
Zend OPcache
```

### Flush APCu
#### Service Reload
You can flush APCu with a reload of the php-fpm service, always run a configuration test before reloading

```bash
~]# php-fpm -t
[19-Aug-2019 08:48:54] NOTICE: configuration file /etc/php-fpm.conf test is successful
~]# systemctl reload php-fpm
```

#### PHP Function
You can also clear OPcache using the PHP function:

```bash
<?php
 if (extension_loaded('apcu')) {
    echo "APCu cache: " . apcu_clear_cache() . "\n";
 }
?>
```

### Stack APCu settings
We use the following sed to change the default settings of APCu on our Shopware stacks:

```bash
sed -i 's/;apc.shm_size=32M/apc.shm_size=512M/g' /etc/php.d/*apcu.ini
```

```eval_rst
  .. meta::
     :title: Shopware APCu | UKFast Documentation
     :description: A guide to using APCu on our Shopware optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Shopware, APCu, eCommerce

