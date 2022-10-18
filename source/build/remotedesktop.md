```eval_rst
:orphan:
```

# Remote Desktop Services

### What is Remote Desktop Services (RDS)?
RDS also known as Terminal Services allows end users to connect and access servers or computers remotely as long as a network connection is established on both sides. This gives people the ability to access applications or data that otherwise would require a physical presence such as a workplace or datacentre.

### What is an RDS Farm?
RDS can be used in a simple setup between one source and remote device (How we are all currently working remotely), but it can be expanded on by configuring an RDS Farm which is designed to provide many users with a virtual desktop without having a 1:1 hardware map.

Below outlines how the proposed configuration will be configured for the RDS Farm.

```eval_rst
.. seealso::
   UKFast will configure each role, add the SSL certificate (if purchased through UKFast) and ensure each role is able to communicate with the others.
```

```eval_rst
+--------------+-----------------------+-------------------------+----------------------------------------+
| NetBIOS Name | Role                  | Role Services Installed | Installed Applications                 |
+==============+=======================+=========================+========================================+
| RDSGW1       | RDS Web Access        | RDS Web Access          |                                        |
|              | RDS Connection Broker | RDS Connection Broker   |                                        |
|              | RDS Gateway           | RDS Gateway             |                                        |
+--------------+-----------------------+-------------------------+----------------------------------------+
| RDSSH1       | RDS Session Host      | RDS Session Host        | Web Browser                            |
|              |                       |                         | Purchased Apps (i.e. Microsoft Office) |
+--------------+-----------------------+-------------------------+----------------------------------------+
| RDSSH1       | RDS Session Host      | RDS Session Host        | Web Browser                            |
|              |                       |                         | Purchased Apps (i.e. Microsoft Office) |
+--------------+-----------------------+-------------------------+----------------------------------------+
```

```eval_rst
.. warning::
   UKFast are not responsible for configuring users, Group Policies or RDS Collection Groups. This is the responsibility of the client to administer,although UKFast's award-winning client support is available 24/7/365 should any guidance be required.
```

```eval_rst
   .. title:: UKFast RDS build documentation
   .. meta::
      :title: UKFast RDS build documentation | UKFast Documentation
      :description: Build documentation for UKFast Remote Desktop
      :keywords: ukfast, hosting, rds, server, virtual
```
