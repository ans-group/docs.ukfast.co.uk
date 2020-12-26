# Exchange DNS

Exchange users should have the following records set up via DNS

* MX
  * domain.com MX 10 cas1.contoso.com
  * domain.com MX 10 cas2.contoso.com
  * domain.com MX 20 email.contoso.com

Priority 10 on the `MX` records for cas1 and cas2 will ensure they use DNS round robin to connect, if that fails, it will hit your load balancer for mail.


* SRV
  * Value    : \_autodiscover.\_tcp.domain.com
  * Weight   : 0
  * Priority : 0
  * Port     : 443
  * Target   : email.contoso.com

The `SRV` (autodiscover) is a requirement of having an exchange server, this will ensure that your settings are automatically picked up by your email client.


* SPF
  *  v=spf1 include:spf.contoso.com ~all


This `SPF` record ensures your users look to your `SPF` settings for their own. Essentially allowing you to add servers to the solution without them violating the `SPF` policy of your users.

The alternative would be to ask them to update their settings every time there is a change to the servers in the solution. This is cleaner.

```eval_rst
  .. title:: DNS settings for Microsoft Exchange
  .. meta::
     :title: DNS settings for Microsoft Exchange | UKFast Documentation
     :description: Information and guidance on DNS settings for Microsoft Exchange
     :keywords: ukfast, windows, exchange, dns, mx, a, spf, record, srv, cloud
