## Remote database server
This article discusses how to setup a remote database server and allow access from a seperate Web Server(s). This assumes that you have a split role solution with a separate server that performs the web role and a dedicated server that performs the database roles.

```eval_rst
.. note::

   For split role solutions, we recommend to have a dedicated Firewall to avoid bandwidth constraints between your web and database servers. Please use the internal IP address to connect between servers when a dedicated firewall is in place.

```

### Confirm Connection between Servers

From the web server, confirm ping works to the database server via SSH:

```bash
    $ ping <ip.of.db.server>
```
If ping resolves, you will get a response like this:

```bash
    PING 8.8.8.8 ( 8.8.8.8 ) 56(84) bytes of data.
    64 bytes from  8.8.8.8: icmp_seq=1 ttl=57 time=0.462 ms
    64 bytes from  8.8.8.8: icmp_seq=2 ttl=57 time=0.553 ms
```

Again, from the webserver, confirm that you can connect to the database server over the MySQL port:

```bash
    $ telnet <ip.of.db.server> 3306
```

### Create Database User

On the database server, we will create a mysql user with the required grants to access the database:

```sql
    MariaDB [(none)]> GRANT ALL ON db_name.* TO 'db_user'@'%' IDENTIFIED BY 'db_user-password';
```

```sql
    MariaDB [(none)]> FLUSH PRIVILEGES;
    Query OK, 0 rows affected (0.003 sec)
```

Check the user is created:

```sql
    MariaDB [(none)]> SELECT user,host from mysql.user;
    +-------------+---------------+
    | user        | host          |
    +-------------+---------------+
    | db_user     | %             |
    | root        | 127.0.0.1     |
    | root        | ::1           |
    |             | localhost     |
    | root        | localhost     |
    +-------------+---------------+
    5 rows in set (0.00 sec)
```

### Access Database

Now we have confirmed that the servers can communicate over the MySQL port and have created a user with access from all hosts, we will now test the remote connection. From the web server attempt to log in while passing the hosts flag. You will need the MySQL/MariaDB client installed on the webserver in order to run the following from SSH:

```bash
    $ mysql -u db_user -h <ip.of.db.server> -p
    Enter password:
```

When logged in to the database, confirm the user is able to see the database

```sql
    MariaDB [(none)]> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | db_name            |
    +--------------------+
    2 rows in set (0.00 sec)
```

### Update the Application

Now we have a user able to connect to the database, update your application to start using this user and the remote servers IP address.

WordPress:

Edit the wp-config.php file stored in the websites document root,

```bash
    $ vi /<wp-doc-root>/wp-config.php
```

Update the following values and restart the web service:

```bash
    /**  Username */
    define( 'DB_USER', 'db_user' );

    /** Password */
    define( 'DB_PASSWORD', 'db_user-password' );

    /** Hostname */
    define( 'DB_HOST', '<ip.of.db.server>' );
```

Magento:
Edit the wp-config.php file stored in the websites document root,

```bash
    $ vi /<magento-doc-root>/app/etc/env.php
```

Update the following values and restart the web service:

```bash
    'db' =>
    array (
        'table_prefix' => '',
        'connection' =>
        array (
        'default' =>
        array (
            'host' => '<ip.of.db.server>',
            'dbname' => 'db_name',
            'username' => 'db_user',
            'password' => 'db_user-password',
            'active' => '1',
        ),
        ),
    ),
```

PHP:

```php
    <?php
    //Connect To Database
    $hostname='<ip.of.db.server>';
    $username='db_user';
    $password='db_user_password';

    // Create connection
    $conn = new mysqli($servername, $username, $password);

    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";
    ?>
```

```eval_rst
  .. title::  Set up remote access to MySQL
  .. meta::
     :title: Set up remote access to MySQl | UKFast Documentation
     :description: Set up remote access to MySQL between a split role web server and database server, ensuring the application is aware of the new changes.
     :keywords: ukfast, mysql, sql, db, dbserver, webserver, application, remote, connection
```
