# Composer

### Composer Setup

Download composer Installer 

```bash
~]# wget -O /tmp/composer-installer.php https://getcomposer.org/installer
```
Composer can be then installed with the following commands: 

#### Composer 1

```bash
~]# php /tmp/composer-installer.php --version=1.10.20 --filename=composer1 --install-dir=/usr/bin
```

#### Composer 2

```bash
~]# php /tmp/composer-installer.php --version=2.0.1 --filename=composer2 --install-dir=/usr/bin
```

Please make sure to update Composer 2 to the latest version: 

```bash
~]# php /usr/bin/composer2 self-update
```

#### Version Check

You can check the installed version of Composer with the command:

```bash
~]$ composer1  -V
Composer version 1.10.20 2021-01-27 15:41:06
```

```bash
~]$ composer2  -V
Composer version 2.1.3 2021-06-09 16:31:20
```

```eval_rst
.. warning::
   **Do not run Composer as the ``root`` user!**
```

```eval_rst
  .. title:: Magento Composer
  .. meta::
     :title: Magento Composer | UKFast Documentation
     :description: A guide to using Composer on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, composer, eCommerce
```
