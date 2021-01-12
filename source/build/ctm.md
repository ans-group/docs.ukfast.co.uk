# Capacity Threshold Monitoring

Capacity Threshold Monitoring allows you to track every aspect of your dedicated server, from bandwidth consumption to disk utilisation, enabling you to configure a range of monitoring checks for your servers. This ensures both you and your UKFast support team will be alerted if a problem occurs.

The following CTM alerts will be configured on your servers, as applicable:

```eval_rst
+----------------------+------------------+-----------------------+------------------+---------+
| Name                 | Acceptable Range | Alert Triggered When  | Operating System | Default |
+======================+==================+=======================+==================+=========+
| CPU Usage            | 0% - 80%         | CPU usage hits 81%    | Windows / Linux  | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| Memory Usage         | 0% - 80%         | Memory usage hits 81% | Windows          | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| C Drive Space (free) | 15% - 100%       | Free space hits 14%   | Windows          | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| D Drive Space (free) | 15% - 100%       | Free space hits 14%   | Windows          | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| / Space (free)       | 15% - 100%       | Free space hits 14%   | Linux            | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| /var Space (free)    | 15% - 100%       | Free space hits 14%   | Linux            | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| /home Space (free)   | 15% - 100%       | Free space hits 14%   | Linux            | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
| Swap Usage           | 0% - 80%         | Swap usage hits 81%   | Linux            | Enabled |
+----------------------+------------------+-----------------------+------------------+---------+
```

```eval_rst
  .. title:: UKFast CTM build documentation
  .. meta::
      :title: UKFast CTM build documentation | UKFast Documentation
      :description: Build documentation for UKFast CTM
      :keywords: ukfast, hosting, ctm, server, virtual
```
