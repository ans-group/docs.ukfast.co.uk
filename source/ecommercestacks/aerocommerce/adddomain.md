# Adding Domain(s) To The Stack

To add a domain to your `AeroCommerce` optimised stack please provide us with the following information:

- Domain name
- Is this domain for UAT / Staging or is it going to be used for live traffic

We will then setup the following for you:

- NGINX configuration file (`/etc/nginx/conf.d/exampledomain.co.uk.conf`)
- PHP-FPM configuration file (`/etc/php-fpm.d/exampledomain.co.uk.conf`)
- Document Root (`/var/www/vhosts/exampledomain.co.uk/htdocs/`)
- Local System User and password (`exampledomain.co.uk`)
- Database (`exampledomaincouk`)
- Database User and password (`exampleFwpO`)

The credentials will be saved on the server in the `/root/` directory similar to:

```bash
~]$ /root/AeroCommerce.exampledomain.co.uk_setup.txt
```

```eval_rst
  .. title:: AeroCommerce Adding Domain(s) To The Stack
  .. meta::
     :title: AeroCommerce Adding Domain(s) To The Stack | ANS Documentation
     :description: A guide to adding domains to the AeroCommerce optimised stack
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, AeroCommerce, security, php-fpm, mysql, percona, eCommerce
```
