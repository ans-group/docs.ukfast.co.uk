# SSH (Secure Shell)

## OpenSSH challenge-response exploit.

*What Is OpenSSH?*


Open SSH is a tool on some Unix-like servers to allow server administration over a secure channel. The software runs on the server and handles the new requests, creation and deletion of secure SSH tunnels.

OpenSSH encrypts traffic sent over the SSH tunnel, which keeps keystrokes and commands secret as they travel across large networks, like the internet. This is negotiated when the connection is set-up and it depends on what is configured in the configuration files for the OpenSSH server software. This is the most common way to log into and administer Linux servers and is bundled with almost all Linux server distributions.

*What is the OpenSSH Challenge-Response exploit?*


The OpenSSH Challenge-Response Exploit was mostly affecting BSD systems, however, can affect OpenSSH versions prior to OpenSSH 3.4. This exploit is able to give attackers an opportunity to execute shellcode on the target system.

An attacker can do this, by responding to the password challenge when logging into the server with a malicious request. If this is completed successfully, the program will be able to run some arbitrary code on the server. This works because it is a type of Buffer Overflow attack.

*What can I do?*


The recommended action for this is to update OpenSSH to Version 3.4 or better. If an update is not available it is also recommended to enable the OpenSSH privilege-separation feature. To do this:
* Open /etc/ssh/sshd_config in your favourite text editor.
* Uncomment the line `UsePrivilegeSeparation sandbox`
* Save the file
* Restart OpenSSH with `sudo service sshd restart`

## SSH CRC-32 Compensation attack.

*What Is OpenSSH?*


Open SSH is a tool on some Unix-like servers to allow server administration over a secure channel. The software runs on the server and handles the new requests, creation and deletion of secure SSH tunnels.

OpenSSH encrypts traffic sent over the SSH tunnel, which keeps keystrokes and commands secret as they travel across large networks, like the Internet. This is negotiated when the connection is set-up and it depends on what is configured in the configuration files for the OpenSSH server software. This is the most common way to log into and administer Linux servers and is bundled with almost all Linux server distributions.

* What is the SSH CRC-32 Compensation attack?


An SSH CRC-32 Compensation attack is an attack which affects the authentication of SSH1 Servers. This affects OpenSSH Version 2.3.0 and earlier. This is done by sending packets to the SSH Server with a 32-bit packet length. This causes problems in SSH1 because it uses a 16-bit variable to store this in. This means that when the variable gets assigned it gets assigned as a zero, or just very low in general. Due to this, attackers can write certain numerical values in arbitrary memory locations and can allow an attacker to gain root access to the SSH server if done right.

*What can I do?*


Do not support SSH Version 1. This can be done by following the steps below as the root user or using `sudo`:
* Open the following file in your favourite text editor `\etc\sshd_config`
* Uncomment the line `#Protocol 2,1`
* Change the line to `Protocol 2`
* Restart OpenSSH: `service sshd restart`

Done. This turns off support for SSH1 which is where the vulnerability lies.

```eval_rst
.. meta::
     :title: SSH Rules Explained | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up

