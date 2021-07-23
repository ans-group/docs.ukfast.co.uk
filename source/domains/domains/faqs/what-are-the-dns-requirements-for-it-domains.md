# What are the DNS requirements for .IT domains?

```eval_rst
   .. title:: Domain Name FAQ What are the DNS requirements for .IT domains?
   .. meta::
       :title:: Domain Name FAQ What are the DNS requirements for .IT domains?
       :description: Domain Name FAQ What are the DNS requirements for .IT domains?
```

To activate a .IT domain you must provide at least two functional nameservers, which can be provided when registering the domain or when activating it.

All DNS zones should be configured beforehand. The IT registry checks the DNS requirements at registration and if that fails, it checks them periodically thereafter. If, after 30 days, the DNS requirements are not met, the IT registry will delete the domain.

Every domain name registered must have the following requirements pre-configured:

1. The servers' IP addresses must be static and correspond to those actually associated with them.
2. The first nameserver must be the same as indicated in the Server of Authority (SOA) record of the domain name.
3. A CNAME must not be associated with the domain name.
4. The name of the nameserver specified in the SOA cannot be a CNAME.
5. At least one MX or A record must exist for the domain name.
6. Where an MX record is listed, it must not have an associated CNAME.
7. Whenever interrogated, the servers must not give the following responses: not responding, not reachable, not running, non-existent   domain, host not found, server failure, query failed.
8. Indicated nameservers must be authoritative for the domain name.

**IMPORTANT:** You cannot use the nameservers <nospell>(dns2.nic.it) or (dns3.nic.it)</nospell>

**NOTE:** The domain name and nameserver details are transferred to the zone file within 24 hour, after which time the domain name becomes active.

**NOTE:** Nameserver changes can take up to five days to complete pending validation by the Registry. During that time, the domain's status is pending update, and the old nameservers continue to be displayed.
