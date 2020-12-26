# ProFTPd

## proftpd FTP brute force (multiple failed logins).

*What does this rule tell me?*


A brute force attack is one of the more common attacks used today. Its a generic term used when an attacker tries different username and password combinations. This kind of attack is most common on FTP and SSH servers. In this case, your FTP server may have experienced a brute force attack.

A false-positive can sometimes fire if a user has forgotten their login details and is repeatedly failing to log in - Please bear this in mind.

Brute Force attacks are usually based on dictionary attacks, where a list of common passwords is used. It can take a few minutes to try hundreds of password combinations.

What program/service does this rule relate to?


FTP Server [File Transfer Protocol]

*How can I fix this?*


The easiest way to protect yourself from brute force attacks is to employ a strong password. A strong password may consist of 15 characters, upper-case, lower-case, symbols and numbers.

Restrict access to your login URL. Your login page may be publicly facing, if so, you may want to restrict it to an internal IP address range.

*Does this mean I am being attacked?*

In this situation, there is a high chance that your server is being targeted by a brute force attack. If the numbers are relatively low, this may not be the case and it might be that someone has forgotten their login credentials and is trying to regain access.

```eval_rst
   .. title: FTP Rules Explained
   .. meta::
      :title: FTP Rules Explained | UKFast Documentation
      :description: Our Threat Monitoring ruleset explained
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
```
