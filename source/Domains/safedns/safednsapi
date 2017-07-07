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

<table class="tg">
  <tr>
    <th class="tg-yw4l">Parameter</th>
    <th class="tg-yw4l">Description</th>
    <th class="tg-yw4l">Always Required</th>
    <th class="tg-yw4l">Size</th>
    <th class="tg-yw4l">Type &lt;br&gt;(A = Alpha numeric; &lt;br&gt;N = Numeric)</th>
  </tr>
  <tr>
    <td class="tg-yw4l">`username`</td>
    <td class="tg-yw4l">Your API username</td>
    <td class="tg-yw4l">Yes</td>
    <td class="tg-yw4l">100</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`password`</td>
    <td class="tg-yw4l">Your API password converted to MD5</td>
    <td class="tg-yw4l">Yes</td>
    <td class="tg-yw4l">32</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`command`</td>
    <td class="tg-yw4l">The API command you wish to perform</td>
    <td class="tg-yw4l">Yes</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`domain_id`</td>
    <td class="tg-yw4l">The domain ID of the entry in the database this can be obtained via get_domain_id</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`domain_name`</td>
    <td class="tg-yw4l">The domain name you want to add/edit/delete</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">255</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`pri_ip`</td>
    <td class="tg-yw4l">IP for the non www domain.com A record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">16</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`sec_ip`</td>
    <td class="tg-yw4l">IP for the www.domain.com A record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">16</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`soa_refresh`</td>
    <td class="tg-yw4l">The time (in seconds) a secondary DNS server waits before querying the primary DNS server to check for changes</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">6</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`soa_retry`</td>
    <td class="tg-yw4l">The time (in seconds a secondary server waits before retrying a failed zone transfer</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">6</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`soa_expire`</td>
    <td class="tg-yw4l">The time (in seconds) that a secondary server will keep trying to complete a zone transfer</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">6</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`soa_ttl`</td>
    <td class="tg-yw4l">The minimum time-to-live value for all records to inform other servers how long they should keep the data in cache</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">6</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`sub_a_id`</td>
    <td class="tg-yw4l">ID for the domains A record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`sub_a_name`</td>
    <td class="tg-yw4l">Hostname for the domains A record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">255</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`sub_a_ip`</td>
    <td class="tg-yw4l">IP for the domains A record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">16</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`mx[1-4]`</td>
    <td class="tg-yw4l">The MX records you want to set out or edit, i.e. mx1, mx2, mx3, mx4</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">255</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`mx[1-4]_pri`</td>
    <td class="tg-yw4l">The corresponding priority entries for the MX record, i.e mx1_pri, mx2_pri, mx3_pri, mx4_pri</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">2</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`alias`</td>
    <td class="tg-yw4l">The hostname to be used for the record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">255</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`destination`</td>
    <td class="tg-yw4l">The value/answer to be returned for the record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">1024</td>
    <td class="tg-yw4l">A</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`cname_id`</td>
    <td class="tg-yw4l">ID for the domains CNAME record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`txt_id`</td>
    <td class="tg-yw4l">ID for the domains TXT record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`spf_id`</td>
    <td class="tg-yw4l">ID for the domains SPF record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`srv_id`</td>
    <td class="tg-yw4l">ID for the domains SPF record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`aaaa_id`</td>
    <td class="tg-yw4l">ID for the domains AAAA record</td>
    <td class="tg-yw4l">No</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">N</td>
  </tr>
</table>

## Commands

This is a list of the commands accepted by the SafeDNS API

<table class="tg">
  <tr>
    <th class="tg-031e">Command</th>
    <th class="tg-031e">Description</th>
    <th class="tg-031e">Parameters</th>
    <th class="tg-yw4l">Expected Output</th>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_domains`</td>
    <td class="tg-yw4l">lists the domains in your SafeDNS account</td>
    <td class="tg-yw4l">-</td>
    <td class="tg-yw4l">domain_id|domain_name</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`check_domain`</td>
    <td class="tg-yw4l">Confirms if a domain is in your account or not</td>
    <td class="tg-yw4l">domain_id or domain_name</td>
    <td class="tg-yw4l">0 = Domain doesn't exist<br>1 = Domain does exist<br>99 = Domain cannot be added</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`get_domain_id`</td>
    <td class="tg-yw4l">Returns the domain ID for a given domain name</td>
    <td class="tg-yw4l">domain_name</td>
    <td class="tg-yw4l">domain_id</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`get_soa`</td>
    <td class="tg-yw4l">Lists the SOA record values for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">soa_refresh|soa_retry|soa_expire|soa_ttl</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`get_a`</td>
    <td class="tg-yw4l">Returns the IP for the domain name and the www.domain name</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">domain_id|www.domain_ip</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`get_sub_a`</td>
    <td class="tg-yw4l">Returns the IP for the sub domain name</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">sub_domain|sub_domain_ip</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`get_mx`</td>
    <td class="tg-yw4l">Lists the MX records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">MX[1-4]|mx_record|mx_priority</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_sub_domains`</td>
    <td class="tg-yw4l">Lists the sub domains for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">sub_domain_id|sub_domain_name</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_cnames`</td>
    <td class="tg-yw4l">Lists the CNAME records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">cname_id|alias|destination</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_txt`</td>
    <td class="tg-yw4l">Lists the TXT records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">txt_id|alias|destination</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_spf`</td>
    <td class="tg-yw4l">Lists the TXT records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">spf_id|alias|destination</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_srv`</td>
    <td class="tg-yw4l">Lists the SRV records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">srv_id|alias|destination|priority</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`list_aaaa`</td>
    <td class="tg-yw4l">Lists the AAAA records for a given domain</td>
    <td class="tg-yw4l">domain_id</td>
    <td class="tg-yw4l">aaaa_id|alias|destination</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_a`</td>
    <td class="tg-yw4l">Adds the domain to your SafeDNS account</td>
    <td class="tg-yw4l">domain_name</td>
    <td class="tg-yw4l">A records created, or a dynamic text response if there's an issue with an A record</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_suba`</td>
    <td class="tg-yw4l">Adds a sub domain record to your domain</td>
    <td class="tg-yw4l">domain_id<br>sub_a_name<br>sub_a_ip</td>
    <td class="tg-yw4l">Sub A record created or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_cname`</td>
    <td class="tg-yw4l">Adds a CNAME record to your domain</td>
    <td class="tg-yw4l">domain_id<br>alias<br>destination</td>
    <td class="tg-yw4l">CNAME record created oor a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_txt`</td>
    <td class="tg-yw4l">Adds a TXT record to your domain</td>
    <td class="tg-yw4l">domain_idalias<br>destination</td>
    <td class="tg-yw4l">TXT record created or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_spf`</td>
    <td class="tg-yw4l">Adds an SPF record to your domain</td>
    <td class="tg-yw4l">domain_id<br>alias<br>destination</td>
    <td class="tg-yw4l">SPF record created or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_srv`</td>
    <td class="tg-yw4l">Adds an SRV record to your domain.<br><br>Use the destination format `&lt;weight&gt; &lt;port&gt; &lt;target&gt;`<br>e.g.`5 5060 sip.example.com`</td>
    <td class="tg-yw4l">domain_id<br>alias<br>destination<br>srv_pri</td>
    <td class="tg-yw4l">SRV record created or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`create_aaaa`</td>
    <td class="tg-yw4l">Adds an AAAA record to your domain</td>
    <td class="tg-yw4l">domain_id<br>alias<br>destination</td>
    <td class="tg-yw4l">AAAA record created or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_soa`</td>
    <td class="tg-yw4l">Updates the SOA record values for a domain.<br><br>Access to modify SOA records must be active on your account.</td>
    <td class="tg-yw4l">domain_id<br>soa_refresh<br>soa_retry<br>soa_expire<br>soa_ttl</td>
    <td class="tg-yw4l">SOA Record updated or a dynamic text response if record couldn't be updated</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_a`</td>
    <td class="tg-yw4l">Allows you to update an A record for the domain name and www.domain name</td>
    <td class="tg-yw4l">domain_id<br>pri_ip<br>sec_ip</td>
    <td class="tg-yw4l">A Record(s) updated or a dynamic text response if there's an issue with one or more A records</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_suba`</td>
    <td class="tg-yw4l">Allows you to update an A record on your domain</td>
    <td class="tg-yw4l">domain_id<br>sub_a_id<br>sub_a_name<br>sub_a_ip</td>
    <td class="tg-yw4l">A record updated or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_mx`</td>
    <td class="tg-yw4l">This will set the MX records for a domain name, given that the A records are already setup</td>
    <td class="tg-yw4l">domain_id or domain_name<br>mx[1-4]<br>mx[1-4]_pri</td>
    <td class="tg-yw4l">MX Records updated or a dynamic text response if there's an issue with one or more MX records</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_cname`</td>
    <td class="tg-yw4l">Allows you to update a CNAME record on your domain</td>
    <td class="tg-yw4l">domain_id<br>cname_id<br>alias<br>destination</td>
    <td class="tg-yw4l">CNAME record updated or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_txt`</td>
    <td class="tg-yw4l">Allows you to update a TXT record on your domain</td>
    <td class="tg-yw4l">domain_id<br>txt_id<br>alias<br>destination</td>
    <td class="tg-yw4l">TXT record updated or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_spf`</td>
    <td class="tg-yw4l">Allows you to update an SPF record on your domain</td>
    <td class="tg-yw4l">domain_id<br>spf_id<br>alias<br>destination</td>
    <td class="tg-yw4l">SPF record updated or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_srv`</td>
    <td class="tg-yw4l">Allows you to update an SRV record on your domain. <br><br>Use the destination format<br>`&lt;weight&gt; &lt;port&gt; &lt;target&gt;`<br>e.g. `5 5060 sip.example.com`</td>
    <td class="tg-yw4l">domain_id<br>srv_id<br>alias<br>destination<br>srv_pri</td>
    <td class="tg-yw4l">SRV record updated or a dynamic text response if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`set_aaaa`</td>
    <td class="tg-yw4l">Allows you to update an AAAA record on your domain</td>
    <td class="tg-yw4l">domain_id<br>aaaa_id<br>alias<br>destination</td>
    <td class="tg-yw4l">AAAA record updated or a dynamic text if there's an error</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_domain`</td>
    <td class="tg-yw4l">Removes a domain from your SafeDNS account</td>
    <td class="tg-yw4l">domain_id or domain_name</td>
    <td class="tg-yw4l">DNS deleted or a dynamic text response if domain couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_suba`</td>
    <td class="tg-yw4l">Removes an A record from a domain</td>
    <td class="tg-yw4l">domain_id or domain_name<br>sub_a_id</td>
    <td class="tg-yw4l">A Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_cname`</td>
    <td class="tg-yw4l">Removes a CNAME record from a domain</td>
    <td class="tg-yw4l">domain_id<br>cname_id</td>
    <td class="tg-yw4l">CNAME Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_mx`</td>
    <td class="tg-yw4l">Removes all MX records for a domain</td>
    <td class="tg-yw4l">domain_id or domain_name</td>
    <td class="tg-yw4l">MX Records deleted or a dynamic text response with if the records couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_txt` A</td>
    <td class="tg-yw4l">Removes a TXT record from a domain</td>
    <td class="tg-yw4l">domain_id<br>txt_id</td>
    <td class="tg-yw4l">TXT Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_spf`</td>
    <td class="tg-yw4l">Removes an SPF record from a domain</td>
    <td class="tg-yw4l">domain_id<br>spf_id</td>
    <td class="tg-yw4l">SPF Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_srv`</td>
    <td class="tg-yw4l">Removes an SRV record from a domain</td>
    <td class="tg-yw4l">domain_id<br>srv_id</td>
    <td class="tg-yw4l">SRV Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`delete_aaaa`</td>
    <td class="tg-yw4l">Removes an AAAA record from a domain</td>
    <td class="tg-yw4l">domain_id<br>aaaa_id</td>
    <td class="tg-yw4l">AAAA Record deleted or a dynamic text response if the record couldn't be removed</td>
  </tr>
</table>

## Error Messages

This is a list of error messages you may encounter whilst using the SafeDNS API.  Error messages will be preceeded with `ERROR`

<table class="tg">
  <tr>
    <th class="tg-031e">Error Message</th>
    <th class="tg-031e">Information</th>
  </tr>
  <tr>
    <td class="tg-yw4l">`missing username`</td>
    <td class="tg-yw4l">Indicates a missing username</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`missing password`</td>
    <td class="tg-yw4l">Indicates a missing password</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`Invalid Login`</td>
    <td class="tg-yw4l">Indicates an invalid username and/or password</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`your account is inactive`</td>
    <td class="tg-yw4l">SafeDNS account is currently not activated</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`Domain doesn't exist in your DNS account`</td>
    <td class="tg-yw4l">The domain name specified doesn't exist in your account, so cannot be retrieved or updated</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`Can't update MX records without at least one A record for the domain`</td>
    <td class="tg-yw4l">MX records cannot be set or updated until the primary A records are set for the domain name</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`(primary/secondary/tertiary/fourth) mx is too long`</td>
    <td class="tg-yw4l">One of the MX records specified is too long; the MX record in question will be shown</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`invalid priority for (primary/secondary/tertiary/fourth) mx`</td>
    <td class="tg-yw4l">One of the MX record priorities is invalid; the MX priority record in question will be shown</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`Invalid (primary/secondary) IP`</td>
    <td class="tg-yw4l">An IP specified for the primary or secondary is invalid</td>
  </tr>
  <tr>
    <td class="tg-yw4l">`database error, please try again later`</td>
    <td class="tg-yw4l">Database error, please try again or contact support</td>
  </tr>
</table>

For help using the SafeDNS API, please contact UKFast support by raising a ticket in [MyUKFast](https://my.ukfast.co.uk/pss/add.php) or by calling 0800 230 0032.
