# Adding Domain(s) To The Stack

To add a domain to your Shopware optimised stack please provide us with the following information:

- Domain name
- Shopware version
- If this a Subshop domain? If so please provide the main website domain name
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
~]$ /root/shopware.exampledomain.co.uk_setup.txt
```

```eval_rst
  .. title:: Shopware Adding Domain(s) To The Stack
  .. meta::
     :title: Shopware Adding Domain(s) To The Stack | UKFast Documentation
     :description: A guide to adding domains to the Shopware optimised stack
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Shopware, security, php-fpm, mysql, percona, eCommerce


