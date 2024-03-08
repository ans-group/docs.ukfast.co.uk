# PHP

### Create Backup

If you have PHP already installed and would like to take a backup of the configuration files, you can run the following (You can copy and paste the whole block below into your SSH terminal):

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

### Ubuntu

You can find our PHP guide for Ubuntu [here](php_ubuntu)

### Remi Repository

We use the Remi YUM repository for PHP. You can install the Remi repository with the command:

#### CentOS 8

```bash
dnf install https://rpms.remirepo.net/enterprise/remi-release-8.rpm
```

#### CentOS 7

```bash
wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm && rpm -Uvh remi-release-7.rpm && rm -f remi-release-7.rpm
```

### Install / Downgrade

If you are installing or downgrading PHP you need to remove PHP from the server and then follow the install guide below. We can remove PHP with the command:

We highly recommend taking a backup before running this command (See PHP Backup above)

```bash
yum remove "php*"
```

### Install PHP

This includes the PHP modules required by Magento 2.

#### PHP 7.3

```bash
yum install --disablerepo='*' --enablerepo=base,remi-php73,remi,epel,updates php php-pecl-mcrypt php-pdo php-mysqlnd php-opcache php-xml php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap php-sodium libsodium
```

#### PHP 7.4

```bash
yum install --disablerepo='*' --enablerepo=base,remi-php74,remi,epel,updates php php-pecl-mcrypt php-pdo php-mysqlnd php-opcache php-xml php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap php-sodium libsodium
```

#### PHP 8.1

```bash
yum install --disablerepo='*' --enablerepo=base,remi-php81,remi,epel,updates php php-pecl-mcrypt php-pdo php-mysqlnd php-opcache php-xml php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap php-sodium libsodium
```

#### PHP 8.2

```bash
yum install --disablerepo='*' --enablerepo=base,remi-php82,remi,epel,updates php php-pecl-mcrypt php-pdo php-mysqlnd php-opcache php-xml php-gd php-devel php-mysql php-intl php-mbstring php-bcmath php-json php-iconv php-pecl-redis php-fpm php-zip php-soap php-sodium libsodium
```
### Update PHP

You can perform an update of PHP with the following command depending on the desired version:

#### PHP 7.3

```bash
yum update --disablerepo='*' --enablerepo=base,remi-php73,remi,epel,updates 'php-*'
```

#### PHP 7.4

```bash
yum update --disablerepo='*' --enablerepo=base,remi-php74,remi,epel,updates 'php-*'
```

#### PHP 8.1

```bash
yum update --disablerepo='*' --enablerepo=base,remi-php81,remi,epel,updates 'php-*'
```

#### PHP 8.2

```bash
yum update --disablerepo='*' --enablerepo=base,remi-php82,remi,epel,updates 'php-*'
```

If any of the following packages are updated as dependencies, NGINX will require a restart after updating PHP

* `curl`
* `nss`
* `openssl`
* `libcurl`

You can restart NGINX with the commands:

```bash
nginx -t
systemctl restart nginx
```

### OPcache Setting

Review and then apply the OPcache settings (Simply copy and paste the entire block below):

```bash
sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=0/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=1/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/opcache.save_comments=0/opcache.save_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=1/opcache.load_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=0/opcache.load_comments=1/g' /etc/php.d/*opcache.ini
sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/php.d/*opcache.ini
```

You can find more information on OPcache [here](/ecommercestacks/magento/magento2/opcache/opcache/index#stack-opcache-settings)

### `/etc/php.ini` Settings

Review and copy the settings from `/root/php_upgrade_backup-$(date +%d_%b_%Y)/php.ini` to `/etc/php.ini`. Alternatively use our standard settings for the `php.ini` file. You can copy and paste the whole block below into your SSH terminal:

```bash
cp /etc/php.ini /root/php.ini.default
sed -ie "s_;date.timezone =_date.timezone = \"Europe/London\"_g" /etc/php.ini
sed -ie "s/; max_input_vars = 1000/max_input_vars = 20000/g" /etc/php.ini
sed -ie "s/;max_input_vars = 1000/max_input_vars = 20000/g" /etc/php.ini
sed -ie "s/memory_limit = 128M/memory_limit = 2G/" /etc/php.ini
sed -ie "s/memory_limit = 512M/memory_limit = 2G/" /etc/php.ini
sed -ie "s/max_execution_time = 30/max_execution_time = 18000/" /etc/php.ini
sed -ie "s/max_input_time = 60/max_input_time = 90/" /etc/php.ini
sed -ie "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini
sed -ie "s/;always_populate_raw_post_data = On/always_populate_raw_post_data = -1/" /etc/php.ini
sed -ie "s/expose_php = On/expose_php = Off/" /etc/php.ini
sed -ie "s/upload_max_filesize = 2M/upload_max_filesize = 8M/" /etc/php.ini
sed -ie "s/zlib.output_compression = Off/zlib.output_compression = On/" /etc/php.ini
echo "suhosin.session.cryptua = off" >> /etc/php.ini
```

### PHP-FPM Default Pool

Stop the default PHP-FPM pool (`www`) from running with the command:

```bash
echo ";Default file, please don't remove" > /etc/php-fpm.d/www.conf
```

### Start `PHP-FPM`

#### Configuration Test

Run a configuration test of PHP-FPM before starting:

```bash
php-fpm -t
[21-Aug-2019 07:53:29] NOTICE: configuration file /etc/php-fpm.conf test is successful
```

#### Start and Enable On Boot

You can start and enable `PHP-FPM` on boot:

```bash
systemctl enable --now php-fpm
```

### New Relic

You can enable or disable New Relic per domain be editing the `php-fpm` configuration file for the given domain:

```bash
php_flag[newrelic.enabled] = off
```

You can also set the New Relic APM name:

```bash
php_value[newrelic.appname] = "My App 1"
```

Further information on how to configure New Relic with `PHP-FPM` can be found in the following New Relic documentation:
https://docs.newrelic.com/docs/agents/php-agent/configuration/php-directory-ini-settings/

```eval_rst
  .. title:: Magento2 PHP
  .. meta::
     :title: Magento2 PHP | ANS Documentation
     :description: A guide to using PHP on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, PHP, eCommerce, NewRelic
```
