# RabbitMQ

### Install RabbitMQ
RabbitMQ is available from the rabbitmq_rabbitmq-server repository, this repository can be installed with the following command:
```bash
curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash
```

You also need the rabbitmq_erlang repository so you can install erlang:

```bash
curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash
```

RabbitMQ erlang can then be installed with the command:
```bash
~]# yum install rabbitmq-server erlang --enablerepo=rabbitmq_erlang,rabbitmq_rabbitmq-server
```

##### Start On Boot
You can enable rabbitmq-server on boot after installing it with this command:

```bash
~]# systemctl enable rabbitmq-server
```

```eval_rst
  .. meta::
     :title: Magento RabbitMQ | UKFast Documentation
     :description: A guide to using RabbitMQ on our Magento optimised stacks
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, RabbitMQ

