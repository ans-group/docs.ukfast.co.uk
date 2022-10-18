```eval_rst
:orphan:
```

# Recommended Configuration for BCP (Business Continuity Platform)

UKFast's Linux clustering solution, BCP (Business Continuity Platform) ensures high-availability and minimal downtime for your Linux servers. As part of your BCP Solution you will receive a Pre-Launch Questionnaire specific to your solution. Due to the complexity of the BCP solution UKFast doesn't offer default configurations, below are our recommended configurations if you are unsure on the configuration required for your business needs.

```eval_rst
.. seealso::
   Please contact your Account Manager to ensure you receive a copy of the BCP Pre-Launch Questionnaire.
```
## Two Node Web/DB BCP Example Diagram

```eval_rst
.. image:: files/2-Node-BCP.png
   :width: 400
```

## Disk Space

```eval_rst
+--------------------+-----------------------------+
| Clustered Resource | % of recommended disk space |
+====================+=============================+
| NFS                | 100%                        |
+--------------------+-----------------------------+
| Database and NFS   | 50% / 50%                   |
+--------------------+-----------------------------+
| Database           | 100%                        |
+--------------------+-----------------------------+
| Web and Database   | 50% / 50%                   |
+--------------------+-----------------------------+
```

## Software Versions

```eval_rst
+----------------------+--------------+-------------+-------------+
| Recommended Versions | No Magento   | Magento 1   | Magento 2   |
+======================+==============+=============+=============+
| PHP                  | 7.3          | 7.2         | 7.2         |
+----------------------+--------------+-------------+-------------+
| DB                   | MariaDB 10.4 | Percona 5.6 | Percona 5.7 |
+----------------------+--------------+-------------+-------------+
| Web Server           | nginx        | nginx       | nginx       |
+----------------------+--------------+-------------+-------------+
```
```eval_rst
  .. title:: UKFast Default BCP Configuration
  .. meta::
      :title: UKFast Default BCP Configuration | UKFast Documentation
      :description: Default Configuration for a BCP Solution.
      :keywords: ukfast, hosting, server, linux, bcp, business continuity platform
```
