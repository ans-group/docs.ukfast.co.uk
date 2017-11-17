# Creating Databases and Users

The commands below need to be used in the MySQL command line. You can create remote users too, by using an IP address instead of using `user@localhost`.

```sql
  CREATE DATABASE dbname;
  CREATE USER dbuser@00.00.00.00;
  SET PASSWORD FOR dbuser@00.00.00.00= PASSWORD("password");
  GRANT ALL PRIVILEGES ON dbname.* TO dbuser@00.00.00.00 IDENTIFIED BY 'password';
  FLUSH PRIVILEGES;
```

```eval_rst
  .. meta::
     :title: Creating database users in Linux | UKFast Documentation
     :description: A guide to creating database users in Linux
     :keywords: ukfast, mysql, database, users, add, create, sql, server, virtual
