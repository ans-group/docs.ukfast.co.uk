# Redis

### Install Redis

Redis can be installed from the Remi YUM repository with the following command:

```bash
yum install redis --enablerepo=remi
```

### Updating Redis

Redis can be updated with the following command:

```bash
yum update redis --enablerepo=remi
```

### Version Check

You can check the installed version of Redis with the command:

```bash
rpm -qa | grep redis
```

```console
redis-5.0.5-1.el7.remi.x86_64
```

### Install Multiple Instances

The following script will install an additional instances of Redis. Simply define the `REDISINSTANCE` number and the desired `REDISPORT` in the script. The below example uses:

```bash
REDISINSTANCE="3"
REDISPORT="6382"
```

#### Redis Creation Script

Simply define the `REDISINSTANCE` number and the desired `REDISPORT` before running this script:

```bash
cat > /tmp/redis-add.sh
```

Copy and paste this into the terminal, and then press `ctrl+d`:

```bash
#!/bin/bash
########## First run creates Redis2 and second run creates redis3

if [[ -f /etc/redis.conf ]]
then
    echo "File /etc/redis.conf not found, please review"
    exit 1
fi

REDISINSTANCE="3"
REDISPORT="6382"

if [[ ! -f /etc/redis${REDISINSTANCE}.conf ]]
then
    echo "File /etc/redis${REDISINSTANCE}.conf already exists, please review"
    exit 1
fi

cp -a /etc/redis.conf /etc/redis${REDISINSTANCE}.conf
mkdir /var/lib/redis${REDISINSTANCE}
chown -R redis: /var/lib/redis${REDISINSTANCE}
touch /var/log/redis/redis${REDISINSTANCE}.log
chown redis: /var/log/redis/redis${REDISINSTANCE}.log
sed -i "s/redis.pid/redis${REDISINSTANCE}.pid/g" /etc/redis${REDISINSTANCE}.conf
sed -i "s/redis.log/redis${REDISINSTANCE}.log/g" /etc/redis${REDISINSTANCE}.conf
sed -i "s#dir /var/lib/redis#dir /var/lib/redis${REDISINSTANCE}#g" /etc/redis${REDISINSTANCE}.conf
sed -i "s/port 6379/port ${REDISPORT}/g" /etc/redis${REDISINSTANCE}.conf
sed -i "s/redis.sock/redis${REDISINSTANCE}.sock/g" /etc/redis${REDISINSTANCE}.conf

if [[ "`grep "release 7" /etc/redhat-release`" =~ "release 7" ]]
then
    cp -a /usr/lib/systemd/system/redis.service /usr/lib/systemd/system/redis${REDISINSTANCE}.service
    sed -i "s/redis.conf/redis${REDISINSTANCE}.conf/g" /usr/lib/systemd/system/redis${REDISINSTANCE}.service
    sed -i "s/redis-shutdown/redis${REDISINSTANCE}-shutdown/g" /usr/lib/systemd/system/redis${REDISINSTANCE}.service
    cp -a /usr/libexec/redis-shutdown /usr/libexec/redis${REDISINSTANCE}-shutdown
    sed -i "s/SERVICE_NAME=redis/SERVICE_NAME=redis${REDISINSTANCE}/" /usr/libexec/redis${REDISINSTANCE}-shutdown
    sed -i "s/6379/${REDISPORT}/" /usr/libexec/redis${REDISINSTANCE}-shutdown
    systemctl start redis${REDISINSTANCE}.service
    systemctl enable redis${REDISINSTANCE}.service
else
    cp -a /etc/init.d/redis /etc/init.d/redis${REDISINSTANCE}
    sed -i "s/redis.pid/redis${REDISINSTANCE}.pid/g" /etc/init.d/redis${REDISINSTANCE}
    sed -i "s/redis.conf/redis${REDISINSTANCE}.conf/g" /etc/init.d/redis${REDISINSTANCE}
    sed -i "s/redis-shutdown/redis-shutdown redis${REDISINSTANCE}/g" /etc/init.d/redis${REDISINSTANCE}
    service redis${REDISINSTANCE} start
    chkconfig redis${REDISINSTANCE} on
fi
```

#### Run Redis Creation Script Again

Run twice if you want two additional instances (`redis2` and `redi3`)

```bash
sh /tmp/redis-add.sh
```

### Check Running Instances

```bash
ps awux | grep redis
```

```console
redis    24372  0.2  0.0 153952  2644 ?        Ssl  15:37   0:00 /usr/bin/redis-server 127.0.0.1:6381
redis    24645  0.2  0.0 153952  2820 ?        Ssl  15:40   0:00 /usr/bin/redis-server 127.0.0.1:6379
```

### Disable Snapshotting

Unless you need to preserve session / cache information we recommend you disable Snapshotting to reduce I/O. Comment out everything under `SNAPSHOTTING` in `redis.conf`. Typically the following:

```bash
#save 900 1
#save 300 10
#save 60 10000

#dbfilename dump.rdb

#dir /var/lib/redis/
```

### Enable asynchronous deletion

If you wish to enable asynchronous deletion for performance tuning, you can add the below into your `redis.conf`:

```bash
lazyfree-lazy-eviction yes
lazyfree-lazy-expire yes
lazyfree-lazy-server-del yes
replica-lazy-flush yes
```

On Redis 6.x or later, you can also add the below:

```bash
lazyfree-lazy-user-del yes
```

#### Truncate Redis Database

Remove or truncate any existing `dump.rdb` files:

```bash
> /var/lib/redis/dump.rdb
> /var/lib/redis/dump2.rdb
> /var/lib/redis/dump3.rdb
```

### OS Settings

Redis recommends the following OS settings:

```bash
sysctl  vm.overcommit_memory=1
sysctl -w net.core.somaxconn=65535
echo never > /sys/kernel/mm/transparent_hugepage/enabled
```

#### OS Settings on Startup

```bash
chmod +x /etc/rc.d/rc.local
echo "vm.overcommit_memory=1" >> /etc/sysctl.conf
echo "net.core.somaxconn=65535" >> /etc/sysctl.conf
echo "echo never > /sys/kernel/mm/transparent_hugepage/enabled"  >> /etc/rc.d/rc.local
```

### Redis Status

You can run the following command to see the status of a Redis instance. This includes version number, memory usage plus information on the databases:

```bash
redis-cli -h 127.0.0.1 -p 6379 info
```

### Flush Single Database

To flush a single database. define the database number with `-n` and run the command `flushdb`:

```bash
redis-cli -h 127.0.0.1 -p 6379 -n 0 flushdb
```

### Flush All Databases

```bash
redis-cli -h 127.0.0.1 -p 6379 flushall
```

### Monitor Redis

You can review the information to and from Redis with the monitor command:

```bash
redis-cli -h 127.0.0.1 -p 6379 monitor
```

```eval_rst
  .. title:: Redis
  .. meta::
     :title: Redis | UKFast Documentation
     :description: A guide to using Redis
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Shopware, Magento, Magento2, Redis, eCommerce
```
