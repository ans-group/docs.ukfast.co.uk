# Example configurations

Here are two example configurations using their own vhosts file.

```eval_rst
.. note::
   It's worth noting that these configuration files use the php-fpm setup described in the following document:
   - :doc:`/operatingsystems/linux/apache/phpfpm`
```

## First Domain

File name:

```bash
  /etc/httpd/conf.d/bobscarpets.net.conf
```

Contents:

```console
<VirtualHost *:80>
    ServerAdmin webmaster@bobscarpets.net
    DocumentRoot /var/www/vhosts/bobscarpets.net/htdocs
    ServerName bobscarpets.net
    ServerAlias www.bobscarpets.net
    ErrorLog logs/bobscarpets.net-error_log
    CustomLog logs/bobscarpets.net-access_log combined

    <Directory "/var/www/vhosts/bobscarpets.net/htdocs">
        Options FollowSymLinks
        AllowOverride All

        Order allow,deny
        Allow from all
    </Directory>

    <FilesMatch "\.php$">
        SetHandler "proxy:unix:/var/run/php-fcgi-bobscarpetsnet.sock|fcgi://127.0.0.1"
    </FilesMatch>
    ProxyTimeout 600
</VirtualHost>

<VirtualHost *:443>
    ServerAdmin webmaster@bobscarpets.net
    DocumentRoot /var/www/vhosts/bobscarpets.net/htdocs
    ServerName bobscarpets.net
    ServerAlias www.bobscarpets.net
    ErrorLog logs/bobscarpets.net-error_log
    CustomLog logs/bobscarpets.net-access_log combined

    SSLEngine on
    SSLProtocol all -SSLv2 -SSLv3 -TLSv1
    SSLCipherSuite ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS
    SSLCertificateFile /etc/pki/tls/certs/bobscarpets.net.crt
    SSLCertificateKeyFile /etc/pki/tls/private/bobscarpets.net.key

    <Directory "/var/www/vhosts/bobscarpets.net/htdocs">
        Options FollowSymLinks
        AllowOverride All

        Order allow,deny
        Allow from all
    </Directory>

    <FilesMatch "\.php$">
        SetHandler "proxy:unix:/var/run/php-fcgi-bobscarpetsnet.sock|fcgi://127.0.0.1"
    </FilesMatch>
    ProxyTimeout 600
</VirtualHost>
```

## Second Domain

File name:

```bash
  /etc/httpd/conf.d/getschwifty.org.conf
```

Contents:

```apacheconf
  <VirtualHost *:80>
      ServerAdmin webmaster@getschwifty.org
      DocumentRoot /var/www/vhosts/getschwifty.org/htdocs
      ServerName getschwifty.org
      ServerAlias www.getschwifty.org
      ErrorLog logs/getschwifty.org-error_log
      CustomLog logs/getschwifty.org-access_log combined

      <Directory "/var/www/vhosts/getschwifty.org/htdocs">
          Options FollowSymLinks
          AllowOverride All

          Order allow,deny
          Allow from all
      </Directory>

      <FilesMatch "\.php$">
          SetHandler "proxy:unix:/var/run/php-fcgi-getschwiftyorg.sock|fcgi://127.0.0.1"
      </FilesMatch>
      ProxyTimeout 600
  </VirtualHost>

  <VirtualHost *:443>
      ServerAdmin webmaster@getschwifty.org
      DocumentRoot /var/www/vhosts/getschwifty.org/htdocs
      ServerName getschwifty.org
      ServerAlias www.getschwifty.org
      ErrorLog logs/getschwifty.org-error_log
      CustomLog logs/getschwifty.org-access_log combined

      SSLEngine on
      SSLProtocol all -SSLv2 -SSLv3
      SSLCipherSuite ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS
      SSLCertificateFile /etc/pki/tls/certs/getschwifty.org.crt
      SSLCertificateKeyFile /etc/pki/tls/private/getschwifty.org.key

      <Directory "/var/www/vhosts/getschwifty.org/htdocs">
          Options FollowSymLinks
          AllowOverride All

          Order allow,deny
          Allow from all
      </Directory>

      <FilesMatch "\.php$">
          SetHandler "proxy:unix:/var/run/php-fcgi-getschwiftyorg.sock|fcgi://127.0.0.1"
      </FilesMatch>
      ProxyTimeout 600
  </VirtualHost>
```

```eval_rst
  .. title:: Example configurations for Apache
  .. meta::
     :title: Example configurations for Apache | ANS Documentation
     :description:  Some example configurations for the Apache web server
     :keywords: ukfast, apache, linux, config, configuration, web, server. virtual, vm, example
