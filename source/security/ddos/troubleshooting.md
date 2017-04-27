# Troubleshooting

This section should help with any problems you run in to.

## I can't connect my domain(s) to the DDoSX<sup>TM</sup> network

If you're struggling to connect your domains, first check that you are using [SafeDNS](/Domains/safedns/index.html) to manage your DNS records.  You neeed to use SafeDNS and point your domains to the UKFast nameservers, which are
- ns0.ukfast.co.uk
- ns1.ukfast.co.uk

You'll find SafeDNS in [MyUKFast](https://my.ukfast.co.uk) - just log in and go to `SafeDNS` under the `Products and Services` menu.  You should also read the full [SafeDNS guide](/Domains/safedns/index.html)

## My domain is showing as Not Configured, why is this?

If your domain is connected to the DDoSX<sup>TM</sup> network but not yet configured, you'll see a red icon in the Status column on the Manage Domains page - see example below

![manage](files/manage.PNG)

To configure your domain, simply click on the Settings button next to the domain in question, and then `Configure`.  Run through the process as set out in the [Getting Started guide](/security/ddos/gettingstarted.html)

## I've removed my domain from the DDoSX<sup>TM</sup> network, and now my website is offline.

If you've previously had a domain connected to the DDoSX<sup>TM</sup> network and then removed it, make sure to use [SafeDNS](/Domains/safedns/index.html) to point your DNS records directly back to your own server or firewall.  See the section on [Removing a domain from DDoSX<sup>TM</sup>](/security/ddos/remove.html) for more details.

## My website does not work as expected over HTTPS

Ensure that the correct SSL certificate is selected in the dropdown box in the DDoSX<sup>TM</sup> configuration section (click `Products & Services` > `DDoSX` > `Configure` to find this).  If this is set to none, there will be no HTTPS configuration for your domain. If using a custom SSL, ensure that the full SSL is correctly entered in the "SSL Certificates" tab. 

![config_clipped](files/config_clipped.png)
