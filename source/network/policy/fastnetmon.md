# FastNetMon

##  What is a FastNetMon Ban? 
`FastNetMon` is a tool to allow for real time black holing of IP addresses by systems that collect traffic/ netflow data directly from our routers.

- If a threshold is met and the systems believe there to be a targeted attack, the targeted IP address will be temporarily blocked, while the block is in place, networking is suspended to protect the network and the client’s 

- The bans will be automatically lifted after approximately 30 minutes, should the attack continue, this will then be reinstated 

This data is logged by UKFast and further information can be provided should this be needed [on the nature of the attack and its vectors] 

## What to do after multiple bans?
If multiple bans keep occurring over time, it is wise to assume that this is a targeted attack (DoS or DDoS) and appropriate actions should be taken to prevent this happening again. 

If targeted attack, if is safe to assume that work has been undertaken before the initiation of the attack, this means that IP addresses will have been noted. 

It is unlikely that the attack is domain based and actually targeted at the backend IP addresses of the servers, meaning that we need to assume that any DNS records such as A, MX, TXT etc that are associated with an IP address have also been taken note off. 

From here on out, it is recommended that all of the domains on the affected server are put behind a **DDoS protection platform** such as our own DDoSX platform

Putting the domains behind DDoSX will masquerade the real IP address of the backend server and will only show the attacker the IP address of the anti DDoS platform.
Because the attacker will most likely have the backend IP addresses, the backend IP addresses will also have to change to new ones otherwise the attack will be routed around the Anti DDoS platform and hit the backend directly. 

## Changing IP addresses
There are 2 ways this can be achieved, an additional IP address can be added to your server which may incur an additional cost, this will have to be approved by an Account Manager prior to this work, and then you can migrate the sites to the new IP address, this will need an update of your A records within your DNS platform. 
https://docs.ukfast.co.uk/domains/safedns/addarecord.html

Once complete, the removal of the attacked IP address can then be removed. 

The alternative would be to perform a full IP swap of the server once everything has been put behind an Anti DDoS Platform, depending on your setup, this may require configuration changes to your application

Speak to an UKFast engineer for further advice on which option would be best for your solution. 

Please note, any changes to DNS may incur a small amount of downtime while DNS records are updated. 

Additional Steps
Once the sites are running via the new platform, it is strongly advised that all web traffic (port 80 and 443) be locked down within your MyUKFast firewall to only accept connections from the IP addresses from the Anti DDoS platform, to prevent any other web traffic going direct to the backend
Ensure that no other DNS records such as MX, SPF, TXT records point or are associated with this new IP address, if this is, then exposed then the new IP address may then be targeted once again. 

You can check your DNS records here: 
* [MX Toolbox](https://mxtoolbox.com/DNSLookup.aspx)

If you are hosting mail, to which means that you need IP based MX records, we recommend that you look at our Office365 platform or other email providers in which also masquerade the mail servers IP address. 

If you continue to use the previously attacked IP address for hosting email, it may well be the case that the IP for the mail gets blocked during an attack (since this is/was the one being targeted) but the sites will stay online. This means that no mail will be received while an attack is taking place. 

To summarise: 
Put all domains behind an anti DDoS platform (all domains not just one or two) as this hides the sites IP address association  

Add or change IP address of the server and migrate all sites over to new IP, this creates a new domain to IP association the attackers will not be aware of

Lock down [web]port[s] 80 and 443 within UKFast firewall to anti DDoS platform IP addresses – 

Please see the below for the DDoSX IP range
https://docs.ukfast.co.uk/security/ddos/ips.html

``` warning:: Never expose the new IP address: treat this like a password that you wouldn't expose.
```

```eval_rst
  .. title:: Network Protection with FastNetMon
  .. meta::
     :title: Network Protection with FastNetMon | UKFast Documentation
     :description: Network Protection with FastNetMon
     :keywords: ssl, certbot, renew, autorenew, revoke, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
