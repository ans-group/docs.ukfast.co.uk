# How does Threat Monitoring work?

Once Threat Monitoring agents are installed on your server(s) they will be automatically configured to deliver the following services:

## Host-Based Intrusion Detection (HIDS) and log file collation

Host-Based Intrusion Detection (HIDS) will monitor numerous aspects of your infrastructure in order to detect suspicious activity.  UKFast provide a default list of logs and events collected as standard, however this can be customised for your environment during the [planning phase](/security/threatmonitoring/gettingstarted.html) where you will work with a UKFast security analyst.

UKFast have created rulesets which analyse log files from all core technologies such as: syslog, MySQL, Sendmail, Postfix, sshd, sysmon, MS-auth, Squid, PHP and more. If any of the 2,000+ rules are triggered then an alert will be sent to a nominated email address (or multiple contact addresses) for you to investigate.  If you have the additional Threat Response service then the UKFast security team will proactively investigate the alert and consult with you on recommended mitigating actions.

Additionally you can [view a report](/security/threatmonitoring/alerts.html) highlighting all activity detected in MyUKFast.

Example rules often triggered:
1.	Certain users logging onto the infrastructure out of core business hours
2.	Multiple attempts to login to a server followed by successful authentication
3.	Attempts to escalate account privileges to that of a super user


## Vulnerability scans

Operating system and application vulnerabilities are often the primary cause of a breach of a business's infrastructure. Part of the UKFast Threat Monitoring service is a scheduled vulnerability scan which detects any components that require patching and updating, and will also highlight the severity of leaving such vulnerabilities unpatched.

By default, vulnerability scans are scheduled monthly, however additional scans can be requested by raising a ticket to UKFast Support via [MyUKFast](https://my.ukfast.co.uk).  Reports are available via download from MyUKFast. Once you have the results of your report, you may choose to either manage any necessary patching and updates yourself, or request that this is carried out by UKFast engineers during normal business hours.


## File Integrity Monitoring (FIM)

As part of your setup of Threat Monitoring, you can can provide UKFast with a list of core system files and directories for which you wish to have [alerts raised](/security/threatmonitoring/alerts.html) in the event that any changes are made.  This is known as File integrity Monitoring (FIM).  A common use of FIM is to ensure payment gateway or redirect pages are not manipulated in order to divert customer payments elswhere.

FIM works by taking a hash of each file, and then any changes to this hash are alerted with the time, date and user who made the changes.


## Rootkit detection

A "rootkit" is a combination of software designed to enable administrator-level access to a computer or network, typically with malicious intent.  It is vital to detect when root access has been gained to your IT systems before any malicious activity takes place.  Rootkits are often combined with malware; there are different types of rootkits but they all attempt to disguise classic malware activity to prevent rootkit detection.

Threat Monitoring has been designed to detect rootkits in a number of ways, for example scanning the /dev directory and filesystem to detect anomalies, searching for the presence of hidden processes and ports, and scanning system interfaces to detect those in promiscuous mode.


```eval_rst
.. meta::
     :title: How Threat Monitoring works | UKFast Documentation
     :description: Guidance relating to UKFast's Threat Monitoring solution
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection
```
