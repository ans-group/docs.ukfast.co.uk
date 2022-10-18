# What factors affect DNS propagation time?

```eval_rst
   .. title:: Domain Names | DNS Propagation
   .. meta::
      :title: Domain Names | DNS Propagation | UKFast Documentation
      :description: How to change your domain nameservers with UKFast
```

When updating domain name system (DNS) records for your domain there are a number of considerations to make when predicting the amount of time that the settings will take to be propagated across the internet. By default, it will likely take up to 24 hours (sometimes longer) for those updates to propagate across the internet when adding or editing the DNS records for your domain within [SafeDNS<sup>®</sup>](https://portal.ans.co.uk/safedns/index.php).

You can make changes to your SOA records to attempt to speed up the propagation process, however there are a number of other factors outside of our control.

```eval_rst
.. note::
   All nameservers, servers and browsers will be working to slightly different schedules depending on the last time their DNS information for your domain was updated. Because of this, whilst your new settings propagate across the internet, it is possible for some clients to be using new records and others to be using old records concurrently.
```

## Factors that affect DNS propagation times
- **TTL Settings**:  Time to live settings within the SOA     settings for each DNS record specify the amount of time that servers and nameservers will cache your DNS entry (in seconds). By default at UKFast this is set to `86400` (24 hours), decreasing the TTL settings can decrease propagation time as servers and browsers will only cache your DNS settings for a shorter amount of time.

  You will only be able to benefit from this after the value has been propagated across the network, setting a `3600` (1 hour) TTL from the default `86400` (24 hours) will still take upto 24 hours to propagate.

```eval_rst
.. note::
   Shorter TTL times should shorten overall propagation time, however this will create an increased number of queries to your nameserver, potentially increasing this overhead will slow your server's processing time.
```

A guide to changing your DNS records TTL settings can be found [here](/domains/safedns/ttl.md).

- **Internet Service Providers**: Many ISPs cache DNS settings to speed up browsing and reduce outbound traffic. It's possible that some of these servers will ignore your TTL and only update their cached records every couple of days. This could mean that clients using ISPs with long cache refreshing times could be waiting much longer to be served the new records.

- **Domain Name Registries**: Changes made within SafeDNS<sup>®</sup> will be changed within our registries in a matter of minutes, however some domain name registries try to protect their servers from excess load by setting an overriding TTL of 48 hours or more, which could delay the record's propagation across the internet.

