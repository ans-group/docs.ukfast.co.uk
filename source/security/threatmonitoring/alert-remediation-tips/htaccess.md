# Page authentication and restrictions with htaccess

Administration panels and gateways are a prime target for attackers, brute force attacks and XSS attacks are common to try and gain access to your website with administrative privileges. Websites powered by a CMS, like WordPress or Magento are especially vulnerable to this. Login and administration panels can be easily found with these CMS systems, so enabling an extra step of authentication is pivotal to ensure security.

Luckily, we can employ access control rules through the use of an htaccess file. This file will communicate with the web server whenever a user tries to access a restricted path, '/wp-admin' for example. This communication with the web servers allows authentication checks to be employed, these could include asking the user for a username and password, requiring certain IP addresses or even blocking certain user agents and browsers.

From a Threat Monitoring standpoint, we find that servers that employ this type of security on administration panels see a 90% reduction in the number of brute force attacks sitewide.

For more information on setting this up, feel free to follow our guide on setting up htaccess rules.

```eval_rst
.. meta::
     :title: htaccess Authentication | ANS Documentation
     :description: Useful threat remediation and prevention tips
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
