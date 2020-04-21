# Database Server Default Configuration

## MS-SQL Database
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

## MySQL/Percona/MariaDB Database
```eval_rst
+--------------------------------+-------------------------+
| Database Setting               | Default                 |
+================================+=========================+
| Installed Version:             | Latest Stable Release   |
+--------------------------------+-------------------------+
| Mount Point:                   | /var/lib/mysql          |
+--------------------------------+-------------------------+
| Collation:                     | utf8mb4_general_ci      |
+--------------------------------+-------------------------+
| Additional Features / Modules: | N/A                     |
+--------------------------------+-------------------------+
```

```eval_rst
  .. meta::
      :title: UKFast database build documentation | UKFast Documentation
      :description: Build documentation for database servers
      :keywords: ukfast, hosting, database, server, virtual
