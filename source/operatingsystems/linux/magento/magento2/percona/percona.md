# Percona

### Percona Repository
You can install the Percona repoistory with the command:
```bash
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
```

### Install Percona
#### 5.6
```bash
yum install Percona-Server-server-56
```
#### 5.7
```bash
yum install Percona-Server-server-57
```

### Updating Percona
#### 5.6
```bash
yum update Percona-Server-server-56
```
#### 5.7
```bash
yum update Percona-Server-server-57
```

### Enable On Boot
```bash
systemctl enable mysqld
```

### Start Percona
```bash
systemctl start mysqld
```

### Increase max_connections
You can edit the writeable variable max_connections like so:
```sql
set global max_connections = 400;
```

To make the change permenmant you need to change the value in /etc/my.cnf

### ~/.my.cnf (User-specific options)

### Wildcard Grants
This is an example of a wildcard grant to databasename*
```sql
GRANT ALL PRIVILEGES ON `databasename\_%`.* TO 'databaseuser'@'172.18.68.%';
```

### Disalbe Warnings
```sql
mysql> set global log_warnings = 0;
```

### Display Current User
```sql
mysql> select CURRENT_USER();
```

### MySQL Tuner
```bash
wget mysqltuner.pl -O mysqltuner.pl
perl mysqltuner.pl
```


```eval_rst
  .. meta::
     :title: Magento2 Percona | UKFast Documentation
     :description: A guide to using Percona on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, Percona

