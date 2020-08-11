# Elasticsearch

### Install Elasticsearch
#### Install Java
You first need to install Java which is required by Elasticsearch

```bash
yum install java
```
#### Elasticsearch Repository Setup
Create a file called elasticsearch.repo in the /etc/yum.repos.d/ directory and include the below. If you wish for ElasticSearch v7 then replace all instances of '6' with 7.

```bash
vim /etc/yum.repos.d/elasticsearch.repo

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
yum install elasticsearch 
```

###### Start On Boot
Once installed you can configure elasticsearch to start on boot with the command:

```bash
systemctl enable elasticsearch
```

### Start Elasticsearch
You can start Elasticsearch with the command:

```bash
systemctl start elasticsearch
```

### Check Elasticsearch is running
Run the following curl command on the server to test Elasticsearch is running:

```bash
curl -X GET "127.0.0.1:9200/?pretty"
{
  "name" : "5qXM9wk",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "sWWOH_oGTuOAQPs8USjiyQ",
  "version" : {
    "number" : "6.8.2",
    "build_flavor" : "default",
    "build_type" : "rpm",
    "build_hash" : "b506955",
    "build_date" : "2019-07-24T15:24:41.545295Z",
    "build_snapshot" : false,
    "lucene_version" : "7.7.0",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

### Bind/Listen IP Address
In order to changfe the listen IP address for elasticsearch you need to configure network.host in /etc/elasticsearch/elasticsearch.yml

```bash
vim /etc/elasticsearch/elasticsearch.yml

network.host: 10.0.0.17
```

The elasticsearch service will need a restart after this change.


 ```eval_rst
.. meta::
   :title: Elasticsearch | UKFast Documentation
   :description: guides relating to using Elasticsearch
   :keywords: ukfast, Magento, Magento2, Shopware, optimised, stack, Elasticsearch, eCommerce
