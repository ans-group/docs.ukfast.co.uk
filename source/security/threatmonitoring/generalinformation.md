.. meta::
   :title: Threat Monitoring | General Information | UKFast Documentation
   :description: General technical overview of Threat Monitoring and Response

# Threat Monitoring and Response - General Information

Threat Monitoring uses agents installed on each of your servers, which continuously analyse data to distinguish between potential security breaches and normal activity. It works to deliver the following services:
- Host-based Intrusion Detection and log file collation
- Internal vulnerability scanning
- File integrity monitoring
- Rootkit detection

## Host-based Intrusion Detection and log file collation
UKFast provide a default list of logs and events collected as standard but this can be customised for your environment during a discovery day with a security analyst (subject to an additional charge).

A central Threat Monitoring server sits within your management zone which all agents will forward logs to for rule analysis in real-time.

UKFast have created rulesets which analyse log files from all core technologies such as: syslog, mysql, sendmail, postfix, sshd, sysmon, ms-auth, squid, php etc.

If any of the 2000+ rules are triggered, an alert will be sent to a nominated email address (or multiple contact addresses) for investigation by the client. For example:
- Certain users logging onto the infrastructure outside of core hours.
- Multiple failed attempts to login to a server followed by successful authentication.
- Attempts to escalate account privileges to that of a super user.

Threat Monitoring activity will be displayed within MyUKFast in both a graphical format and as raw log files, this is displayed for the past 30 days by default but can be scheduled how the client would like (activity between two certain dates, weekly, daily etc.). This can help you to satisfy certain compliance requirements such as PCI DSS. Exporting and sending these reports directly to auditors can help to prove that all neccessary logging and monitoring is being performed, and that any incidents are properly investigated and responded to.

## Internal vulnerability scanning
Operating system and application vulnerabilities are often the primary cause of exploit on a client’s infrastructure. Part of our Threat Monitoring agent is a scheduled scan which detects any components that require patching and updating and the severity of leaving these vulnerabilities unpatched.

You can decide to either manage a patching and update schedule yourselves, or request this be executed by one of our support engineers on a schedule that works for your service.

## File integrity monitoring
After providing UKFast with a list of core system files and directories that you would like us to monitor, any changes to these core files are monitored and tracked. For example, you could monitor your payment gateway or redirect pages to ensure they are not manipulated to skim details or redirect customer payments elsewhere.

A hash of the file is taken and any changes to the hash generates alerts which are sent directly to you, with the time, date and user who made the changes.
