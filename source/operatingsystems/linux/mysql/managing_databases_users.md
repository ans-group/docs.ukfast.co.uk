# Managing Databases and Users

## List all Users

If you need to see all the users currently on your database server, run the following query in MySQL:
```sql
  SELECT host, user, password FROM mysql.user;
```

## Reset a users password

Run the following query to change a users password:
 ```sql
  UPDATE mysql.user SET Password = PASSWORD("ChooseAStrongPassword") WHERE User="username" ;
  exit
 ```

## Reset the root user password

If the MySQL root password has been lost or forgotten, it can be a problem. Luckily there is a fairly quick solution to reset the root password with minimal downtime.

Stop MySQL and start it without grant tables so we can log in without the password. Log into MySQL as root:

```console
  service mysql stop
  mysql -u root
```

Run the following query to change the root user password, then exit:
 ```sql  
  UPDATE mysql.user SET Password = PASSWORD("ChooseAStrongPassword") WHERE User="root" ;
  exit
 ```

Stop and restart MySQL:
 ```console
  service mysql stop
  service mysql start
```

Test logging in with the new password:
 ```console
  mysql -u root -p
```

```eval_rst
  .. meta::
     :title: Managing database users in Linux | UKFast Documentation
     :description: A guide to managing database users in Linux
     :keywords: ukfast, mysql, database, users, add, create, reset, sql, root, password
