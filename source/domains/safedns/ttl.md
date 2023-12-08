# Changing TTL (Time to Live)

```eval_rst
  .. title:: SafeDNS | Changing TTL on a DNS record
   .. meta::
      :title: SafeDNS | Changing TTL on a DNS record | ANS Documentation
      :description: Changing TTL on a DNS record within SafeDNS

```

The Time to Live (TTL) value of your domain is set in seconds, this is the amount of time other DNS servers are told they are allowed to cache your records for before rechecking with an authoritative server (though they don't all honour this). The default time is 86400 seconds, which is 24 hours. This isn't an issue most of the time, but if you ever want to change the IP on one of your records, a 24 hour delay may be unacceptable.

You can modify the TTL value for records in the following location:

Select `Product and Services` > `SafeDNS` > select your domain name > Under the `SOA` heading is the `TTL` value.

Please remember this value is in seconds and that the lowest recommended value is `300` seconds.

Also note that there are a number of different factors that can affect the total propagation time of DNS record changes. Please see ["What factors affect DNS propagation time?"](/domains/domains/dnspropagation) for more information.
