# Redis

Magento 1 has been around for a while now and is one of the most frequently used eCommerce platforms on the Web. This means different techniques for increasing performance have been tested and several have come out as no brainers in terms of their benefit in relation to the effort required to get it up and running.

Magento out of the box stores its cache data on the file system, this works OK for small low traffic sites but once your catalog and visitor base grows this can quickly become a bottleneck.

Using Redis for your cache and session data is one of those no brainers that a lot of the community would recommend. Magento supports many different caching mechanisms with the most widely used being APC or Memcached. Redis however has one main advantage over these methods and that is the ability to support tagging. Redis is a high performance scalable key value store that is easy to integrate with the Magento application.

Using APC/Memcached if data is edited in the backend of Magento will need to invalidate certain cache data related to this. This data is identified by tags and with these methods not supporting tagging, Magento will need to check through all files in the cache directory to find these entries. With a couple of thousand products which is not out of the norm, this folder can contain thousands of files and hundreds of megabytes of data or more. With Redis, Magento can pass the tag and only data related to that tag will be returned making it a lot more efficient.

At UKFast on our Magento optimised hosting platforms we configure three different instances of Redis running on different ports:

```bash
~]$ ps awux | grep redis
redis    16693  0.2  0.1 159584 12448 ?        Ssl  Jul01  51:41 /usr/bin/redis-server 127.0.0.1:6380
redis    16752  0.1  0.2 163168 16508 ?        Ssl  Jul01  48:10 /usr/bin/redis-server 127.0.0.1:6381
redis    16810  0.1  0.1 153952  8284 ?        Ssl  Jul01  48:47 /usr/bin/redis-server 127.0.0.1:6379
```

This is beneficial for the following reasons;

- Redis maxmemory is configurable per instance meaning certain data can over utilise this and leave insufficient space for other data such as cache. With separate instances this can be configured per instance to allow more flexibility.<br>
- Statistics are stored globally meaning this would be unhelpful if this encompasses all data.<br>
- Configurations are usually per instance rather than per database making it inflexible if all data is in the same instance.<br>
- Redis is single threaded meaning performance peaks when one core is fully utilised. With multiple instances this is less of an issue.

To integrate Redis with Magento there is two key components, the Redis service running on the server itself and the Redis extension that allows Magento/PHP to communicate correctly with the Redis service.

UKFast will install and configure your Redis instances so you can begin enabling this in Magento as soon as you are ready.

The Magento Redis modules for cache and session data were originally community projects from Colin Mollenhour until they were integrated as part of the core code in the following versions;

Cm_RedisSession<br>
Magento CE – 1.8.0<br>
Magento EE – 1.13.1

Cm_Cache_Backend_Redis<br>
Magento CE – 1.8.0<br>
Magento EE – 1.13.1

The Repositories for these modules can be found here along with installation details for older versions of Magento

Cm_RedisSession - [https://github.com/colinmollenhour/Cm_RedisSession](https://github.com/colinmollenhour/Cm_RedisSession)<br>
Cm_Cache_Backend_Redis - [https://github.com/colinmollenhour/Cm_Cache_Backend_Redis](https://github.com/colinmollenhour/Cm_Cache_Backend_Redis)

### Using Redis for Session Data

In order to utilise Redis for session data storage you must first enable the Cm_RedisSession module. This is one of the most common mistakes we come across with clients trying to configure Magento sessions with Redis. Since this is not required when configuring the cache it is often overlooked. To enable this open the following file

app/etc/modules/CM_RedisSession.xml

In this file change the value from “false” to “true” as below;

```bash
<config>
  <modules>
    <Cm_RedisSession>
      <active>true</active>
      <codePool>community</codePool>
    </Cm_RedisSession>
  </modules>
</config>
```

Along with this you then need to configure Magento to utilise Redis in your app/etc/local.xml file. Below is an example configuration that can be used;

```bash
<!-- example of redis session storage -->
        <session_save>db</session_save>
        <redis_session>
            <host>127.0.0.1</host>
            <port>6379</port>
            <password></password>
            <timeout>2.5</timeout>
            <persistent></persistent>
            <db>0</db>
            <compression_threshold>2048</compression_threshold>
            <compression_lib>gzip</compression_lib>
            <log_level>1</log_level>
            <max_concurrency>6</max_concurrency>
            <break_after_frontend>5</break_after_frontend>
            <break_after_adminhtml>30</break_after_adminhtml>
            <first_lifetime>600</first_lifetime>
            <bot_first_lifetime>60</bot_first_lifetime>
            <bot_lifetime>7200</bot_lifetime>
            <disable_locking>0</disable_locking>
            <min_lifetime>60</min_lifetime>
            <max_lifetime>2592000</max_lifetime>
        </redis_session>
```

If you are carrying out this change on a production website you may wish to migrate your existing session data over to Redis to prevent customers experiencing disruption such as being logged out or having their basket emptied.

Colin Mollenhours repository also provides scripts to enable you to do this.  Depending on whether you was previously using files or database to store sessions you can follow the steps below.

#### Files to Redis

```bash
(in Magento document root folder)
~]$ touch maintenance.flag
~]$ wget https://raw2.github.com/colinmollenhour/Cm_RedisSession/master/migrateSessions.php
~]$ php migrateSessions.php -y
~]$ rm maintenance.flag
```

#### Database to Redis

```bash
(in Magento document root folder)
~]$ touch maintenance.flag
~]$ wget https://raw2.github.com/colinmollenhour/Cm_RedisSession/master/migrateSessions_mysql_redis.php
~]$ php migrateSessions_mysql_redis.php -y
~]$ rm maintenance.flag
```

Once sessions have been Migrated (or before if you don’t mind losing session data) you can test if Magento is now utilising Redis by clearing out your (docroot)/var/session directory (or core_session if db was previously used) and browsing the site then ensuring this directory remains empty. Another way to check is to actually monitor the data in Redis using the following command;

```bash
~]$ redis-cli -h 127.0.0.1 -p 6379 monitor
```

This will show the data being pulled through to the Redis instance.

### Redis for Cache Data

Utilising Redis for cache data does not require the enabling of a module as above. This can simply be enabled by adding the configuration to your app/etc/local.xml file. See example below

```bash
<!-- example of redis cache -->
        <cache>
          <backend>Cm_Cache_Backend_Redis</backend>
          <backend_options>
            <server>127.0.0.1</server>
            <port>6380</port>
            <persistent></persistent>
            <database>0</database>
            <password></password>
            <force_standalone>0</force_standalone>
            <connect_retries>1</connect_retries>
            <read_timeout>10</read_timeout>
            <automatic_cleaning_factor>0</automatic_cleaning_factor>
            <compress_data>1</compress_data>
            <compress_tags>1</compress_tags>
            <compress_threshold>20480</compress_threshold>
            <compression_lib>gzip</compression_lib>
            <use_lua>0</use_lua>
          </backend_options>
        </cache>
```

For versions of Magento before 1.8.0 (CE) where the Cm_Cache_Backend_Redis module has been installed replace the following line

```bash
<backend>CACHE_BACKEND_CLASS_NAME</backend>
With
<backend>Cm_Cache_Backend_Redis</backend>
 ```
For Magento (CE) versions 1.8.0 and (EE) 1.13.0 replace the following line

```bash
<backend>CACHE_BACKEND_CLASS_NAME</backend>
With
<backend>Mage_Cache_Backend_Redis</backend>
```

Once this has been added you should be able to clear the (document root)/var/cache/ directory and browse to the site and this folder should remain empty. Another way to check as above is to actually monitor the data in Redis using the following command;

```bash
~]$ redis-cli -h 127.0.0.1 -p 6380 monitor
```

This will show the data being pulled through to the Redis instance.

### Using Redis for Full Page Cache Data (EE)

As above, the following configuration can be added to the app/etc/local.xml file, again adding the backend class name as above. See example below

```bash
<!-- example of redis Magento Enterprise FPC -->
        <full_page_cache>
          <backend>Cm_Cache_Backend_Redis</backend>
          <backend_options>
            <server>127.0.0.1</server>
            <port>6381</port>
            <persistent></persistent>
            <database>1</database>
            <password></password>
            <force_standalone>0</force_standalone>
            <connect_retries>1</connect_retries>
            <lifetimelimit>57600</lifetimelimit>
            <compress_data>0</compress_data>
          </backend_options>
        </full_page_cache>
```

When this is enabled you can clear the (document root)/var/full_page_cache directory and browse to the site and this folder should remain empty. Another way to check as above is to actually monitor the data in Redis using the following command;

```bash
~]$ redis-cli -h 127.0.0.1 -p 6381 monitor
```

This will show the data being pulled through to the Redis instance.

### Cleaning out old Cache Tags

It is recommended to clear out old cache tags if the cache is cleared infrequently. This can be done using the garbage collection script provided by Colin Mollenhour. An example of this can be found below

```bash
<?php PHP_SAPI == 'cli' or die('<h1>:P</h1>');
ini_set('memory_limit','1024M');
set_time_limit(0);
error_reporting(E_ALL | E_STRICT);
require_once '../app/Mage.php';
Mage::app()->getCache()->getBackend()->clean('old');
// uncomment this for Magento Enterprise Edition
// Enterprise_PageCache_Model_Cache::getCacheInstance()->getFrontend()->getBackend()->clean('old');
```

We would recommend adding this to the shell folder and configuring a cron to run daily.

### Redis Service
You can find more information on the Redis service [here](/operatingsystems/linux/redis/redis)

```eval_rst
  .. title:: Magento 1 IP Restrict File/Folder
  .. meta::
     :title: Magento 1 IP Restrict File/Folder | UKFast Documentation
     :description: A guide to IP restrict a file or folder within Nginx
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, security, eCommerce

