# Removing a domain from DDoSX<sup>TM</sup>

If you want to remove a domain from DDoSX<sup>TM</sup> then follow these steps:

1. Login to [MyUKFast](https://my.ukfast.co.uk) and go to the `DDoS Protection` section under `Products and Services`.
2. Click the delete icon next to the domain in question
3. You'll be asked to re-enter your MyUKFast password to confirm you wish to go ahead and delete the domain.
4. Your domain will now be disconnected from the DDoSX<sup>TM</sup> network.  You can reconnect your domain at any time until the billing period expires.
5. You should use [SafeDNS](/Domains/safedns/index.html) to point your domain records back to your own server or filewall, so that traffic to the domain is no longer being routed via the UKFast DDoS Protection network.

```eval_rst
.. warning::
   If you don't point your domain records back to your own server or firewall, your domain will go offline when the domain's DDoSX\ :sup:`TM` billing period expires.
```
