# Disable remote login for accounts

Many services on your server will create their user on the system, this is normal behaviour. These services should also disable remote login for these accounts, only allow the server itself to access the accounts and removing the possibility for remote users to log in as these services. We can also utilise this functionality to secure our user accounts from external access. We can do this by editing the /etc/passwd file in a Linux system.

Feel free to follow the below steps to disable remote login for a user account.

Edit the file /etc/passwd with your preferred text editor.

In this file was can see all the user accounts on the server managed by PAM (Pluggable authentication module) Please note user accounts for services that have their user database will not show in here.

In this example, we can see that the root user is allowed to log in to a bash terminal.

`root:x:0:0:root:/root:/bin/bash`

We can also see that the `nails` user, used for McAfee AV, cannot log into a bash terminal.

`nails:x:1003:1004:McAfeeVSEForLinux Administrator:/home/nails:/sbin/nologin`

Let's use the above examples to edit the user `brad` shown below, preventing them from logging into a bash terminal.

Orginal line:

`brad:x:1001:1001::/home/brad:/bin/bash`

Modified line:

`brad:x:1001:1001::/home/brad:/sbin/nologin`

The user `brad` can no longer log in to the server remotely.

```eval_rst
.. meta::
     :title: Disabling remote login for accounts | ANS Documentation
     :description: Useful threat remediation and prevention tips
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
