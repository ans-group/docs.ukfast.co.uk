# Migrate Your Databases

In this article, we discuss how to successfully migrate a MySQL/MariaDB database between servers. This can be achieved in a few easy steps and can be a relatively quick process depending on the size of the database(s) are being transferred.

### Prereqesuites
* Ensure the same version of MySQL is installed on both servers.
* Ensure there is enough free space for the size of the database on both servers.
    * To find out the size of each database use the following query:
    ```sql
        SELECT table_schema AS "Database",
        ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS "Size (MB)"
        FROM information_schema.TABLES
        GROUP BY table_schema;
    ```

### Create a database dump

On the current databases server, run the relative commands via `SSH`. Depending on how large the database(s) is, it may take a short while to complete.

For a single database :

```bash
    $ mysqldump --events --routines --triggers --single-transaction dbname > dbname
```

For all/multiple databases, the below commands will split the individual databases into seperate files in the mysqldumps directory:

```bash
    $ mkdir /root/mysqldumps
```
```bash
    $ for i in $(mysql -NBe 'show databases' | grep -v 'performance_schema')
    do mysqldump --force --events --routines --single-transaction --triggers $i > /root/mysqldumps/$i
    done
```

### Transfer the dump

When the database dump is complete, its time to transfer the file(s) to the alternate server. This example uses scp to securely copy the files and directories between remote hosts without using an FTP client. For servers behind the same dedicated firewall, use the internal IP address of the remote server.

For a single database :

```bash
    $ scp -v -P <ssh-port> dbname root@ip.ip.ip.ip:~/dbname
```

For multiple databases :

```bash
    $ scp -vr  -P <ssh-port> /root/mysqldumps root@ip.ip.ip.ip:mysqldumps
```

Check that the files transferred as expected on the remote host :

```bash
    $ ll /root/mysqldumps/
```
```bash
total 2068
-rw-r--r-- 1 root root    2107 Jul 10 17:25 example1
-rw-r--r-- 1 root root  533999 Jul 10 17:25 example2
-rw-r--r-- 1 root root    2372 Jul 10 17:25 example3
-rw-r--r-- 1 root root 1033415 Jul 10 17:25 information_schema
-rw-r--r-- 1 root root  515484 Jul 10 17:25 mysql
-rw-r--r-- 1 root root    2247 Jul 10 17:25 example4
```

### Before the Import

Before the import, first ensure the files do not contain `USE` or `CREATE DATABASE` statments as this can cause unexpected outcomes.

Use the following grep command to check, if blank, move on to import your database:
```bash
  $ egrep "^USE|^CREATE DATABASE" example1
  CREATE DATABASE /*!32312 IF NOT EXISTS*/ `example1` /*!40100 DEFAULT CHARACTER SET latin1 */;
  USE `example1`;
```

Theses lines can be deleted manually, or by using the following sed commands:
```bash
  $ sed -i '/^USE/d' example1
  $ sed -i '/^CREATE DATABASE/d' example1
```
### Import your database

Now the files are transferred, it's time to to perform the import. If there is an existing database of that name there will be conflicts and you may wish to rename the conflicting database.

For a single database :

```sql
   MariaDB [(none)]> CREATE DATABASE example1;
```

To import the database, run the following command:

```bash
  $ mysql -u root -p example1 < example1
  Enter password:
```

For multiple databases :

```bash
    $ for i in $(ls /root/mysqldumps);
    do mysql -e "CREATE DATABASE $i" && mysql -u root -p $i < /root/mysqldumps/$i;
    done
```

```eval_rst
  .. title:: Migrate your database
  .. meta::
     :title: Migrate your database | UKFast Documentation
     :description: A guide to migrating one or more databases from an existing database server to a remote one.
     :keywords: ukfast, linux, mysql, database, backup, dump, migrate, recovery, security, cloud, import, sql, mysqldump, scp, transfer, migration