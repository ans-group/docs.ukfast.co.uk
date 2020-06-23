# Magento 1 in a Sub Directory

If you have Magento 1 in a sub directory within your document root you will need to edit your domain's Nginx configuration (Example: /etc/nginx/conf.d/example.com.conf). 

For this example we have Magento 1 in the sub directory /var/www/vhosts/example.com/htdocs/shop/. You need to replace the instance of replacemebackend with the PHP-FPM configuration pool name (This should be defined at the top of your Nginx configuration file) 

```bash
location ~ ^/shop/ {
  index index.php index.html index.htm;
  try_files $uri $uri/ @shophandler;
  expires 30d;

  location ~ (index|get|static|report|404|503)\.php$ {
  try_files $uri =404;
 #fastcgi_param MAGE_RUN_TYPE store;
 #fastcgi_param MAGE_RUN_CODE $magesite;

  fastcgi_pass replacemebackend;
  fastcgi_buffers 1024 4k;

  fastcgi_param PHP_FLAG "session.auto_start=off \n suhosin.session.cryptua=off";
  fastcgi_param PHP_VALUE "memory_limit=768M \n max_execution_time=600";
  fastcgi_read_timeout 600s;
  fastcgi_connect_timeout 600s;

  fastcgi_index index.php;
  fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
  include fastcgi_params;
     }
  }

  location @shophandler {rewrite / /shop/index.php; }
```

To implement this change you need to reload the Nginx service. First perform a configuration test with the following command:

```bash
 ~]$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If there are no errors in the configuration test proceed to reload the Nginx service with the following command:

```bash
 ~]$ nginx -s reload
```

```eval_rst
  .. title:: Magento 1 in a Sub Directory | UKFast Documentation
  .. meta::
     :title: Magento 1 in a Sub Directory | UKFast Documentation
     :description: A guide to adding Magento 1 Nginx configuration when running in a sub directory
     :keywords: ukfast, linux, permissions, nginx, install, centos, cloud, lamp, server, virtual, Magento
