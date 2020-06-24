# Redis

We have 3 instances of Redis installed and Running on our WooCommerce optimised stack:

```bash
~]# ps awux | grep redis
redis    24372  0.2  0.0 153952  2644 ?        Ssl  15:37   0:00 /usr/bin/redis-server 127.0.0.1:6381
redis    24667  0.2  0.0 153952  2822 ?        Ssl  15:42   0:00 /usr/bin/redis-server 127.0.0.1:6380
redis    24645  0.2  0.0 153952  2820 ?        Ssl  15:40   0:00 /usr/bin/redis-server 127.0.0.1:6379
```

These can be used with any WordPress Redis plugin.

### Redis Service
You can find more information on the Redis service [here](/operatingsystems/linux/redis/redis.html)

```eval_rst
  .. title:: WooCommerce Redis
  .. meta::
     :title: WooCommerce Redis | UKFast Documentation
     :description: A guide to using Redis on our WooCommerce optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, WooCommerce, Redis, eCommerce

