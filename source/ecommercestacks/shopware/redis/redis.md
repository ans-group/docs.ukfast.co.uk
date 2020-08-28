# Redis

### Cache
From Shopware 5.3 it is possible to use [Redis](https://redis.io/) as cache adapter. Add the following to config.php:

```bash
'model' => [
    'redisHost' => '127.0.0.1',
    'redisPort' => 6379,
    'redisDbIndex' => 0,
    'cacheProvider' => 'redis'
],
'cache' => [
    'backend' => 'redis', // e.G auto, apcu, xcache
    'backendOptions' => [
        'servers' => [
            [
                'host' => '127.0.0.1',
                'port' => 6379,
                'dbindex' => 0,
                'redisAuth' => ''
            ],
        ],
    ],
]
```

Be aware, that for Zend_Cache::CLEANING_MODE_ALL the cache implementation will issue "FLUSHDB" and therefore clear the current redis db index. For that reason, the db index for the cache should not be used for persistent data.

### Sessions
You can use Redis for sessions by adding to the config.php file:
```bash
'session' => [
    'save_handler' => 'redis',
    'save_path' => "tcp://127.0.0.1:6379",
],

'backendsession' => [
    'save_handler' => 'redis',
    'save_path' => "tcp://127.0.0.1:6379",
],
```

You may need to change the IP address and you can change the port to run backend sessions and frontend sessions on different instances.

### Redis Service
You can find more information on the Redis service [here](/operatingsystems/linux/redis/redis)

```eval_rst
  .. title:: Shopware Redis
  .. meta::
     :title: Shopware Redis | UKFast Documentation
     :description: A guide to using Redis on our Shopware optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Shopware, Redis, eCommerce

