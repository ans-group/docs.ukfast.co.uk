# Troubleshooting (hardware-based WAFs)

This page relates to hardware-based WAFs only.  Please [see here](/security/ddos/wafsettings) for guidance on WAF on DDoSX.

Typically WAFs suffer from very few problems as long as they have been [set up correctly](/security/webapplicationfirewall/gettingstarted).

Here are a few possible fixes in the event of any issues:

  - **WAF doesn't appear to be working:**  Ensure the DNS is pointing towards the WAF IP rather than your internal server IP, as the WAF is acting as a proxy to provide the smoothest way of checking incoming traffic.

  - **WAF isn't blocking any traffic:**  This is most likely due to the WAF being in [learning mode](/security/webapplicationfirewall/gettingstarted).  Contact UKFast immediately to have the WAF fully switched-on.

  - **400 error:** This is typically due to either the WAF having a problem connecting to your internal server, or a problem on the internal server itself.

  - **500 error:** This isn't typically a WAF problem, usually it means a problem has occurred server-side

If you experience any problems with your WAF then please contact support or raise a ticket via [MyUKFast](https://my.ukfast.co.uk)


```eval_rst
   .. title:: Troubleshooting a WAF
   .. meta::
      :title: Troubleshooting a WAF | UKFast Documentation
      :description: Help to troubleshoot common problems when using a Web Application Firewall
      :keywords: ukfast, ddosx, web application firewall, waf, owasp, owasp top 10
```
