# ALIAS Record
```eval_rst
   .. title:: SafeDNS | ALIAS Record
   .. meta::
      :title: SafeDNS | ALIAS Record | UKFast Documentation
      :description: Explanation of the ALIAS Record

```
### Why should you use an `ALIAS` record over a `CNAME` record?

`ALIAS` records are used to overcome a limitation of the `CNAME` record from the [RFC2181](https://tools.ietf.org/html/rfc2181#section-10.1):
> <sub><sup>There may be only one</sup></sub></br>
> <sub><sup>such canonical name for any one alias.</sup></sub></br>

Which means you can't have another record along with a `CNAME` record. For example:
```
www.example.org 300 IN CNAME example.org
www.example.org 300 IN TXT "some text"
```
would be an invalid configuration.

However you can't just remove all records from your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apexdomain.html) when you want to use the `CNAME` record. As this breaks another RFC from the [Zone authority section](https://tools.ietf.org/html/rfc2181#section-6.1):
> <sub><sup>The authoritative servers for a zone are enumerated in the NS records</sup></sub></br>
> <sub><sup>for the origin of the zone, which, along with a Start of Authority</sup></sub></br>
> <sub><sup>(SOA) record are the mandatory records in every zone.</sup></sub></br>

So you have a mandatory `NS` and `SOA` with your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apex-domain.html), so using a `CNAME` there is an invalid configuration. This is where the `ALIAS` record comes in to help work around this problem.

If you want to use a domain name that been provided by a CDN/DDoS provider on your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apex-domain.html) SafeDNS allows you to set the `ALIAS` record and we will return the address records. For example:
```
example.org 300 IN ALIAS example.com
```
When you look up example.org we will return the `A` and if configured the `AAAA` records of example.com.

<b>Note: The `ALIAS` record is not actually officially an RFC, so where possible you should use the `CNAME` record</b>