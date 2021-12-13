=================================================
`Varnish <https://varnish-cache.org/>`_
=================================================

Varnish is recommended for Full Page Caching with Magento2. Website performance is greatly increased when using Varnish. 

Traffic flow on a single server with Varnish is typically:

- Port 80 (:doc:`/ecommercestacks/magento/magento2/varnish/index`) -> Port 8080 (:doc:`/operatingsystems/linux/nginx/index`) -> :doc:`/operatingsystems/linux/php-fpm/index`
- Port 443 (:doc:`/operatingsystems/linux/nginx/index`) - Port 80 (:doc:`/ecommercestacks/magento/magento2/varnish/index`) -> Port 8080 (:doc:`/operatingsystems/linux/nginx/index`) -> :doc:`/operatingsystems/linux/php-fpm/index`

.. toctree::
   
   varnish.md
   
.. meta::
   :title: Magento2 Varnish | UKFast Documentation
   :description: guides relating to Magento2 using Varnish
   :keywords: ukfast, Magento2, optimised, stack, varnish, eCommerce

