# .php File allow list

The Magento 2 Nginx configuration file has an allow list (List of allowed file names) to be passed to PHP-FPM. This guide is intended to show you how to add a new filename to the allow list.

We are going to use testfile.php as the example new php file we are trying to add to the Nginx allow list.

If you have created a new file within your Magento 2 website and you are getting a 404 when trying to access the file:

```bash
 ~]$ curl -I www.example.com/testfile.php
 HTTP/1.1 404 Not Found
```

First ensure the new file is in the pub folder within the document root. All files and folders outside of the pub folder are not publicly accessible. Example pub folder:

```bash
/var/www/vhosts/example.com/htdocs/pub/
```

Second, add the new filename to the Nginx domain configuration file:

```bash
~]$ vim /etc/nginx/conf.d/example.com.conf

# PHP entry point for main application (Define files to be executed)
 location ~ (index|get|static|report|404|503|health_check|testfile)\.php$ {
  try_files $uri =404;
  fastcgi_pass examplecombackend;
  fastcgi_buffers 1024 4k;
  fastcgi_read_timeout 600s;
  fastcgi_connect_timeout 600s;
  fastcgi_index index.php;
  fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
  include fastcgi_params;
}
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

You should now be able to access the new file without any issues:

```bash
 ~]$ curl -I www.example.com/testfile.php
 HTTP/1.1 200 OK
```

```eval_rst
  .. title:: Magento 2 .php File allow list
  .. meta::
     :title: Magento 2 .php File allow list | UKFast Documentation
     :description: A guide to adding new php filenames to the Nginx allow list
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, eCommerce

