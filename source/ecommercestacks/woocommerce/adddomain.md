# Adding Domain(s) To The Stack

To add a domain to your WooCommerce optimised stack please provide us with the following information:

- Domain name
- Wordpress version
- Is this domain for UAT/Staging or is it going to be used for live traffic

We will then setup the following for you:

- Nginx configuration file (/etc/nginx/conf.d/exampledomain.co.uk.conf)
- PHP-FPM configuration file (/etc/php-fpm.d/exampledomain.co.uk.conf)
- Document Root (/var/www/vhosts/exampledomain.co.uk/htdocs/)
- Local System User and password (exampledomain.co.uk)
- Database (exampledomaincouk)
- Database User and password (exampleFwpO)

The credentials will be saved on the server in the /root/ directory similar to:
```bash
~]$ /root/WooCommerce.exampledomain.co.uk_setup.txt
```

```eval_rst
  .. title:: WooCommerce Adding Domain(s) To The Stack
  .. meta::
     :title: WooCommerce Adding Domain(s) To The Stack | UKFast Documentation
     :description: A guide to adding domains to the WooCommerce optimised stack
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, WooCommerce, security, php-fpm, mysql, percona, eCommerce


