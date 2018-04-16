# VPN capacity on UKFast dedicated firewalls

The VPN capacity on your firewall depends on the model of firewall you're using. You can check your firewall model in [MyUKFast](https://my.ukfast.co.uk/server/dedicated-firewall.php), and then refer to the list below:

```eval_rst
+------------------------------------------+----------------+-----------------+----------------+----------------+
| Firewall Model                           | Cisco ASA 5505 | Cisco ASA 5506X | Cisco ASA5508X | Cisco ASA5512X |
+==========================================+================+=================+================+================+
| Concurrent IPSec VPN sessions (default)  |       10       |        10       |       100      |       250      |
+------------------------------------------+----------------+-----------------+----------------+----------------+
| Concurrent IPSec VPN sessions (upgraded) |        2       |        2        |                |                |
+------------------------------------------+----------------+-----------------+----------------+----------------+
| WebSSL VPN sessions (default)            |       25       |        50       |        2       |        2       |
+------------------------------------------+----------------+-----------------+----------------+----------------+
| WebSSL VPN sessions (upgraded)           |       50       |        50       |       100      |       250      |
+------------------------------------------+----------------+-----------------+----------------+----------------+
```


```eval_rst
  .. meta::
     :title: VPN Capacity of UKFast firewalls | UKFast Documentation
     :description: A reference for the number of supported VPN connections per firewall type
     :keywords: ukfast, firewall, rebooting, network, myukfast, cloud, hosting, dedicated
```
