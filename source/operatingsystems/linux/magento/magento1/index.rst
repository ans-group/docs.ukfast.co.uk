=================================================
Magento 1
=================================================

Our Magento 1 optimised stack has been going since 2008. The core components of this stack are:


- **Firewall**: :doc:`Dedicated/Shared Firewall </network/firewalls/index>` 
- **Web Service**: Nginx
- **PHP Utilities**: PHP-FPM, Magento 1 Recommended PHP modules, OPCache
- **Mail Services**: Postfix, Sendmail
- **SSH/FTP Access**: SSH, VSFTPd, ProFTPD
- **Database services**: MySQL Percona, :doc:`/operatingsystems/linux/magento/magento1/redis/index`
- **Version Control Utilities**: :doc:`/operatingsystems/linux/magento/magento1/git/index` 
- **File system distribution**: NFS

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
   
.. meta::
   :title: Magento 1 Optimised Stack | UKFast Documentation
   :description: guides relating to UKFast Magento 1 Optimised Stack
   :keywords: ukfast, Magento, optimised, stack

