# Redis

### Magento2 Modules
We recommend you ensure the Magento2 modules are kept up to date, these can be located here:

#### Sessions
```bash
https://github.com/colinmollenhour/Cm_RedisSession
https://github.com/colinmollenhour/credis
```
#### Cache
```bash
https://github.com/colinmollenhour/Cm_Cache_Backend_Redis
```

### Configure Magento2 For Redis
You can use the Magento2 CLI to configure Redis. Please review the below commands before running, you may need to change the host, port and or db values.

#### Sessions
```bash
php bin/magento setup:config:set --session-save=redis --session-save-redis-host=127.0.0.1 --session-save-redis-port=6379 --session-save-redis-log-level=3 --session-save-redis-db=2
```

#### Cache
```bash
php bin/magento setup:config:set --cache-backend=redis --cache-backend-redis-server=127.0.0.1 --cache-backend-redis-port=6380 --cache-backend-redis-db=0
```

#### Page Cache
```bash
php bin/magento setup:config:set --page-cache=redis --page-cache-redis-server=127.0.0.1 --page-cache-redis-port=6381 --page-cache-redis-db=1
```

### Redis Service
You can find more information on the Redis service [here](/operatingsystems/linux/redis/redis.html)

```eval_rst
  .. meta::
     :title: Magento2 Redis | UKFast Documentation
     :description: A guide to using Redis on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, Redis, eCommerce

