# ALIAS Record
```eval_rst
   .. title:: SafeDNS | ALIAS Record
   .. meta::
      :title: SafeDNS | ALIAS Record | UKFast Documentation
      :description: Explanation of the ALIAS record and its use

```
### Why should you use an `ALIAS` record over a `CNAME` record?

`ALIAS` records are used to overcome a limitation of the `CNAME` record. From the [RFC2181](https://tools.ietf.org/html/rfc2181#section-10.1):

> 10.1. CNAME resource records
>
<<<<<<< HEAD
<<<<<<< HEAD
>   The DNS CNAME ("canonical name") record exists to provide the canonical name associated with an alias name. There may be only one such canonical name for any one alias.
=======
>   The DNS CNAME ("canonical name") record exists to provide the canonical name associated with an alias name. There may be only one such canonical name for any one alias.  
>>>>>>> A little reformatting
=======
>   The DNS CNAME ("canonical name") record exists to provide the canonical name associated with an alias name. There may be only one such canonical name for any one alias.
>>>>>>> Remove trailing spaces

Which means you can't have another record along with a `CNAME` record. For example, this would be an invalid configuration:

```none
www.example.org 300 IN CNAME example.org
www.example.org 300 IN TXT "some text"
```

However you can't just remove all records from your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apexdomain.html) when you want to use the `CNAME` record. This would  break another RFC from the [Zone authority section](https://tools.ietf.org/html/rfc2181#section-6.1):

> The authoritative servers for a zone are enumerated in the `NS` records for the origin of the zone, which, along with a Start of Authority (`SOA`) record are the mandatory records in every zone.

You have a mandatory `NS` and `SOA` record on your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apex-domain.html), so if using a `CNAME` too there is an invalid configuration. This is where the `ALIAS` record comes in, to help work around this problem.

If you want to use a domain name that been provided by a CDN / DDoS provider on your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apex-domain.html), SafeDNS allows you to set the `ALIAS` record and we will return the address records. For example:

```none
example.org 300 IN ALIAS example.com
```

In that example, when you look up `example.org`, we will return the `A` and (if configured) the `AAAA` records of `example.com`.

```eval_rst
.. note::
  The ``ALIAS`` record is not an official type under the RFC, so where possible you should use the ``CNAME`` record
```
