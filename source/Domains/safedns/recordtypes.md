# Different types of DNS records

Whilst not specific to SafeDNS, it's always nice to have a breakdown of the various types of DNS records available, so here's a bit of a glossary:

* CNAME (Canonical Name) Record:

 Lnks a domain to the A name record of another domain for ease of redirection. So, when you setup a CNAME you are basically saying “Use the same IP for this domain (X) as this other domain (Y)”.

* TXT (Text) Record:

A TXT record allows you to provide extra information about a domain in unformatted human readable way. This is commonly used to provide information about a server, network, data centre etc.

* A (Address) Record:

An A record is used to map domain names to the IPv4 address of a resource on the internet, such as another computer or server.

* AAAA (Quad-Address) Record:

An AAAA record is the same as the A record except it points the hostname to an IPv6 address instead of an IPv4 address. These records are only required if your server supports IPv6 traffic.

* MX (Mail Exchanger) Record:

An MX (Mail Exchanger) record specifies the servers that deal with incoming email and in which order your servers that will be tried if you have several and the preferred one is unavailable.

* SPF (Sender Policy Framework) Record:

SPF records are designed to prevent spammers from spoofing emails from your domain by providing you with a statement confirming which servers are authorised to send email on your domain’s behalf.

* SRV (Service) Record

A SRV record provides data regarding a domain that tells you its location within the domain name system e.g. its host name and port number.

* Start of Authority(SOA) Record:

SOA records are used to define the authoritative settings for your domain. This controls how your zone propagates to secondary nameservers across the Internet. SafeDNS creates an SOA record automatically for each domain added into our system.

SOA Records have the following fields:

    * Primary Nameserver - This is the authoritative nameserver that other nameservers will use to get the most up-to-date records for the domain to resolve conflicting records from other nameservers.
    * Administrator Email - This specifies the mailbox of the person responsible for managing records on this domain.
    * Refresh - The time interval (in seconds) before records should be refreshed. Recommended value - 86400 (24 Hours).
    * Retry - The time interval (in seconds) before a failed refresh should be retried. Recommended value - 7200 (2 Hours).
    * Expire - The time interval (in seconds) that specifies the upper limit on the time interval that can elapse before the records are no longer valid. Recommended value - up to 2419200 (672 Hours).
    * TTL - The number of seconds that this record will be cached on other servers.* TTL - The number of seconds that this record will be cached on other servers.

```eval_rst
  .. meta::
     :title: Different types of DNS records | UKFast Documentation
     :description: Information on the different types of DNS records
     :keywords: ukfast, dns, type, information, guide, record, cloud, hosting

