# Elasticsearch

### Install Elasticsearch
#### Install Java
You first need to install Java which is required by Elasticsearch

```bash
~]# yum install java
```
#### Elasticsearch Repoistory Setup
Create a file called elasticsearch.repo in the /etc/yum.repos.d/ directory

```bash
~]# vim /etc/yum.repos.d/elasticsearch.repo

[elasticsearch-6.x]
name=Elasticsearch repository for 6.x packages
baseurl=https://artifacts.elastic.co/packages/6.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

##### Install Elasticsearch
```bash
~]# yum install elasticsearch 
```

 ```eval_rst
.. meta::
   :title: Magento Elasticsearch | UKFast Documentation
   :description: guides relating to using Elasticsearch on our Magento2 optimised stack
   :keywords: ukfast, Magento, Magento2, optimised, stack, Elasticsearch
