# Microsoft Security Essentials

##  Microsoft Security Essentials - Virus detected, but unable to remove.


###  What does this rule mean?


Triggered when Microsoft Security Essentials was unable to remove a virus/malware, this rule should be acted upon quickly. This indicated that a virus/malware was detected, but for some reason was not successfully removed. This could be due to the virus preventing the anti-virus application from removing it. Alternatively, and more commonly, the anti-malware program may not have the right permissions to remove the malware.

As a side note, we do commonly see Microsoft SE trigger this rule when it did actually remove the malware successfully. We recommend always double checking manually and taking any action as needed.

Many attackers follow an attack with malware by installing a trojan, backdoor or, rootkit or RAT on your server. This is high on an attackers priority list. Should they be discovered, and the exploits patched, the installed backdoor could allow the attacker to regain access to your server, potentially bypassing authentication and security auditing techniques.

###  What triggers this rule?


One of the most common triggers for this rule is unwanted software that is installed along with third-party applications, ranging from third party Tool Bars to viruses like the infamous PCOptimiserPro Trojan. This rule can also be triggered by legitimate software. This can happen when Windows doesnt recognise an application or the software acts in a similar way to a virus (such as installing updates by connecting to an external IP in an obscure way.

Additionally, malware may have infected the system from other sources, such as through a malicious email or suspicious file downloaded by a user or system administrator. After the initial malware event has been dealt with, the Threat Monitoring team is on hand to provide support when investigating further into the origins of malware.

###  What action do I need to take?

As a first responder, you should log into the server in question to determine whether the file in question was deleted by the anti-virus software. If it was successfully removed, we recommend manually running a system scan to check for any remnants of the malware. Should the malware be present on the system still, it should be removed, either through the anti-virus programs quarantine features or manually? Once this has been done another system scan should be run. 


##  Multiple Microsoft Security Essentials AV warnings detected.

###  What does this rule mean?


Potentially indicating an outbreak, this rule is triggered when multiple anti-virus warning messages are triggered. This could mean that multiple instances of malware have been discovered, and further action may be needed. Its common to see other rules trigger in addition to this, that may give further understanding on the nature of the malware. Nevertheless, we always recommend manually checking your anti-viruss logs and status for information, and act accordingly.

Many attackers follow an attack with malware. Such as installing a trojan, backdoor or, rootkit or RAT on your server is high on an attackers priority list. Should they be discovered, and the exploits patched, this malware could allow the attacker to regain access to your server, potentially bypassing authentication and auditing techniques.

Outbreaks are common with the more difficult malware. Theyll often replicate themselves, creating different signatures and changing their code in the progress in an attempt to become undetectable. This is called polymorphic malware and its incredibly difficult to discover and remove.

###  What triggers this rule?


One of the most common triggers for this rule is unwanted software that is installed along with third-party applications, ranging Tool Bars to viruses like the infamous PCOptimiserPro Trojan. This rule can also be triggered by legitimate software. This can happen when Windows doesnt recognise an application or the software acts in a similar way to a virus (such as installing updates by connecting to an external IP in an obscure way.

Additionally, malware may have infected the system from other sources, like succeeding an attack, through a malicious email or suspicious file. After the initial malware event has been dealt with, the Threat Monitoring team is on hand to provide support when investigating further into the origins of malware.

###  What action do I need to take?


As a first responder, you should log into the server in question to determine whether the file in question was deleted by the anti-virus software. If it was successfully removed, we recommend manually running a system scan to check for any remnants of the malware. Should the malware be present on the system still, it should be removed, either through the anti-virus programs quarantine features or manually? Once this has been done another system scan should be run. 

# McAfee Anti Virus

##  McAfee Windows AV - Virus detected and not removed.

###  What does this rule mean?


Triggered when McAfee Windows AV was unable to remove a virus, this rule should be acted upon quickly. This indicated that a virus was detected, but for some reason was not successfully removed. This could be due to the virus preventing the anti-virus application from removing it. Alternatively, and more commonly, the anti-malware program may not have the right permissions to remove the malware.

As a side note, we regularly see McAfee Windows Anti-Virus trigger this rule when it did actually remove the malware successfully. We recommend always double checking manually and taking any action as needed.

Many attackers follow an attack with malware. Installing a trojan, backdoor or, rootkit or RAT on your server is high on an attackers priority list. Should they be discovered, and the exploits patched, this malware could allow the attacker to regain access to your server, potentially bypassing authentication and auditing techniques.

### What triggers this rule?


One of the most common triggers for this rule is unwanted software that is installed along with third-party applications, ranging from Tool Bars to viruses like the infamous PCOptimiserPro Trojan. This rule can also be triggered by legitimate software. This can happen when Windows doesnt recognise an application or the software acts in a similar way to a virus (such as installing updates by connecting to an external IP in an obscure way.

Additionally, malware may have infected the system from other sources, like succeeding an attack, through a malicious email or suspicious file. After the initial malware event has been dealt with, the Threat Monitoring team is on hand to provide support when investigating further into the origins of malware.

### What action do I need to take?


As a first responder, you should log into the server in question to determine whether the file in question was deleted by the anti-virus software. If it was successfully removed, we recommend manually running a system scan to check for any remnants of the malware. Should the malware be present on the system still, it should be removed, either through the anti-virus programs quarantine features or manually? Once this has been done another system scan should be run. 

## ClamAV


### ClamAV Virus detected multiple times

### What does this rule mean?


Potentially indicating an outbreak, this rule is triggered when multiple anti-virus warning messages are triggered. This could mean that multiple malware has been discovered, and further action may be needed. Its common to see other rules trigger in addition to this that may elaborate on the nature of the malware. Nevertheless, we always recommend manually checking your anti-viruss logs and status for information, and acting accordingly.

Many attackers follow an attack with malware. Installing a trojan, backdoor or, rootkit or RAT on your server is high on an attackers priority list. Should they be discovered, and the exploits patched, this malware could allow the attacker to regain access to your server, potentially bypassing authentication and auditing techniques.

Outbreaks are common with the more difficult malware. Theyll often replicate themselves, creating different signatures and changing their code in the progress in an attempt to become undetectable. This is called polymorphic malware and its incredibly difficult to discover and remove.

### What triggers this rule?


One of the most common triggers for this rule is unwanted software that is installed along with third-party applications, such as Tool Bars to viruses like the infamous PCOptimiserPro Trojan. This rule can also trigger when legitimate software is triggered. This can happen when the operating system doesnt recognise an application.

Additionally, malware may have infected the system from other sources, like succeeding an attack, through a malicious email or suspicious file. After the initial malware event has been dealt with, the Threat Monitoring team is on hand to provide support when investigating further into the origins of malware.

### What action do I need to take?


As a first responder, you should log into the server in question to determine whether the file in question was deleted by the anti-virus software. If it was successfully removed, we recommend manually running a system scan to check for any remnants of the malware. Should the malware be present on the system still, it should be removed, either through the anti-virus programs quarantine features or manually? Once this has been done another system scan should be run. 

For good measure, we also recommend running a fresh Clam AV scan.

First, you have to update the virus definitions with:

    sudo freshclam

Then you can scan for viruses.

    clamscan OPTIONS File/Folder

If necessary start with root permissions: sudo clamscan.

Examples:

To check all files on the computer, displaying the name of each file:

    clamscan -r /

To check all files on the computer, but only display infected files and ring a bell when found:

    clamscan -r --bell -i /

To scan all files on the computer but only display infected files when found and have this run in the background:

    clamscan -r -i / &

Note - Display background processs status by running the jobs command.

To check files in the all users home directories:

    clamscan -r /home

To check files in the USER home directory and move infected files to another folder:

    clamscan -r --move/home/USER/VIRUS /home/USER

To check files in the USER home directory and remove infected files (WARNING: Files are gone.):

    clamscan -r --remove /home/USER

To see more options:

    clamscan --help

Source: https://askubuntu.com/questions/250290/how-do-i-scan-for-viruses-with-clamav


## CLamD Error

### What does this mean?


As an informational rule, this will trigger when the ClamAV service hits an error. Pending further investigation, this error could mean that the ClamAV watchdog/service has crashed or that a scan has failed before it could complete.

Unfortunately, ClamAV does not pass much information as the root cause of the error in its log file to Threat Monitoring. In response to this rule, a quick investigation into the cause of the issue is recommended and any remediation to pick the service up again would be advisable.

### How can I fix this?


We recommend looking directly at the raw ClamAV log, they may share some more verbose information that could indicate why the service hot an error state. 

The claim service can be restarted easily with:


service clamd restart


or on a cpanel installation:


/scripts/restartsrv_clamd


For good measure, we also recommend running a fresh Clam AV scan.

First, you have to update the virus definitions with:

sudo freshclam
Then you can scan for viruses.

clamscan OPTIONS File/Folder 


If necessary start with root permissions: sudo clamscan.

Examples:

To check all files on the computer, displaying the name of each file:

clamscan -r /

To check all files on the computer, but only display infected files and ring a bell when found:

clamscan -r --bell -i /

To scan all files on the computer but only display infected files when found and have this run in the background:

clamscan -r -i / &

Note - Display background processs status by running the jobs command.

To check files in the all users home directories:

clamscan -r /home

To check files in the USER home directory and move infected files to another folder:

clamscan -r --move/home/USER/VIRUS /home/USER

To check files in the USER home directory and remove infected files (WARNING: Files are gone.):

clamscan -r --remove /home/USER

To see more options:

clamscan --help

Source: https://askubuntu.com/questions/250290/how-do-i-scan-for-viruses-with-clamav

#Auditd

## Audit: Replay attack dedtected

### What is a Replay Attack?


A replay attack is designed to purposely delay network traffic or to send it to the target again. This is usually done to confuse a target program, or to fool it into sending the attacker sensitive information. 

For example, Alice is on public WiFi and is logging into the electricity company to pay her bill. Eve is an attacker listening to her traffic. Alice logs in and receives an authentication token so that she does not have to log in again for a few hours. Eve captures that traffic and replays it to the electricity companies accounts page. On a poorly designed website, when Eve sends the authentication token, the server will think that Eve is Alice, and serve the account page. Now Eve can use this account and gain personal information such as names, addresses, and even credit card information. 

###  How can I prevent a replay attack?


* A lot of websites tend to use things like Session Identifiers which are used to change the information sent in some way, which prevents a third-party like Eve from being able to replay messages because they will not verify with the unique session identifier. 
* Other sites use a one-time password, which expires after they are used. This means that anything sent using that one-time password after the first time will be rejected by the server. 
* Other websites use Number used Once (Nonce) and Message Authentication Codes (MAC) which are verified against each other. This increases the security of the sessions because an attacker replaying a session ID cannot forge the nonce or MAC.


#SSH

## OpenSSH challenge-response exploit.

### What Is OpenSSH?


Open SSH is a tool on some Unix-Like servers to allow server administration over a secure channel. The software runs on the server and handles the new requests, creation and deletion of secure SSH tunnels. 

OpenSSH encrypts traffic sent over the SSH tunnel, which keeps keystrokes and commands secret as they travel across large networks, like the internet. This is negotiated when the connection is set-up and it depends on what is configured in the configuration files for the OpenSSH server software. This is the most common way to log into and administer Linux servers and is bundled with almost all Linux server distributions. 

### The OpenSSH Challenge-Response Exploit


The OpenSSH Challenge-Response Exploit was mostly affecting BSD systems, however, can affect OpenSSH versions prior to OpenSSH 3.4. This exploit is able to give attackers an opportunity to execute shell code on the target system. 

An attacker can do this, by responding to the password challenge when logging into the server with a malicious request. If this is completed successfully, the program will be able to run some arbitrary code on the server. This works because it is a type of Buffer Overflow attack.  

### What can I do?


The recommended action for this is to update OpenSSH to Version 3.4 or better. If an update is not available it is also recommended to enable the OpenSSH privilege-separation feature. To do this:
* Open /etc/ssh/sshd_config in your favourite text editor.
* Uncomment the line `UsePrivilegeSeparation sandbox`
* Save the file
* Restart OpenSSH with `sudo service sshd restart`

## SSH CRC-32 Compensation attack.

### What Is OpenSSH?


Open SSH is a tool on some Unix-Like servers to allow server administration over a secure channel. The software runs on the server and handles the new requests, creation and deletion of secure SSH tunnels. 

OpenSSH encrypts traffic sent over the SSH tunnel, which keeps keystrokes and commands secret as they travel across large networks, like the Internet. This is negotiated when the connection is set-up and it depends on what is configured in the configuration files for the OpenSSH server software. This is the most common way to log into and administer Linux servers and is bundled with almost all Linux server distributions. 

### The SSH CRC-32 Compensation Attack


An SSH CRC-32 Compensation attack is an attack which affects the authentication of SSH1 Servers. This affects OpenSSH Version 2.3.0 and earlier. This is done by sending packets to the SSH Server with a 32-bit packet length. This causes problems in SSH1 because it uses a 16-bit variable to store this in. This means that when the variable gets assigned it gets assigned as a zero, or just very low in general. Due to this, attackers can write certain numerical values in arbitrary memory locations and can allow an attacker to gain root access to the SSH server if done right. 

### What can I do?


Do not support SSH Version 1. This can be done by following the steps below as the root user or using `sudo`:
* Open the following file in your favourite text editor `\etc\sshd_config`
* Uncomment the line `#Protocol 2,1`
* Change the line to `Protocol 2`
* Restart OpenSSH: `service sshd restart`

Done. This turns off support for SSH1 which is where the vulnerability lies. 


#MySQL

## MySQL fatal error.

### What is a MySQL Fatal Error?


A MySQL fatal error generally comes about through a malformed SQL search query, which will error out the SQL engine. This will mean that the changes the command was trying to do will not happen.

This can come about through poorly written SQL queries or the website makes a lot of connections to the database, however this will generally leave a site feature not working, and is caught in development and testing. More commonly, the malformed query may come from the user of a website by use of a controlled character, or an attempt at a deliberate SQL injection attack. 

Attackers may attempt to SQL Inject to discover data about how the underlying database works. If they can get this information they can attempt to trick it into giving actual information in your database, which would be classed as a data breach, especially if they can get a hold of sensitive or personal information.

### How to stop MySQL Fatal Errors?


Many different websites try various different techniques to try and mitigate this. Escaping Strings is by far the most popular. Making sure that any inputs on your website are properly escaped, so that the user cannot input any control characters into a search box or a user input field. Escaping strings is the act of encoding the control characters so that they do not register as these characters to database engines. Examples of control characters are semi-colons `;` and quotes `"` ``.

MySQL shutdown message.


### What is MySQL?


MySQL is an object-relational database with NoSQL type features, including adding data in and returning data in a JSON format. It is designed as the hybrid to allow full use of the SQL language and allow the versatility of processing data in the JSON data format. This means that the database can be used in a variety of applications and is a popular choice for many.

### What is a Database Shutdown Message?


When MySQL receives this message it will try to shut down the SQL databases. This means that MySQL will refuse any and all new connections to the database, and shall wait for all current clients to disconnect. Sometimes this can take a while, and sometimes this cannot. You must disconnect all clients before you can restart the database. 

MySQL can receive a shutdown message mainly from its own sever through its daemon. The daemon will not perform a graceful shutdown on its own, so this command is triggered. 

### What do can I do about this?


Usually, this command is intentionally issued to the MySQL server. If it is not, then you should check that you have nothing automated which is attempting to restart the service. If there is, disable it for the time being. If there is not, take a look at the recent logins with the Linux command `last`. This may give you more insight into who may have stopped the MySQL server.



#PostgreSQL

## PostgreSQL Database shutdown message.

### What is PostgreSQL?


PostgreSQL is a relational database which can be queried using the SQL language with extended features, and more secure design. It is designed to conform to the majority of the SQL:2011 standard. This is designed as a standard replacement to other SQL based databases. 
This is not always a drop-in replacement for other databases such as MySQL, because of the slight variations of the syntax PostgreSQL implements. 

### What is Database Shutdown?


When PostgreSQL Postmaster is told to shut down the SQL databases. This means that PostgreSQL will refuse any and all new connections to the database, and shall wait for all current clients to disconnect. Sometimes this can take a while, and sometimes this cannot. You must disconnect all clients before you can restart the database. 

PostgreSQL can receive a shutdown message mainly from its own server through its daemon. The daemon will not perform a graceful shutdown on its own, so this command is triggered. 

### What do can I do about this?


Checking that no automated scripts try to restart the PostgreSQL service is paramount to this. If you are sure that nothing is trying to shut down the service, then checking the system logs to work out what ran the command to shut down the PostgreSQL service is recommended. 

#MS Defender

## Windows Defender detected potentially unwanted software.

### What does this rule mean?


Defending your server from viruses and malware, this rule triggers when Windows Defender (Microsofts Anti Virus and Malware Solution) detects a suspicious PUP (Potentially Unwanted Program) program. As stated, this is flagged as a potentially unwanted program or software.

Many attackers follow an attack with malware. Installing a trojan, backdoor or, rootkit or RAT on your server is high on an attackers priority list. Should they be discovered, and the exploits patched, this malware could allow the attacker to regain access to your server, potentially bypassing authentication and auditing techniques.

### What triggers this rule?


One of the most common triggers for this rule is unwanted software that is installed along with third-party applications, ranging Tool Bars to viruses like the infamous PCOptimiserPro Trojan. This rule can also trigger when legitimate software is triggered. This can happen when Windows doesnt recognise an application.

### What action do I need to take?


As a first responder, you should log into the server in question to determine whether the PUP (Potentially Unwanted Program) was deleted by the anti-virus software. If the action was taken, we recommend manually running another system scan to check for any remnants of the malware. Should the malware be present on the system still, it should be removed, either through the anti-virus program or manually? Then, a manual anti-virus scan should be run. 


#Common Attacks

## Stack overflow

### What is a Stack Overflow attack?


Similar to a buffer overflow attack, the stack overflow attack is a common attack on older systems, software and processes. This attack takes advantage of the way memory data blocks and stacks are allocated to system processes. A stack overflow attack occurs when a system process tries to write data to a memory block or stack when it is already full. This causes the data to be written to a memory address adjacent to the original destination stack. This occurs when a program does not sufficiently manage its memory allocation, does not sufficiently implement bounds checking flags and discard data when too much is sent to a memory stack.

Memory blocks are used to allocate a specific place in Memory (RAM) for an application to store information. During this process, the application will ask the operating system for memory resources, the operating system will then create a selection of memory (block) for that information to be stored. This is so the application/operating system can easily refer to that information when needed and to separate information from other applications.


To understand this further, we can use the following simplified example. Lets say you have a container that can hold a maximum of 8 cubes. If you then try to put 9 cubes in that container, the last cube is obviously not going to fit, but, you need to put that remaining cube somewhere, so you need to overflow into the next container and place the remaining cube next container along. This container was not meant to hold this cube but due to the overflow, we have now unexpectedly added data to that container.

Attackers can utilize this to their advantage to get the computer to run malicious code. An attacker can send over sided payloads to a vulnerable application in an attempt to get it to write code to other memory blocks (containers). The payload can be specially crafted so that the overflowed data can be read by other applications, ran and then executed to allow the attacker access to the system.

### How can I remediate a stack overflow vulnerability?


As a stack overflow is a low-level attack, happening at the memory level, its difficult to remediate or prevent. Its important that software developers implement proper memory block bounds checking to check of the variable its about to write to has enough space to hold the desired payload. 

As a system administrator, the best course of action would be to ensure that the latest software versions are used where possible and ensuring that any custom made software is created properly and tested vigorously.

## Heap overflow

### What is a Heap Overflow attack?


Similar to a buffer overflow attack, the heap overflow attack is a common attack on older systems, software and processes. This attack takes advantage of the way memory data blocks and heaps are allocated to system processes. A heap overflow attack occurs when a system process tries to write data to a memory block or heap when it is already full. This causes the data to be written to a memory address adjacent to the original destination heap. This occurs when a program does not sufficiently manage its memory allocation, does not sufficiently implement bounds checking flags and discard data when too much is sent to a memory heap.

Memory blocks are used to allocate a specific place in Memory (RAM) for an application to store information. During this process, the application will ask the operating system for memory resources, the operating system will then create a selection of memory (block) for that information to be stored. This is so the application/operating system can easily refer to that information when needed and to separate information from other applications.


To understand this further, we can use the following simplified example. Lets say you have a container that can hold a maximum of 8 cubes. If you then try to put 9 cubes in that container, the last cube is obviously not going to fit, but, you need to put that remaining cube somewhere, so you need to overflow into the next container and place the remaining cube next container along. This container was not meant to hold this cube but due to the overflow, we have now unexpectedly added data to that container.

Attackers can utilize this to their advantage to get the computer to run malicious code. An attacker can send over sided payloads to a vulnerable application in an attempt to get it to write code to other memory blocks (containers). The payload can be specially crafted so that the overflowed data can be read by other applications, ran and then executed to allow the attacker access to the system.

### How can I remediate a heap overflow vulnerability?


As a heap overflow is a low-level attack, happening at the memory level, is difficult to remediate or prevent after the fact. Its important that software developers implement proper memory block bounds checking to check of the variable its about to write to has enough space to hold the desired payload. 

As a system administrator, the best course of action would be to ensure that the latest software versions are used where possible and ensuring that any custom made software is created properly and tested vigorously.

## Buffer Overflow Attck

### What is a Buffer Overflow attack?


The buffer overflow attack is a common attack on older systems, software and processes. This attack takes advantage of the way memory data blocks and buffers are allocated to system processes. A buffer overflow attack occurs when a system process tries to write data to a memory block or buffer when it is already full. This causes the data to be written to a memory address adjacent to the original destination buffer. This occurs when a program does not sufficiently manage its memory allocation, does not sufficiently implement bounds checking flags and discard data when too much is sent to a memory buffer.

Memory blocks are used to allocate a specific place in Memory (RAM) for an application to store information. During this process, the application will ask the operating system for memory resources, the operating system will then create a selection of memory (block) for that information to be stored. This is so the application/operating system can easily refer to that information when needed and to separate information from other applications.

To understand this further, we can use the following simplified example. Lets say you have a container that can hold a maximum of 8 cubes. If you then try to put 9 cubes in that container, the last cube is obviously not going to fit, but, you need to put that remaining cube somewhere, so you need to overflow into the next container and place the remaining cube next container along. This container was not meant to hold this cube but due to the overflow, we have now unexpectedly added data to that container.

Attackers can utilize this to their advantage to get the computer to run malicious code. An attacker can send oversized payloads to a vulnerable application in an attempt to get it to write code to other memory blocks (containers). The payload can be specially crafted so that the overflowed data can be read by other applications, ran and then executed to allow the attacker access to the system.

### How can I remediate a buffer overflow vulnerability?


As a buffer overflow is a low-level attack, happening at the memory level, its difficult to remediate or prevent after the fact. Its important that software developers implement proper memory block bounds checking to check of the variable its about to write to has enough space to hold the desired payload. 

As a system administrator, the best course of action would be to ensure that the latest software versions are used where possible and ensuring that any custom made software is created properly and tested vigorously.

## Shellshock attack detected

### What is a Shellshock attack?


A very common attack vector is a shellshock attack. Attacking the BASH (Bourne Again Shell) service on your server, this form of attack could allow an attacker to run arbitrary code on your server. This attack tries to get the target service to interpret input as a BASH command which is then ran as if the command was input into a BASH shell. The BASH shell allows us to command and manage our server. Though here we can do things like creating users, set passwords, and control the operatings system kernel. SSH (Secure Shell)works similar to a bash shell.

A common target for these types of attacks is a web server service. An attacker will try to input BASH commands in a web request to try and get the web server to interpret the URL as a bash command, and then run that in a bash style shell. This is one way that an attacker can get their own malicious code to run on your server.

Lets look at the below example web server log.

"GET / HTTP/1.1" 200 3684 "() { _; OpenVAS; } >_[$($())] {  echo Content-Type: text/plain; echo; echo; PATH/usr/bin:/usr/local/bin:/bin; export PATH; id; }" "-"

Here we can see a shell attack, firstly, we can see that the server responded with a 200 code (successful), this means that the web server accepted this input. This does not necessarily mean that the attack was successful, but that the web server has seen this as a valid web request and tried to find that page/function to the server to the user.

We can also see that the user agent on this occasion was OpenVAS, which is an Open Source vulnerability scanner. From this, we can determine that a vulnerability scanner was trying to see if this server was susceptible to a shell shock attack.

We can also see that the payload attack was trying to input BASH commands via the web service, we can see that this particular attack was trying to access the /bin and similar directories.

### How can I remediation this attack?


We can prevent these attacks by ensuring that our web service and BASH is updated to the latest version with the latest security patches to allow the service to recognize the malicious input and drop it before any malicious code is able to run.

This rule also implements Dynamic Protection IP blocking, meaning that the attacking IP address will be blocked from accessing any content hosted on the server.


## Brute Force Attacks

### What is a brute force attack?


One of the most common forms of attack is a brute force attack. As its name suggests, this attack is a relentless attempt to gain access to a system by constantly trying user name and password combinations in an effort to guess the correct credentials.

A simple brute force attack will try many commonly used usernames and password combinations. For example, the user name admin or administrator coupled with passwords like password, admin or changeme.

We also see more sophisticated brute force attacks that have the ability to detect what service they are trying to gain access to, and then try common user name and password combinations for that service, or even try the default credentials for that service. For example, an SSH or PHPMyAdmin Brute Force attack will usually try the username root, as this the most common user name used by default. Another example could be administrator for Windows RDP 

### How can I prevent a brute force attack?


A successful brute force attack can easily be avoided by ensuring a strong user name and password combination is used. For more information on this, please consider reading our guide on how to set secure usernames and passwords here.

One of the best ways to mitigate these attacks is to remove the attackers access to affected services completely. We can do this by implementing restriction rules to only allow safe, trusted IP addresses to access certain services and ports. By restricting access to SSH for example, we can ensure that only trusted locations/IP addresses can access SSH and run commands on our server(s). For more information and a step by step guide on creating firewall rules, please follow our documentation here.


## Null user changed some information

### What does this mean?


To understand this rule, its best if we first break down what is meant by null. As you probably know, null is the name given when a value is empty or not present. For example, if we have a variable that is called My_name but we have not saved and data into this variable, this variable will have a value of null, or nothing. 

Building on this, when information is changed on your server, the operating system will usually track what user or what process changed that information, for tracking and management purposed. On this occasion, the operating system was unable to determine why or what changed this information, this could be potentially malicious. 

A common objective for an attacker is to remain anonymous as possible, for as long as possible, so they can do as much damage as they can. Preventing the Operating System from tracking what user or process is making changes to specific information can help the attacker to remain anonymous.

This anomalous activity can help us identify that some unexpected activity may be in progress.

lets not forget however that is it entirely possible that a program/service may have entered an error state or not correctly changed information in the proper way, not telling the operating system that I changed some information and triggering this alert as a false positive.

### What do I need to do if I receive this alert?


If you receive this alert, we recommend being extra vigilant and looking out for any other alerts that may be triggered as a result of a potential attackers activity. Your MyUKFast dashboard is a great place to keep track of events on your server. Additionally, UKFast support is always on hand to provide assistance where needed.

Multiple authentication failures from the same IP address followed by a success.


### #What does this rule mean?


This is an all round rule for alerting on multiple failed authentication attempts, followed by a successful login. This is triggered when a user tried to log in multiple times before succeeding. This can indicate that an attacker accessed your server through a brute force attack. Alternatively, this could indicate that a service/process on your solution was unable to authenticate onto this server for a small period of time. It is also possible that a genuine user has forgotten their password, and has tried many times to authenticate, then remembered their password and logged in.

Its always best to double check the user account in question and take the appropriate measures to check that this was a genuine login. If you are unsure about this login, one of the quickest ways to take preventative action is to disable the added user account. For more information on this, please see the documentation here.

Additionally, to minimize these alerts and secure your server from this type of brute force attack, its recommended to lock down access to these services. SSHd, for example, can be locked down to certain IP addresses at a firewall level. This means that only predefined IP addresses will be able to access the SSH port, securing access to this service. A VPN could also be used. More information on this can be found here.

Its best practice to ensure you have a strong password set for all these services. Passwords longer than 8 characters that contain numbers, wildcards and MixEd CaSe letters are very difficult to brute force. You can use a service like AuditD to enforce password strength policies on your server. You can contact UKFast Support for assistance on this.


## Network scan from same source IP.

### What is a network scan?


Often a preliminary action to an attack, a network scan can be used to find potential vulnerabilities in your configuration, operating system and services running on your server. With information about potential exploits that can be utilized, an attacker can then run a more targeted attempt to exploit a vulnerability in your system to gain access, steal data or to cause damage.

Looking more specifically at a Network Scan, these scans tend to try and detect how your network is set up and determined the best attack vectors based on your setup. These attacks could detect open ports for example, or detect what services are listening on your server. This information will allow them to establish what functionality it has and therefore what will be trying to connect to it. As a rough example, if the attacker detects that port 53 is listening, it knows that that a DNS service is running, and can tailor attacks accordingly.

### How can network scans be prevented


Unwanted network scans can be an annoyance and potentially dangerous, but due to the way networks are designed, some infrastructure needs to be visible to the Internet, and therefore susceptible to scans. One of the best ways to prevent these scans is to recognize when a scan is in progress and then block the attacking scanner. Threat Monitoring Dynamic Protection takes care of this automatically and will block scanning IPs.

Additionally, its important to ensure that your network is set up properly with the right security precautions in place to minimize the number of attack vectors that a network scan may find. Regular patching and updating will ensure that the amount of vulnerabilities that are publicly visible are non existent and therefore cannot be exploited.

## System user successfully logged to the system.

### What does this rule mean?


A user account that is reserved for a system process has successfully logged onto the server. This could indicate that a system account with a common user name (like Apache, or MySQL) has been hacked. Attackers will use automated scripts to find a vulnerable server on the Internet. These scripts will try common usernames and passwords to try and gain unauthorized access to a server and take control of it. Programs/services that run on your server all need a user name to run as this helps the operating system to keep track of whats doing what.

The user name in question will depend on the program/service that has been attacked. This will most likely be services like Apache, MySQL, MongoDB, Nginx. You can look at your raw logs for more detail on this event, as well as the user name that accessed in the attack. Alternatively, you can ask us to take a look for you by raising a support ticket or calling UKFast support. 

### How can I fix this?


All system user accounts should have remote login disabled, meaning that attackers wont be able to access this account from the internet, making it impossible to attack. For more information on this, visit this page for information on how to disable login for certain accounts.


## Attacks followed by the addition of a user.

### What does this mean?

One of our most serious attacks; this is triggered whenever an attack is followed by the addition of a user account on your server. Its common that when an attack has succeeded, the attacker will add an account for themselves on the system in an attempt to leave a way back into the system should the original account be disabled. If this goes unnoticed, your server could be compromised again, even after removing the original vulnerability and compromised account.


Remediation needs to be immediate to tackle this attack. Firstly, the original attack should be dealt with as appropriate. Following that, any user accounts made during the attack or during the patch phrase should be removed or disabled, to minimize the risk of the attacker regaining access to the system.

To prevent this from happening again, you can implement rules that only allow an administrative user to add user accounts. This would prevent accounts from being added even if one of your current accounts is compromised. This is enabled by default. If your administrative user is compromised, then you would need to look at another defensive technique, such as restoring from backups prior to the initial attack

For more information on how to disable user accounts, please take a look at our documentation on this topic here.

## Multiple viruses detected - Possible outbreak.


### What does this rule mean?


Triggered when more than 8 virus detection events occur during a 360 second period, this rule could indicate that a malware/virus outbreak has occurred. This can occur when a particularly resistant piece of malware has managed to make its way onto your server, and is either replicating itself or is allowing a flood of viruses to be installed onto the system.

This rule will trigger even if your virus/malware scanner has successfully removed the infection(s). To check this out, you can view your alerting history for virus detection events, view your virus malware scanners logs, or contact UKFast support for assistance.

### How can I remediate this.


If the viruses/malware was not removed by your scanner, you need to jump into action and remove as many infections items as possible. Please refer to this page for more information on how to do this, or contact UKFast support for assistance.

If the viruses/malware has been removed by your scanner, its recommended to immediately run another virus/malware scan to try and detect any missed infections. Then, consult with your developers and UKFast support to secure your server in the future.

## Postfix

### Postfix Multiple misuse of SMTP service (bad sequence of commands).

Multiple Misuse of SMTP Service is a feature where some Postfix commands are being used in unsupported configurations and returns ```503 Bad Sequence of Commands```. This can be caused by servers sending multiple commands out at a time or messing up the ordering of the commands. 

This can relate to all mail servers, however, this page focuses on Postfix. This is a standard communication between mail servers which allows for communication of email servers of different types. Postfix is a more commonly used system which runs in Unix-like systems such as Linux, MacOS and FreeBSD.

### Does this mean I am being attacked?


This can happen for multiple reasons. It doesnt always mean that there is an attack. However, rarely, an attacker may try to break a mail server and may try to send packets out of order to see what they can break. Modern mail servers combat this by showing a 503, which is the error handler code to cancel the connection, but not crash the whole program. This is the most they are going to receive.  

### How can I fix this?


Monitoring is the best thing to do in this situation. Check the Postfix logs, to work out where the issue is. This is the best place to start as these commands can be oddly specific and sometimes fairly random. 
Client authentication is also a good place to look. Modern Mail systems use ```STARTTLS``` to serve emails. Older systems may use ```SSL TLS```. This is an older protocol which is incompatible with the newer ```STARTTLS```.  Making sure that the programs or the client connecting to it use the right authentication method is key to its success.



Review the logs to make sure that the issue is isolated. They can be found at:

/var/log/mail.log


This error is very rarely to do with your server configuration and is more likely a client misconfiguration. This can be identified and fixed so that a bad user experience can be avoided.

If an attacker is trying to break your mail server, blocking their IP address on your firewalls will stop them from being able to reach your mail server, so they will not be able to send the wrong commands. 


## Postfix Multiple attempts to send e-mail from black-listed IP address (blocked).


### What does this mean?


This rule is informing you that there have been multiple attempts at sending an email from an IP that is blacklisted, meaning the IP address is known to be involved in spam activities. Its not uncommon for a mail IP address to end up on the blacklist, especially on a shared server. This can be due to the volume of mail coming from that server or messages possessing spam-like characteristics. It can also be caused by email forwarders. 

This does not mean that you are being attacked. It is more likely because blacklists automatically add your mail servers IP address that is assigned via your ISP. An IP can also end up being on a blacklist due to a virus, malware or spam. Should you have a virus or malware on your computer and it is constantly pinging or attempting to communicate with other computers, it is likely that the admin of another computer will see this attack and block the IP address and report it. If spam email is sent or a mail server is run that is not properly configured and it allows spam to be sent then the IP address becomes blacklisted. 

### So, How do I fix this?


First, you should make sure that all devices on your network are not infected. After youve determined your network is clean and that no unauthorized traffic is going out, find where your IP address is blacklisted and remove it. 

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


**Note**: File /var/tmp/mail.send is not rotated automatically and it is not recommended to leave it for a long period of time as it could consume a server disk space. Delete and create a new file /var/tmp/mail.send after every check up.

5. Check /var/tmp/mail.send file. There should be lines starting with "X-Additional-Header" pointing to the domain folders where the scripts that sent the mail are located.
The directories, from which mail PHP scripts are run, can be seen using the following command:


grep X-Additional /var/tmp/mail.send | grep `cat /etc/psa/psa.conf | grep HTTPD_VHOSTS_D | sed -e s/HTTPD_VHOSTS_D// `


**Note**: If no output is shown from the command above, it means no mail was sent using the PHP mail function from the Plesk virtual hosts directory.

Usually, that means one of the mail accounts has been compromised. Check the login attempt count:


#zgrep -c sasl_methodLOGIN /usr/local/psa/var/log/maillog*
/usr/local/psa/var/log/maillog:221000
/usr/local/psa/var/log/maillog.processed:362327
/usr/local/psa/var/log/maillog.processed.1.gz:308956


If an unusually high number of login attempts is shown, it is very likely accounts were compromised. Try identifying these accounts in the following way:


zgrep saslmethodLOGIN /usr/local/psa/var/log/maillog | awk {print $9} | sort | uniq -c | sort -nr | head
891574 saslusernameadmin@example.com**


6. To stop spam from being sent, change passwords for the compromised accounts and restart the Postfix service.

#Syslog (Generic Events)

## Three failed attempts to run sudo

### What does this mean?


This rule tells you that there have been 3 incorrect password attempts on syslog within the space of a few minutes. This could be someone forgetting their passwords. Usually, this is an administrator or someone who has access to the system. 

This does not discount an attacker from triggering this rule. Some investigation should be done to make sure that this is a valid authorised user completing these actions. 

### What program/service does this rule relate to?


This relates to user management and permissions management. The `sudo` program allows users to act as root when performing actions that directly relate to the system. This allows the users to start and stop services, modify configuration files and access restricted parts of the file system. 

This program is also very locked-down to specific individuals. The program needs authorization to allow a user to use it. This is meant as an administration tool, to allow the root account login to be disabled.  

### How can I fix this?


Finding out which user triggered this alert would be useful. It should be listed on our alert to you. This would allow you to investigate to see what they have been doing. 

If the user is not meant to be able to use the `sudo` command then looking through their `.bash_histroy` files by looking in their home directory,  `/home/<user>` usually. This file lists all the commands the user has run on the system. If it is a system user that has tried to this, a ClamAV scan or a McAfee scan would be a good idea to make sure that a program is not a virus or malware. 


## SCSI RAID ARRAY ERROR, drive failed

### What does this mean?


This tells you that one or more of the drives in RAID array have failed, this is usually because the drive has been in operation for a long while so is suffering from general wear and tear. This needs to be looked at immediately.  

**NOTE**: This does not indicate an attack. This is caused by a disk physically failing in the server. 

### What does this rule relate to?


This can affect everything in your server. Anything which needs to access data on that disk will error out and fail. This is a serious issue. Mostly RAIDs are used to store data, so the operating system of the server is unlikely to be affected by a disk failure.

### How can I fix this?


Contact the providers of your server. Make sure your backups are as up to date as they can be, and work with them to get everything back up and running. Keeping an open dialogue with them, so that you are informed of any updates and developments would be good too.  

Other than that, there isnt much you can do. Getting the drive replaced, and your RAID array rebuilt is the only solution. If you are using RAID as a redundancy, not a backup, then there may not be a lot of downtimes as your RAID array will fail over. 

A good backup solution is also a must in these situations, as if the array does become completely corrupted, then your data is still kept safe, in a backup. Running daily backups is a recommended configuration. 

## Possible Disk failure. SCSI controller error.

### What does this mean?


This means that there is a failure on the hard drive or an error with the SCSI controller. This is usually caused by normal wear and tear of the server, and can often lead to data loss, if not monitored carefully. 

Linux and Windows Servers will do some monitoring of Hard Disks and some SCSI controllers. This will generally do this through the general system logs (syslog) via its own Health Checking systems. These alerts trigger when the drive is approaching unusability. This means that you will still have time to recover all data from usable sectors. 

This does not mean that an attack is taking place. This is a hardware alert which is generated to inform the user of hardware that is about to fail. 
 
### How can I fix this?


Replace hard drive will be necessary to preserve all the data. Migrating data from onto a new drive is the best way to not lose data. Please contact your technical team, or our support staff to help you with this. 

**NOTE**: If you are dealing with a RAID array, please seek the advice of our support staff or another experienced IT professional for the best way to replace disks in a RAID array. 


To find out more about the health of your hard drives on Linux run the command replacing the `<device_id>` with the device you wish to run it against, such as `sda` or `sdb`.


smartctl -a /dev/<device_id>


On Windows open PowerShell and type in:


* `wmic`
* `diskdrive get status`



This will return `Status OK` if the drive is all good, or an error message. This error message will indicate problems with your hard drive.

#ProFTPd

## proftpd FTP brute force (multiple failed logins).

### What does this rule tell me?


A brute force attack is one of the more common attacks used today. Its a generic term used when an attacker tries different username and password combinations. This kind of attack is most common on FTP and SSH servers. In this case, your FTP server may have experienced a brute force attack. 

A false-positive can sometimes fire if a user has forgotten their login details and is repeatedly failing to log in - Please bear this in mind. 

Brute Force attacks are usually based on dictionary attacks, where a list of common passwords is used. It can take a few minutes to try hundreds of password combinations. 

What program/service does this rule relate to?


FTP Server [File Transfer Protocol] 

### How can I fix this?


The easiest way to protect yourself from brute force attacks is to employ a strong password. A strong password may consist of 15 characters, upper-case, lower-case, symbols and numbers. 

Restrict access to your login URL. Your login page may be publicly facing, if so, you may want to restrict it to an internal IP address range. 

### Does this mean I am being attacked?

In this situation, there is a high chance that your server is being targeted by a brute force attack. If the numbers are relatively low, this may not be the case and it might be that someone has forgotten their login credentials and is trying to regain access.








