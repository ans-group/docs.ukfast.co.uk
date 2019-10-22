=================================================
WooCommerce
=================================================

WooCommerce is an open-source e-commerce plugin for WordPress. The core components of our optimised WooCommerce stack are:

- **Firewall**: :doc:`Dedicated/Shared Firewall </network/firewalls/index>` 
- **Web Service**: :doc:`/operatingsystems/linux/nginx/index`
- **PHP Utilities**: :doc:`/ecommercestacks/shopware/php/index` , :doc:`/operatingsystems/linux/php-fpm/index`, :doc:`/ecommercestacks/shopware/opcache/index`, :doc:`/ecommercestacks/shopware/apcu/index`
- **Mail Services**: :doc:`Postfix </operatingsystems/linux/mail/postfix>`
- **SSH/FTP Access**: :doc:`/operatingsystems/linux/ssh/index`, :doc:`/operatingsystems/linux/ftp/setup_vsftpd`
- **Database services**: :doc:`/operatingsystems/linux/percona/index`, :doc:`/ecommercestacks/shopware/redis/index`, :doc:`/operatingsystems/linux/elasticsearch/index`
- **HTTP Caching Utilities**: :doc:`/ecommercestacks/shopware/varnish/index`
- **Version Control Utilities**: :doc:`/operatingsystems/linux/git/index`
- **File system distribution**: :doc:`/operatingsystems/linux/nfs/index`

We have a number of guides for our Shopware optimised stack:

.. toctree::
   :maxdepth: 1

   php/index
   opcache/index
   apcu/index
   redis/index
   varnish/index
   
.. meta::
   :title: WooCommerce Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast WooCommerce Optimised Stack
   :keywords: ukfast, WooCommerce, optimised, stack, eCommerce

