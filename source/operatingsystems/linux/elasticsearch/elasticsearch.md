# Elasticsearch

### Install Elasticsearch
#### Install Java
You first need to install Java which is required by Elasticsearch

```bash
yum install java
```
#### Elasticsearch Repository Setup

Create a file called `elasticsearch.repo` in the `/etc/yum.repos.d/` directory and include the below.

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

If you need to install Elasticsearch `7.x`, then copy the below into `/etc/yum.repos.d/elasticsearch.repo` instead.

```bash
vim /etc/yum.repos.d/elasticsearch.repo

[elasticsearch-7.x]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
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
##### Elasticsearch 7.6.x

If you require Elasticsearch `7.6` specifically you will need to install with the below command

```bash
yum install https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.2-x86_64.rpm
```

###### Start On Boot

Once installed you can configure Elasticsearch to start on boot with the command:

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
In order to change the listen IP address for Elasticsearch you need to configure `network.host` in `/etc/elasticsearch/elasticsearch.yml`

```bash
vim /etc/elasticsearch/elasticsearch.yml

network.host: 10.0.0.17
```

The Elasticsearch service will need a restart after this change.

### Memory Limit/Heap Size
As of Elasticsearch version 7, the default memory allocation is no longer 2GB. The service will make assumptions based on total memory and can potentially set the heap size as high as 32GB, which can cause "Out of Memory" issues if left unchanged. We recommend that you set this to 2GB in `/etc/elasticsearch/jvm.options`

```bash
vim /etc/elasticsearch/jvm.options

 -Xms2g
 -Xmx2g

```

The Elasticsearch service will need a restart after this change.

```bash

systemctl restart elasticsearch.service

```

### Multiple Magento installations using one Elasticsearch instance
When you have more than one site using a single instance of Elasticsearch, production and staging environments for example, you will need to bear this in mind when configuring Elasticsearch in the Magento admin. You need to specify a unique value in the Elasticsearch `Index Prefix` for each installation. This is set in the Magento admin panel when configuring Elasticsearch. If you do not set a unique value, you may face issues, such as the catalog search not working, or products not showing.

```eval_rst
  .. title:: Elasticsearch
  .. meta::
     :title: Elasticsearch | UKFast Documentation
     :description: guides relating to using Elasticsearch
     :keywords: ukfast, Magento, Magento2, Shopware, optimised, stack, Elasticsearch, eCommerce
```
