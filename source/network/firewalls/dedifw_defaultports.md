# UKFast dedicated firewall - default configurations

The default configurations for UKFast dedicated firewalls are set out below; these are dependant upon your server's operating system.  You can change or edit your firewall rules in [MyUKFast](https://my.ukfast.co.uk/server/dedicated-firewall.php)

## Linux

Traffic allowed **in** over the Internet to your Linux server:

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

Traffic allowed **out** from your Linux server to the Internet:

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


## Microsoft Windows Server

Traffic allowed **in** over the Internet to your Microsoft Windows Server:

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
| DNS      | UDP 53  |
+----------+---------+
| NTP      | UDP 123 |
+----------+---------+
```

```eval_rst
  .. meta::
     :title: UKFast Dedicated Firewall Default Configurations | UKFast Documentation
     :description: Default firewall configurations for Linux and Microsoft Windows servers at UKFast
     :keywords: ukfast, firewall, dedicated, default, port, ports
```
