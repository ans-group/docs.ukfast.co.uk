# UKFast shared firewall - default configurations

Below you will find the default configurations for your shared UKFast firewall, which are dependant upon your server's operating system.  You can edit or change your firewall rules in [MyUKFast](https://my.ukfast.co.uk/server/shared-firewall.php).

## Linux

Traffic allowed **in** over the Internet to the server:

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

Traffic allowed **out** from your Linux server to the Internet:

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

## Microsoft Windows Server

Traffic allowed **in** over the Internet to your Microsoft Windows Server:

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

Traffic allowed **out** from your Microsoft Windows Server to the Internet:

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
     :title: UKFast Shared Firewall Default Ports | UKFast Documentation
     :description: Shared Firewall Default Ports for UKFast-hosted servers
     :keywords: ukfast, firewall, shared, default, port, ports
```
