# What is a name server?

```eval_rst
   .. title:: Domain Name FAQ What is a name server?
   .. meta::
      :description: Domain Name FAQ What is a name server?
```


A name server is essentially a signpost that the domain name system uses to connect your IP address to your domain name.


For example, you would type in a domain name and your computer uses the Domain Name System (DNS) to retrieve its current name servers.


It would then query these name servers for the A (address) name record for the domain, and the nameservers would respond with an IP address.


Your computer then sends a request to the IP returned to load the requested page.


Two nameservers are required to add redundancy. If one fails, you always have a backup.


The name servers therefore allow you to see who currently manages a domain name's DNS. If you are using UKFast's SafeDNS your nameservers need to point to our name servers so that any changes you make to your DNS take effect.

