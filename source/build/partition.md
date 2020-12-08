# Partitions

A disk partition is a section of the hard drive that is separated from other segments. Partitions enables you to divide a physical disk into logical sections, which inturn gives you greater control of storage within your solution.

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

## Virtual Machines

The size of disk allocation to virtual machines can be edited depending on requirements in the Enterprise Launch Questionnaire.

```eval_rst
   .. title:: UKFast server partitions
   .. meta::
      :description: UKFast server partitions
      :keywords: ukfast, hosting, partitions, server, virtual
```
