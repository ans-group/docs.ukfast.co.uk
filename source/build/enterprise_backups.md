# Default Configuration for Backups

In order for UKFast to simplify our backup schedule offering without losing the ability to tailor the configuration to your solution, we have predefined backup options available for you to select from. Please note that: 
- The retention for Shared eCloud Backups is 28 days.
- The default retention for Dedicated eCloud Backup solutions is 28 days.
- The time backups run at is stipulated by UKFast in an overnight window, unless otherwise specified.
```eval_rst
.. seealso::
   To make changes to the backup window, frequency or retention of any of your backup policies post launch, along with adding any backup excultions to specific folders, files or file types please use the Priority Support System in the MyUKFast portal.
```
## Operating System and File Level Backups

### Backup Options
```eval_rst
+---------------------------------+-------------+--------------------+
| Option                          | Full Backup | Incremental Backup |
+=================================+=============+====================+
| File Level - Option 1 (default) | Weekly      | Once Daily         |
+---------------------------------+-------------+--------------------+
| File Level - Option 2           | Daily       | n/a                |
+---------------------------------+-------------+--------------------+
```
- Physical and virtual machines have a full backup taken once a week by default.
- Physical and virtual machines have incremental backups taken every day (except for the day the full backup is taken).

## Database Backups

### Backup Agents

When referring to Database Backups by default we will apply the below configurations to the following Backups Agents: 
-	Microsoft Exchange 
-	Microsoft SharePoint 
-	Microsoft SQL Server
-	PostgreSQL
-	Oracle DB 
-	MySQL Server / MariaDB

### Backup Options
```eval_rst
+-------------------------------------+-------------+------------------+
| Option                              | Full Backup | Transaction Log  |
+=====================================+=============+==================+
| Database Level - Option 1           | Weekly      | Once Daily       |
+-------------------------------------+-------------+------------------+
| Database Level - Option 2           | Daily       | n/a              |
+-------------------------------------+-------------+------------------+
| Database Level - Option 3 (default) | Daily       | Every Hour       |
+-------------------------------------+-------------+------------------+
| Database Level - Option 4           | Daily       | Every 15 minutes |
+-------------------------------------+-------------+------------------+
```
-	Physical and virtual machines have a full backup taken once a week by default.
-	Physical and virtual machines have transaction log backups taken every day (except for the day the full backup is taken).

## Standalone Database Backups

To enable UKFast to provide a more granular level for restores of databases, by default: 
-	Database servers (e.g. MSSQL, MySQL, PostgreSQL) are backed up at the database level.
-	Database backup times are different to the operating system backup times to limit the impact on performance.

## File and Database Clusters

To enable UKFast to provide a more granular level for restores of database clusters, by default:
-	Nodes in the clusters are backed up at different times to limit the impact on performance.
-	Database Clusters have an additional database level backup (again at different times to the nodes).
-	File Server Clusters will have an additional backup set up for the cluster drives. 

## Virtual Machine Level Backups

### Backup Options
```eval_rst
+---------------------+-------------+--------------------+
| Option              | Full Backup | Incremental Backup |
+=====================+=============+====================+
| VM Level - Option 1 | Weekly      | Once Daily         |
+---------------------+-------------+--------------------+
```
All full backups for Virtual Machines are performed on a weekly basis with daily incremental backups taken daily except for the day the full backup is taken.

```eval_rst
  .. title:: UKFast Enterprise backup build documentation | UKFast Documentation
  .. meta::
      :title: UKFast Enterprise backup build documentation | UKFast Documentation
      :description: Build documenation for UKFast Enterprise Backups
      :keywords: ukfast, hosting, backup, server, virtual, enterprise
