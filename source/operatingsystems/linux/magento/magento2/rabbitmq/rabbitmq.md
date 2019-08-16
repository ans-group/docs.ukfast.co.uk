# RabbitMQ

### Install RabbitMQ
RabbitMQ is available from the rabbitmq_rabbitmq-server repository, this repository can be installed with the following command:
```bash
curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash
```

Varnish 4.1 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish41.epel'
```
##### Start On Boot
You can enable Varnish on boot after installing it with this command:

```bash
~]# systemctl enable varnish
```

```eval_rst
  .. meta::
     :title: Magento RabbitMQ | UKFast Documentation
     :description: A guide to using RabbitMQ on our Magento optimised stacks
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, RabbitMQ

