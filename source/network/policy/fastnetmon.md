# FastNetMon

##  What is a FastNetMon Ban?

UKFast utilises a service called FastNetMon to analyse traffic entering our network to determine whether it is legitimate. FastNetMon is configured to automatically make decisions based on the nature of the inbound traffic and can "ban" an IP.

This action is taken to prevent the attack from affecting our systems and other customers on our network.

- If a threshold is met in terms of bandwidth or packets per second, the targeted IP address will be temporarily blocked. While the block is in place, no traffic will be routed to the targeted IP address.

- The ban will be automatically lifted after approximately 30 minutes. Should the attack continue, the ban will be reinstated.

This data is logged by UKFast and further information (on the nature of the attack and its vectors) can be provided, should this be needed.

## What to do after multiple bans?

If multiple bans keep occurring over time, it is wise to assume that this is a targeted attack (DoS or DDoS), and appropriate action should be taken to prevent this happening again.

If it is a targeted attack, it is safe to assume that the attack will have been planned, and the targeted IP addresses will have been noted.

```eval_rst
.. warning::
   It is unlikely that an attack will target a domain name, as returned by DNS. More often than not, it's the IP address that DNS pointed to that will be targeted. This means that we need to assume that any DNS records such as ``A``, ``MX``, ``TXT``, etc. associated with an IP address will have also been taken note off.

```

From here on out, it is recommended that all of the domains on the affected server are put behind a DDoS protection platform, such as our own DDoSX<sup>®</sup> platform.

Putting the domains behind DDoSX<sup>®</sup> will masquerade the real IP address(es) of the backend server(s), and will only show the attacker the IP address of the anti-DDoS platform. As the attacker will most likely have the backend IP addresses, those IPs will also need to be changed. Otherwise, the attack will be routed around the anti-DDoS platform and will still reach the backend, taking it offline as happened previously.

## Changing IP addresses

There are 2 ways this can be achieved:

 - An additional IP address can be added to your server, which may incur an additional cost. This will need to be approved by an Account Manager, prior to the work. You can then migrate the sites to the new IP address and update your DNS records to use it.

   Once complete, the attacked IP address can then be removed.

 - The alternative would be to perform a full IP swap of the server, once everything has been put behind an anti-DDoS platform. Depending on your setup, this may require configuration changes to your application.

Speak to an UKFast engineer for further advice on which option would be best for your solution.

```eval_rst
.. note::
   Please note, any changes to DNS may incur a small amount of downtime while DNS records are updated.
```

## Additional Steps

Once the sites are running via the new platform, it is strongly advised that all web traffic (port 80 and 443) be locked down on your firewall to only accept connections from the IP addresses from the anti-DDoS platform. This can be done in the MyUKFast portal, and will prevent any other web traffic going direct to the backend.

Ensure that no other DNS records such as `MX`, `SPF`, `TXT` records point to, or are associated with, this new IP address. If it is, the new IP address will be exposed to the attacker and may then be targeted instead.

You can check your DNS records here:

* [MX Toolbox](https://mxtoolbox.com/DNSLookup.aspx)

If you are hosting a mail service which needs IP based ``MX`` records, we recommend that you look at an email filtering service. These services masquerade your mail server's IP address. Office 365 can provide this service, and can also be purchase through UKFast.

If you continue to use the previously attacked IP address for hosting email, it may be that that IP continues to gets attacked in future attacks. If this happens, it is likely that your sites will stay online but no email will be received.

## To Summarise:

* Put all domains behind an anti-DDoS platform as this hides the site's real IP address. This should really be all domains, not just one or two.
* Add or change the IP address of the server, and migrate all sites over to new IP whilst updating the anti-DDoS platform to use the new IP.
* Do not update or create DNS records to point to the new IP. Doing so will tell the attackers the new IP address, which they will then target instead.
* Lock down HTTP/S ports (80 and 443) on your firewall within MyUKFast to anti-DDoS platform IP addresses

[DDoSX IP range](/security/ddos/ips)

```
.. warning::
   Never expose the new IP address. Treat this like a password that you wouldn't expose.
```

```eval_rst
  .. title:: Network Protection with FastNetMon
  .. meta::
     :title: Network Protection with FastNetMon | ANS Documentation
     :description: Network Protection with FastNetMon
     :keywords: fastnetmon, banning, ban, Ban, traffic, guide, fast, net, mon, security, firewall, attack, flood, ddos, ddosx, IP, ip, address, Address, protection, DDoS, DDoSX, FastNetMon, cloudflare, block
```
