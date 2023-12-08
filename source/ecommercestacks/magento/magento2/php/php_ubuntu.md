# Install PHP

Run the following script to install PHP on Ubuntu. Simply replace the version number for the variable `PHPVersion`.

```bash
vim php_install_script.sh
```

```bash
PHPVersion="8.1"

if [ ! "$(apt -q list --installed 2>/dev/null | grep php/$PHPVersion)" ]; then
 printf "Installing php/$PHPVersion...."
 apt-get -q install software-properties-common -y
 add-apt-repository ppa:ondrej/php -y
 apt-get -q update -y > /dev/null
 apt -qq install php$PHPVersion php$PHPVersion-common php$PHPVersion-gmp php$PHPVersion-curl php$PHPVersion-soap php$PHPVersion-bcmath php$PHPVersion-intl php$PHPVersion-mbstring php$PHPVersion-xmlrpc php$PHPVersion-mysql php$PHPVersion-gd php$PHPVersion-xml php$PHPVersion-cli php$PHPVersion-zip php$PHPVersion-fpm php$PHPVersion-opcache php$PHPVersion-memcache php$PHPVersion-memcached -y

  sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.memory_consumption=512/opcache.memory_consumption=512/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.save_comments=0/opcache.save_comments=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.save_comments=1/opcache.save_comments=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/opcache.save_comments=0/opcache.save_comments=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.load_comments=1/opcache.load_comments=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.load_comments=0/opcache.load_comments=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini
  sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/php/$PHPVersion/mods-available/*opcache.ini

  sed -i 's/opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.memory_consumption=128/opcache.memory_consumption=512/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/opcache.interned_strings_buffer=8/opcache.interned_strings_buffer=12/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/opcache.max_accelerated_files=4000/opcache.max_accelerated_files=60000/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.save_comments=0/opcache.save_comments=1/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.save_comments=1/opcache.save_comments=1/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/opcache.save_comments=0/opcache.save_comments=1/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.load_comments=1/opcache.load_comments=1/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.load_comments=0/opcache.load_comments=1/g' /etc/php/$PHPVersion/fpm/php.ini
  sed -i 's/;opcache.enable_file_override=0/opcache.enable_file_override=1/g' /etc/php/$PHPVersion/fpm/php.ini

  sed -ie "s_;date.timezone =_date.timezone = "Europe/London"_g" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/; max_input_vars = 1000/max_input_vars = 20000/g" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/;max_input_vars = 1000/max_input_vars = 20000/g" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/memory_limit = 128M/memory_limit = 756M/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/memory_limit = 512M/memory_limit = 756M/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/max_execution_time = 30/max_execution_time = 18000/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/max_input_time = 60/max_input_time = 90/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/short_open_tag = Off/short_open_tag = On/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/;always_populate_raw_post_data = On/always_populate_raw_post_data = -1/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/expose_php = On/expose_php = Off/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/upload_max_filesize = 2M/upload_max_filesize = 8M/" /etc/php/$PHPVersion/fpm/php.ini
  sed -ie "s/zlib.output_compression = Off/zlib.output_compression = On/" /etc/php/$PHPVersion/fpm/php.ini
  echo "suhosin.session.cryptua = off" >> /etc/php/$PHPVersion/fpm/php.ini
  echo ";Default" > /etc/php/$PHPVersion/fpm/pool.d/www.conf
  systemctl daemon-reload > /dev/null 2>&1
  systemctl -q enable php/$PHPVersion-fpm.service
fi

rm -f $0
echo "File: $0 removed"
```

```bash
bash php_install_script.sh
```

```eval_rst
  .. title:: Magento2 PHP Ubuntu
  .. meta::
     :title: Magento2 PHP Ubuntu | ANS Documentation
     :description: A guide to installing PHP on Ubuntu for our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, PHP, eCommerce, NewRelic, Ubuntu
```
