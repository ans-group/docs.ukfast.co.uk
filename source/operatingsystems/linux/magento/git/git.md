# Git

### Install Git
You can install git with the following command:

```bash
~]# yum install git
```

#### Updating Git
You can update git with the following command:

```bash
~]# yum update git
```

#### Version Check
You can check the version of git installed with the following command:

```bash
~]# git --version
git version 1.8.3.1
```
### Change Port
IF the server has port 2020 defined as the default outbound SSH port:

```bash
~]# grep Port /etc/ssh/ssh_config
   Port 2020
```

You will need to add a hostmatch to change the port to the file /etc/ssh/ssh_config:

```bash
Host github.com
    HostName github.com
    Port 22
```


```eval_rst
  .. meta::
     :title: Magento Git | UKFast Documentation
     :description: A guide to using Git on our Magento optimised stacks
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, git

