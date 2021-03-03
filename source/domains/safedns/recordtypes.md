# Different types of DNS records

Whilst not specific to SafeDNS, it's always nice to have a breakdown of the various types of DNS records available, so here's a bit of a glossary:

* `CNAME` (Canonical Name) Record:

 Links a domain to the `A` name record of another domain for ease of redirection. So, when you setup a `CNAME` you are basically saying "Use the same IP for this domain (X) as this other domain (Y)".

* `CAA` (Certification Authority Authorisation)

CAA records are used to allow domain owners to declare which certificate authorities are allowed to issue a certificate for that domain. If a `CAA` record is present, only the `CA`s listed in the records are allowed to issue certificates for that hostname.

* `TXT` (Text) Record:

A `TXT` record allows you to provide extra information about a domain in unformatted human readable way. This is commonly used to provide information about a server, network, data centre etc.

* `A` (Address) Record:

An `A` record is used to map domain names to the <nospell>IPv4</nospell> address of a resource on the internet, such as another computer or server.

* `AAAA` (Quad-Address) Record:

An `AAAA` record is the same as the `A` record except it points the hostname to an <nospell>IPv6</nospell> address instead of an <nospell>IPv4</nospell> address. These records are only required if your server supports <nospell>IPv6</nospell> traffic.

* `MX` (Mail Exchanger) Record:

An `MX` record specifies the servers that deal with incoming email and in which order your servers that will be tried if you have several and the preferred one is unavailable.

* `SPF` (Sender Policy Framework) Record:

`SPF` records are designed to prevent spammers from spoofing emails from your domain by providing you with a statement confirming which servers are authorised to send email on your domain's behalf.

* `SRV` (Service) Record

`SRV` records provides data regarding a domain that tells you its location within the domain name system, e.g. its host name and port number.

* `SOA` (Start of Authority) Record:

`SOA` records are used to define the authoritative settings for your domain. This controls how your zone propagates to secondary nameservers across the Internet. SafeDNS creates an `SOA` record automatically for each domain added into our system.

`SOA` Records have the following fields:

* `Primary Nameserver` - This is the authoritative nameserver that other nameservers will use to get the most up-to-date records for the domain to resolve conflicting records from other nameservers.
* `Administrator Email` - This specifies the mailbox of the person responsible for managing records on this domain.
* `Refresh` - The time interval (in seconds) before records should be refreshed. Recommended value - 86400 (24 Hours).
* `Retry` - The time interval (in seconds) before a failed refresh should be retried. Recommended value - 7200 (2 Hours).
* `Expire` - The time interval (in seconds) that specifies the upper limit on the time interval that can elapse before the records are no longer valid. Recommended value - up to 2419200 (672 Hours).
* `TTL` - The number of seconds that this record will be cached on other servers.  
</br>

* `ALIAS` Record:

`ALIAS` are used to mimic `CNAME` behaviour, but can also be used on your [apex domain](https://docs.ukfast.co.uk/domains/safedns/apexdomain.html) and return the `A` and if configured the `AAAA` records. For more information on why you might use `ALIAS` record over `CNAME` please see this [guide](https://docs.ukfast.co.uk/domains/safedns/aliasrecord.html)

```eval_rst
   .. title:: SafeDNS | Different types of DNS records
   .. meta::
      :title: SafeDNS | Different types of DNS records | UKFast Documentation
      :description: Different types of DNS records within SafeDNS
```
