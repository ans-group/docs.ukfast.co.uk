# How does Threat Monitoring work?

Once Threat Monitoring agents are installed on your server(s) they will be automatically configured to deliver the following services:

## Host-Based Intrusion Detection (HIDS) and log file collation

Host-Based Intrusion Detection (HIDS) will monitor numerous aspects of your infrastructure in order to detect suspicious activity.  UKFast provide a default list of logs and events collected as standard, however this can be customised for your environment during the [planning phase](/security/threatmonitoring/gettingstarted.html) where you will work with a UKFast security analyst.

A central threat monitoring server will be installed within your management zone which all Threat Monitoring agents will forward logs to for real-time rule analysis.

UKFast have created rulesets which analyse log files from all core technologies such as: syslog, MySQL, Sendmail, Postfix, sshd, sysmon, MS-auth, Squid, PHP and more.

If any of the 2,000+ rules created are triggered an alert will be sent to a nominated email address (or multiple contact addresses) for you to investigate.  If you have the additional Threat Response service then the UKFast security team will proactively investigate the alert and consult with you on recommended mitigating actions.

Additionally you can [view a report based](/security/threatmonitoring/alerts.html) on all activity detected in MyUKFast.

Example rules often triggered:
1.	Certain users logging onto the infrastructure out of core hours or on the weekend.
2.	Multiple attempts to login to a server followed by successful authentication.
3.	Attempts to escalate account privileges to that of a super user.


## Vulnerability scans

Operating system and application vulnerabilities are often the primary cause of exploit on a customer's infrastructure. Part of the UKFast Threat Monitoring service is a scheduled scan which detects any components that require patching and updating, which will also highlight the severity of leaving such vulnerabilities unpatched.

By default, vulnerability scans are scheduled monthly, however additional scans can be scheduled by raising a ticket to UKFast Support via [MyUKFast](https://my.ukfast.co.uk).  Reports are available via download from MyUKFast. You may choose to either manage any necessary patching and updates yourself, or request this to be done by UKFast Threat Response engineers during normal business hours.

[add screenshot of MyUKFast]

## File integrity monitoring

As part of your setup of Threat Monitoring, you can can
As part of the base tier system, as currently proposed, clients will need to provide UKFast with a list of core system files or directories that they would like to be monitored and any changes tracked. The biggest application seen for this is ensuring payment gateway or redirect pages are not manipulated to send customer payments elsewhere. A hash of the file is taken, any changes to the hash generates alerts which are sent directly to clients, with the time, date and user who made the changes. Clients are directly sent these alerts as the likelihood of false positives occurring, due to development work for example, can be quite regular.

## Rootkit detection

We don't have any information on this as Stephen Crow our top security guy wouldn't provide any. if you want to complain please email Stephen.crow@ukfast.co.uk
