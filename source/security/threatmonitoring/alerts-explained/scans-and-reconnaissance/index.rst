.. meta::
   :title: Scans and Reconnaissance| ANS Documentation
   :description: Guidance on Threat Monitoring and Threat Response solutions from UKFast
   :keywords: security, threat, monitoring, response, alerts, blocking, hacking, ransomware, protection

=====================================
Scans and Reconnaissance
=====================================

Before attacking, many targeted attacks and bots will perform a network scan on your server. This scan may check if common ports are open, what services are listening on those ports and the version of those services. With this information, an attacker or bot may be able to tailor their attacking strategy to that specific software version.

For example, if you were running a vulnerable version of Exim on a common mail port, then the attacker could launch an RCE attack (CVE-2019-15846) against your server.

Threat Monitoring can detect when a network scan or version gathering scan may be in progress, and take the needed actions to block the scan.

.. toctree::
   :maxdepth: 1

   network-scans