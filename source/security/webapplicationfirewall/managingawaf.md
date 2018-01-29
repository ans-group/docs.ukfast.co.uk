# Managing a Web Application Firewall in-life (hardware-based)

This page relates to hardware-based WAFs only.  Please [see here](/security/ddos/wafsettings.html) for guidance on managing a WAF on DDoSX.

Once your WAF has been through the learning phase and is fully operational, our analysts will monitor traffic patterns and identify any changes needed to the configuration and rulesets.

It's important you keep UKFast updated as and when you make any changes to your applications or IT environment that might impact the WAF and traffic being whitelisted or blocked.  Failure to do so could result in either legitimate traffic being blocked unnecessarily, or in your applications being exposed to attack.  Please advise UKFast of changes such as:

  - IP addresses
  - changes to web applications and user access/experience
  - changes to domains and where they are hosted
  - changes in how your web applications are hosted. This is of particular importance for attacks such as SQL injections or directory traversal attacks.

Please raise a ticket via [MyUKFast](https://my.ukfast.co.uk) to provide us details of any relevant changes.


```eval_rst
.. meta::
     :title: Managing a hardware-based WAF | UKFast Documentation
     :description: General information on managing a UKFast hardware-based Web Application Firewall
     :keywords: ukfast, ddosx, web application firewall, waf, owasp, owasp top 10
```
