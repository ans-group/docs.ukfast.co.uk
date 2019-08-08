# Magento 2 Varnish

## Install Varnish

### Configuration Test
It's very important to run a configuration test before starting/restarting the Varnish service. You can run a configruation test with the following command:
```bash
~]# varnishd -C -f /etc/varnish/default.vcl
```
A susceeful output from this command will be the VCL displayed  on the terminal with no error message.
#### Start Varnish
You can start the Varnish service with the following command:
```bash
~]# systemctl start varnish
```
## Health Check

## Generate VCL

## Memory Limit

## Version Check
You can see the version of Varnish installed with the following command:
```bash
~]# varnishd -V
varnishd (varnish-4.1.11 revision 61367ed17d08a9ef80a2d42dc84caef79cdeee7a)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2019 Varnish Software AS
```

## Pipe timeout
pipe_timeout is set to 60 seconds by default. This can cause time out issues when running exports in the Magento admin interface. You can increase this by adding the option:

-p pipe_timeout=600

Within the DAEMON_OPTS sections in the file /etc/varnish/varnish.params. You need to restart Varnish for this setting to take affect.

## SSL Termination
Varnish does not support SSL-encrypted traffic, therefore we use Nginx for SSL termination.



```eval_rst
  .. meta::
     :title: Magento 2 Varnish | UKFast Documentation
     :description: A guide using Varnish with Magento 2
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, varnish


