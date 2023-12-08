# File/Directory Outside /pub

If you have a file/directory you want to be accessible but is outside of the Magento 2 pub directory you need to edit your domains NGINX configuration (Example: `/etc/nginx/conf.d/example.com.conf`).

### PHP Files

For this example we will use `info.php` which is located in `/var/www/vhosts/example.com/htdocs/`. This file will produce a 404 as it's not located in the pub directory (`/var/www/vhosts/example.com/htdocs/pub/`):

```bash
 ~]$ curl -I www.example.com/info.php
 HTTP/1.1 404 Not Found
```

You can add the following to the domains NGINX configuration file anywhere within the server block:

```bash
~]$ vim /etc/nginx/conf.d/example.com.conf

# info.php outside of the pub folder
location /info.php {
    try_files $uri $uri/;
    location ~* \.php$ {
      fastcgi_pass replacemebackend;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include fastcgi_params;
    }
  }
 ```

You need to edit `replacemebackend` with the PHP-FPM configuration pool name. This should be defined at the top of your NGINX configuration file.

You also need to add info to the `.php` file allow list. We have a guide for this [here](/ecommercestacks/magento/magento2/nginxphpfileallowlist)

### Text / XML

For this example we will use `sitemap.xml` which is located in `/var/www/vhosts/example.com/htdocs/`. This file will produce a 404 as it's not located in the pub directory (`/var/www/vhosts/example.com/htdocs/pub/`):

```bash
 ~]$ curl -I www.example.com/sitemap.xml
 HTTP/1.1 404 Not Found
```

You can add the following to the domains NGINX configuration file anywhere within the server block:

```bash
~]$ vim /etc/nginx/conf.d/example.com.conf

# sitemap.xml outside of the pub folder
location /sitemap.xml {
    root $MAGE_ROOT;
}
 ```

To implement this change you need to reload the NGINX service. First perform a configuration test with the following command:

```bash
 ~]$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If there are no errors in the configuration test, proceed to reload the NGINX service with the following command:

```bash
 ~]$ nginx -s reload
```

You should now be able to access `sitemap.xml` without any issues:

```bash
 ~]$ curl -I www.example.com/sitemap.xml
 HTTP/1.1 200 OK
```

```eval_rst
  .. title:: Magento 2 File/Directory Outside /pub
  .. meta::
     :title: Magento 2 File/Directory Outside /pub | ANS Documentation
     :description: A guide to adding Files/Directories to run outside /pub in NGINX
     :keywords: ukfast, linux, permissions, nginx, install, centos, cloud, lamp, server, virtual, WordPress, Magento, eCommerce
```
