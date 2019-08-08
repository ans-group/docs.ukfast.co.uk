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
Varnish does not support SSL-encrypted traffic, therefore we use Nginx for SSL termination. You need to remove the 443 listen from the server block in the Nginx vhosts configruation file and then add a new server block for 443. Example block:

```bash
server {
  server_name example.domain.com;
  listen 10.0.0.17:443 ssl http2;
  ssl_certificate /etc/nginx/ssk/example.domain.com.crt;
  ssl_certificate_key /etc/nginx/ssk/example.domain.com.key;

  access_log /var/log/nginx/example.domain.com-ssl-access.log main buffer=32k flush=300;
  error_log /var/log/nginx/example.domain.com-ssl-error.log;

  location / {
            proxy_pass http://10.0.0.17:80;
            proxy_set_header X-Real-IP  $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto https;
            proxy_set_header X-Forwarded-Port 443;
            proxy_set_header Host $host;
  }
}
```

This block performs an SSL handshake and then sends traffic to port 80 which Varnish should be running on.



```eval_rst
  .. meta::
     :title: Magento 2 Varnish | UKFast Documentation
     :description: A guide using Varnish with Magento 2
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, varnish


