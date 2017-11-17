# Troubleshooting

Typically WAFs suffer from very few problems as long as they have been [set up correctly](https://docs.ukfast.co.uk/security/webapplicationfirewall/gettingstarted.html).

Here are a few possible fixes in the event of any issues: 

  - **WAF doesn't appear to be working:**  Ensure the DNS is pointing towards the WAF IP rather than your internal server IP, as the WAF is acting as a proxy to provide the smoothest way of checking incoming traffic.
  
  - **WAF isn't blocking any traffic:**  This is most likely due to the WAF being in [learning mode](https://docs.ukfast.co.uk/security/webapplicationfirewall/gettingstarted.html).  Contact UKFast immediately to have the WAF fully switched-on.

  - **400 error:** This is typically due to either the WAF having a problem connecting to your internal server, or a problem on the internal server itself.

  - **500 error:** This isn't typically a WAF problem, usually it means a problem has occurred server-side

If you experience any problems with your WAF then please contact support or raise a ticket via [MyUKFast](https://my.ukfast.co.uk)

```eval_rst
  .. meta::
     :title: Troubleshooting issues with Web Application Firewalls | UKFast Documentation
     :description: A guide to troubleshooting issues with a WAF
     :keywords: ukfast, security, web, application, firewall, waf, troubleshooting, issues, cloud, hosting

