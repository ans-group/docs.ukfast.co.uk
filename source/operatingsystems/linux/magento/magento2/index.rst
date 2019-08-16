=================================================
Magento 2
=================================================

Our Magento 2 optimised stack has been going since 2015. The core components of this stack are:

* **Firewall**: :doc:`Dedicated/Shared Firewall </network/firewalls/index>` 
* **Web Service**: :doc:`/operatingsystems/linux/nginx/index`
* **PHP Utilities**: PHP-FPM, Magento 2 Recommended PHP modules, :doc:`/operatingsystems/linux/magento/magento2/composer/index`, OPCache
* **Mail Services**: :doc:`Postfix </operatingsystems/linux/mail/postfix>` , Sendmail
* **SSH/FTP Access**: :doc:`/operatingsystems/linux/ssh/index`, :doc:`/operatingsystems/linux/ftp/setup_vsftpd`
* **HTTP Caching Utilities**: :doc:`/operatingsystems/linux/magento/magento2/varnish/index`
* **Database services**: MySQL Percona, Elasticsearch, Memcached, Redis, Sphinx, RabbitMQx
* **Version Control Utilities**: :doc:`/operatingsystems/linux/magento/magento2/git/index`
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
   git/index
   composer/index
   
.. meta::
   :title: Magento 2 Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast Magento 2 Optimised Stack
   :keywords: ukfast, Magento, Magento2, optimised, stack

