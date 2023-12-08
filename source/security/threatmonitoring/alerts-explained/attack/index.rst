.. meta::
   :title: Common Attacks | ANS Documentation
   :description: Guidance on Threat Monitoring and Threat Response solutions from UKFast
   :keywords: security, threat, monitoring, response, alerts, blocking, hacking, ransomware, protection

=====================================
Common Attacks
=====================================

Many attacks to internet-facing servers are performed by robots. These scripts are created to scan the internet for servers that they can attack or exploit. A common example of this is RDP/SSH exploit bots.

These bots would search the internet for servers that have common RDP or SSH ports open, such a TCP 3389 or TCP 22. Once a server is found, they may try to brute force their way into that server using some common username and password combinations. More advanced bots may also try and exploit the service, taking advantage of a vulnerability to gain control of the system.

UKFast Threat Monitoring can detect common attacks and exploits to mission-critical services such as SSH and RDP. Coupled with Active Response, these attacks can be automatically blocked to ensure your server is protected.

.. toctree::
   :maxdepth: 1

   common-attacks