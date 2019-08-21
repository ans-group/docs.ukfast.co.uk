# PHP

### PHP Backup
If you have PHP already installed and would like to take a backup of the configuration files, you can run the follolwing:

```bash
mkdir /root/php_upgrade_backup-$(date +%d_%b_%Y)
php -v > /root/php_upgrade_backup-$(date +%d_%b_%Y)/version
php -m > /root/php_upgrade_backup-$(date +%d_%b_%Y)/modules
php -i > /root/php_upgrade_backup-$(date +%d_%b_%Y)/info
rpm -qa | grep -i php > /root/php_upgrade_backup-$(date +%d_%b_%Y)/rpms
cp -r /etc/php.d/ /root/php_upgrade_backup-$(date +%d_%b_%Y)/
cp -r /etc/php-fpm.conf /root/php_upgrade_backup-$(date +%d_%b_%Y)/
cp -r /etc/php-fpm.d/ /root/php_upgrade_backup-$(date +%d_%b_%Y)/
cp /etc/php.ini /root/php_upgrade_backup-$(date +%d_%b_%Y)/
```

### Remi Repository
We use the remi yum repository for PHP. You can install the remi repoistory with the command:

#### CentOS 7
```bash
~]# wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm && rpm -Uvh remi-release-7.rpm && rm -f remi-release-7.rpm
```

#### CentOS 7
```bash
~]# wget http://rpms.remirepo.net/enterprise/remi-release-6.rpm && rpm -Uvh remi-release-6.rpm && rm -f remi-release-6.rpm
```

### Upgrade/Download
If you are upgrading or downgrading a major version of PHP you need to remove PHP from the server and then follow the install guide below. We can remove PHP with the command:

We highly recommend taking a backup before running this command (See PHP Backup above)

```bash
~]# yum remove '*php*'
```

### Install PHP
This includes the PHP modules needed by Magento. If you are replacing another version of PHP you should review the backup file /root/php_upgrade_backup-$(date +%d_%b_%Y)/modules taken above. If there are any additional modules to the list before, simply add them to the command.

#### PHP 5.5
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php55,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```
#### PHP 5.6
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php56,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```
#### PHP 7.0
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php70,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```
#### PHP 7.1
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php71,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```
#### PHP 7.2
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php72,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```
#### PHP 7.3
```bash
yum install --disablerepo='*' --enablerepo=base,remi-php73,remi,epel php php-pdo php-mysqlnd php-opcache php-xml php-mcrypt php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap 
```

### OPcache Setting
Review and then apply the OPcache settings outlined here: [https://docs.ukfast.co.uk/operatingsystems/linux/magento/magento1/opcache/opcache.html#stack-opcache-settings](https://docs.ukfast.co.uk/operatingsystems/linux/magento/magento1/opcache/opcache.html#stack-opcache-settings)

### /etc/php.ini Settings



```eval_rst
  .. meta::
     :title: Magento PHP | UKFast Documentation
     :description: A guide to using PHP on our Magento optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, PHP

