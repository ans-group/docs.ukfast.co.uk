# What is a Web Application Firewall?

A Web Aplication Firewall (WAF) is a piece of software installed on a proxy that is used to filter, control, and analyse traffic sent to and from a web application e.g. a website.
On a simple level a WAF is a firewall that has been specifically configured from the ground up to cover web applications, as opposed to a standard firewall that works based on access lists, input & output, and access controls.

UKFast WAFs follow the good security practice of "blacklist everything, only whitelist what is necessary". This approach ensures the WAF detects and prevents as many attacks as possible, and secures your application accordingly.

## How does a WAF work?

A WAF operates by following specially built rules and rulesets. Starting from a standard ruleset, UKFast can configure these specifically for your solution and applications to ensure that all traffic to the monitored web applications are checked.  If traffic matches the ruleset it will be allowed through, otherwise it will be dropped immediately and the potential attack will be prevented.

However, every web application can be different and have specific methods of inputting data. Given this, it is possible for some legitimate traffic to get caught by the WAF filter and dropped.  To mitigate this risk on an ongoing basis, UKFast has a dedicated analyst team who will work with you to advise on ruleset updates and tweaks for your WAF.  Often this team will spot problems and correct them before it becomes apparent to customers, however if you do believe your WAF is not functioning optimally then please contact support, raise a ticket via [MyUKFast](https://my.ukfast.co.uk) or call your UKFast account manager.

Further information relating to WAF on DDoSX can be found [here](/security/ddos/wafsettings.html)


```eval_rst
.. meta::
     :title: What is a Web Application Firewall? | UKFast Documentation
     :description: General information on Web Application Firewalls and how they work
     :keywords: ukfast, ddosx, web application firewall, waf, owasp, owasp top 10
```
