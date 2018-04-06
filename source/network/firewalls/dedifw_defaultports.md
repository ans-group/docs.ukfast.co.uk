# Default Firewall Configuration - Dedicated Firewall

To edit or change the your firewall rules, please login to the following area <https://my.ukfast.co.uk/server/dedicated-firewall.php>

The default open ports are dependent on the type server operating system you have:

## Linux

Traffic allowed **IN** over the internet to your Linux server:

```eval_rst
+----------+-------+
| Service  | Port  |
+==========+=======+
| HTTP     | 80    |
+----------+-------+
| HTTPS    | 443   |
+----------+-------+
| FTP      | 21    |
+----------+-------+
| FTP-DATA | 20    |
+----------+-------+
| SMTP     | 25    |
+----------+-------+
| POP      | 110   |
+----------+-------+
| IMAP     | 143   |
+----------+-------+
| SSH      | 2020  |
+----------+-------+
| MCAFEE   | 65443 |
+----------+-------+
```


Traffic allowed **OUT** from your Linux server to the Internet:

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
| DNS      | UDP 53  |
+----------+---------+
| NTP      | UDP 123 |
+----------+---------+
```


## Windows

Traffic allowed **IN** over the internet to your Windows server:

```eval_rst
+----------+-------+
| Service  | Port  |
+==========+=======+
| HTTP     | 80    |
+----------+-------+
| HTTPS    | 443   |
+----------+-------+
| FTP      | 21    |
+----------+-------+
| FTP-DATA | 20    |
+----------+-------+
| RDP      | 3389  |
+----------+-------+
| POP      | 110   |
+----------+-------+
| IMAP     | 143   |
+----------+-------+
| MCAFEE   | 65443 |
+----------+-------+
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
| DNS      | UDP 53  |
+----------+---------+
| NTP      | UDP 123 |
+----------+---------+
```

```eval_rst
  .. meta::
     :title: Dedicated Firewall Default Ports | UKFast Documentation
     :description: Dedicated Firewall Default Ports
     :keywords: ukfast, firewall, dedicated, default, port, ports
```
