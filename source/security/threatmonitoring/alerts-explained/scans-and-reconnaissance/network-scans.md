
## Network scan from same source IP.

*What is a network scan?*


Often a preliminary action to an attack, a network scan can be used to find potential vulnerabilities in your configuration, operating system and services running on your server. With information about potential exploits that can be utilized, an attacker can then run a more targeted attempt to exploit a vulnerability in your system to gain access, steal data or to cause damage.

Looking more specifically at a Network Scan, these scans tend to try and detect how your network is set up and determined the best attack vectors based on your setup. These attacks could detect open ports for example, or detect what services are listening on your server. This information will allow them to establish what functionality it has and therefore what will be trying to connect to it. As a rough example, if the attacker detects that port 53 is listening, it knows that a DNS service is running, and can tailor attacks accordingly.

```eval_rst
.. meta::
     :title: Network Scans | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan,