# MySQL Troubleshooting and Tuning

This guide covers some common and simple tweaks to troubleshoot MySQL - for example dealing with slow queries and improving response times. However please be aware that MySQL is very complex and we strongly recommend further reading.

## Slow Query Logging

The external [Slow Query Log](https://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) is one of the most important troubleshooting tools available if you're seeing performance issues with MySQL. It lets you see a list of all queries which take over a certain time to complete. That can help you diagnose the problem - whether it's a configuration issue, or a particular query which needs optimisation.

To turn on slow logging, log into MySQL and run the following queries:

```sql
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 10;
SET GLOBAL slow_query_log_file = '/my/log/file.log';
```

Once you have enough data, make sure to turn off slow logging again, as there is a small performance cost to having it enabled:

```sql
SET GLOBAL slow_query_log = 'OFF';
```

## Table Locking

Locking is a vital function of SQL, designed to protect your data integrity. By locking a table during a query, SQL is making sure that no other queries can edit that table at the same time, therefore preventing data corruption.

However, locking an entire table during a long-running query and making other queries wait can cause bottlenecks and even timeouts in your application. In MySQL you can look at the process list to determine if you have locking at that moment:

```console
mysql> SHOW FULL PROCESSLIST\G
*************************** 1. row ***************************
     Id: 12121
   User: root
   Host: localhost:41998
     db: database_name
Command: Query
   Time: 132
  State: Locked
   Info: [MySQL query]
```

Alternatively you can look more generally at the total number of locks your system has seen:

```console
mysql> SHOW STATUS LIKE 'Table_locks%';
+-----------------------+---------+
| Variable_name         | Value   |
+-----------------------+---------+
| Table_locks_immediate | 4509    |
| Table_locks_waited    | 156     |
+-----------------------+---------+
```

A generally effective fix is to change your table [storage engine](https://en.wikipedia.org/wiki/Comparison_of_MySQL_database_engines) to one that supports row locking. In the majority of cases, this means changing from [MyISAM](https://dev.mysql.com/doc/refman/5.7/en/myisam-storage-engine.html) to [InnoDB](https://dev.mysql.com/doc/refman/5.7/en/innodb-storage-engine.html). InnoDB helps avoids full table locking, by locking only the row currently being worked on. To see what storage engine your tables are currently using, you can run the following query:

```sql
SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'database_name';
```

For a full guide on the details of converting to InnoDB please do refer to the [official guide](https://dev.mysql.com/doc/refman/5.7/en/converting-tables-to-innodb.html). To convert an existing MyISAM table to InnoDB, you can run the following query:

```sql
ALTER TABLE table_name ENGINE=InnoDB;
```

```eval_rst
.. warning::
    We recommend reading the official guide in full, and testing this conversion before attempting it on your live application. Switching to InnoDB is not a catch-all solution, and there are exceptions. For example, tables which have an ``auto_increment`` column may not behave as you expect.
```

## Buffers and Caches

Reading data from RAM is a few orders of magnitude faster than reading data from disks, even with SSDs. With that in mind, setting up correct buffering and caching to make optimal use of the available memory will give you faster responses from your database. There's no single right way way to set these up as it varies depending on the server and the application, but below are some general recommendations.

```eval_rst
.. warning::
    Adjust these values slowly, and monitor performance over time. Setting these values too high can cause other problems, and at worst can cause your server to become unstable and crash. There's no definitive optimal value, so take your time and tune them for your application, on your server.
```

#### InnoDB Buffer Pool Size

In an ideal world, `innodb_buffer_pool_size` should be slightly larger than the total amount of data you store in InnoDB tables. That means your server can hold the entire dataset in memory, and helps avoid slow disk IO when reading data. In the real world, that's not always possible. You may not have enough RAM, or you don't want to take memory away from your other applications and risk making your server unstable.

To see the total size of your InnoDB tables in MB, you can run the following command:

```sql
SELECT TABLE_SCHEMA, SUM(ROUND(DATA_LENGTH/1024/1024,2)) AS total_size_mb FROM information_schema.tables WHERE ENGINE LIKE 'innodb' GROUP BY table_schema;
```

As a rule of thumb, if you add those numbers and round up to the nearest GB, that is a good number to aim for. Be mindful of your available memory, and if in doubt, increase this value slowly.

#### InnoDB Buffer Pool Instances

The `innodb_buffer_pool_instances` variable was only introduced in MySQL 5.5.4, so if you are using an older version, ignore this section. Otherwise, this should be set to 1 per GB of `innodb_buffer_pool_size`. Please refer to the external [MySQL documentation](https://dev.mysql.com/doc/refman/5.6/en/innodb-multiple-buffer-pools.html) for more information.

## Temp tables writing to disk

During normal operation, MySQL sometimes needs to create temporary tables. Ideally we'd like to keep these in memory, rather than on disk, to avoid slow disk IO. There are two reasons why MySQL uses disk tables instead of memory. Either the table is bigger than our limits, or it uses BLOB or TEXT columns. Adjusting the column types would require application development, so we'll focus on the limits.

To see the total number of temp tables compared to the number of temp tables on disk, run the following query:

```console
mysql> SHOW GLOBAL STATUS LIKE "Created%table";
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| Created_tmp_disk_tables | 44    |
| Created_tmp_tables      | 311   |
+-------------------------+-------+
```

In this case, only 44 out of 311 (or about 14%) tables were created on disk, which isn't bad. As a general rule, the lower the better. The two limits we can adjust to change this are `tmp_table_size` and `max_heap_table_size`. By default these are 16MB, so if you're seeing a high percent of temp tables created on disk it may be worth slowly increasing them in your `my.cnf` configuration file.

```ini
tmp_table_size=32M
max_heap_table_size=32M
```

As a good rule of thumb, increase them to 32M, restart MySQL, then let your server run for 24 hours before checking the number of `created_tmp_disk_tables` again for improvement.

## MySQLTuner

[MySQLTuner](https://github.com/major/MySQLTuner-perl) is an open source Perl project that aims to provide a quick way to review your MySQL install, and makes some general suggestions for performance and stability. Please bear in mind that these are only suggestions. MySQLTuner does not know about your application or your server, so it may not make the best recommendations for you. They give a clear warning, which we will repeat here:

```eval_rst
.. warning::
    It is extremely important for you to fully understand each change you make to a MySQL database server. If you don't understand portions of the script's output, or if you don't understand the recommendations, you should consult a knowledgeable Database Administrator (DBA) or System Administrator that you trust. Always test your changes on staging environments, and always keep in mind that improvements in one area can negatively affect MySQL in other areas.
```

With that warning in mind, it is a useful tool for seeing a wide range of performance metrics quickly. If you wish to run it on your server, you can, via SSH:

```console
wget http://mysqltuner.pl/ -O mysqltuner.pl
wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/basic_passwords.txt -O basic_passwords.txt
wget https://raw.githubusercontent.com/major/MySQLTuner-perl/master/vulnerabilities.csv -O vulnerabilities.csv
perl mysqltuner.pl
```

## Percona Wizard

Percona offer [Configuration Wizard](https://tools.percona.com/wizard), which also aims to help you review and optimise your MySQL performance. The same warnings apply here as with MySQLTuner. While it may help with the most common issues and configurations, it is no substitute for an experienced DBA who can optimise for your applications.


## References and further external reading

* [The official MySQL documentation](https://dev.mysql.com/doc/)
* [Use The Index, Luke: A guide to database performance for developers](https://use-the-index-luke.com/)
* [O'Reilly: SQL Tuning](http://books.google.com/books?id=pKXF7UU0gBYC&printsec=frontcover&dq=sql%2Btuning)
* [SQL Performance Tuning](http://books.google.com/books?id=3H9CC54qYeEC&dq=sql+performance+tuning&printsec=frontcover&source=bn&hl=en&ei=1dDoSYmjMOrlnQfX-bSYBw&sa=X&oi=book_result&ct=result&resnum=4)
* [<nospell>MySQLTuner-perl</nospell> on GitHub](https://github.com/major/MySQLTuner-perl)

```eval_rst
  .. title:: MySQL Tuning
  .. meta::
     :title: MySQL Tuning | ANS Documentation
     :description: A guide to the basics of tuning MySQL for web servers
     :keywords: linux, mysql, sql, database, tuning, performance, db, ukfast
```
