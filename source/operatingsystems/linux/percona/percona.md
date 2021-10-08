# Percona

## Percona Repository
You can install the Percona repository with the command:

```bash
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
```

## Install Percona on `CentOS`

* **5.6**

```bash
yum install Percona-Server-server-56
```

* **5.7**

```bash
yum install Percona-Server-server-57
```

## Install Percona on `Ubuntu`
```bash
apt-get install gnupg2
wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
apt-get update
```
* **8.0**
 ```bash
percona-release setup ps80
```

## Updating Percona

* **5.6**

```bash
yum update Percona-Server-server-56
```

* **5.7**

```bash
yum update Percona-Server-server-57
```

#### Major Version Update
If you are updating MySQL from 5.6 to 5.7 run the command:

```bash
mysql_upgrade
```

#### 5.7 -> 8.0 Update

If you are updating to version 8.x you will need to follow the steps detailed below. We are using an update from Percona `5.7.29-32` as an example.

* Dump all databases in case of corruption:

```bash
mysqldump --all-databases > alldatabases.sql
```

* Check what Percona versions are installed:

```bash
rpm -qa | grep –i percona
```

* Remove these versions:

```bash
yum remove Percona-Server-server-57-5.7.29-32.1.el7.x86_64 Percona-Server-client-57-5.7.29-32.1.el7.x86_64 Percona-Server-shared-57-5.7.29-32.1.el7.x86_64 Percona-Server-shared-compat-57-5.7.29-32.1.el7.x86_64
```

* Add the below to `/etc/my.cnf` underneath the `[mysql]` section:

```ini
default-authentication-plugin=mysql_native_password
skip-log-bin
```

* Comment out the `query_cache` variables in that same file by adding a hash to the start of each line:

```ini
#query_cache_size = 128M
#query_cache_limit = 8M
#query_cache_type = 1
```

* Set up the repository ready to install the updated version:

```bash
percona-release setup ps80
```

* Install the new version:

```bash
yum install percona-server-server percona-toolkit
```

* Start the new version:

```bash
systemctl enable --now mysqld
```

### Enable On Boot

```bash
systemctl enable mysqld
```

## Start Percona

```bash
systemctl start mysqld
```

## Increase max_connections

You can edit the writable variable `max_connections` like so:

```sql
set global max_connections = 400;
```

To make the change permanent you need to change the value in `/etc/my.cnf`

## User-specific options

You can create the file `~/.my.cnf` in the home directory of your desired user to configure and save MySQL options:

```ini
[client]
host=IP.IP.IP.IP
user=username
password=password
```

Now when running the `mysql` command the values in the file `.my.cnf` will be used.

## Wildcard Grants

This is an example of a wildcard grant to `databasename`

```sql
mysql> GRANT ALL PRIVILEGES ON `databasename\_%`.* TO 'databaseuser'@'172.18.68.%';
```

## Disable Warnings

```sql
mysql> set global log_warnings = 0;
```

To make this change permanent add to `/etc/my.cnf` under `[mysqld]`:

```ini
log_warnings = 0
```

## Display Current User
```sql
mysql> select CURRENT_USER();
```

## Database Sizes

You can list the sizes in megabytes for all databases with the command:

```sql
mysql> SELECT table_schema "DB", Round(Sum(data_length + index_length) / 1024 / 1024, 1) "MB" FROM information_schema.tables GROUP BY table_schema;
```

```none
+-----------------------------+--------+
| DB                          | MB     |
+-----------------------------+--------+
| information_schema          |    0.2 |
| database1                   |   53.0 |
| database2                   |   48.9 |
| mysql                       |    8.0 |
| performance_schema          |    0.0 |
| sys                         |    0.0 |
| testingdb                   | 1376.7 |
+-----------------------------+--------+
7 rows in set (1.00 sec)
```

## Table Sizes In DB

You can view the table sizes within a database with the command:

Replace `DBNAME` with the database name you want to see the table sizes for:

```sql
mysql> SELECT table_name AS "Table", round(((data_length + index_length) / 1024 / 1024), 2) as SIZE FROM information_schema.TABLES WHERE table_schema = "DBNAME" order by SIZE;
```

```none
+---------------------------------------------------------+---------+
| Table                                                   | SIZE    |
+---------------------------------------------------------+---------+
| table1                                                  |    NULL |
| table2                                                  |    0.00 |
| table3                                                  |   15.06 |
| table4                                                  |   34.09 |
| table5                                                  | 1145.53 |
+---------------------------------------------------------+---------+
702 rows in set (0.16 sec)
```

## MySQL Tuner

MySQL tuner is a great tool to review resource usage and MySQL settings. You can download and run MySQL tuner with the commands:

```bash
wget mysqltuner.pl -O mysqltuner.pl
perl mysqltuner.pl
```

### `innodb_buffer_pool_instances`
This variable was only introduced in MySQL 5.5.4, so if you are using an older version, ignore this section. Otherwise, this should be set to 1 per GB of `innodb_buffer_pool_size`. Please refer to the external [MySQL documentation](https://dev.mysql.com/doc/refman/5.6/en/innodb-multiple-buffer-pools.html) for more information.

### `innodb_buffer_pool_size`

In an ideal world, `innodb_buffer_pool_size` should be slightly larger than the total amount of data you store in InnoDB tables. That means your server can hold the entire dataset in memory, and helps avoid slow disk IO when reading data. In the real world, that's not always possible. You may not have enough RAM, or you don't want to take memory away from your other applications and risk making your server unstable.

To see the total size of your InnoDB tables in MB, you can run the following command:

```sql
SELECT TABLE_SCHEMA, SUM(ROUND(DATA_LENGTH/1024/1024,2)) AS total_size_mb FROM information_schema.tables WHERE ENGINE LIKE 'innodb' GROUP BY table_schema;
```

As a rule of thumb, if you add those numbers and round up to the nearest GB, that is a good number to aim for. Be mindful of your available memory, and if in doubt, increase this value slowly.

```eval_rst
  .. title:: All About Percona
  .. meta::
     :title: All About Percona | UKFast Documentation
     :description: A guide to using Percona and its settings
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, Shopware, Percona, eCommerce
```
