# Database Server Default Configuration

UKFast will setup Microsoft SQL Server with a default configuration that conforms to Microsoft best practices.

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
| Unit Allocation Size              | 64KB NTFS                                                              |
+-----------------------------------+------------------------------------------------------------------------+
| Instant File Initialisation       | Enabled                                                                |
+-----------------------------------+------------------------------------------------------------------------+
| Configuration:                    | Data, Logs and TempDB will be configured onto separate disk partitions |
+-----------------------------------+------------------------------------------------------------------------+
```

## Unit Allocation Size

SQL server prefers 64KB NTFS allocation unit size as data is loaded in blocks referred to as extents (64KB in size), made up out of 8 x 8KB pages. Any volume containing client databases (.MDF/.NDF files) and TempDB should be provisioned with a 64KB unit allocation size. This does not apply to any volumes containing just log (.LDF) files. Volumes containing both can use 64KB allocation.

## Instant File Initialisation

Whenever SQL Server needs to allocate space for certain operations like creating/restoring a database or growing data/log files, SQL Server first fills the space it needs with zeros. In many cases, writing zeros across the disk space before using that space is unnecessary. 

Instant file initialization (IFI) allows SQL Server to skip the zero-writing step and begin using the allocated space immediately for data files. It doesn’t impact growths of transaction log files, those still need all the zeroes. 

## Service Accounts

Indiviual service accounts are created for each standalone SQL server or cluster in the following naming conventions:

- Standalone: SQL.<NETBIOS> (Eg: sql.ukf-sql-01)
- Cluster: SQL.<cluster_name> (Eg: sql.ukfclstr01)

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
.. seealso::
   DB data files (.MDF/.NDF files), Logs (.LDF) and system databases (TempDB) ideally should be segregated across different drives and sized accordingly. 
```

```eval_rst
   .. title:: UKFast Enterprise MS-SQL database build documentation
   .. meta::
      :description: Build documentation for Enterprise MS-SQL database servers
      :keywords: ukfast, hosting, database, server, virtual, mssql
```
