# Changing your installed PHP version

When looking at your web stack, you may notice you are running on a version of PHP which is behind the latest one. Often, we might assume the best course of action would be to update to the latest version. For most software, that is true, however PHP versions are a little different. It can still be a good idea to update, but there are several things to consider before you do.

## Considerations before you upgrade

PHP is still being actively developed, and the developers have chosen not to maintain backwards compatibility. This means as the language changes, features which are no longer considered good practice, or have been superseded by faster or more secure versions are "deprecated". That means they are marked as deprecated, and eventually removed from the language entirely. If your application uses one of these deprecated features, it will stop working if you update PHP versions without also updating your application!

PHP.net provide a comprehensive list of these deprecated functions between each released version:

[5.2 > 5.3](http://php.net/manual/en/migration53.deprecated.php)
[5.3 > 5.4](http://php.net/manual/en/migration54.deprecated.php)
[5.4 > 5.5](http://php.net/manual/en/migration55.deprecated.php)
[5.5 > 5.6](http://php.net/manual/en/migration56.deprecated.php)
[5.6 > 7.0](http://php.net/manual/en/migration70.deprecated.php)
[7.0 > 7.1](http://php.net/manual/en/migration71.deprecated.php)
[7.1 > 7.2](http://php.net/manual/en/migration72.deprecated.php)

As you can see, there's a fair amount there which may cause your application to break under a new version of PHP. Due to this, we always recommend testing your application under the PHP version of choice before

Another thing to consider are your installed PHP modules. You'll want to check that you can have the same modules under the new interpreter version.

## How to upgrade on your system

Making the change to a different PHP interpreter version varies in difficulty depending on what type of server you have. Some are as easy as selecting a dropdown, while some require manually configuring the new version

### Plesk 12+

From version 12 onwards, Plesk has support for multiple PHP versions built in. Installing different versions is done via the Updates & Upgrades section, and changing between them is done by a dropdown menu in Plesk. This allows you to switch PHP versions quickly and easily. For more information please do take a look at [the official Plesk guide.](https://support.plesk.com/hc/en-us/articles/213949705-Multiple-PHP-Versions-in-Plesk-12-and-higher-Out-of-the-Box)

### WHM/cPanel

WHM/cPanel also supports multiple versions of PHP, if you are running EasyApache 4. PHP interpreter versions can be installed via EasyApache 4 and managed in WHM under Home >> Software >> MultiPHP Manager.

For more information please do take a look at [the official cPanel guide.](https://documentation.cpanel.net/display/68Docs/MultiPHP+Manager+for+WHM)

### UKFast Magento managed platform

If you have one of our Magento managed platforms, our support team will assist in changing the PHP version to what you require. Please just let us know by raising a support request and our engineers will arrange a time to make the change. Please do note that while we will make the change to the PHP version, your should still be testing your application beforehand to make sure your application will run on the requested PHP version.

### Standard Apache or Nginx server

If you expect to be changing PHP versions over the lifetime of your application we highly recommend a multi PHP environment. It is possible to do so without a control panel, but it is an involved process which requires downtime and carries risks.

```eval_rst
.. warning::
    This is an advanced process and you should only attempt this if you are very comfortable with setting up web stacks by hand. All code given here is for example only, please do not copy paste it directly as the process will vary depending on how your server is set up. The basic steps are the same but the commands will change in different setups.
```

The example here assumes you are using a CentOS 7 server and running PHP-FPM. If you run any other OS or do not use PHP-FPM, please adjust this to be suitable to your environment.

#### Backups
The first step is to ensure you have backups in place so should there be any issues you have a fallback. You can also take a copy of all your existing PHP configuration which may let you roll back

```bash
mkdir /root/php_upgrade_backup/
php -v > /root/php_upgrade_backup/version
php -m > /root/php_upgrade_backup/modules
php -i > /root/php_upgrade_backup/info
rpm -qa | grep -i php > /root/php_upgrade_backup/rpms
cp -r /etc/php.d/ /root/php_upgrade_backup/
cp -r /etc/php-fpm.conf /root/php_upgrade_backup/
cp -r /etc/php-fpm.d/ /root/php_upgrade_backup/
cp /etc/php.ini /root/php_upgrade_backup/
```

#### Remove the current PHP version and reinstall

We're working on a CentOS 7 server and we are going to install PHP 7.1 from the Remi repository. So first we'll install Remi (if it's not already present):
```bash
wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm && rpm -Uvh remi-release-7.rpm && rm -f remi-release-7.rpm
```

Now we need to remove all the existing PHP packages from the server:
```bash
yum remove '*php*'
```

And install the version we want, with all the modules needed:
```bash
yum install --enablerepo=remi-php71,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap
```

#### Reinstate old settings

Now we've removed and reinstalled a new version, we need to copy our previous settings into the new PHP version. We can use the backup we took earlier (/root/php_upgrade_backup/php.ini) to see all our previous values and copy those to the new php.ini using the editor of your choice:  

If we have custom pools set up in PHP-FPM, then we probably want to stop the default pool running, which we can do by blanking the default www.conf file:
```bash
echo ";Default file, please don't remove" > /etc/php-fpm.d/www.conf
```

#### Config test and start

Now that's set up, we can test the configuration, and start the PHP-FPM service.
```bash
php-fpm -t
service php-fpm start
```

And ensure that PHP-FPM will start on a system reboot:
```bash
systemctl enable php-fpm
```

You should then have your application running under the new version of PHP.

```eval_rst
  .. title:: Upgrading your PHP version | UKFast Documentation
  .. meta::
     :title: Upgrading your PHP version | UKFast Documentation
     :description: A guide to changing PHP verions
     :keywords: ukfast, php, install, update, upgrade, fpm, 5.4,5.5,5.6,7.0,7.1,7.2
