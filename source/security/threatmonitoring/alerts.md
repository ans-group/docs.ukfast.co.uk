# Alerts and rulesets

The alerts you wish to have generated will depend on your specific requirements, which you will define in the [planning phase](/security/threatmonitoring/gettingstarted.html)

Examples of events that can be detected include: users logging onto your infrastructure out of core business hours, or multiple failed attempts to log in to a server, followed by a successful log in.

You can choose to categorise alerts as follows:

- **Critical (14-16)** -
Critical alerts which will need to be investigated immediately, indicators of a system compromise, such events as successful logins after failed attempts, modifications to core system files, modifications to payment gateway files. Immediate investigation required.

- **High (11-13)** -
High level alerts which may need quick investigation, such as successful logins from unknown IP addresses, change of user account permissions. These events should be infrequent and not ignored.

- **Normal (6-10)** -
Events are categorised as user activity that is expected, but should be monitored. These are events such as successful logins from IP’s that are expected and during normal hours.

- **Low (1-5)** -
Low level events that we expect to see on systems as day to day use. Usually created by the system itself, they vary from failover events from users clusters, to Windows audit success / failures for Kerberos tickets / NTLM. These events are often ignored due to the amount that occur, but all will be visible on reporting functions.

You should be careful to categorise your alerts and rulesets, such that you are not overwhelmed by alerts for normal expected user behaviour.  The UKFast security team can advise you on this during the planning phase.

## MyUKFast dashboard

You can gain a real-time view of all your Threat Monitoring alerts in the [Threat Monitoring section of MyUKFast](https://my.ukfast.co.uk/threat-monitoring/) in the `Dashboard` tab, which will look as follows:

![dashboard](files/dashboardscreenshot.png)
