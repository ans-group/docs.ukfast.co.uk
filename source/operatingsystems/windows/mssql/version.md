# Finding the version of Microsoft SQL you are running

If you want to find which version of Microsoft SQL and what Service Pack you are running easily, the below query can be utilised.

## Microsoft SQL Server Management Studio

You will need to open up and connect into Microsoft SQL Server Management Studio. the easiest way in Windows 2012 is to click on start and start free-typing ssms

Then Click on New Query and paste the below query which will then present a results window supplying the relevant information:-

![SQL Studio Manager Query](Images/checkversion/ssms_Version2.PNG)  

```SQL
USE master
GO
 
SELECT @@version AS Version,
          SERVERPROPERTY('Edition') As Edition,
          SERVERPROPERTY('ProductVersion') AS Product,
          SERVERPROPERTY('ProductLevel') AS "Service Pack"
GO
```

You can Parse the query to check syntax via the Green tick highlighted in the above screenshot or just Click on `Execute`

![Query Results](Images/checkversion/ssms_Version1.PNG)


Take a copy of the Product results in the query, in this case when searching `13.0.1771.0` Go to the link below either CTRL + F and search for the build number or manually scroll and Search.

### MSSQL build numbers explained
```
https://buildnumbers.wordpress.com/sqlserver/
```

To explain build numbers: Build 13 is the edition which in this case is MSSQL 2016, 00 or 0 indicates that it is a non-r2 build and 17710 is the patch version.

In this example I have a patch installed:

* 13.00.1711.0	2015.130.1711.0	3179258 Processing a partition causes data loss on other partitions after the database is restored in SQL Server 2016 (1200)	August 17, 2016

```eval_rst
  .. title:: Which Microsoft SQL Server version am I on?
  .. meta::
     :title: Which Microsoft SQL Server version am I on? | UKFast Documentation
     :description: How to find which version of Microsoft SQL Server you're running
     :keywords: ukfast, guide, database, mssql, sql, sql server, server, version, find, microsoft
