
# How does Threat Monitoring work?

Once Threat Monitoring agents are installed on your server(s) they will be automatically configured to deliver the following services:

## Attack Detection, Threat Detection and log file collation

UKFast's Host-Based Intrusion Detection (HIDS) solution, Threat Monitoring, will monitor numerous aspects of your infrastructure in order to detect suspicious activity. UKFast provide full list of log locations to be monitored and event types that are collected as standard. Log locations and can be customised for your environment, you can work with a UKFast security analyst to find the optimal configuration for your solution.

UKFast have created rulesets which analyse log files from all core technologies such as: syslog, MySQL, FTP, Postfix, SSHd, CPanel, MS-auth, Apache, Nginx, PHP and more. Thease events are parsed through our 2,000+ rules, should a high level event trigger, an alert will be sent to a nominated email address (or multiple contact addresses) for you to investigate.

If you have the additional Threat Response service then the UKFast security team will proactively investigate the alert and consult with you with recommended mitigating actions.

Additionally you can [view a dashboard](/security/threatmonitoring/alerts.html), highlighting all activity detected through MyUKFast.

Example rules often triggered:
1.	Multiple attempts to login to a server followed by successful authentication
2.	Attempts to escalate account privileges to that of a super user
3.	SQL Injection attacks
4.	XSS (Cross-Site Scripting) Attacks

Shown below is an example Threat Monitorngn email alert. In the below alert, we can see that a shellshock attack, a level 15 alert has been detectted.

EXAMPLE ALERT IMAGE HERE


## Vulnerability scans

Operating system and application vulnerabilities are often the primary cause of a breach of a business's infrastructure. Delivered as part of the UKFast Threat Monitoring service are on-demand vulnerability scans, which detect any components that require patching or updating and and configurations thaty need changing to ensure security. Detected items are also highlighted with a severity score allowing you to taiolor your remedation efforts to the most critial threats.

Internal and external vulnerability scnas can be conducted through MyUKFast. Once completed, a detailed online report will be generated, clearly defind any vulnerabilities found. A report can also be genrated, contained the top vulnerabiolties found in that scan. 

For continued vulnerability monitoring, shceduled scans can be created, to reguarly scan and detec new vuylnerabilties on your solution, ensuring that your inferstructire is always safe and secure.

Once you have the results of your report, you may choose to either manage any necessary patching and updates yourself, or request that this is carried out by UKFast engineers during normal business hours.

Shown below is an example vulnerability scan, ran on-demand trhough MyUKfast, In the image below, we can see a overview of this scan report, e can see the amount of critical, high, mediuma nd low vulnerabilities found during the scan. We can also see what server's we have scaned. and the operating systemdetected by the scanner.

VULN SCAN SUMMARY IMAGE HERE

Expanding the drop down for the firsty server, we can see all the edtected items for that particvilar servers, alsong with its corrwespondong severity level and threat score.

VULN SCAN EXPANDINGED IMAG HERE

Expanding further into a detected item, we can see exactly what this vulnerability relates to, along with a sysopsis, a detailed description and solutions advice on patching the vulnerability.

VULN SCAN ITEM EXPANDED IMAGE HERE


## File Integrity Monitoring (FIM)

As part of your setup of Threat Monitoring, you can can provide UKFast with a list of core system files and directories for which you wish to have [alerts raised](/security/threatmonitoring/alerts.html) in the event that any changes are made. This is known as File integrity Monitoring (FIM). A common use of FIM is to ensure payment gateway or redirect pages are not manipulated in order to divert customer payments elswhere.

FIM works by taking a hash of each file or utilising audit processes sauch and Auditd in linux and the Microsoft Windows audit system, any changes to thease files are alerted with the time, date, process and user who made the changes.

File Integrioty Monitoring alerts and accessible through MyUKFast, under the 'Alerts' sections on your Threat Monitoring dashboard. Shown below is an example FIM alert in MyUKFast, here we can what file has changed, when, what process changed the file and exactly what has changed.

FIM ALERT IMAGE HERE


## Rootkit and Malware detection

A "rootkit" is a combination of software designed to enable administrator-level access to a computer or network, typically with malicious intent.  It is vital to detect when root access has been gained to your IT systems before any malicious activity takes place.  Rootkits are often combined with malware; there are different types of rootkits but they all attempt to disguise classic malware activity to prevent rootkit detection.

Threat Monitoring has been designed to detect rootkits in a number of ways, for example scanning the /dev directory and filesystem to detect anomalies, searching for the presence of hidden processes and ports, and scanning system interfaces to detect those in promiscuous mode.


## Server Baseline Hardening (available on Linux servers only)

In order to minimize the threat of an attack on computer infrastructure, a security baseline should be implemented. Our Threat Monitoring solution has the ability to scan your servers and compare them to industry-recognised baselines (PCI-DSS, CIS, NIST), to show where improvements can be made. Though security vulnerabilities are difficult or even impossible to predict, many of them require multiple conditions to be met at once in order to be successfully exploited.  Often by changing configuration files and disabling unused services, you can ensure that your infrastructure won't meet these conditions. For Linux servers, we can run baseline scans every day, providing you with a report of insecure settings that exist on your operating system, along with suggestions on how to improve them.


```eval_rst
.. meta::
     :title: How Threat Monitoring works | UKFast Documentation
     :description: Guidance relating to UKFast's Threat Monitoring solution
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection
```
