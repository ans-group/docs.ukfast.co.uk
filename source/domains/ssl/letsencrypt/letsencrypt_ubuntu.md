# How to secure your sites with Let's Encrypt on Ubuntu

You can install the Certbot utility in `Ubuntu` using the official PPA (Personal Package Archive).

First, install the `software-properties-common` package, if you don't already have this.

```bash
apt install software-properties-common
```

Next, install the repo, update the apt database and install the module for your chosen web service.

For `Apache`

```bash
add-apt-repository ppa:certbot/certbot
apt update
apt install certbot python3-certbot-apache
```

or for `NGINX`

```bash
apt install python-certbot-nginx
```

There after you can use the same methods to install a certificate as previously mentioned for [Apache](/domains/ssl/letsencrypt/letsencrypt_centos_apache.html#installation) and [NGINX](/domains/ssl/letsencrypt/letsencrypt_centos_nginx.html#installation)


```eval_rst
  .. title:: SSL | How to secure your sites with Let's Encrypt on Ubuntu
  .. meta::
     :title: SSL | How to secure your sites with Let's Encrypt on Ubuntu | UKFast Documentation
     :description: How to secure your sites with Let's Encrypt on Ubuntu
     :keywords: ubuntu, ukfast, ssl, letsencrypt, let's encrypt, secure, security, Apache, NGINX, linux, server, guide, tutorial
```
