# PostgreSQL

## PostgreSQL Database shutdown message.

*What is PostgreSQL?*


PostgreSQL is a relational database which can be queried using the SQL language with extended features, and more secure design. It is designed to conform to the majority of the SQL:2011 standard. This is designed as a standard replacement to other SQL based databases.

This is not always a drop-in replacement for other databases such as MySQL, because of the slight variations of the syntax PostgreSQL implements.

*What is Database Shutdown?*


When PostgreSQL Postmaster is told to shut down the SQL databases. This means that PostgreSQL will refuse any new connections to the database, and shall wait for all current clients to disconnect. Sometimes this can take a while, and sometimes this cannot. You must disconnect all clients before you can restart the database.

PostgreSQL can receive a shutdown message mainly from its server through its daemon. The daemon will not perform a graceful shutdown on its own, so this command is triggered.

*What do can I do about this?*


Checking that no automated scripts try to restart the PostgreSQL service is paramount to this. If you are sure that nothing is trying to shut down the service, then checking the system logs to work out what ran the command to shut down the PostgreSQL service is recommended.

```eval_rst
.. meta::
     :title: PostgreSQL rules Explained | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
