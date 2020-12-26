# Installing PHP modules

The default installation of php as described in [Installing PHP](/operatingsystems/linux/php/installation) will install the following php modules:

```console
[root@websrv ~]# php -m
[PHP Modules]
bz2
calendar
Core
ctype
curl
date
ereg
exif
fileinfo
filter
ftp
gettext
gmp
hash
iconv
json
libxml
mysql
mysqli
openssl
pcntl
pcre
PDO
pdo_mysql
pdo_sqlite
Phar
readline
Reflection
session
shmop
SimpleXML
sockets
SPL
sqlite3
standard
tokenizer
xml
zip
zlib
```

That's quite a lot of modules, thanks to `php-common`, but different websites often need different modules installing, and there are a couple of ways to install them.

## Package manager method

In the below example, we'll install the soap extension using the systems default package manager, `yum`.

After using `php -m` as above, we can see that soap is not in the list.

To install, use the following command:

```console
yum install php-soap
```

The format of that command could be changed to install different modules, so you could install `imap` or `snmp` with the following commands:

```console
yum install php-imap
```
```console
yum install php-snmp
```

After you've accepted this, the install will run and you can re-run `php -m` to confirm that the module is now in the list.

A restart of your webserver will be needed to load this new module in before your webserver can access it:

```console
service httpd restart
```

## Pecl

Some modules may not be available in your standard repositories, but fear not. As long as you have the `php-pear` package installed, you'll have access to `pear` and `pecl`, which are like package managers especially for php.

In this example, we'll be installing the memcache module for php.

The command to start it all off is:

```console
pecl install memcache
```

```eval_rst
   .. note::
      Using pecl will often need you to install a few dependencies.

      Which ones will depend on what's installed on your system already, but in the above example on a CentOS minimal install, I had to install ``gcc``, ``make`` and ``zlib-devel``
```

Pecl installs often ask a few questions during the install process. If you're not too sure what to put, hitting enter will accept the default value.

Once this has finished, you'll have to tell PHP where it can find it's new module, as the text on complete will tell you.

In the memcache example, the following line needs to be added to your php configuration:

```console
extension=memcache.so
```

This could just be added to the bottom of `/etc/php.ini`, but to keep things neat I opted to put it in the following file:

```console
/etc/php.d/memcache.ini
```

The file likely won't exist, and you can call it what you want as long as it ends in `.ini`

After you've done this, the install will run and you can re-run `php -m` to confirm that the module is now in the list.

A restart of your webserver will be needed to load this new module in before your webserver can access it:

```console
service httpd restart
```

```eval_rst
   .. title:: Installing PHP modules on Linux
   .. meta::
      :title: Installing PHP modules on Linux | UKFast Documentation
      :description: A guide to installing PHP modules on Linux
      :keywords: ukfast, linux, php, modules, guide, tutorial, install, file
```