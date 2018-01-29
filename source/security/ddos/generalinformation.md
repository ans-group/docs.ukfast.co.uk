# General information / FAQs

Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks are becoming increasingly common. They work by flooding your server and firewall with hundreds of thousands of fake requests.  This is an attempt to overwhelm your servers and IT infrastructure, and cause downtime.

## How do DDoS attacks work?

Most DDoS attacks are layer 3 or 4 network "volumentric flood" attacks, where the objective is to saturate the bandwidth to your servers and consume your server resources to the point where requests can no longer be processed correctly.  These flood attacks target various network protocols such as UDP, IMCP, SYN/TCP and more.  They are often measured based on the amount of traffic attacking your site in Gbit/s.

DDoS attacks may also target your application itself (layer 7 attacks), to try and exploit vulnerabilities and cause your web server to fail.  These attacks may often send malformed packets which can't be handled correctly by your application, again causing it to fail.

## How does DDoSX<sup>®</sup> DDoS protection work?

DDoSX<sup>®</sup>, our DDoS protection service, is designed to detect and filter out DDoS attacks, and only deliver genuine traffic to your servers.  This is based on our global network which detects and absorbs the large amounts of traffic that DDoS attacks are comprised of, as close to the source of the attack as possible.  Suspicious traffic targeting your domains is intelligently filtered out and redirected to a decoy; the anomalies believe that they've reached and overwhelmed their target, and degradation of your website is avoided.

## Where does DDoSX<sup>®</sup> sit in my IT stack?

DDoSX<sup>®</sup> is a network-based solution which sits in front of your UKFast-hosted environment.  By repointing the DNS records of the domains you wish to protect to UKFast using [SafeDNS](/Domains/safedns/index.html), we can broadcast your IP address(es) across our global DDoSX<sup>®</sup> network.  All traffic destined for your domains will then be routed via this network, enabling us to filter out malicious traffic as described above.

## What type of traffic and applications does DDoSX support?

DDoSX supports HTTP and HTTPS web traffic on ports 80 and 443 respectively. If you need to route other types of traffic to your UKFast-hosted solution then please contact us before setting up DDoSX.

## What is a Web Application Firewall (WAF)?

Web Application Firewall (WAF) on DDoSX uses a global network to protect your online property from suspicious activity, meaning there is no physical hardware and no change to your existing infrastructure.  WAF on DDoSX can be simply provisioned for any domain you wish to add to DDoSX. It is an alternative approach to Web Application Firewall protection compared to a hardware-based WAF, as it allows you to set your own parameters as ‘paranoia levels’. WAF on DDoSX also allows you to select the domains you wish to protect, meaning that you only pay for those you want protecting.

## How does WAF on DDoSX work?

WAF on DDoSX is an example of a cloud-based WAF, designed to be more efficient via scalability. By using a WAF on the UKFast DDoSX global network, you benefit from a much greater capacity, which makes attack prevention more effective.  WAF on DDoSX is designed to protect you from the [OWASP top 10 vulnerabilities](/security/webapplicationfirewall/attacks.html)  


```eval_rst
.. meta::
     :title: DDoSX and CDN from UKFast | UKFast Documentation
     :description: General information on UKFast's global DDoSX network with CDN and WAF
     :keywords: ddos, ddos protection, anti-ddos, cdn, content delivery, content delivery network, ukfast, ddosx, web application firewall, waf
```
