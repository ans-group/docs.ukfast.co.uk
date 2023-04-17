# Multiple PHP Installations

### Install Additional PHP Version

#### PHP 7.3

```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php73-php php73-php-pecl-mcrypt php73-php-pdo php73-php-mysqlnd php73-php-opcache php73-php-xml php73-php-gd php73-php-devel php73-php-mysql php73-php-intl php73-php-mbstring php73-php-bcmath php73-php-json php73-php-iconv php73-php-pecl-redis php73-php-fpm php73-php-zip php73-php-soap php73-php-sodium libsodium
```

#### PHP 7.4

```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php74-php php74-php-pecl-mcrypt php74-php-pdo php74-php-mysqlnd php74-php-opcache php74-php-xml php74-php-gd php74-php-devel php74-php-mysql php74-php-intl php74-php-mbstring php74-php-bcmath php74-php-json php74-php-iconv php74-php-pecl-redis php74-php-fpm php74-php-zip php74-php-soap php74-php-sodium libsodium
```

#### PHP 8.1

```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php81-php php81-php-pecl-mcrypt php81-php-pdo php81-php-mysqlnd php81-php-opcache php81-php-xml php81-php-gd php81-php-devel php81-php-mysql php81-php-intl php81-php-mbstring php81-php-bcmath php81-php-json php81-php-iconv php81-php-pecl-redis php81-php-fpm php81-php-zip php81-php-soap php81-php-sodium libsodium
```

#### PHP 8.2

```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php82-php php82-php-pecl-mcrypt php82-php-pdo php82-php-mysqlnd php82-php-opcache php82-php-xml php82-php-gd php82-php-devel php82-php-mysql php82-php-intl php82-php-mbstring php82-php-bcmath php82-php-json php82-php-iconv php82-php-pecl-redis php82-php-fpm php82-php-zip php82-php-soap php82-php-sodium libsodium
```

### Apply Magento 2 PHP optimisations

Simply copy and paste the below:

```bash
sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=0/opcache.save_comments=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=1/opcache.save_comments=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/opcache.save_comments=0/opcache.save_comments=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=1/opcache.load_comments=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=0/opcache.load_comments=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/opt/remi/php*/php.d/*opcache.ini
sed -ie "s_;date.timezone =_date.timezone = "Europe/London"_g" /etc/opt/remi/php*/php.ini
sed -ie "s/; max_input_vars = 1000/max_input_vars = 20000/g" /etc/opt/remi/php*/php.ini
sed -ie "s/;max_input_vars = 1000/max_input_vars = 20000/g" /etc/opt/remi/php*/php.ini
sed -ie "s/memory_limit = 128M/memory_limit = 756M/" /etc/opt/remi/php*/php.ini
sed -ie "s/memory_limit = 512M/memory_limit = 756M/" /etc/opt/remi/php*/php.ini
sed -ie "s/max_execution_time = 30/max_execution_time = 18000/" /etc/opt/remi/php*/php.ini
sed -ie "s/max_input_time = 60/max_input_time = 90/" /etc/opt/remi/php*/php.ini
sed -ie "s/short_open_tag = Off/short_open_tag = On/" /etc/opt/remi/php*/php.ini
sed -ie "s/;always_populate_raw_post_data = On/always_populate_raw_post_data = -1/" /etc/opt/remi/php*/php.ini
sed -ie "s/expose_php = On/expose_php = Off/" /etc/opt/remi/php*/php.ini
sed -ie "s/upload_max_filesize = 2M/upload_max_filesize = 8M/" /etc/opt/remi/php*/php.ini
sed -ie "s/zlib.output_compression = Off/zlib.output_compression = On/" /etc/opt/remi/php*/php.ini
echo ";Default" | tee /etc/opt/remi/php*/php-fpm.d/www.conf > /dev/null
echo "suhosin.session.cryptua = off" | tee -a /etc/opt/remi/php*/php.ini > /dev/null
```

### Configure PHP-FPM

#### Copy Original PHP-FPM Configuration File(s)

We recommend you only copy the domain(s) configuration file you want to use the additional PHP version. We are using version 7.2 in this example:

```bash
cp /etc/php-fpm.d/examplecom.conf /etc/opt/remi/php72/php-fpm.d/examplecom.conf
```
#### Edit The Copied File(s)

Ensure you change the following lines in the copied PHP-FPM configuration file, using your desired version of PHP (Using version 7.2 in this example):

```ini
[examplecom82]
listen = '/var/run/php-fpm-examplecom82.sock'
slowlog = /var/www/vhosts/example.com/example.com-phpfpm-slow82.log
php_admin_value[error_log] = /var/www/vhosts/example.com/example.com-phpfpm-error82.log
```

### PHP-FPM configuration check

Using 7.2 in this example:

```bash
/opt/remi/php82/root/sbin/php-fpm -t
NOTICE: configuration file /etc/opt/remi/php82/php-fpm.conf test is successful
```

### Start and Enable

Using 8.2 in this example:

```bash
systemctl daemon-reload
systemctl enable --now php82-php-fpm
```

### Reload

If you make a configuration change to one of the PHP-FPM configuration files, perform a config test and then reload with the command (Using 7.2 in this example)

```bash
systemctl reload php82-php-fpm
```

### NGINX VirtualHost Change

Change the sock file in NGINX so the domain(s) use the desired version of PHP. We are using 8.2 in this example and editing the file `/etc/nginx/conf.d/example.com.conf`:

```nginx
# Define the PHP-FPM socket file for nginx to proxy-pass to
upstream examplecombackend {
    server unix:/var/run/php-fpm-examplecom82.sock;
}
```

Following this you will need to test the NGINX configuration and reload the service:

```bash
nginx -t && nginx -s reload
```

### Checking Running PHP Installations

You can find out which PHP-FPM versions are running on the server with the following command:

```bash
ps awux | grep php | grep master
```

Example:

```bash
~]# ps awux | grep php | grep master
root     16718  0.0  0.2 934204 22708 ?        Ss   Jul03   8:39 php-fpm: master process (/etc/php-fpm.conf)
root     25623  0.1  0.3 519820 31280 ?        Ss   15:00   0:00 php-fpm: master process (/etc/opt/remi/php81/php-fpm.conf)
root     25761  4.0  0.2 535516 17496 ?        Ss   15:02   0:00 php-fpm: master process (/etc/opt/remi/php82/php-fpm.conf)
```

### Checking Installed PHP Versions

You can review the installed PHP versions with the command:

```bash
rpm -qa | grep php-common
```

Example:

```bash
~]# rpm -qa | grep php-common
php70-php-common-7.0.33-13.el7.remi.x86_64
php-common-7.2.19-2.el7.remi.x86_64
php73-php-common-7.3.9-1.el7.remi.x86_64
```

### Magento2 CLI

Using 8.2 in this example:

```bash
php82 bin/magento cache:status
```

### Uninstalling  Additional PHP Version

Example using PHP 8.2

```bash
yum remove --disablerepo='*' --enablerepo=base,remi,epel,updates php82-*
```

```eval_rst
  .. title:: Magento 2 Multiple PHP Installations
  .. meta::
     :title: Magento 2 Multiple PHP Installations | UKFast Documentation
     :description: A guide to installing and running multiple versions of PHP
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, php-fpm, php, eCommerce
```
