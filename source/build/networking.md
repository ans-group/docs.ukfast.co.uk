```eval_rst
:orphan:
```

# Networking

## VPN Connections

A virtual private network (VPN) provides a tunnel between two separate networks to allow for encrypted communication to take place over the public internet.

```eval_rst
.. seealso::
   Depending on the firewall you have purchased will depend on the number of available VPN connections for each device.
```

Below you will find the maximum number of supported Site to Site VPNs:

```eval_rst
+--------------------------------+------------------------+
| Firewall                       | Maximum Number of VPNs |
+================================+========================+
| Cisco ASA 5506-X Security Plus | 50                     |
+--------------------------------+------------------------+
| Cisco ASA 5508-X               | 100                    |
+--------------------------------+------------------------+
| Cisco ASA 5516-X               | 300                    |
+--------------------------------+------------------------+
| Cisco ASA 5525-X               | 750                    |
+--------------------------------+------------------------+
| Cisco ASAv5                    | 50                     |
+--------------------------------+------------------------+
| Cisco ASAv10                   | 250                    |
+--------------------------------+------------------------+
```

## Default VLANs

Your solution will be configured with a single VLAN which will contain all of your virtual machines.

```eval_rst
+-----------+--------------+
| VLAN Name | Purpose      |
+===========+==============+
| Inside    | All servers. |
+-----------+--------------+
```

```eval_rst
.. warning::
   If you require additional VLAN segregation, please speak to your Account Manager as soon as possible. This must be done before the solution build is started, or we may not be able to fulfil your request.
   Each VLAN will be assigned a separate internal subnet, defined by UKFast.
```

```eval_rst
  .. title:: UKFast networking build documentation
  .. meta::
      :title: UKFast networking build documentation | UKFast Documentation
      :description: Build documentation for UKFast networking
      :keywords: ukfast, hosting, networking, server, virtual
```
