
# How does Threat Monitoring work?

Once Threat Monitoring agents are installed on your server(s) they will be automatically configured to deliver the following services.

<div style="text-align: center;">

![hwo-it-works](files/hwo-it-works.png)

</div>

## Threat Detection, Attack Protection and log file collation

### Detection
UKFast's Host-Based Intrusion Detection (HIDS) solution, Threat Monitoring, will monitor numerous aspects of your infrastructure to detect suspicious activity. UKFast provide a full list of log locations to be monitored and event types that are collected as standard. Log locations can be customised for your environment, you can work with a UKFast security analyst to find the optimal configuration for your solution.

UKFast have created rule sets which analyse log files from all core technologies such as syslog, MySQL, FTP, Postfix, SSHd, cPanel, MS-auth, Apache, NGINX, PHP and more. These events are parsed through our 2,000+ rules, should a high-level event trigger, an alert will be sent to a nominated email address (or multiple contact addresses) for you to investigate.

If you have the additional Threat Response service then the UKFast security team will pro-actively investigate the alert and consult with you with recommended mitigating actions.

Additionally, you can [view a dashboard](/security/threatmonitoring/alerts.md), highlighting all activity detected through MyUKFast.

Example rules often triggered:
1.    Multiple attempts to log in to a server followed by a successful authentication
2.    Attempts to escalate account privileges to that of a superuser
3.    SQL Injection attacks
4.    XSS (Cross-Site Scripting) Attacks

Shown below is an example Threat Monitoring email alert. In the below alert, we can see that a shell shock attack, a level 15 alert has been detected.

<div style="text-align: center;">

![example-alert](files/example-alert.PNG)

</div>

### Dynamic Protection

Providing real-time protection against incoming attacks, UKFast's Threat Monitoring solution can block attacking IP addresses, through the use of a host-based firewall, such as IPTables (Linux) or Windows firewall. This protection, called Dynamic Protection, will block an attacker for 30 minutes, afterwards, removing the block. Should the attacker continue, the IP address is placed on a global blocklist for 30 days. This global blocklist spans across all customers protected with Threat Monitoring, enabling a wide area of protection, from a wide and varied attack base.

### Log collation

As per PCI-DSS requirements, all collected logs are securely stored on our Threat Monitoring infrastructure for 12 months. The last 3 months of this data is readily accessible and can be accessed through your MyUKFast dashboard.


## Vulnerability Scans

Operating system and application vulnerabilities are often the primary cause of a breach of a business's infrastructure. Delivered as part of the UKFast Threat Monitoring service are on-demand vulnerability scans, which detect any components that require patching or updating and configurations that need changing to ensure security. Detected items are also highlighted with a severity score allowing you to tailor your remediation efforts to the most critical threats.

Internal and external vulnerability scans can be conducted through MyUKFast. Once completed, a detailed online report will be generated, clearly defining any vulnerabilities found. A report can also be generated, containing the top vulnerabilities found in that scan.

For continued vulnerability monitoring, scheduled scans can be created to regularly scan and detect new vulnerabilities on your solution, ensuring that your infrastructure is always safe and secure.

Once you have the results of your report, you may choose to either manage any necessary patching and updates yourself or request that this is carried out by UKFast engineers during normal business hours.

Shown below is an example vulnerability scan ran on-demand through MyUKFast. In the image below, we can see an overview of this scan report. We can see the amount of critical, high, medium and low vulnerabilities found during the scan. We can also see what server's we have scanned, and the operating system detected by the scanner.


<div style="text-align: center; border: 1px solid black;">

![vuln-scan-summary](files/vuln-scan-summary.PNG)


</div>


Expanding the drop-down for the first server, we can see all the detected items for that particular servers, along with its corresponding severity level and threat score.

<div style="text-align: center; border: 1px solid black;">

![vuln-scan-expanded](files/vuln-scan-expanded.PNG)

</div>

Expanding further into a detected item, we can see exactly what this vulnerability relates to, along with with a synopsis, a detailed description and solutions advice on patching the vulnerability.

<div style="text-align: center; border: 1px solid black;">

![vuln-scan-item-expanded](files/vuln-scan-item-expanded.PNG)

</div>


## File Integrity Monitoring (FIM)

As part of your setup of Threat Monitoring, you can provide UKFast with a list of core system files and directories for which you wish to have [alerts raised](/security/threatmonitoring/alerts) if any changes are made. This is known as File Integrity Monitoring (FIM). A common use of FIM is to ensure payment gateways or redirect pages are not manipulated to divert customer payments elsewhere.

FIM works by taking a hash of each file or utilizing audit processes such as 'AuditD' in Linux and the 'Microsoft Windows audit system', any changes to these files are alerted with the time, date, process and user who made the changes.

File Integrity Monitoring alerts are accessible through MyUKFast, under the 'Alerts' sections on your Threat Monitoring dashboard. Shown below is an example FIM alert in MyUKFast, here we can see what file has changed, when, what process changed the file and exactly what has changed.

<div style="text-align: center;;">

![fim-alert](files/fim-alert.PNG)


</div>


## Rootkit and Malware detection

A "Rootkit" is a combination of software designed to enable administrator-level access to a computer or network, typically with malicious intent. Using deception techniques and interfacing directly with the kernel, rootkits are often very difficult to detect. UKFast's Threat Monitoring can detect common rootkits, searching for suspicious processes with root access to your IT systems. Rootkits are often combined with Malware; there are different types of rootkits but they all attempt to disguise classic Malware activity to prevent Rootkit detection.

Threat Monitoring has been designed to detect rootkits in several ways, for example scanning the /dev directory and file system to detect anomalies, searching for the presence of hidden processes and ports, and scanning system interfaces to detect those in promiscuous mode.

Through close integration with industry-leading Anti Virus scanners, such as McAfee AV and Clam AV, Threat Monitoring can alert you when a detection event has accrued, allowing for rapid response and threat removal from your IT Infrastructure. When coupled with Threat Response, Threat Monitoring Malware alerts prove to be a powerful tool against viruses and Malware.


## Server Baseline Hardening (available on Linux servers only)

To minimise the threat of an attack on computer infrastructure, a security baseline should be implemented. Our Threat Monitoring solution can scan your servers and compare them to industry-recognised baselines (PCI-DSS, CIS, NIST), to show where security enhancements can be made. Though security vulnerabilities are difficult or even impossible to predict, many of them require multiple conditions to be met at once to be successfully exploited.  Often by changing configuration files and disabling unused services, you can ensure that your infrastructure won't meet these conditions. For Linux servers, we can run baseline scans upon request, providing you with a report of insecure settings that exist on your operating system, along with suggestions on how to improve them.


```eval_rst
   .. title:: How Threat Monitoring Works
   .. meta::
      :title: How Threat Monitoring Works | ANS Documentation
      :description: Guidance relating to UKFast's Threat Monitoring solution
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection
```
