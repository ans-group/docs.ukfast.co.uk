# WordPress in a Subdirectory

If you have WordPress in a sub directory within your Magento 1 document root you will need to edit your domains NGINX configuration (Example: `/etc/nginx/conf.d/example.com.conf`).

For this example we have WordPress in the sub directory `/var/www/vhosts/example.com/htdocs/wp/`. You need to replace the two instances of `replacemebackend` with the PHP-FPM configuration pool name. This should be defined at the top of your NGINX configuration file.

```bash
location ~ ^/wp/ {
        index index.php index.html index.htm;
        try_files $uri $uri/ @wphandler;
        expires 30d;

        location ~* \.(ico|jpg|jpeg|png|gif|svg|js|css|swf|eot|ttf|otf|woff|woff2)$ {
                add_header Cache-Control "public";
                add_header X-Frame-Options "SAMEORIGIN";
                expires +1y;
                try_files $uri $uri/ /get.php?$args;
        }

        location ~* /(wp-admin/|wp-login\.php) {
                  try_files $uri $uri/ @wphandler;
                  index index.html index.htm index.php;
                  fastcgi_pass replacemebackend;

                  add_header Cache-Control "no-store";
                  fastcgi_buffers 1024 4k;
                  #fastcgi_param HTTPS $my_https; # Uncomment the below for SSL offloading
                  #fastcgi_param SERVER_PORT $my_port; # Uncomment the below for SSL offloading
                  fastcgi_read_timeout 600s;
                  fastcgi_connect_timeout 600s;
                  fastcgi_index index.php;
                  fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                  include fastcgi_params;
        }

        location ~* \.php$ {
                try_files $uri $uri/ =404;
                fastcgi_pass replacemebackend;
               #fastcgi_param HTTPS $my_https; # Uncomment the below for SSL offloading
               #fastcgi_param SERVER_PORT $my_port; # Uncomment the below for SSL offloading
                include fastcgi_params;
                fastcgi_index index.php;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
        }
  }

  location @wphandler {
        rewrite / /wp/index.php;
  }
```

To implement this change you need to reload the NGINX service. First perform a configuration test with the following command:

```bash
 ~]$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If there are no errors in the configuration test proceed to reload the NGINX service with the following command:

```bash
 ~]$ nginx -s reload
```

```eval_rst
  .. title:: Magento 1 WordPress in a Sub Directory
  .. meta::
     :title: Magento 1 WordPress in a Sub Directory | UKFast Documentation
     :description: A guide to adding WordPress NGINX configuration when running WordPress in a sub directory
     :keywords: ukfast, linux, permissions, nginx, install, centos, cloud, lamp, server, virtual, WordPress, Magento
```
