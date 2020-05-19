# Server Partitions

Please find below the UKFast Default Partitions configured as part of your solution. 

## Windows Server
```eval_rst
+-----------+-----------------+--------------------------+
| Partition | Size or %       | Example (2x 256GB RAID1) |
+===========+=================+==========================+
| C: Drive  | 100GB           | 100GB                    |
+-----------+-----------------+--------------------------+
| D: Drive  | Remaining Space | 135GB                    |
+-----------+-----------------+--------------------------+
```

## Linux Server

The below configuration applies to the following Linux Servers:
-	LAMP 
-	Magento
-	Control Panels 

```eval_rst
+-----------------+---------------------+--------------------------+
| Partition       | Size or %           | Example (2x 256GB RAID1) |
+=================+=====================+==========================+
| Swap            | 25% of Total Memory | 4GB                      |
+-----------------+---------------------+--------------------------+
| /boot Partition | 1GB Minimum         | 1GB                      |
+-----------------+---------------------+--------------------------+
```

```eval_rst
  .. meta::
      :title: UKFast server partitions | UKFast Documentation
      :description: UKFast server partitions
      :keywords: ukfast, hosting, partitions, server, virtual
