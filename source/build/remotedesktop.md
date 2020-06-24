## Remote Desktop Services

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
   UKFast are not responsible for configuring users, Group Policies or RDS Collection Groups. This is the responsibility of the client to administer, although UKFast Support is on-hand if any guidance is required.
```
```eval_rst
  .. title:: UKFast RDS build documentation
  .. meta::
      :title: UKFast RDS build documentation | UKFast Documentation
      :description: Build documentation for UKFast Remote Desktop
      :keywords: ukfast, hosting, rds, server, virtual
