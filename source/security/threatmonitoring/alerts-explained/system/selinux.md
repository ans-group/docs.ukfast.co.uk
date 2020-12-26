# SELinux/Auditd

## Audit: Replay attack dedtected

*What is a Replay Attack?*


A replay attack is designed to purposely delay network traffic or to send it to the target again. This is usually done to confuse a target program, or to fool it into sending the attacker sensitive information.

For example, Alice is on public WiFi and is logging into the electricity company to pay her bill. Eve is an attacker listening to her traffic. Alice logs in and receives an authentication token so that she does not have to log in again for a few hours. Eve captures that traffic and replays it to the electricity companies accounts page. On a poorly designed website, when Eve sends the authentication token, the server will think that Eve is Alice, and serve the account page. Now Eve can use this account and gain personal information such as names, addresses, and even credit card information.

*How can I prevent a replay attack?*


* A lot of websites tend to use things like Session Identifiers which are used to change the information sent in some way, which prevents a third-party like Eve from being able to replay messages because they will not verify with the unique session identifier.
* Other sites use a one-time password, which expires after they are used. This means that anything sent using that one-time password after the first time will be rejected by the server.
* Other websites use Number used Once (Nonce) and Message Authentication Codes (MAC) which are verified against each other. This increases the security of the sessions because an attacker replaying a session ID cannot forge the nonce or MAC.

```eval_rst
.. meta::
     :title: SELinux Rules Explained | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
