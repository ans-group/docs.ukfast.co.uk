# IP Based Allow listing

Services like SSH, FTP and SQL are frequently subject to a wide variety of attacks, from brute force attacks to software firewall bypasses and challenge-response exploits. We find that 70% of all Threat Monitoring alerts are caused by brute force attacks, so securing access to these services is critical to ensure your server is safe.

To prevent an attacker from accessing sensitive services like ssh or FTP, we can implement IP based restrictions on a firewall level. This will only allow connections to certain ports from predetermined, safe IP addresses, such as your office IP or developers.

Follow the steps below to implement this, in the example shown we implement IP based restrictions on SSH, which is port 2020 for UKFast servers. Please bear in mind that the steps for dedicated firewalls are different from shared firewalls. We have documented both below. Please ensure you're following the right guide for your type of firewall.

### Shared firewalls

1. Under the ‘Products and Services’ ‘Firewall’ section, select ‘Shared’
2. Select the Shared Firewall used for the affected server.
3. Navigate to the ‘Admin Port Config’ Tab.
4. Add the ports that you wish to secure to the incoming and outgoing interfaces, for example, SSH would be e 2020, FTP would be 21 etc
6. Press save changes to apply your configuration.
7. Navigate to the 'Admin Config' tab.
8. Add the Ip addresses that you'd like to allow access to previously specified ports.
9. Click save changes.
10. Click the 'Port config' tab.
11. Ensure that any ports that you wish to secure are not in this list. This will ensure that this port is not accessible from the entire internet.
12. Click save changes.



### Dedicated firewalls

1.    Under the ‘Products and Services’ ‘Firewall’ section, select ‘Dedicated`.
2.    Select the Dedicated Firewall used for the affected server.
3.    Navigate to the ‘IP Groups Tab.
4.    Press ‘New Non-UKFast Group’
5.    Give this IP group a relevant name.
6.    Give this IP group a description if needed.
7.    Add the IP to restrict access to in the IP address field, set the ‘IP Type’ to ‘Single IP’.
8.    Add the attacking IP address in the ‘IP Address’ field.
9.    Leave a note if required.
10.    You can add additional IP addresses  by pressing ‘Add Network Location’
11.    Press ‘Create Group’ To save this IP group.

12.    Navigate to the ‘Port Groups’ Section
13.    Press ‘New Port Group’
14.    Set the ‘Service’ to TCP or UDP as required, most services like SSH and FTP require TCP.
15.    Give this port group a name
16.    Give the port group a description if necessary
17.    Set ‘Port Type’ to ‘Port Number’
18.    Enter the port you wish to secure in both boxes.
19.    Enter a note for these ports if needed.
20.    Press ‘Create group’ to save this port group.


21.    Navigate to the ‘Access Lists’ Section
22.    Press ‘Add incoming Interface Rule’
23.    Set the ‘Action’ Field to 'Permit'
24.    Set the ‘Source’ Field to the IP Group you just created.
25.    Set the ‘Destination’ to the server you want to secure access to, Or select ‘All Servers’ to secure access from IP across your entire infrastructure.
26.    Set the ‘Ports’ Field to the TCP group you made earlier.
27. Click the create button.
28.    Add another similar ‘Incoming Interface Rule’, but change the action to 'Den' and set the source to 'anywhere', ensuring that the destination and ports are the same as the previous access-list rule.
29. Click the create button.
30. By clicking and holding the arrows next to the rule in the order column, move the rule to ensure that the Permit rule you just created is at the top of the list and that the Deny rule you just created is directly below it.
31.    Press the ‘Save Changes’ button to apply your configuration.

```eval_rst
   .. title:: IP Allow Listing
   .. meta::
      :title: IP Allow Listing | UKFast Documentation
      :description: Useful threat remediation and prevention tips
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```
