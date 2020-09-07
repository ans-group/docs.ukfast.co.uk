# How to configure Redis with WPTotalCache on Wordpress

This article will discuss how to install the utilise Redis on Wordpress using the W3TotalCache Plugin. Redis is a high performance in-memory data storage platform that can significantly boost the performance of any Wordpress site. We would reccomend that if you are running Wordpress, you look into using Redis where possible and here we outline one such method for achiving this using the plugin W3TotalCache.

## Installing Redis

Firstly, you will need to ensure that Redis is installed on your server. For the purposes of this guide, we can install a basic single instance of Redis like so:

### Installing Redis on CentOS 7

Log into the server using SSH and run the following command to install Redis on CentOS 7:

```bash
$ yum install epel-release
$ yum install redis
```

