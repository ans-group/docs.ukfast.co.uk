# Blocking user-agents using htaccess (Apache)

Many malicious scripts and vulnerability scanners will have their own user-agent, a filed that is passed to the web server to help the web server send the website to the user properly. We can use this information to block known bad user agents to certain areas of our site, or site-wide.

To implement this, follow the below instructions for an Apache-based web server.


If you don't already have a .htaccess file in the directory path you'd like to protect, you can create one with the following commands.

`touch .htaccess`
`chmod 644 .htaccess`

If you do already have a .htaccess file, simple prepend the following to the top of your file instead of creating a new file.


Block a singular user agent:
```
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP_USER_AGENT} ^USERAGENT [NC]
  RewriteRule .* - [F,L]
</IfModule>
```
We can use the following to block multiple user agents, separating each with a `|` character, shown below.

```
<IfModule mod_rewrite.c>
  RewriteEngine On
  RewriteCond %{HTTP_USER_AGENT} ^(USERAGNT1|USERAGENT2) [NC]
  RewriteRule .* - [F,L]
</IfModule>
```

```eval_rst
.. meta::
     :title: Blocking User Agents| ANS Documentation
     :description: Useful threat remediation and prevention tips
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, UKFast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, HIDS, intrusion detection, set up
