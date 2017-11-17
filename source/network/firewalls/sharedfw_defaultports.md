# Default Firewall Config - Shared Firewall

To edit or change the your firewall rules, please login to the following area <https://my.ukfast.co.uk/server/shared-firewall.php>


The default open ports, are dependent on the type server operating system you have:

## Linux

Traffic allowed **IN** over the internet to the server:

```eval_rst
+------------+-------+
| Service    | Port  |
+============+=======+
| HTTP       | 80    |
+------------+-------+
| HTTPS      | 443   |
+------------+-------+
| FTP        | 21    |
+------------+-------+
| FTP-DATA   | 20    |
+------------+-------+
| SMTP       | 25    |
+------------+-------+
| SUBMISSION | 587   |
+------------+-------+
| POP        | 110   |
+------------+-------+
| IMAP       | 143   |
+------------+-------+
| SSH        | 2020  |
+------------+-------+
| MCAFEE     | 65443 |
+------------+-------+
| MYSQL      | 3306  |
+------------+-------+
| PANEL      | 8090  |
+------------+-------+
| PANEL      | 8091  |
+------------+-------+
| PLESK      | 8443  |
+------------+-------+
| PLESK      | 8447  |
+------------+-------+
| PLESK      | 5224  |
+------------+-------+
| PLESK      | 11444 |
+------------+-------+
| WHM        | 2083  |
+------------+-------+
| WHM        | 2087  |
+------------+-------+
| WHM        | 2095  |
+------------+-------+
| WHM        | 2096  |
+------------+-------+
```

Traffic allowed **OUT** from your Linux server to the Internet:

```eval_rst
+------------+---------+
| Service    | Port    |
+============+=========+
| HTTP       | 80      |
+------------+---------+
| HTTPS      | 443     |
+------------+---------+
| FTP        | 21      |
+------------+---------+
| FTP-DATA   | 20      |
+------------+---------+
| SMTP       | 25      |
+------------+---------+
| SUBMISSION | 587     |
+------------+---------+
| MYSQL      | 3306    |
+------------+---------+
| PLESK      | 5224    |
+------------+---------+
| PLESK      | 8443    |
+------------+---------+
| PLESK      | 8447    |
+------------+---------+
| MCAFEE     | 65443   |
+------------+---------+
| WHM        | 2083    |
+------------+---------+
| WHM        | 2087    |
+------------+---------+
| WHM        | 2095    |
+------------+---------+
| WHM        | 2096    |
+------------+---------+
| WHM        | 2086    |
+------------+---------+
| WHM        | 2082    |
+------------+---------+
| DNS        | UDP 53  |
+------------+---------+
| NTP        | UDP 123 |
+------------+---------+
```

## Windows


Traffic allowed **IN** over the internet to your Windows server:

```eval_rst
+------------+-------+
| Service    | Port  |
+============+=======+
| HTTP       | 80    |
+------------+-------+
| HTTPS      | 443   |
+------------+-------+
| FTP        | 21    |
+------------+-------+
| FTP-DATA   | 20    |
+------------+-------+
| SMTP       | 25    |
+------------+-------+
| SUBMISSION | 587   |
+------------+-------+
| POP        | 110   |
+------------+-------+
| IMAP       | 143   |
+------------+-------+
| MSSQL      | 1334  |
+------------+-------+
| MCAFEE     | 65443 |
+------------+-------+
| MYSQL      | 3306  |
+------------+-------+
| PLESK      | 8197  |
+------------+-------+
| PLESK      | 8198  |
+------------+-------+
| PLESK      | 8443  |
+------------+-------+
| PLESK      | 8447  |
+------------+-------+
| PLESK      | 5224  |
+------------+-------+
```

Traffic allowed **OUT** from your Windows server to the Internet:

```eval_rst
+----------+---------+
| Service  | Port    |
+==========+=========+
| HTTP     | 80      |
+----------+---------+
| HTTPS    | 443     |
+----------+---------+
| FTP      | 21      |
+----------+---------+
| FTP-DATA | 20      |
+----------+---------+
| SMTP     | 25      |
+----------+---------+
| MSSQL    | 1334    |
+----------+---------+
| MYSQL    | 3306    |
+----------+---------+
| PLESK    | 8197    |
+----------+---------+
| PLESK    | 8443    |
+----------+---------+
| PLESK    | 8447    |
+----------+---------+
| NTP      | UDP 123 |
+----------+---------+
| DNS      | UDP 53  |
+----------+---------+
```

```eval_rst
  .. meta::
     :title: Default Firewall Config - Shared Firewall | UKFast Documentation
     :description: Information on the default firewall config on shared firewalls
     :keywords: ukfast, network, firewall, shared, dedicated, default, config, cloud, hosting

