# Restrict Website

This guide is to show you how you can Password and or IP restrict a website. This is most common for staging or development websites. This guide is for the Nginx web service and is applicable for Magento 1 or Magento 2.

### htpasswd File

For password restriction you need to generate a username and password before configuring Nginx. You can do this with the following command:

```bash
~]$ htpasswd -c /etc/nginx/conf.d/.htpasswd adminusername
New password:
Re-type new password:
Adding password for user adminusername
~]$
```
### Password Restriction

To password restrict your website following configuration options for Nginx:

```bash
# PASSWORD RESTRICTED WEBSITE
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
 ```

 ### IP Restriction

 To IP restrict your website use the following configuration options for Nginx:

 ```bash
# IP RESTRICTED WEBSITE
    allow 192.168.0.13; # Office IP Address
    allow 192.168.0.51; # Warehouse IP Address
    deny all;
 ```

 ### Password with IP Allow list

To password restrict the website whilst allowing certain IP address(s) access to the website without password restrictions you can use the following configuration options for Nginx:

  ```bash
# PASSWORD RESTRICTED WITH IP ALLOW LIST WEBSITE
    satisfy any;
    allow 192.168.0.13; # Office IP Address
    allow 192.168.0.51; # Warehouse IP Address
    deny all;
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
 ```

### Password and IP Restriction

The most secure method is to restrict the website to an allowed list of IP addresses and then have password restriction for the allow list. You can achieve this with the following configuration options in Nginx:

  ```bash
# PASSWORD AND IP RESTRICTED WEBSITE
    satisfy all;
    allow 192.168.0.13; # Office IP Address
    allow 192.168.0.51; # Warehouse IP Address
    deny all;
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/conf.d/.htpasswd;
 ```

These configuration options need to be placed within the server block of your Nginx configuration file.

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
  .. title:: Magento Restrict Website
  .. meta::
     :title: Magento Restrict Website | UKFast Documentation
     :description: A guide to restrict access to a website
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security

