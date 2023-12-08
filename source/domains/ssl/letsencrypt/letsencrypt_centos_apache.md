# How to secure Apache with Let's Encrypt on CentOS

For Linux servers, the `certbot` tool is currently the most popular tool for issuing **Let's Encrypt** certificates in a hassle free way. Here, we will show you how to install `certbot` on **CentOS**, but this will be available on most Linux distributions.

`Certbot` has an additional plugin specifically for servers that use `Apache` as the web service.

```eval_rst
.. warning::
  These plugins will amend your virtual host configurations, but may interfere with any application rewrite rules you already have in place. Always ensure you have backed up vital configuration files before use.

```

For alternative `ACME` clients/libraries/projects, `Let's Encrypt` have an extensive list at the following link;

[Let's Encrypt client options](https://letsencrypt.org/docs/client-options/)

## Installation

You will need to have the **EPEL** repository (or repo) enabled to install `certbot`. If not installed, run the following;

```bash
yum install epel-release
```

Next, install the following Certbot plugin for Apache from this repo. This will pull in additional packages automatically, such as `mod_ssl` if not already installed

```bash
yum install certbot-apache --enablerepo=epel
```

## Issuing a certificate

As `root` (or using `sudo`), you can specify multiple domains / subdomains using the following syntax.

```bash
certbot --apache -d yourdomain.com -d www.youdomain.com
```

You can secure up to **100** domains using `-d` in the one command.

```eval_rst
.. note::
  If issuing a multidomain certificate, please note that if you remove one of the domains on it you will have to reissue the entire certificate. As this could prove problematic upon renewal, we would instead recommend issuing a certificate per domain.
```

You will be prompted by a few questions before it proceeds with the installation (agreeing to terms of service, challenge method etc.). It will also ask if you want to add a redirect to HTTPS. If you select 'yes', It will amend your Apache vhost with a permanent redirect.

##  Additional options

Here is a selection of additional flags/options that you can use, should you need a more granular installation.

* `certonly` - If you wish to install the certificate manually, this will provide you with the SSL component files;
* `--webroot` - If you have a non-standard document root that perhaps is obfuscated in your application, this is useful so that the `HTTP-01` challenge file can be placed correctly
* `-d` - For specifying up to 100 domains/subdomains in the same command.
* `standalone` - Runs a webserver that binds to port `80`, so you may need to stop your current web server
* `--agree-tos` - Automatically agree to the terms of service
* `--email` - To specify an address for registration/correspondence
* `--uir` - This enables a `Content-Security-Policy` in every request to upgrade insecure requests

```eval_rst
  .. title:: SSL | How to secure Apache with Let's Encrypt on CentOS
  .. meta::
     :title: SSL | How to secure Apache with Let's Encrypt on CentOS | ANS Documentation
     :description: How to secure Apache with Let's Encrypt on CentOS
     :keywords: ssl, certbot, apache, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
