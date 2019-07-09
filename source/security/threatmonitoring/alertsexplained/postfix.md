```eval_rst
.. meta::
     :title: Postfix Rules Explained | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
```
## Postfix

### Postfix Multiple misuses of SMTP service (bad sequence of commands).

Multiple Misuse of SMTP Service is a feature where some Postfix commands are being used in unsupported configurations and return ```503 Bad Sequence of Commands```. This can be caused by servers sending multiple commands out at a time or messing up the ordering of the commands. 

This can relate to all mail servers, however, this page focuses on Postfix. This is a standard communication between mail servers which allows for communication of email servers of different types. Postfix is a more commonly used system which runs in Unix-like systems such as Linux, MacOS and FreeBSD.

### Does this mean I am being attacked?


This can happen for multiple reasons. It doesn't always mean that there is an attack. However, rarely, an attacker may try to break a mail server and may try to send packets out of order to see what they can break. Modern mail servers combat this by showing a 503, which is the error handler code to cancel the connection, but not crash the whole program. This is the most they are going to receive.  

### How can I fix this?


Monitoring is the best thing to do in this situation. Check the Postfix logs, to work out where the issue is. This is the best place to start as these commands can be oddly specific and sometimes fairly random. 
Client authentication is also a good place to look at. Modern Mail systems use ```STARTTLS``` to serve emails. Older systems may use ```SSL TLS```. This is an older protocol which is incompatible with the newer ```STARTTLS```.  Making sure that the programs or the client connecting to it use the right authentication method is key to its success.



Review the logs to make sure that the issue is isolated. They can be found at:

/var/log/mail.log


This error is very rarely to do with your server configuration and is more likely a client misconfiguration. This can be identified and fixed so that bad user experiences can be avoided.

If an attacker is trying to break your mail server, blocking their IP address on your firewalls will stop them from being able to reach your mail server, so they will not be able to send the wrong commands. 


## Postfix Multiple attempts to send e-mail from a black-listed IP address (blocked).


### What does this mean?


This rule is informing you that there have been multiple attempts at sending an email from an IP that is blacklisted, meaning the IP address is known to be involved in spam activities. It's not uncommon for a mail IP address to end up on the blacklist, especially on a shared server. This can be due to the volume of mail coming from that server or messages possessing spam-like characteristics. It can also be caused by email forwarders. 

This does not mean that you are being attacked. It is more likely because blacklists automatically add your mail servers IP address that is assigned via your ISP. An IP can also end up being on a blacklist due to a virus, malware or spam. Should you have a virus or malware on your computer and it is constantly pinging or attempting to communicate with other computers, it is likely that the admin of another computer will see this attack and block the IP address and report it. If spam email is sent or a mail server is run that is not properly configured and it allows spam to be sent then the IP address becomes blacklisted. 

### So, How do I fix this?


First, you should make sure that all devices on your network are not infected. After you've determined your network is clean and that no unauthorized traffic is going out, find where your IP address is blacklisted and remove it. 

To implement this, log into your server via SSH and follow the steps below

1. Create a /usr/sbin/sendmail.postfix-wrapper script with the following content:

#!/bin/sh
(echo X-Additional-Header: $PWD ;cat) | tee -a 
/var/tmp/mail.send|/usr/sbin/sendmail.postfix-bin "$@"


2. Create /var/tmp/mail.send log file and set a+rw permissions. Make the wrapper executable, rename the old sendmail.postfix file, and link it to the new wrapper:


touch /var/tmp/mail.send
chmod a+rw /var/tmp/mail.send
chmod a+x /usr/sbin/sendmail.postfix-wrapper
mv /usr/sbin/sendmail.postfix /usr/sbin/sendmail.postfix-bin
ln -s /usr/sbin/sendmail.postfix-wrapper /usr/sbin/sendmail.postfix


3. Wait for a while to collect data: 30 -60 min.

4. Rename sendmail.postfix-bin back to /usr/sbin/sendmail.postfix:


mv /usr/sbin/sendmail.postfix /root/backupsendmail.postfix
mv /usr/sbin/sendmail.postfix-bin /usr/sbin/sendmail.postfix


**Note**: File /var/tmp/mail.send is not rotated automatically and it is not recommended to leave it for a long period of time as it could consume a server disk space. Delete and create a new file /var/tmp/mail.send after every check-up.

5. Check /var/tmp/mail.send file. There should be lines starting with "X-Additional-Header" pointing to the domain folders where the scripts that sent the mail are located.
The directories, from which mail PHP scripts are run, can be seen using the following command:


grep X-Additional /var/tmp/mail.send | grep `cat /etc/psa/psa.conf | grep HTTPD_VHOSTS_D | sed -e s/HTTPD_VHOSTS_D// `


**Note**: If no output is shown from the command above, it means no mail was sent using the PHP mail function from the Plesk virtual hosts directory.

Usually, that means one of the mail accounts has been compromised. Check the login attempt count:

zgrep -c sasl_methodLOGIN /usr/local/psa/var/log/maillog*
/usr/local/psa/var/log/maillog:221000
/usr/local/psa/var/log/maillog.processed:362327
/usr/local/psa/var/log/maillog.processed.1.gz:308956


If an unusually high number of login attempts is shown, it is very likely accounts were compromised. Try identifying these accounts in the following way:


zgrep saslmethodLOGIN /usr/local/psa/var/log/maillog | awk {print $9} | sort | uniq -c | sort -nr | head
891574 saslusernameadmin@example.com**


6. To stop spam from being sent, change passwords for the compromised accounts and restart the Postfix service.
