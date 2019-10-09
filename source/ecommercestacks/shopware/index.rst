=================================================
Shopware
=================================================

The UKFast Shopware optimised stack was created in 20017. The core components of this stack are:

- **Firewall**: :doc:`Dedicated/Shared Firewall </network/firewalls/index>` 
- **Web Service**: :doc:`/operatingsystems/linux/nginx/index`
- **PHP Utilities**: :doc:`/ecommercestacks/magento/magento1/php/index` , :doc:`/ecommercestacks/magento/magento1/php-fpm/index`, :doc:`/ecommercestacks/magento/magento1/opcache/index`
- **Mail Services**: :doc:`Postfix </operatingsystems/linux/mail/postfix>`
- **SSH/FTP Access**: :doc:`/operatingsystems/linux/ssh/index`, :doc:`/operatingsystems/linux/ftp/setup_vsftpd`
- **Database services**: :doc:`ecommercestacks/magento/magento1/percona/index`, :doc:`/ecommercestacks/magento/magento1/redis/index`
- **Version Control Utilities**: :doc:`/ecommercestacks/magento/magento1/git/index` 
- **File system distribution**: :doc:`/ecommercestacks/magento/magento1/nfs/index`

We have a number of guides for our Magento 1 optimised stack:

.. toctree::
   :maxdepth: 1

   permissionguide
   wpinsubdir.md
   restrictfilefolder.md
   magentoinsubdir.md
   redis/index
   adddomain.md
   ../redtrictwebsite.md
   ../magentottfb.md
   ../dbtriggers.md
   git/index
   opcache/index
   php-fpm/index
   nfs/index
   php/index
   multiphp/index
   percona/index
   
We also have guides for :doc:`/ecommercestacks/magento/magento2/index`
   
.. meta::
   :title: Shopware Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast Shopware Optimised Stack
   :keywords: ukfast, Shopware, optimised, stack, eCommerce

