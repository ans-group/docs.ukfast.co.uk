# Redis

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

You can find more information on the Redis service [here](https://docs.ukfast.co.uk/operatingsystems/linux/redis/redis.html)

```eval_rst
  .. meta::
     :title: Shopware Redis | UKFast Documentation
     :description: A guide to using Redis on our Shopware optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Shopware, Redis, eCommerce

