```eval_rst
:orphan:
```

# Firewall Configuration

Establishing a barrier between trusted and untrusted networks, firewalls, when configured correctly can greatly increase the security of your Solution. UKFast provides a diverse range of firewall options to suit your requirements. Outlined below is the UKFast default firewall rules for both inbound and outbound access.

## Default Firewall Rules

The following rules apply to all servers in the environment. Changes required for specific servers should be listed under the Custom Firewall Rules section of your Enterprise Launch Questionnaire.

### Inbound:
All ports closed.

### Outbound:

```eval_rst
+----------+------+-----------+--------------------+
| Protocol | Port | TCP / UDP | From / To          |
+==========+======+===========+====================+
| SMTP     | 25   | TCP       |                    |
+----------+------+-----------+--------------------+
| DNS      | 53   | TCP & UDP | UKFast DNS Servers |
+----------+------+-----------+--------------------+
| NTP      | 123  | UDP       | UKFast NTP Servers |
+----------+------+-----------+--------------------+
| HTTP     | 80   | TCP       |                    |
+----------+------+-----------+--------------------+
| HTTPS    | 443  | TCP       |                    |
+----------+------+-----------+--------------------+
```
If your solution design includes multiple VLANs, other ports may be required to communicate internally between VLANs as part of the configuration and setup of the solution by UKFast, for example Active Directory. If so additional ports may be opened depending on the technical requirements of your solution.

```eval_rst
.. seealso::
   Depending on your solution design & complexity, firewall rules can be viewed & configured in MyUKFast.
```

```eval_rst
  .. title:: UKFast Enterprise Firewall Default Configuration
  .. meta::
      :title: UKFast Enterprise Firewall Default Configuration | ANS Documentation
      :description: Default Configuration for UKFast Enterprise Firewalls
      :keywords: ukfast, hosting, firewall, server, virtual, enterprise
```
