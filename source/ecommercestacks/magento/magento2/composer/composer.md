# Composer

### Install Composer
Composer can be installed from the epel yum repository with the following command:

```bash
~]# yum install composer --enablerepo=epel
```

#### Updating Composer
Composer can be updated with the following command:

```bash
~]# yum update composer --enablerepo=epel
```

#### Version Check
You can check the installed version of Composer with the command:
```bash
~]$ composer  -V
Composer version 1.8.6 2019-06-11 15:03:05
```
```eval_rst
.. warning::
   **Do not run Composer as root/super user!**
```

```eval_rst
  .. meta::
     :title: Magento Composer | UKFast Documentation
     :description: A guide to using Composer on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento2, composer, eCommerce

