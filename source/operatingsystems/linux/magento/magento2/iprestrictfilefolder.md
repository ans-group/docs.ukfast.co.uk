# Magento 2 IP Restrict File/Folder

This guide is to show you how you can IP restrict a file or folder within your document root using Nginx.

We highly recommend IP restricting the Magento 2 admin URI so will use this as an example. You can achieve this with the following configuration options for Nginx:

```bash
# IP RESTRICTED URI 
location ~* ^/(index\.php/mageadmin|mageadmin) {
    index index.php;
    try_files $uri $uri/ @handler;
    allow 192.168.0.13; # Office IP Address
    allow 192.168.0.51; # Warehouse IP Address
    deny all;
    location ~* \.php$ {
      fastcgi_pass replacemebackend;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include fastcgi_params;
    }
  }
 ```

This location block can be placed anywhere within the server block of your Nginx configuration file. You need to edit replacemebackend with the PHP-FPM configuration pool name (This should be defined at the top of your Nginx configuration file).
 
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
  .. meta::
     :title: Magento 2 IP Restrict File/Folder | UKFast Documentation
     :description: A guide to IP restrict a file or folder within Nginx
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security

