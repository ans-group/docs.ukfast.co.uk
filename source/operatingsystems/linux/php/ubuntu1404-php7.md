# Installing PHP 7 on Ubuntu 14.04

## Installation

By default, Ubuntu 14.04 ships with PHP 5.5.9 as the latest available version. If you would like to install PHP 7.x then you will need to do so using additional software repositories. For this guide we will be using [an excellent 3rd party PPA](https://launchpad.net/~ondrej/+archive/ubuntu/php).

First you need to ensure you have the `software-properties-common` package installed:

```bash
apt-get install software-properties-common
```

Then you can add the repository in:

```bash
add-apt-repository ppa:ondrej/php
apt-get update
```

Now you can install PHP 7:

```bash
apt-get install php7.1 php7.1-common php7.1-mysqli php7.1-dev php7.1-mcrypt
```

## Configuration

Configuration files are located in specific directories for the version you installed. In the example above, `7.1` this would be:

```bash
/etc/php/7.1/
```

```eval_rst
  .. title:: Installing PHP 7 on Ubuntu 14.04
  .. meta::
     :title: Installing PHP 7 on Ubuntu 14.04 | UKFast Documentation
     :description: A guide to installing and configuring PHP 7 on Ubuntu 14.04
     :keywords: ukfast, php, install, ubuntu, fpm, guide, tutorial, configuration, cloud
```
