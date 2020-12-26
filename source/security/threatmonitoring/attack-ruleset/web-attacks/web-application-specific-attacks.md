# Web Application Specific Attacks

Many attacks are targeted to exploit a known vulnerability in a specific web application like Word Press, Magneto or Joomla. These attacks have a higher likelihood of being successful, as they tend to specifically exploit known weaknesses in these applications. UKFast Threat Monitoring can detect common attacks and block the source IP address via a host-based firewall.


## osCOmmerce login.php bypass


**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```login.php```

Regex:  ```"POST /\S+.php/login.php?cPath=```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## osCommerce file manager bypass

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```login.php```

Regex: ```/admin/\w+.php/login.php```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Uploadify Exploit

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```uploadify.php```

Regex: ```"GET /\S+/uploadify.php?src=http://\S+.php```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## BBS delete.php Exploit

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```delete.php```

Regex: ```"GET \S+/delete.php?board_skin_path=http://\S+.php```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Simple shell.php Command Usage

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```shell.php```

Regex: ```GET \S+/shell.php?cmd=```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## PhpMyAdmin Setup Scans

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```phpMyAdmin/scripts/setup.php```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Suspicious URLs

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```.swp$ | .bak$ | /.htaccess | /server-status | /.ssh | /.history | /wallet.dat```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## High amount of POST Requests

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Request Type: ```POST```

Frequency: ```16```

Time frame: ```20```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Anomaly URL query (attempting to pass null termination).

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```%00```

Regex: ```"GET /\S+.php?\S+%00```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Timthumb Exploit

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

URL Contains: ```thumb.php | timthumb.php```

Regex: ```"GET \S+thumb.php?src=\S+.php```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.

## Timthumb Backdoor Access

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```"GET /\S+cart.php?\S+templatefile=../```

URL Contains: ```DECLARE%20@S%20CHAR|%20AS%20CHAR```

**Severity**

Threat Monitoring will classify this attack as a high, triggering the source IP address to be blocked using the below methods. As this attack is not severe, an alert will not be sent out via email, however, these attacks will still show up in dashboards in your MyUKFast.

**Remediation and Blocking**

Should a high-level attack be detected, Threat Monitoring will block the source IP address using a host-based firewall, IPTables (Linux) or Windows firewall for 30 minutes.


```eval_rst
   .. title: Web Application Attacks
   .. meta::
      :title: Web Application Attacks | UKFast Documentation
      :description: Guidance relating to UKFast's Threat Monitoring and Threat Response solutions
      :keywords: threat monitoring, security, compliance, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, threat response
```
