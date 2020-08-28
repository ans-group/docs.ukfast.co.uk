# General information / FAQs

Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks are becoming increasingly common. They work by flooding your server and firewall with hundreds of thousands of fake requests.  This is an attempt to overwhelm your servers and IT infrastructure, and cause downtime.

## How do DDoS attacks work?

Most DDoS attacks are layer 3 or 4 network "volumetric flood" attacks, where the objective is to saturate the bandwidth to your servers and consume your server resources to the point where requests can no longer be processed correctly.  These flood attacks target various network protocols such as UDP, ICMP, SYN/TCP and more.  They are often measured based on the amount of traffic attacking your site in Gbit/s.

DDoS attacks may also target your application itself (layer 7 attacks), to try and exploit vulnerabilities and cause your web server to fail.  These attacks may often send malformed packets which can't be handled correctly by your application, again causing it to fail.

## How does DDoSx<sup>®</sup> DDoS protection work?

DDoSx<sup>®</sup>, our DDoS protection service, is designed to detect and filter out DDoS attacks, and only deliver genuine traffic to your servers.  This is based on our global network which detects and absorbs the large amounts of traffic that DDoS attacks are comprised of, as close to the source of the attack as possible.  Suspicious traffic targeting your domains is intelligently filtered out and redirected to a decoy; the anomalies believe that they've reached and overwhelmed their target, and degradation of your website is avoided.

## Where does DDoSx<sup>®</sup> sit in my IT stack?

DDoSx<sup>®</sup> is a network-based solution which sits in front of your UKFast-hosted environment.  By re-pointing the DNS records of the domains you wish to protect to UKFast using [SafeDNS](/domains/safedns/index), we can broadcast your IP address(es) across our global DDoSx<sup>®</sup> network.  All traffic destined for your domains will then be routed via this network, enabling us to filter out malicious traffic as described above.

## What type of traffic and applications does DDoSx support?

DDoSx supports HTTP and HTTPS web traffic on ports 80 and 443 respectively. If you need to route other types of traffic to your UKFast-hosted solution then please contact us before setting up DDoSx.

## What is a Web Application Firewall (WAF)?

Web Application Firewall (WAF) on DDoSx uses a global network to protect your online property from suspicious activity, meaning there is no physical hardware and no change to your existing infrastructure.  WAF on DDoSx can be simply provisioned for any domain you wish to add to DDoSx. It is an alternative approach to Web Application Firewall protection compared to a hardware-based WAF, as it allows you to set your own parameters as ‘paranoia levels'. WAF on DDoSx also allows you to select the domains you wish to protect, meaning that you only pay for those you want protecting.

## How does WAF on DDoSx work?

WAF on DDoSx is an example of a cloud-based WAF, designed to be more efficient via scalability. By using a WAF on the UKFast DDoSx global network, you benefit from a much greater capacity, which makes attack prevention more effective.  WAF on DDoSx is designed to protect you from the [OWASP top 10 vulnerabilities](/security/webapplicationfirewall/attacks)  

## How do I set up a CNAME?

In order to protect your root domain, for example UKFast.co.uk, you must first check that your DNS provider will support root level forwarding such as; an ALIAS or ANAME. If your DNS provider does not support this we cannot protect the root domain. The root domain will also not be protected by WAF or able to serve CDN. However, for example,  www.ukfast.co.uk  and all subdomains will be fully protected. For more information read our documentation.

A CNAME record links a domain to the A name record of another domain for ease of redirection.

1. Login to MyUKFast and head to DDoSx Protection in the Products and Services menu.
2. Click Connect Now
3. Type the domain you would like to protect in the domain box.
4. A message will pop up to add a CNAME record. Click Connect.

In order to connect your domain to the DDoSx network you must first verify that this is your domain. To do this follow the on screen instructions. Once this process has been completed and the verification has been confirmed you will proceed to the configure tab within DDoSx. To then complete the set up of your domain on DDoSx read our [documentation here](/security/ddos/index). 

```eval_rst
   .. title:: DDoSx and CDN from UKFast
   .. meta::
      :title: DDoSx and CDN from UKFast | UKFast Documentation
      :description: General information on UKFast's global DDoSx network with CDN and WAF
      :keywords: ddos, ddos protection, anti-ddos, cdn, content delivery, content delivery network, ukfast, ddosx, web application firewall, waf
```
