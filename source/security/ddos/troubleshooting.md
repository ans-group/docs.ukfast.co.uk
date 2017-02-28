# Troubleshooting

This section should help with any problems you run in to:

## I can't connect my domain(s) to the DDoS Protection network

If you're struggling to connect your domains, first check that you are using [SafeDNS](/source/Domains/safedns/index) to manage your DNS records.  You neeed to use SafeDNS and point your domains to the UKFast nameservers, which are
- ns0.ukfast.co.uk
- ns1.ukfast.co.uk

You'll find SafeDNS in [MyUKFast](https://my.ukfast.co.uk) - just log in and go to `SafeDNS` under the `Products and Services` menu.  You should also read the full [SafeDNS guide](/source/Domains/safedns/index)

## My domain is showing as Not Configured, why is this?

If your domain is connected to the DDoS Protection network but not yet configured, you'll see a red icon in the Status column on the Manage Domains page - see example below

![manage](files/manage.PNG)

To configure your domain, simply click on the Settings button next to the domain in question, and then `Configure`.  Run through the process as set out in the [Getting Started guide](/gettingstarted)
