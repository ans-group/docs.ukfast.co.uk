# Application Monitoring

For increased peace of mind, application based monitoring is enabled as standard to ensure alerts are generated proactively in the event of application failure, even if the server remains online. Depending on the application and configuration of your solution will depend on whether this is applicable.

```eval_rst
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
| Application              | When Applicable                                                                                                    |
+==========================+====================================================================================================================+
| DFS-R                    | When Distributed File System Replication is configured across more than one servers this is enabled by default.    |
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
| Hyper-V Replica          | When Hyper-V Replication is configured across more than one server this is enabled by default.                     |
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
| Active Directory         | When Active Directory is installed and replicating between more than one servers this is enabled by default.       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
| Failover Cluster Manager | When Failover Cluster Manager is installed and contains one or more clustered services this is enabled by default. |
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
| Microsoft SQL Server     | When Microsoft SQL Server is installed this will monitor the SQL Service.                                          |
+--------------------------+--------------------------------------------------------------------------------------------------------------------+
```

```eval_rst
  .. title:: UKFast application monitoring documentation
  .. meta::
      :title: UKFast application monitoring documentation | UKFast Documentation
      :description: Monitoring documentation for UKFast application
      :keywords: ukfast, hosting, application_monitoring, server, virtual
```
