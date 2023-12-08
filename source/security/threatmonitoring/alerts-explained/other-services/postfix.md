# Postfix

## Postfix Multiple misuses of SMTP service (bad sequence of commands).

Multiple Misuse of SMTP Service is a feature where some Postfix commands are being used in unsupported configurations and return ```503 Bad Sequence of Commands```. This can be caused by servers sending multiple commands out at a time or messing up the ordering of the commands.

This can relate to all mail servers, however, this page focuses on Postfix. This is a standard communication between mail servers which allows for communication of email servers of different types. Postfix is a more commonly used system which runs on Unix-like systems such as Linux, macOS and FreeBSD.

*Does this mean I am being attacked?*


This can happen for multiple reasons. It doesn't always mean that there is an attack. However, rarely, an attacker may try to break a mail server and may try to send packets out of order to see what they can break. Modern mail servers combat this by showing a 503, which is the error handler code to cancel the connection, but not crash the whole program. This is the most they are going to receive.

*How can I fix this?*


Monitoring is the best thing to do in this situation. Check the Postfix logs, to work out where the issue is. This is the best place to start as these commands can be oddly specific and sometimes fairly random.
Client authentication is also a good place to look at. Modern Mail systems use ```STARTTLS``` to serve emails. Older systems may use ```SSL TLS```. This is an older protocol which is incompatible with the newer ```STARTTLS```.  Making sure that the programs or the client connecting to it use the right authentication method is key to its success.



Review the logs to make sure that the issue is isolated. They can be found at:

`/var/log/mail.log`


This error is very rarely to do with your server configuration and is more likely a client misconfiguration. This can be identified and fixed so that bad user experiences can be avoided.

If an attacker is trying to break your mail server, blocking their IP address on your firewalls will stop them from being able to reach your mail server, so they will not be able to send the wrong commands.


## Postfix Multiple attempts to send e-mail from a blocked IP address (blocked).


*What does this mean?*


This rule is informing you that there have been multiple attempts at sending an email from an IP that is blocked, meaning the IP address is known to be involved in spam activities. It's not uncommon for a mail IP address to end up on the blocklist, especially on a shared server. This can be due to the volume of mail coming from that server or messages possessing spam-like characteristics. It can also be caused by email forwarders.

This does not mean that you are being attacked. It is more likely because blocklists automatically add your mail servers IP address that is assigned via your ISP. An IP can also end up being on a blocklist due to a virus, malware or spam. Should you have a virus or malware on your computer and it is constantly pinging or attempting to communicate with other computers, the admin of another computer will likely see this attack and block the IP address and report it. If spam email is sent or a mail server is run that is not properly configured and it allows spam to be sent then the IP address becomes blocked.

*How do I fix this?*

First, you should make sure that all devices on your network are not infected. After you've determined your network is clean and that no unauthorised traffic is going out, you may need to request that your IP address be removed from the relevant list. Each list will have guidance on how how to do this for their service.

```eval_rst
   .. title:: Postfix Rules Explained
   .. meta::
      :title: Postfix Rules Explained | ANS Documentation
      :description: Our Threat Monitoring ruleset explained
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```
