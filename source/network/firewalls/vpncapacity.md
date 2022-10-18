# VPN capacity on UKFast dedicated firewalls

The VPN capacity on your firewall depends on the model of firewall you're using. You can check your firewall model in [MyUKFast](https://portal.ans.co.uk/server/dedicated-firewall.php), and then refer to the list below for the maximum number of concurrent connections for IPsec VPN and WebSSL VPN, depending on whether you have a default configuration or upgraded license:

```eval_rst
+----------------------------------------------------+----------------+-----------------+----------------+----------------+
| Firewall Model                                     | Cisco ASA5505  | Cisco ASA5506X  | Cisco ASA5508X | Cisco ASA5512X |
+====================================================+================+=================+================+================+
| Concurrent IPsec VPN sessions (default)            |       10       |        10       |       100      |       250      |
+----------------------------------------------------+----------------+-----------------+----------------+----------------+
| Concurrent IPsec VPN sessions (upgraded license)   |       25       |        50       |                |                |
+----------------------------------------------------+----------------+-----------------+----------------+----------------+
| Concurrent WebSSL VPN sessions (default)           |       2        |        2        |        2       |        2       |
+----------------------------------------------------+----------------+-----------------+----------------+----------------+
| Concurrent WebSSL VPN sessions (upgraded license)  |       50       |        50       |       100      |       250      |
+----------------------------------------------------+----------------+-----------------+----------------+----------------+
```
If you are on a default configuration and need additional VPN capacity, please [contact your UKFast Account Manager](https://portal.ans.co.uk/account/your-account-manager.php) to discuss upgrading your firewall license.


```eval_rst
  .. title:: VPN Capacity of UKFast firewalls
  .. meta::
     :title: VPN Capacity of UKFast firewalls | UKFast Documentation
     :description: A reference for the number of supported VPN connections per firewall type
     :keywords: ukfast, firewall, network, myukfast, vpn, capacity, ipsec, webssl, sessions, concurrent
```
