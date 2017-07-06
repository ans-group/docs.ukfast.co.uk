# SafeDNS API

The SafeDNS API allows you to manage and maintain your DNS records via a HTTPS
interface.  This article details the parameters, commands and error messages you'll need to understand to use the API.

If you need help using the SafeDNS API, please contact UKFast support by raising a ticket in [MyUKFast](https://my.ukfast.co.uk/pss/add.php) or by calling 0800 230 0032.

You can also use SafeDNS through [MyUKFast](https://my.ukfast.co.uk/safedns/index.php) if you don't want to use the API to manage your DNS records programmatically.

## Submission

API requests can be submitted through the following URL:

https://my.ukfast.co.uk/interface/dns.api.php

Any programming language capable of sending POST requests to this URL can be used. This allows you to integrate your existing website or application with SafeDNS directly.  Only POST requests are accepted; GET is not supported due to its limitations in data size.  Requests will only be accepted via https.

## Parameters

This is a list of parameters you can use with the SafeDNS API

|  Parameter   |  Description                                                                                                        |  Always Required |  Size |  Type <br>(A = Alpha numeric; <br>N = Numeric) |
| ------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------- | ----- | -------------------------------------- |
| `username`     |  Your API username                                                                                                  |  Yes             |  100  |  A                                     |
| `password`     |  Your API password converted to MD5                                                                                 |  Yes             |  32   |  A                                     |
| `command`      |  The API command you wish to perform                                                                                |  Yes             |  -    |  A                                     |
| `domain_id`    |  The domain ID of the entry in the database this can be obtained via get_domain_id                          |  No              |  -    |  N                                     |
| `domain_name`  |  The domain name you want to add/edit/delete                                                                        |  No              |  255  |  A                                     |
| `pri_ip`       |  IP for the non www domain.com A record                                                                             |  No              |  16   |  A                                     |
| `sec_ip`       |  IP for the www.domain.com A record                                                                                 |  No              |  16   |  A                                     |
| `soa_refresh`  |  The time (in seconds) a secondary DNS server waits before querying the primary DNS server to check for changes     |  No              |  6    |  N                                     |
| `soa_retry`    |  The time (in seconds a secondary server waits before retrying a failed zone transfer                               |  No              |  6    |  N                                     |
| `soa_expire`   |  The time (in seconds) that a secondary server will keep trying to complete a zone transfer                         |  No              |  6    |  N                                     |
| `soa_ttl`      |  The minimum time-to-live value for all records to inform other servers how long they should keep the data in cache |  No              |  6    |  N                                     |
| `sub_a_id`     |  ID for the domains A record                                                                                        |  No              |  -    |  N                                     |
| `sub_a_name`   |  Hostname for the domains A record                                                                                  |  No              |  255  |  N                                     |
| `sub_a_ip`     |  IP for the domains A record | No | 16 | N |
| `mx[1-4]`      |  The MX records you want to set out or edit, i.e. mx1, mx2, mx3, mx4 |No | 255 | A |
| `mx[1-4]_pri`  |  The corresponding priority entries for the MX record, i.e mx1_pri, mx2_pri, mx3_pri, mx4_pri | No | 2 | N |
| `alias` | The hostname to be used for the record | No | 255 | A |
| `destination` | The value/answer to be returned for the record | No | 1024 | A |
| `cname_id` | ID for the domains CNAME record | No | - | N |
| `txt_id` | ID for the domains TXT record | No | - | N |
| `spf_id` | ID for the domains SPF record | No | - | N |
| `srv_id` | ID for the domains SPF record | No | - | N |
| `aaaa_id` | ID for the domains AAAA record | No | - | N |

## Commands

This is a list of the commands accepted by the SafeDNS API

| Command | Description | Parameters | Expected Output |
| --------| ----------- | ---------- | --------------- |
| `list_domains` | lists the domains in your SafeDNS account | - | domain_id<br>domain_name |
| `check_domain` | Confirms if a domain is in your account or not | domain_id or domain_name | 0 = Domain doesn't exist<br>1 = Domain does exist<br>99 = Domain cannot be added |
| `get_domain_id` | Returns the domain ID for a given domain name | domain_name | domain_id
| `get_soa` | Lists the SOA record values for a given domain | domain_id | soa_refresh<br>soa_retry<br>soa_expire<br>soa_ttl
| `get_a` | Returns the IP for the domain name and the www.domain name | domain_id | domain_id<br>www.domain_ip
| `get_sub_a` | Returns the IP for the sub domain name | domain_id | sub_domain<br>sub_domain_ip
| `get_mx` | Lists the MX records for a given domain | domain_id | MX[1-4]<br>mx_record<br>mx_priority
| `list_sub_domains` | Lists the sub domains for a given domain | domain_id | sub_domain_id<br>sub_domain_name
| `list_cnames` | Lists the CNAME records for a given domain | domain_id | cname_id<br>alias<br>destination
| `list_txt` | Lists the TXT records for a given domain | domain_id | txt_id<br>alias<br>destination
| `list_spf` | Lists the TXT records for a given domain | domain_id | spf_id<br>alias<br>destination
| `list_srv` | Lists the SRV records for a given domain | domain_id | srv_id<br>alias<br>destination<br>priority
| `list_aaaa` | Lists the AAAA records for a given domain | domain_id | aaaa_id<br>alias<br>destination
| `create_a` | Adds the domain to your SafeDNS account | domain_name | A records created, or a dynamic text response if there's an issue with an A record
| `create_suba` | Adds a sub domain record to your domain | domain_id<br>sub_a_name<br>sub_a_ip | Sub A record created or a dynamic text response if there's an error
| `create_cname` | Adds a CNAME record to your domain | domain_id<br>alias<br>destination | CNAME record created oor a dynamic text response if there's an error
| `create_txt` | Adds a TXT record to your domain | domain_id<br>alias<br>destination | TXT record created or a dynamic text response if there's an error
| `create_spf` | Adds an SPF record to your domain | domain_id<br>alias<br>destination | SPF record created or a dynamic text response if there's an error
| `create_srv` | Adds an SRV record to your domain.<br>Use the destination format ``<weight> <port> <target>``<br>e.g.<br>`5 5060 sip.example.com` | domain_id<br>alias<br>destination<br>srv_pri | SRV record created or a dynamic text response if there's an error
| `create_aaaa` | Adds an AAAA record to your domain | domain_id<br>alias<br>destination | AAAA record created or a dynamic text response if there's an error
| `set_soa` | Updates the SOA record values for a domain.<br>Access to modify SOA records must be active on your account. | domain_id<br>soa_refresh<br>soa_retry<br>soa_expire<br>soa_ttl | SOA Record updated or a dynamic text response if record couldn't be updated
| `set_a` | Allows you to update an A record for the domain name and www.domain name | domain_id<br>pri_ip<br>sec_ip | A Record(s) updated or a dynamic text response if there's an issue with one or more A records
| `set_suba` | Allows you to update an A record on your domain | domain_id<br>sub_a_id<br>sub_a_name<br>sub_a_ip | A record updated or a dynamic text response if there's an error
| `set_mx` | This will set the MX records for a domain name, given that the A records are already setup | domain_id or domain_name<br>mx[1-4]<br>mx[1-4]_pri | MX Records updated or a dynamic text response if there's an issue with one or more MX records
| `set_cname` | Allows you to update a CNAME record on your domain | domain_id<br>cname_id<br>alias<br>destination | CNAME record updated or a dynamic text response if there's an error
| `set_txt` | Allows you to update a TXT record on your domain | domain_id<br>txt_id<br>alias<br>destination | TXT record updated or a dynamic text response if there's an error
| `set_spf` | Allows you to update an SPF record on your domain | domain_id<br>spf_id<br>alias<br>destination | SPF record updated or a dynamic text response if there's an error
| `set_srv` | Allows you to update an SRV record on your domain. Use the destination format<br>`<weight> <port> <target>`<br>e.g. `5 5060 sip.example.com` | domain_id<br>srv_id<br>alias<br>destination<br>srv_pri | SRV record updated or a dynamic text response if there's an error
| `set_aaaa` | Allows you to update an AAAA record on your domain | domain_id<br>aaaa_id<br>alias<br>destination | AAAA record updated or a dynamic text if there's an error
| `delete_domain` | Removes a domain from your SafeDNS account | domain_id or domain_name | DNS deleted or a dynamic text response if domain couldn't be removed
| `delete_suba` | Removes an A record from a domain | domain_id or domain_name<br>sub_a_id | A Record deleted or a dynamic text response if the record couldn't be removed
| `delete_cname` | Removes a CNAME record from a domain | domain_id<br>cname_id | CNAME Record deleted or a dynamic text response if the record couldn't be removed
| `delete_mx` | Removes all MX records for a domain | domain_id or domain_name | MX Records deleted or a dynamic text response with if the records couldn't be removed
| `delete_txt` A| Removes a TXT record from a domain | domain_id<br>txt_id | TXT Record deleted or a dynamic text response if the record couldn't be removed
| `delete_spf` | Removes an SPF record from a domain | domain_id<br>spf_id<br> | SPF Record deleted or a dynamic text response if the record couldn't be removed
| `delete_srv`| Removes an SRV record from a domain | domain_id<br>srv_id | SRV Record deleted or a dynamic text response if the record couldn't be removed
| `delete_aaaa` | Removes an AAAA record from a domain | domain_id<br>aaaa_id | AAAA Record deleted or a dynamic text response if the record couldn't be removed

## Error Messages

This is a list of error messages you may encounter whilst using the SafeDNS API.  Error messages will be preceeded with `ERROR`

| Error Message | Information |
| ------------- | ----------- |
| `missing username` | Indicates a missing username
| `missing password` | Indicates a missing password
| `Invalid Login` | Indicates an invalid username and/or password
| `your account is inactive` | SafeDNS account is currently not activated
| `Domain doesn't exist in your DNS account` | The domain name specified doesn't exist in your account, so cannot be retrieved or updated
| `Can't update MX records without at least one A record for the domain` | MX records cannot be set or updated until the primary A records are set for the domain name
| `(primary/secondary/tertiary/fourth) mx is too long` | One of the MX records specified is too long; the MX record in question will be shown
| `invalid priority for (primary/secondary/tertiary/fourth) mx` | One of the MX record priorities is invalid; the MX priority record in question will be shown
| `Invalid (primary/secondary) IP` | An IP specified for the primary or secondary is invalid
| `database error, please try again later` | Database error, please try again or contact support

For help using the SafeDNS API, please contact UKFast support by raising a ticket in [MyUKFast](https://my.ukfast.co.uk/pss/add.php) or by calling 0800 230 0032.
