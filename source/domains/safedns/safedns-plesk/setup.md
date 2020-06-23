# Plesk SafeDNS Extension

## Setup

There are some settings you need to check before use, to make sure the DNS records will be valid.
If you install the extension, the “Welcome” tab will guide you through this.

#### IP Address

The server’s Public IP Address needs to be set in Plesk.
This can be checked in Tools & Settings > IP Addresses. 
Make sure there is a Public IP set for all the IP’s your Domains will use.

#### Hostname

The server’s Hostname should have a valid FQDN set as it’s hostname. (e.g. server.domain.com)
If set incorrectly, your websites will still work, but sending email from the server will result in a poor sender rating and reduced mail deliverability.

You can check and change the Hostname in Plesk > Tools & Settings > Server Settings.
The Hostname should also resolve to the server’s Public IP Address, If it does not, an A record should be created in SafeDNS.


#### Nameservers

The Nameservers in Plesk’s DNS Template at should be set to: 
  - ns0.ukfast.net
  - ns1.ukfast.net

Go to Tools & Settings > General Settings > DNS Zone Template, and set the NS Records as above.
Then, click “Apply DNS Template Changes” , and select “Apply the changes to all zones.”

#### API Key

If you need to create or reset an API Key, Log into your MyUKFast account, go to “API Applications”.
The key should have Read & Write Access to SafeDNS, and DDoSX.

To add your API Key to Plesk, open the extension, and in the “Tasks & Config” tab , click Set API Key.
This can also be set in the welcome tab.

```eval_rst
.. note::
    DDoSX Will be implemented in a future release.
```

```eval_rst
  .. title:: {title goes here}
  .. meta::
     :title: Setup - Plesk SafeDNS Extension | UKFast Documentation
     :description: Setup Guide for UKFast SafeDNS Plesk Extension
     :keywords: ukfast, plesk, extension, safedns, dns, domains, integration, setup
```
