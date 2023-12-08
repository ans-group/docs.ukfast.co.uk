```eval_rst
:orphan:
```

# Monitoring

## Service Monitoring
The following service monitoring will be added across all servers in the solution:

```eval_rst
+-------------------------------------+-------------+
| Monitoring                          | Default     |
+=====================================+=============+
| Enterprise Ping (1 minute interval) | Enabled     |
+-------------------------------------+-------------+
| SMTP                                | Not Enabled |
+-------------------------------------+-------------+
| POP                                 | Not Enabled |
+-------------------------------------+-------------+
| HTTP                                | Not Enabled |
+-------------------------------------+-------------+
| FTP                                 | Not Enabled |
+-------------------------------------+-------------+
```
```eval_rst
.. seealso::
   If additional optional monitoring is required for services not listed above please inform your Account Manager or request via the Priority Support system in the MyUKFast portal after launch to make configuration changes.
```
## Example Additional Monitoring Options

```eval_rst
+-----------------------------------------+--------------------+-------------+
| Hostname                                | Port/ Service/ URL | Default     |
+=========================================+====================+=============+
| e.g. ``http://example.com/status.apsx`` | e.g. URL           | Not enabled |
+-----------------------------------------+--------------------+-------------+
```

## Capacity Threshold Monitoring

Capacity Threshold Monitoring allows you to track every aspect of your dedicated server or virtual machine, from bandwidth consumption to disk utilisation.

More information about Capacity Threshold Monitoring can be found [here](ctm.md).

## Specific Application Monitoring

Monitoring can be enabled for specific applications, such as MSSQL to ensure you're alerted the moment a problem has occurred.

More information about specific application monitoring can be found [here](app_monitoring.md).

```eval_rst
  .. title:: UKFast Enterprise Monitoring Default Configuration
  .. meta::
      :title: UKFast Enterprise Monitoring Default Configuration | ANS Documentation
      :description: Default Configuration for UKFast Enterprise Monitoring
      :keywords: ukfast, hosting, monitoring, server, virtual, enterprise
```
