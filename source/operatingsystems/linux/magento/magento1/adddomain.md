# Magento 1 - Adding Domain(s) To The Stack

To add a domain to your Magento optimised stack please provide us with the following information:

- Domain name
- Magento version
- If this a multi-store domain? If so please provide the main website domain name
- Will wordpress run within the same document root? If so please provide the path
- Is this domain for UAT/Staging or is it going to be used for live traffic

We will then setup the following for you:

- Nginx configuration file (/etc/nginx/conf.d/exampledomain.co.uk.conf)
- PHP-FPM configuation file (/etc/php-fpm.d/exampledomain.co.uk.conf)
- Document Root (/var/www/vhosts/exampledomain.co.uk/htdocs/)
- Local System User and password (exampledomain.co.uk)
- Database (exampledomaincouk)
- Database User and password (exampleFwpO)

```eval_rst
  .. meta::
     :title: Magento 1 Adding Domain(s) To The Stack | UKFast Documentation
     :description: A guide to adding domains to the Magento optimised stack
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security, php-fpm, mysql, percona


