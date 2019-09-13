# Redis

### Install Redis
Redis can be installed from the remi yum repostiroy with the following command:

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
~]# rpm -qa | grep redis
redis-5.0.5-1.el7.remi.x86_64
```

### Install Multiple Instances
#### Create redis-add.sh
```bash
~]# > /tmp/redis-add.sh
#!/bin/bash
########## First run creates Redis2 and second run creates redis3

version=`rpm -qi redis | grep Version | awk '{print $3}'`
versionmajor=`echo $version | cut -d. -f1`
versionminor=`echo $version | cut -d. -f2`
if [ $versionmajor -lt 3 ]; then
        if [ $versionminor -le 6 ]; then
                echo "Redis version is $version. It needs to be version 2.6 or above."
        exit
        fi
fi

if [[ -f /etc/redis2.conf ]]
        then
                REDISINSTANCE="3"
                REDISPORT="6381"
else
        REDISINSTANCE="2"
        REDISPORT="6380"
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

if [[ "`grep "release 7" /etc/redhat-release`" =~ "release 7" ]]; then
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

# File removal
# Create at job to remove this script as a safe guard
echo "rm -f ${PWD}/${0}" | at now + 20 minutes &> /dev/null

# Promt to remove this script or run again
echo -e "\n *** Do you need to run $0 again? y/n ***"
read removeme
if [ $removeme = n ]
  then
    rm -f $0
    echo "File: $0 removed"
  else
    vim $0
fi
```

### Check Running Instances


```eval_rst
  .. meta::
     :title: Magento2 Redis | UKFast Documentation
     :description: A guide to using Redis on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, Redis

