
## Shellshock attack detected

*What is a Shellshock attack?*


A very common attack vector is a shellshock attack. Attacking the BASH (Bourne Again Shell) service on your server, this form of attack could allow an attacker to run arbitrary code on your server. This attack tries to get the target service to interpret the input as a BASH command which is then ran as if the command was input into a BASH shell. The BASH shell allows us to command and manage our server. Though here we can do things like creating users, set passwords, and control the operating system kernel. SSH (Secure Shell)works similar to a bash shell.

A common target for these types of attacks is a webserver service. An attacker will try to input BASH commands in a web request to try and get the webserver to interpret the URL as a bash command, and then run that in a bash style shell. This is one way that an attacker can get their malicious code to run on your server.

Let's look at the below example web server log.

"GET / HTTP/1.1" 200 3684 "() { _; OpenVAS; } >_[$($())] {  echo Content-Type: text/plain; echo; echo; PATH/usr/bin:/usr/local/bin:/bin; export PATH; id; }" "-"

Here we can see a shell attack, firstly, we can see that the server responded with a 200 code (successful), this means that the web server accepted this input. This does not necessarily mean that the attack was successful, but that the webserver has seen this as a valid web request and tried to find that page/function to the server to the user.

We can also see that the user agent on this occasion was OpenVAS, which is an Open Source vulnerability scanner. From this, we can determine that a vulnerability scanner was trying to see if this server was susceptible to a shell shock attack.

We can also see that the payload attack was trying to input BASH commands via the web service, we can see that this particular attack was trying to access the /bin and similar directories.

*How can I remediation this attack?*


We can prevent these attacks by ensuring that our web service and BASH is updated to the latest version with the latest security patches to allow the service to recognize the malicious input and drop it before any malicious code can run.

This rule also implements Dynamic Protection IP blocking, meaning that the attacking IP address will be blocked from accessing any content hosted on the server.


## Brute Force Attacks

*What is a brute force attack?*


One of the most common forms of attack is a brute force attack. As its name suggests, this attack is a relentless attempt to gain access to a system by constantly trying user name and password combinations to guess the correct credentials.

A simple brute force attack will try many commonly used usernames and password combinations. For example, the user name admin or administrator coupled with passwords like password, admin or change.

We also see more sophisticated brute force attacks that can detect what service they are trying to gain access to, and then try common user name and password combinations for that service, or even try the default credentials for that service. For example, an SSH or PHPMyAdmin Brute Force attack will usually try the username root, as this the most common user name used by default. Another example could be the administrator for Windows RDP

*How can I prevent a brute force attack?*


A successful brute force attack can easily be avoided by ensuring a strong user name and password combination is used. For more information on this, please consider reading our guide on how to set secure usernames and passwords here.

One of the best ways to mitigate these attacks is to remove the attacker's access to affected services completely. We can do this by implementing restriction rules to only allow safe, trusted IP addresses to access certain services and ports. By restricting access to SSH, for example, we can ensure that only trusted locations/IP addresses can access SSH and run commands on our server(s). For more information and a step by step guide on creating firewall rules, please follow our documentation here.

## Multiple viruses detected - Possible outbreak.


*What does this rule mean?*


Triggered when more than 8 virus detection events occur during a 360 second period, this rule could indicate that a malware/virus outbreak has occurred. This can occur when a particularly resistant piece of malware has managed to make its way onto your server, and is either replicating itself or is allowing a flood of viruses to be installed onto the system.

This rule will trigger even if your virus/malware scanner has successfully removed the infection(s). To check this out, you can view your alerting history for virus detection events, view your virus malware scanners logs, or contact UKFast support for assistance.

*How can I remediate this.*


If the viruses/malware was not removed by your scanner, you need to jump into action and remove as many infections items as possible. Please refer to this page for more information on how to do this, or contact UKFast support for assistance.

If the viruses/malware has been removed by your scanner, its recommended to immediately run another virus/malware scan to try and detect any missed infections. Then, consult with your developers and UKFast support to secure your server in the future.

```eval_rst
   .. title: Common Attacks
   .. meta::
      :title: Common Attacks | UKFast Documentation
      :description: Our Threat Monitoring ruleset explained
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```

