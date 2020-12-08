# Firewall Configuration

Establishing a barrier between trusted and untrusted networks, firewalls, when configured correctly can greatly increase the security of your system. UKFast provides a diverse range of firewall options to suit your requirements. Outlined below is the UKFast default firewall rules for both inbound and outbound access. 

Please find below the UKFast Default Firewall rules for Inbound and Outbound access. 
```eval_rst
.. warning::
   Please note: Once your solution has been deployed, we would recommend that you use the MyUKFast Firewall Editor to refine these rules to ensure your solution is a secure as possible, we would stongly recommend restricting the likes of RDP and SSH to specific IP addresses. 
```
## Default Firewall Rules
The following rules apply to all servers in the environment. Changes required for specific servers should be listed under the Custom Firewall Rules section of your Launch Questionaire.

### Inbound:
```eval_rst
+----------+---------+-----------+--------------------+
| Protocol | Port    | TCP / UDP | From / To          |
+==========+=========+===========+====================+
| SMTP     | 25      | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| DNS      | 53      | TCP & UDP | UKFast DNS Servers |
+----------+---------+-----------+--------------------+
| NTP      | 123     | UDP       | UKFast NTP Servers |
+----------+---------+-----------+--------------------+
| HTTP     | 80      | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| HTTPS    | 443     | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| FTP      | 20 / 21 | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| SSH      | 2020    | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| RDP      | 3389    | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| POP3     | 110     | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
```

### Outbound:
```eval_rst
+----------+---------+-----------+--------------------+
| Protocol | Port    | TCP / UDP | From / To          |
+==========+=========+===========+====================+
| SMTP     | 25      | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| DNS      | 53      | TCP & UDP | UKFast DNS Servers |
+----------+---------+-----------+--------------------+
| NTP      | 123     | UDP       | UKFast NTP Servers |
+----------+---------+-----------+--------------------+
| HTTP     | 80      | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| HTTPS    | 443     | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
| FTP      | 20 / 21 | TCP       | Everywhere         |
+----------+---------+-----------+--------------------+
```
If your solution design includes multiple VLANs, other ports may be required to communicate internally between VLANs as part of the configuration and setup of the solution by UKFast, for example Active Directory. If so additional ports may be opened depending on the technical requirements of your solution.

```eval_rst
.. seealso::
   Depending on your solution design & complexity, firewall rules can be viewed & configured in MyUKFast.
```
```eval_rst
  .. title:: UKFast Firewall Default Configuration
  .. meta::
      :title: UKFast Firewall Default Configuration | UKFast Documentation
      :description: Default Configuration for UKFast Firewalls
      :keywords: ukfast, hosting, firewall, server, virtual
