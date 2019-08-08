# Magento 2 Varnish

## Install Varnish

### Configuration Test

#### Start Varnish

## Health Check

## Generate VCL

## Memory Limit

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


