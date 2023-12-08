# MySQL

## MySQL fatal error.

*What is a MySQL Fatal Error?*


A MySQL fatal error generally comes about through a malformed SQL search query, which will error out the SQL engine. This will mean that the changes the command was trying to do will not happen.

This can come about through poorly written SQL queries or the website makes a lot of connections to the database, however, this will generally leave a site feature not working, and is caught in development and testing. More commonly, the malformed query may come from the user of a website by the use of a controlled character, or an attempt at a deliberate SQL injection attack.

Attackers may attempt to SQL Inject to discover data about how the underlying database works. If they can get this information they can attempt to trick it into giving actual information in your database, which would be classed as a data breach, especially if they can get a hold of sensitive or personal information.

*How do I stop MySQL Fatal Errors?*


Many different websites try various techniques to try and mitigate this. Escaping Strings is by far the most popular. Making sure that any inputs on your website are properly escaped, so that the user cannot input any control characters into a search box or a user input field. Escaping strings is the act of encoding the control characters so that they do not register as these characters to database engines. Examples of control characters are semi-colons `;` and quotes `"` ``.

## MySQL shutdown message.

*What is a Database Shutdown Message?*


When MySQL receives this message it will try to shut down the SQL databases. This means that MySQL will refuse any new connections to the database, and shall wait for all current clients to disconnect. Sometimes this can take a while, and sometimes this cannot. You must disconnect all clients before you can restart the database.

MySQL can receive a shutdown message mainly from its server through its daemon. The daemon will not perform a graceful shutdown on its own, so this command is triggered.

*What do can I do about this?*


Usually, this command is intentionally issued to the MySQL server. If it is not, then you should check that you have nothing automated which is attempting to restart the service. If there is, disable it for the time being. If there is not, take a look at the recent logins with the Linux command `last`. This may give you more insight into who may have stopped the MySQL server.

```eval_rst
   .. title:: MySQL Rules Explained
   .. meta::
      :title: MySQL Rules Explained | ANS Documentation
      :description: Our Threat Monitoring ruleset explained
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```
