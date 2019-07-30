# Magento 1 Restrict File/Folder

This guide is to show you how you can Password and or IP restrict a file or folder within your document root using Nginx.

We highly recommend restricting the Magento 1 admin URI so will use this as an example. 

## htpasswd File ##

For password restriction you need to generate a username and password before configuring Nginx. You can do this with the following command:

```bash
~]$ htpasswd -c /etc/nginx/conf.d/.htpasswd adminusername
New password:
Re-type new password:
Adding password for user adminusername
~]$
```
## Password Restriction ##

To password restrict your admin URI use the following configuration options for Nginx:

```bash
# PASSWORD RESTRICTED URI
location ~* ^/(index\.php/mageadmin|mageadmin) {
    index index.php;
    try_files $uri $uri/ @handler;
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
    location ~* \.php$ {
      fastcgi_pass replacemebackend;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include fastcgi_params;
    }
  }
 ```
 
 ## IP Restriction ##
 
 To IP restrict your admin URI use the following configuration options for Nginx:
 
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
 
 ## Password and IP Restriction ##
 
To password restrict the website while allowing certain IP address access to the website without password restrictions you can use the following configuration options for Nginx:
 
  ```bash
# PASSWORD AND IP RESTRICTED URI 
location ~* ^/(index\.php/mageadmin|mageadmin) {
    index index.php;
    try_files $uri $uri/ @handler;
    satisfy any;
    allow 192.168.0.13; # Office IP Address
    allow 192.168.0.51; # Warehouse IP Address
    deny all;
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
    location ~* \.php$ {
      fastcgi_pass replacemebackend;
      fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      include fastcgi_params;
    }
  }
 ```

These location block need to be placed anywhere within the server block of your Nginx configuration file. You need to edit replacemebackend with the PHP-FPM configuration pool name (This should be defined at the top of your Nginx configuration file).
 
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
  .. meta::
     :title: Magento 1 IP Restrict File/Folder | UKFast Documentation
     :description: A guide to IP restrict a file or folder within Nginx
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security

