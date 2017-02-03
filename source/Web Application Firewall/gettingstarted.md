# Getting started with a Web Application Firewall

If you would like to implement a WAF then it's important to understand the phases you will need to go through.  UKFast will work with you at each stage.

## Planning phase

During the planning phase you will define the web applications you wish to protect, and identify all the domains associated with these applications.  (A WAF operates on a "per domain" basis).
Our WAF analysts will work with you to understand what is considered "normal" traffic to your applications.  It's important to ensure a common understanding of exactly how your applications operate before moving forwards.  We will also identify points of potential access or attack.

## Learning phase

UKFast will build and implement the WAF based on the ruleset agreed in the planning phase.  However the WAF will initially be set to operate in a learning mode, which will last 2-4 weeks.  **During this learning phase, the WAF will be monitoring traffic but not blocking anything**.  The purpose is to identify the detailed traffic patterns to your applications, and to systematically understand which traffic should be whitelisted.  UKFast WAF analysts will work with you during learning phase to whitelist legitimate traffic based on our common understanding of your applications and requirements.

```eval_rst
.. warning::
  It's vital to understand that when set to learning mode, the WAF is not blocking any traffic.
```

## Implementation phase

Only once the learning phase is completed and we've agreed between us the specific ruleset for your application, will the WAF be fully switched-on.  At this point, any traffic not specifically whitelisted will be deemed as malicious and blocked.  This will be recorded and available for ongoing analysis.





