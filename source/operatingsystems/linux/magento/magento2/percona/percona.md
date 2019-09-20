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

### Disalbe Warnings
```mysql
mysql> set global log_warnings = 0;
```

### Display Current Loggedin User
```mysql
mysql> select CURRENT_USER();
```

### MySQL Tuner


```eval_rst
  .. meta::
     :title: Magento2 Percona | UKFast Documentation
     :description: A guide to using Percona on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, Percona

