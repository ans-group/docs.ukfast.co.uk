```eval_rst
:orphan:
```

# Database Server Default Configuration

UKFast will setup Microsoft SQL Server with a default configuration that conforms to Microsoft best practices.

By default your MS-SQL database server will be configured with the following settings:

```eval_rst
+-----------------------------------+---------------------------------------------------------------------+
| Database Setting                  | Default                                                             |
+===================================+=====================================================================+
| MSSQL Version:                    | As per your Order Form                                              |
+-----------------------------------+---------------------------------------------------------------------+
| Listening TCP / IP Port:          | 1433/TCP                                                            |
+-----------------------------------+---------------------------------------------------------------------+
| Instance Name(s):                 | MSSQLSERVER                                                         |
+-----------------------------------+---------------------------------------------------------------------+
| Collation:                        | Latin1_General_CI_AS                                                |
+-----------------------------------+---------------------------------------------------------------------+
| Additional Features / Components: | All Components                                                      |
+-----------------------------------+---------------------------------------------------------------------+
| Configuration:                    | Log, Data and Backups will all be configured on the large partition |
+-----------------------------------+---------------------------------------------------------------------+
```

```eval_rst
  .. title:: UKFast MS-SQL database build documentation
  .. meta::
      :title: UKFast MS-SQL database build documentation | ANS Documentation
      :description: Build documentation for MS-SQL database servers
      :keywords: ukfast, hosting, database, server, virtual, mssql
