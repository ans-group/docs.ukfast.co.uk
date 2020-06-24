# OPcache

OPcache will cache .php and .phtml files within your Magento2 application. Therefore you should add flushing OPcache to your deployment process.

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
You can flush OPcache with a reload of the php-fpm service, always run a configuration test before reloading

```bash
~]# php-fpm -t
[19-Aug-2019 08:48:54] NOTICE: configuration file /etc/php-fpm.conf test is successful
~]# systemctl reload php-fpm
```

#### PHP Function
You can also clear OPcache using the PHP function:

```bash
<?php
 opcache_reset();
?>
```

### Stack OPcache settings
We use the following sed to change the default settings of OPcache on our Magento1 stacks:

```bash
sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=0/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=1/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.save_comments=0/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=1/opcache.load_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/php.d/*opcache.ini
```

This changes the values to:

```bash
opcache.memory_consumption=512
pcache.interned_strings_buffer=12
opcache.max_accelerated_files=60000
opcache.save_comments=1
opcache.save_comments=1
opcache.enable_file_override=1
```

### OPcache GUI
The OPcache GUI [https://github.com/amnuts/opcache-gui](https://github.com/amnuts/opcache-gui) is a very handy tool which allows you to flush cache, view the files in cache, memory statistics and lots more. You simply need to download the files to your document root:

```bash
~]# cd /var/www/vhosts/magentodomain.com/htdocs/pub/
~]# git clone https://github.com/amnuts/opcache-gui
~]# chown -R magentouser: opcache-gui
```

You can then browse www.magentodomain.com/opcache-gui. We recommend password/ip redirection for this URI, we have guides on how to do this [here](/operatingsystems/linux/magento/magento2/restrictfilefolder)

```eval_rst
  .. title:: Magento2 Opcache
  .. meta::
     :title: Magento2 Opcache | UKFast Documentation
     :description: A guide to using Opcache on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Opcache, eCommerce

