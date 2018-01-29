# Getting started with a Web Application Firewall (hardware-based)

This page relates to hardware-based WAFs only.  Please [see here](/security/ddos/gettingstarted.html) for guidance on getting started with WAF on DDoSX.

If you would like to implement a hardware-based WAF then it's important to understand the phases you will need to go through.  UKFast will work with you at each stage.

## Planning phase

During the planning phase you will define the web applications you wish to protect, and identify all the domains associated with these applications.  (A WAF operates on a "per domain" basis).

You will need to provide UKFast with:

  - The domains hosting the web applications you wish to protect
  - The internal IPs of the servers the web applications are hosted on

Our WAF analysts will work with you to understand what is considered "normal" traffic to your applications.  It's important to ensure a common understanding of exactly how your applications operate before moving forwards.  We will also identify points of potential access or attack.


## Learning phase

UKFast will build and implement the WAF based on the ruleset agreed in the planning phase.  At this stage, you will need to point the DNS records of the domains to be protected towards the WAF, rather than towards the servers hosting the applications. (If you manage your DNS through UKFast we may be able to do this for you.)

The WAF will initially be set to operate in a learning mode, which will last 2-4 weeks.  **During this learning phase, the WAF will be monitoring traffic but not blocking anything**.  The purpose of the learning phase is to identify the detailed traffic patterns to your applications, and to systematically understand which traffic should be whitelisted.  UKFast WAF analysts will work with you during this learning phase to whitelist legitimate traffic based on our common understanding of your applications and requirements.

```eval_rst
.. warning::
  It's vital to understand that when set to learning mode, the WAF is not blocking any traffic.
```


## Implementation phase

Only once the learning phase is completed and we've agreed between us the specific ruleset for your application, will the WAF be fully switched-on.  At this point, any traffic not specifically whitelisted will be deemed as malicious and blocked.  This will be recorded and available for ongoing analysis.


```eval_rst
.. meta::
     :title: Getting started with a hardware-based WAF | UKFast Documentation
     :description: Help with setting up a hardware-based Web Application Firewall from UKFast
     :keywords: ukfast, ddosx, web application firewall, waf, owasp, owasp top 10
```
