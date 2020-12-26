# Magento 2 in a Sub Directory

If you have Magento 2 in a sub directory within your document root you will need to edit your domain's Nginx configuration (Example: /etc/nginx/conf.d/example.com.conf).

For this example we have Magento 2 in the sub directory /var/www/vhosts/example.com/htdocs/shop/. You need to replace the instance of replacemebackend with the PHP-FPM configuration pool name (This should be defined at the top of your Nginx configuration file)

```bash
location ~ ^/shop/static/version {
    expires max;

    # Remove signature of the static files that is used to overcome the browser cache
    location ~ ^/shop/static/version {
      rewrite ^/shop/static/(version\d*/)?(.*)$ /shop/static/$2 last;
    }

    location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
      add_header Cache-Control "public";
      add_header X-Frame-Options "SAMEORIGIN";
      expires +1y;

      if (!-f $request_filename) {
        rewrite ^/shop/static/(version\d*/)?(.*)$ /shop/static.php?resource=$2 last;
      }
    }

    location ~* \.(zip|gz|gzip|bz2|csv|xml)$ {
      add_header Cache-Control "no-store";
      add_header X-Frame-Options "SAMEORIGIN";
      expires off;

      if (!-f $request_filename) {
        rewrite ^/shop/static/(version\d*/)?(.*)$ /shop/static.php?resource=$2 last;
      }
    }

    if (!-f $request_filename) {
      rewrite ^/shop/static/(version\d*/)?(.*)$ /shop/static.php?resource=$2 last;
    }

    add_header X-Frame-Options "SAMEORIGIN";
  }

location ~ ^/shop/ {
  index index.php index.html index.htm;
  try_files $uri $uri/ @shophandler;
  expires 30d;

  location ~ (index|get|static|report|404|503|health_check)\.php$ {
    try_files $uri =404;
    fastcgi_pass replacemebackend;
    fastcgi_buffers 1024 4k;
    fastcgi_read_timeout 600s;
    fastcgi_connect_timeout 600s;

    #fastcgi_param HTTPS $my_https; # Uncomment the below for SSL offloading
    #fastcgi_param SERVER_PORT $my_port; # Uncomment the below for SSL offloading

    #fastcgi_param  MAGE_RUN_CODE <REPLACEME>; # Uncomment the below to set multistore run code
    #fastcgi_param  MAGE_RUN_TYPE store; # Uncomment the below to set multistore run type

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

If there are no errors in the configuration test proceed to reload the Nginx server with the following command:

```bash
 ~]$ nginx -s reload
```

```eval_rst
  .. title:: Magento 2 in a Sub Directory
  .. meta::
     :title: Magento 2 in a Sub Directory | UKFast Documentation
     :description: A guide to adding Magento 2 Nginx configuration when running in a sub directory
     :keywords: ukfast, linux, permissions, nginx, install, centos, cloud, lamp, server, virtual, Magento2, Magento, eCommerce
