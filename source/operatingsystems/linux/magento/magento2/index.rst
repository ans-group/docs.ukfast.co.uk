=================================================
Magento 2
=================================================

In 2015 we created our Magento 2 optimised stack. The core components of this stack are:

* **Firewall**: :doc:`Dedicated/Shared Firewall </network/firewalls/index>` 
* **Web Service**: :doc:`/operatingsystems/linux/nginx/index`
* **PHP Utilities**: :doc:`/operatingsystems/linux/magento/magento2/php/index`, :doc:`/operatingsystems/linux/magento/magento2/php-fpm/index`, :doc:`/operatingsystems/linux/magento/magento2/opcache/index`, :doc:`/operatingsystems/linux/magento/magento2/composer/index`
* **Mail Services**: :doc:`Postfix </operatingsystems/linux/mail/postfix>`
* **SSH/FTP Access**: :doc:`/operatingsystems/linux/ssh/index`, :doc:`/operatingsystems/linux/ftp/setup_vsftpd`
* **HTTP Caching Utilities**: :doc:`/operatingsystems/linux/magento/magento2/varnish/index`
* **Database services**: :doc:`/operatingsystems/linux/magento/magento2/percona/index`, :doc:`/operatingsystems/linux/magento/magento2/elasticsearch/index`, :doc:`/operatingsystems/linux/magento/magento2/redis/index`
* **Version Control Utilities**: :doc:`/operatingsystems/linux/magento/magento2/git/index`
* **File system distribution**: :doc:`/operatingsystems/linux/magento/magento2/nfs/index`

We have a number of guides for our Magento 2 optimised stack:

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
   rabbitmq/index
   varnish/index
   git/index
   composer/index
   elasticsearch/index
   opcache/index
   php-fpm/index
   nfs/index
   php/index
   multiphp/index
   redis/index
   percona/index
   
We also have guides for :doc:`/operatingsystems/linux/magento/magento1/index`
   
.. meta::
   :title: Magento 2 Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast Magento 2 Optimised Stack
   :keywords: ukfast, Magento, Magento2, optimised, stack

