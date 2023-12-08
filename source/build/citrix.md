```eval_rst
:orphan:
```

# Citrix

Below outlines how the proposed configuration will be configured for the Citrix Farm.

```eval_rst
.. seealso::
   UKFast will configure each role, add the SSL certificate (if purchased through UKFast) and ensure each role is able to communicate with the others.
```

```eval_rst
+------------------+----------------------------+----------------------------------------+
| NetBIOS Name     | Role                       | Software / Features Installed          |
+==================+============================+========================================+
| CTXADC01 / CTXNS | Citrix Netscaler ADC       | Citrix ADC Appliance                   |
+------------------+----------------------------+----------------------------------------+
| CTXSF01          | Citrix StoreFront          | Citrix Storefront                      |
|                  |                            | | Citrix Receiver                      |
|                  |                            | | IIS                                  |
+------------------+----------------------------+----------------------------------------+
| CTXDC01          | Citrix Delivery Controller | Citrix Delivery Controller             |
|                  | | Citrix Studio            | | Citrix Studio                        |
|                  |                            | | Citrix Receiver                      |
+------------------+----------------------------+----------------------------------------+
| CTXMISC01        | Citrix Licencing           | Citrix Licencing                       |
|                  | | Citrix Database Host     | | Citrix Receiver                      |
+------------------+----------------------------+----------------------------------------+
| CTXXENAPP01      | Citrix XenApp Host         | Purchased Apps (i.e. Microsoft Office) |
+------------------+----------------------------+----------------------------------------+
| CTXXENAPP02      | Citrix XenApp Host         | Purchased Apps (i.e. Microsoft Office) |
+------------------+----------------------------+----------------------------------------+
```

```eval_rst
.. warning::
   UKFast are not responsible for configuring users, Group Policies or RDS Collection Groups. This is the responsibility of the client to administer, although UKFast Support is on-hand if any guidance is required.
```

```eval_rst
  .. title:: UKFast Citrix build documentation
  .. meta::
      :title: UKFast Citrix build documentation | ANS Documentation
      :description: Build documentation for UKFast Citrix
      :keywords: ukfast, hosting, citrix, server, virtual
```
