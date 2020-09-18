# How to install and configure Redis on Wordpress

This article will discuss how to install the utilise Redis on Wordpress using the W3TotalCache Plugin. Redis is a high performance in-memory data storage platform that can significantly boost the performance of any Wordpress site. We would reccomend that if you are running Wordpress, you look into using Redis where possible and here we outline one such method for achiving this using the plugin W3TotalCache.

## Installing Redis

Firstly, you will need to ensure that Redis is installed on your server. For the purposes of this guide, we can install a basic single instance of Redis like so:

### Installing Redis on CentOS 7

Log into the server using SSH and run the following command:

```bash
$ sudo yum install epel-release
$ sudo yum install redis
```

After installing this, you need to ensure that the application is started

```bash
$ sudo systemctl enable --now redis
```

### Installing Redis on Ubuntu 18 / Ubuntu 20 /Debian 9

```bash
$ sudo apt update
$ sudo apt install redis-server
```

### Testing Redis

```bash
$ redis-cli
127.0.0.1:6379> ping
```

The server should respond "PONG"

### Installing the PHP Redis Module


## Configuring Redis

Open the file: /etc/redis/redis.conf in your prefered text editor:

```bash
$ sudo nano /etc/redis/redis.conf
```

Once open, add the following text to the bottom of the file:

```bash
maxmemory 2048mb
maxmemory-policy allkeys-lru
```

If your server has less than 4GB of RAM, you need to set this to 50% of the avalible memory or consider adding more RAM to your server.

## Configuring WordPress

You need to install W3 Total Cache to be able to utilise the Redis instance running on your server. To install this, you can add this in like any other plugin.

To get started, you need to log into your Wordpress Admin page, this is usually located at https://example.com/wp-admin.php . From here, you need to navigate to Plugins -> Add New

Once this is installed, you need to go to the File Manager for the site to edit the db-config.php file. You can edit this file either via FTP, SFTP or using the inbuilt file manager in your cPanel / Plesk installation if you have one.

The db-config.php file should now be located in the following directory:

```bash
[WORDPRESS LOCATION]/wp-content/plugins/w3-total-cache/db-config.php
```

In this file, you need to add the following text:

```bash
//
// redis config cache
//
define( 'W3TC_CONFIG_CACHE_ENGINE', 'redis');
define( 'W3TC_CONFIG_CACHE_REDIS_SERVERS', '127.0.0.1::6379' );

// optional redis settings
define( 'W3TC_CONFIG_CACHE_REDIS_PERSISTENT', true );
define( 'W3TC_CONFIG_CACHE_REDIS_DBID', 0 );
define( 'W3TC_CONFIG_CACHE_REDIS_PASSWORD', '' );
```