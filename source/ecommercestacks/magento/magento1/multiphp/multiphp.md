# Multiple PHP Installations

### Install Additional PHP Version

*To remove an additional PHP installation simply replace 'install' with 'remove' in the commands below.*

#### PHP 5.6
```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php56-php php56-php-mcrypt php56-php-pdo php56-php-mysqlnd php56-php-opcache php56-php-xml php56-php-gd php56-php-devel php56-php-mysql php56-php-intl php56-php-mbstring php56-php-bcmath php56-php-json php56-php-iconv php56-php-pecl-redis php56-php-fpm php56-php-zip php56-php-soap
```

#### PHP 7.0
```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php70-php php70-php-mcrypt php70-php-pdo php70-php-mysqlnd php70-php-opcache php70-php-xml php70-php-gd php70-php-devel php70-php-mysql php70-php-intl php70-php-mbstring php70-php-bcmath php70-php-json php70-php-iconv php70-php-pecl-redis php70-php-fpm php70-php-zip php70-php-soap
```

#### PHP 7.1
```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php71-php php71-php-mcrypt php71-php-pdo php71-php-mysqlnd php71-php-opcache php71-php-xml php71-php-gd php71-php-devel php71-php-mysql php71-php-intl php71-php-mbstring php71-php-bcmath php71-php-json php71-php-iconv php71-php-pecl-redis php71-php-fpm php71-php-zip php71-php-soap
```

#### PHP 7.2
```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php72-php php72-php-pecl-mcrypt php72-php-pdo php72-php-mysqlnd php72-php-opcache php72-php-xml php72-php-gd php72-php-devel php72-php-mysql php72-php-intl php72-php-mbstring php72-php-bcmath php72-php-json php72-php-iconv php72-php-pecl-redis php72-php-fpm php72-php-zip php72-php-soap
```

#### PHP 7.3
```bash
yum install --disablerepo='*' --enablerepo=base,remi,epel,updates php73-php php73-php-pecl-mcrypt php73-php-pdo php73-php-mysqlnd php73-php-opcache php73-php-xml php73-php-gd php73-php-devel php73-php-mysql php73-php-intl php73-php-mbstring php73-php-bcmath php73-php-json php73-php-iconv php73-php-pecl-redis php73-php-fpm php73-php-zip php73-php-soap
```

### Apply Magento PHP optimizations
Simply copy and paste the below:
```bash
sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -i 's/;opcache.save_comments=1/opcache.save_comments=0/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -i 's/;opcache.load_comments=1/opcache.load_comments=0/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/opt/remi/php??/php.d/*opcache.ini
sed -ie "s_;date.timezone =_date.timezone = \"Europe/London\"_g" /etc/opt/remi/php??/php.ini
sed -ie "s/; max_input_vars = 1000/max_input_vars = 20000/g" /etc/opt/remi/php??/php.ini
sed -ie "s/memory_limit = 128M/memory_limit = 512M/" /etc/opt/remi/php??/php.ini
sed -ie "s/max_execution_time = 30/max_execution_time = 1800/" /etc/opt/remi/php??/php.ini
sed -ie "s/max_input_time = 60/max_input_time = 90/" /etc/opt/remi/php??/php.ini
sed -ie "s/short_open_tag = Off/short_open_tag = On/" /etc/opt/remi/php??/php.ini
sed -ie "s/;always_populate_raw_post_data = On/always_populate_raw_post_data = -1/" /etc/opt/remi/php??/php.ini
sed -ie "s/expose_php = On/expose_php = Off/" /etc/opt/remi/php??/php.ini
sed -ie "s/upload_max_filesize = 2M/upload_max_filesize = 8M/" /etc/opt/remi/php??/php.ini
echo ";Default" > /etc/opt/remi/php??/php-fpm.d/www.conf
```

### Configure PHP-FPM

#### Copy Original PHP-FPM Configuration File(s)
We recommend you only copy the domain(s) configuration file you want to use the additional PHP version. We are using version 7.2 in this example:
```bash
cp /etc/php-fpm.d/examplecom.conf /etc/opt/remi/php72/php-fpm.d/examplecom.conf
```
#### Edit The Copied File(s) 
Ensure you change the following lines in the copied PHP-FPM configuration file, using your desired version of PHP (Using version 7.2 in this example):

```bash
[examplecom72]
listen = '/var/run/php-fpm-examplecom72.sock'
slowlog = /var/www/vhosts/example.com/example.com-phpfpm-slow72.log
php_admin_value[error_log] = /var/www/vhosts/example.com/example.com-phpfpm-error72.log
```

### PHP-FPM configuration check
Using 7.2 in this example:
```bash
/opt/remi/php72/root/sbin/php-fpm -t
NOTICE: configuration file /etc/opt/remi/php72/php-fpm.conf test is successful
```

### Start and Enable
Using 7.2 in this example:
```bash
systemctl daemon-reload
systemctl enable --now php72-php-fpm
```

### Reload
If you make a configuration change to one of the php-fpm configuration files, perform a config test and then reload with the command (Using 7.2 in this example)
```bash
systemctl reload php72-php-fpm
```

### Nginx vHost Change
Change the sock file in Nginx so the domain(s) use the desired version of PHP. We are using 7.2 in this example and editing the file /etc/nginx/conf.d/example.com.conf:

```bash
# Define the PHP-FPM socket file for nginx to proxy-pass to
upstream examplecombackend {
    server unix:/var/run/php-fpm-examplecom72.sock;
}
```

### Checking Running PHP Installations
You can find out which PHP-FPM versions are running on the server with the following command:
```bash
~]# ps awux | grep php | grep master
root     16718  0.0  0.2 934204 22708 ?        Ss   Jul03   8:39 php-fpm: master process (/etc/php-fpm.conf)
root     25623  0.1  0.3 519820 31280 ?        Ss   15:00   0:00 php-fpm: master process (/etc/opt/remi/php70/php-fpm.conf)
root     25761  4.0  0.2 535516 17496 ?        Ss   15:02   0:00 php-fpm: master process (/etc/opt/remi/php73/php-fpm.conf)
```

### Checking Installed PHP Versions
You can review the installed PHP versions with the command:
```bash
~]# rpm -qa | grep php-common
php70-php-common-7.0.33-13.el7.remi.x86_64
php-common-7.2.19-2.el7.remi.x86_64
php73-php-common-7.3.9-1.el7.remi.x86_64
```

### Magento Crons
Using 7.2 in this example, you can define the PHP binary for the Magento crons like so:
```bash
-bash-4.2$ crontab -l
* * * * * /opt/remi/php72/root/bin/php /path/to/magento/cron.sh cron.php -mdefault
```

```eval_rst
  .. title:: Magento Multiple PHP Installations
  .. meta::
     :title: Magento Multiple PHP Installations | UKFast Documentation
     :description: A guide to installing and running multiple versions of PHP
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, php-fpm, php
