# How to secure Nginx with Let's Encrypt on CentOS

For Linux servers, the `certbot` tool is currently the most popular tool for issuing **`Let's Encrypt`** certificates in a hassle free way. Here, we will show you how to install `certbot` on **CentOS**, but this will also be available on most Linux distributions.

`Certbot` has an additional plugin specifically for servers that use `nginx` as the web service.

```eval_rst
.. warning::
  These plugins will amend your virtual host configurations, but may interfere with any application rewrite rules you already have in place. Always ensure you have backed up vital configuration files before use.

```

For alternative `ACME` clients/libraries/projects, `Let's Encrypt` have an extensive list at the following link;

[Let's Encrypt client options](https://letsencrypt.org/docs/client-options/)

## Installation

You will need to have the **Epel** repository (or repo) enabled to install certbot. If not installed, run the following;
```
yum install epel-release
```
Next, install the following package from this repo
```
yum install certbot-nginx --enablerepo=epel
```

## Issuing a certificate

As **root** (or using **sudo** if a sudo user), you can specify multiple domains/subdomains using the following syntax.
```
certbot --nginx -d yourdomain.com -d www.youdomain.com
```
You can secure up to **100** domains using `-d` in the one command.

```eval_rst
.. note::
  If issuing a multidomain certificate, please note that if you remove one of the domains on it you will have to reissue the entire certificate. As this could prove problematic upon renewal, we would instead recommend issuing a certificate per domain.
```

By default, this will append your nginx configuration file for the chosen domain a rewrite to https

```

      server {
    if ($host = shop.yourdomain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


        listen ip.ip.ip.ip:80;
        server_name shop.yourdomain.com;
    return 404; # managed by Certbot


}
```

If you wish to amend this yourself, you should chose the 'certonly' option, and manually specify the new certificates in your domain's nginx configuration file.
```
certbot certonly 

```
##  Additional options

Here is a selection of additional flags/options that you can use, should you need a more granular installation.

* `certonly` -  If you wish to install the certificate manually, this will provide you with the SSL component files;
* `--webroot` - If you have a non-standard document root that perhaps is obfuscated in your application, this is useful so that the HTTP-01 challenge file can be placed correctly
* `-d` - For specifying up to 100 domains/subdomains in the same command.
* `standalone` - Runs a webserver that binds to port `80`, so you may need to stop your current webservice
* `--agree-tos` - Automatically agree to the terms of service
* `--email` - To specify an address for registration/correspondence
* `--uir` - This enables a Content-Security-Policy in every request to *upgrade-insecure-requests*


```eval_rst
  .. title:: SSL | How to secure Nginx with Let's Encrypt on CentOS
  .. meta::
     :title: SSL | How to secure Nginx with Let's Encrypt on CentOS | UKFast Documentation
     :description: How to secure Nginx with Let's Encrypt on CentOS
     :keywords: ssl, certbot, nginx, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
