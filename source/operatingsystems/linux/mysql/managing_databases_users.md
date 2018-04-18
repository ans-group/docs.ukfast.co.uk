# Managing Databases and Users

This guide outlines some common tasks when it comes to managing your MySQL database and users.

## List all Users

If you need to see all the users currently on your database server, run the following query in MySQL:
```sql
  SELECT host, user, password FROM mysql.user;
```

## Reset a user's password

Run the following query to change a user's password:
 ```sql
  UPDATE mysql.user SET Password = PASSWORD("ChooseAStrongPassword") WHERE User="username" ;
  exit
 ```

## Reset the root user password

Losing your MySQL root password can be a problem. Luckily there is a fairly quick solution to reset the root password with minimal downtime.

Stop MySQL, and start it without 'grant tables' so you can login without the password. Log into MySQL as root:

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
     :title: Managing MySQL database users | UKFast Documentation
     :description: A guide to managing MySQL database users
     :keywords: ukfast, mysql, database, users, add, create, reset, sql, root, password, ukfast
