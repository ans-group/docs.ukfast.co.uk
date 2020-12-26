# Adding Domain(s) To The Stack

To add a domain to your Magento 2 optimised stack please provide us with the following information:

- Domain name
- Magento version
- If this a multi-store domain? If so please provide the main website domain name
- Will wordpress run within the same document root? If so please provide the path (wp, wordpress and blog for example)
- Is this domain for UAT/Staging or is it going to be used for live traffic
- What PHP version is required?

We will then setup the following for you:

- Nginx configuration file (/etc/nginx/conf.d/exampledomain.co.uk.conf)
- PHP-FPM configuration file (/etc/php-fpm.d/exampledomain.co.uk.conf)
- Document Root (/var/www/vhosts/exampledomain.co.uk/htdocs/)
- Local System User and password (exampledomain.co.uk)
- Database (exampledomaincouk)
- Database User and password (exampleFwpO)

The credentials will be saved on the server in the /root/ directory similar to:
```bash
~]$ /root/magento2.exampledomain.co.uk_setup.txt
```
## Multistore

You can edit the Nginx configuration file (/etc/nginx/conf.d/exampledomain.co.uk.conf) to configure the MAGE_RUN_CODE and MAGE_RUN_TYPE variables for this domain by uncommenting the following lines:

#fastcgi_param  MAGE_RUN_CODE default;<br>
#fastcgi_param  MAGE_RUN_TYPE store;

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

## Nginx .php File Allow list

The web service (Nginx) configuration file has an allow list for .php files to pass to php-fpm. If you want to access a .php file not in the default list:

```bash
location ~ (index|get|static|report|404|503|health_check)\.php$ {
```

Please refer to this guide: [Magento 2 .php File Allow list](/ecommercestacks/magento/magento2/nginxphpfileallowlist)

## Magento 2 CLI

If running the Magento 2 CLI please ensure you're logged in as the PHP-FPM configured user. You can log into this account via SSH or with the following command when logged in as root (Replacing phpconfigureduser with the PHP-FPM configured user, example exampledomain.co.uk):

```bash
~]# su - phpconfigureduser
```

```eval_rst
  .. title:: Magento 2 Adding Domain(s) To The Stack
  .. meta::
     :title: Magento 2 Adding Domain(s) To The Stack | UKFast Documentation
     :description: A guide to adding domains to the Magento optimised stack
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, security, php-fpm, mysql, percona, eCommerce


