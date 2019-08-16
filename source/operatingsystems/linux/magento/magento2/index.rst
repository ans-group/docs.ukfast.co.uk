=================================================
Magento 2
=================================================

Our Magento 2 optimised stack has been going since 2015. The core components of this stack are:

* **Firewall**: Dedicated/Shared Firewall
* **Web Service**: Nginx
* **PHP Utilities**: PHP-FPM, Magento 2 Recommended PHP modules, Composer, OPCache
* **Mail Services**: Postfix, Sendmail
* **SSH/FTP Access**: SSH, VSFTPd, ProFTPD
* **HTTP Caching Utilities**: :doc:`/operatingsystems/linux/magento/magento2/varnish/`
* **Database services**: MySQL Percona, Elasticsearch, Memcached, Redis, Sphinx, RabbitMQx
* **Version Control Utilities**: Git
* **File system distribution**: NFS

.. toctree::
   :maxdepth: 1

   permissionguide
   nginxphpfilewhitelist
   wpinsubdir.md
   filediroutsidepub.md
   restrictfilefolder.md
   m2insubdir.md
   adddomain.md
   ../redtrictwebsite.md
   ../magentottfb.md
   ../dbtriggers.md
   varnish/index
   
.. meta::
   :title: Magento 2 Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast Magento 2 Optimised Stack
   :keywords: ukfast, Magento, optimised, stack

