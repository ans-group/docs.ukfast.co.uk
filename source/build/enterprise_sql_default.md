# Database Server Default Configuration

By default your MS-SQL database server will be configured with the following settings:

```eval_rst
+-----------------------------------+------------------------------------------------------------------------+
| Database Setting                  | Default                                                                |
+===================================+========================================================================+
| MSSQL Version:                    | As per your Order Form                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| Listening TCP / IP Port:          | 1433/TCP                                                               |
+-----------------------------------+------------------------------------------------------------------------+
| Instance Name(s):                 | MSSQLSERVER                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| Collation:                        | Latin1_General_CI_AS                                                   |
+-----------------------------------+------------------------------------------------------------------------+
| Additional Features / Components: | None                                                                   |
+-----------------------------------+------------------------------------------------------------------------+
| Instant File Initialisation       | Enabled                                                                |
+-----------------------------------+------------------------------------------------------------------------+
| Configuration:                    | Data, Logs and TempDB will be configured onto separate disk partitions |
+-----------------------------------+------------------------------------------------------------------------+
```

## Example of Disk Configuration

```eval_rst
+--------------+-------+------+---------------------+
|              | Data  | Logs | System DBs (TempDB) |
+==============+=======+======+=====================+
| Drive Letter | D:    | L:   | T:                  |
+--------------+-------+------+---------------------+
| Size         | 100GB | 30GB | 10GB                |
+--------------+-------+------+---------------------+
```

```eval_rst
  .. title:: UKFast Enterprise MS-SQL database build documentation
  .. meta::
      :title: UKFast Enterprise MS-SQL database build documentation | UKFast Documentation
      :description: Build documentation for Enterprise MS-SQL database servers
      :keywords: ukfast, hosting, database, server, virtual, mssql
