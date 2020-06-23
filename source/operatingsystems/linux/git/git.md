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
### SSH Port
If the server has port 2020 defined as the default outbound SSH port:

```bash
~]# grep Port /etc/ssh/ssh_config
   Port 2020
```

You will need to add a host name match to change the port to 22 in the file /etc/ssh/ssh_config:

```bash
Host github.com
    HostName github.com
    Port 22
```

This block needs to be added at the top of the file.

#### Firewall
You need to ensure the firewall for the server allows port 22 outbound. This can be done through the MyUKFast portal, you can find more information on this [here](/network/firewalls/)

```eval_rst
  .. title:: Git | UKFast Documentation
  .. meta::
     :title: Git | UKFast Documentation
     :description: A guide to using Git
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, git, eCommerce

