
# WordPress

WordPress is an incredibly powerful website CMS that powers over 40% of websites on the Internet, so its no surprise that it's also one of the most common targets for attackers. WordPress, being more user-orientated and it's the ability to be expanded with plugins is especially susceptible to exploits and Zero-Day attacks.

## Monitor WordPress Activity

UKFast's Threat Monitoring has the ability to track WordPress activity and detect common attacks.

* Plugins activated, deactivated and upgraded
* Successful account logins
* Failed User Account Logins
* User password reset
* New User added
* New Blog Post Published
* Blog Post Deleted
* New Attachments

## Login Brute Force

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```wp-login.php|/administrator```

Regex: ```"POST \S+wp-login.php| "POST /administrator```

Frequency: ```8```

Timeframe: ```30```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Comment Spam from fake Search Engine Bots

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Request Type: ```POST```

URL ```Contains: /wp-comments-post.php```

Regex: ```Googlebot | MSNBot | BingBot```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.


```eval_rst
.. meta::
     :title: WordPress Rules | UKFast Documentation
     :description: Guidance relating to UKFast's Threat Monitoring and Threat Response solutions
     :keywords: threat monitoring, security, compliance, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, threat response

