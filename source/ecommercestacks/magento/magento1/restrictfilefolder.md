# Restrict File/Folder (URI)

This guide is to show you how you can Password and or IP restrict a file or folder within your document root using NGiNX.

We highly recommend restricting the Magento 1 admin URI so will use this as an example (mageadmin).

## htpasswd File

For password restriction you need to generate a username and password before configuring NGiNX. You can do this with the following command:

```bash
 ~]$ htpasswd -c /etc/nginx/conf.d/.htpasswd adminusername
New password:
Re-type new password:
Adding password for user adminusername
 ~]$
```

## Password Restriction

To password restrict your admin URI use the following configuration options for NGiNX:

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

## IP Restriction

To IP restrict your admin URI use the following configuration options for NGiNX:

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

## Password with IP Allow list

To password restrict the URI whilst allowing certain IP address(s) access to the URI without password restrictions you can use the following configuration options for NGiNX:

```bash
# PASSWORD RESTRICTED WITH IP ALLOW LIST URI
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

## Password and IP Restriction

The most secure method is to restrict the admin URI to an allowed list of IP addresses and then have password restriction for the allow list. You can achieve this with the following configuration options in NGiNX:

```bash
# PASSWORD AND IP RESTRICTED URI
location ~* ^/(index\.php/mageadmin|mageadmin) {
  index index.php;
  try_files $uri $uri/ @handler;
  satisfy all;
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

These location blocks need to be placed within the server block of your NGiNX configuration file. You need to edit replacemebackend with the PHP-FPM configuration pool name (This should be defined at the top of your NGiNX configuration file).

To implement this change you need to reload the NGiNX service. First perform a configuration test with the following command:

```bash
 ~]$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If there are no errors in the configuration test proceed to reload the NGiNX service with the following command:

```bash
 ~]$ nginx -s reload
```

```eval_rst
  .. title:: Magento 1 Restrict File/Folder
  .. meta::
     :title: Magento 1 Restrict File/Folder | UKFast Documentation
     :description: A guide to restrict a file or folder within NGiNX
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security
```
