# OPcache

OPcache will cache `.php` and `.phtml` files within your WooCommerce application. Therefore you should add flushing OPcache to your deployment process.

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

### Flush OPcache

#### Service Reload

You can flush OPcache with a reload of the PHP-FPM service, always run a configuration test before reloading

```bash
~]# php-fpm -t
[19-Aug-2019 08:48:54] NOTICE: configuration file /etc/php-fpm.conf test is successful
~]# systemctl reload php-fpm
```

#### PHP Function

You can also clear OPcache using the PHP function:

```php
<?php
 opcache_reset();
?>
```

### Stack OPcache settings

We use the following `sed` to change the default settings of OPcache on our Shopware stacks:

```bash
sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=10000/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.fast_shutdown=0/opcache.fast_shutdown=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.validate_timestamps=1/opcache.validate_timestamps=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.revalidate_freq=2/opcache.revalidate_freq=60/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/php.d/*opcache.ini
```

This changes the values to:

```ini
opcache.memory_consumption=512
pcache.interned_strings_buffer=12
opcache.max_accelerated_files=10000
opcache.fast_shutdown=1
opcache.validate_timestamps=1
opcache.revalidate_freq=60
opcache.enable_file_override=1
```

### OPcache GUI

The OPcache GUI [https://github.com/amnuts/opcache-gui](https://github.com/amnuts/opcache-gui) is a very handy tool which allows you to flush cache, view the files in cache, memory statistics and lots more. You simply need to download the files to your document root:

```bash
~]# cd /var/www/vhosts/woocommercedomain.com/htdocs/pub/
~]# git clone https://github.com/amnuts/opcache-gui
~]# chown -R woocommerceuser: opcache-gui
```

You can then browse `www.shopwaredomain.com/opcache-gui`. We recommend password / IP redirection for this URI. You can do this following our guide on [restricting file access](/ecommercestacks/magento/magento2/restrictfilefolder)

```eval_rst
  .. title:: WooCommerce Opcache
  .. meta::
     :title: WooCommerce Opcache | ANS Documentation
     :description: A guide to using Opcache on our WooCommerce optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, WooCommerce, Opcache, eCommerce
```
