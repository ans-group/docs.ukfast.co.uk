# Default Configuration for BCP (Business Continuity Platform)

As part of your BCP Solution you will receive a Pre-Launch Questionnaire specific to your solution. Due to the complexity of the BCP solution UKFast doesn't offer default configurations, below are our recommended configurations if you are unsure on the configuration required for your business needs. 

Please contact your Account Manager to ensure you receive a copy of the BCP Pre-Launch Questionnaire. 

## Disk Space

```eval_rst
+--------------------+-----------------------------+
| Clustered Resource | % of recommended disk space |
+====================+=============================+
| NFS                | 100%                        |
+--------------------------------------------------+
| Database           | 100%                        |
+--------------------------------------------------+
| Database and NFS   | 50% / 50%                   |
+--------------------------------------------------+
| Web and Database   | 50% / 50%                   |
+--------------------------------------------------+
```

## Software Versions

```eval_rst
+----------------------+--------------+--------------+--------------+
| Recommended Versions | No Magento   | Magento 1    | Magento 2    |
+======================+==============+==============+==============+
| PHP                  | 7.3          | 5.6          | 7.2          |
+----------------------+--------------+--------------+--------------+
| DB                   | MariaDB 10.3 | Percona 5.6  | Percona 5.7  |
+----------------------+--------------+--------------+--------------+
| Web Server           | nginx        | nginx        | nginx        |
+----------------------+--------------+--------------+--------------+
```

```eval_rst
  .. meta::
      :title: UKFast Default BCP Configuration | UKFast Documentation
      :description: Default Configuration for a BCP Solution.
      :keywords: ukfast, hosting, server, linux, bcp, business continuity platform
