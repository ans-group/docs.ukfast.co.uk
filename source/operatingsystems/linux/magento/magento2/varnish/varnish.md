# Magento 2 Varnish

### Install Varnish
#### Version 4.1
Varnish 4.1 is available from the varnishcache_varnish41 repository, this repository can be installed with the following command:
```bash
curl -s https://packagecloud.io/install/repositories/varnishcache/varnish41/script.rpm.sh | sudo bash
```

Varnish 4.1 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish41'
```

#### Version 5.2
Varnish 5.2 is available from the varnishcache_varnish52 repository, this repository can be installed with the following command:
```bash
curl -s https://packagecloud.io/install/repositories/varnishcache/varnish52/script.rpm.sh | sudo bash
```

Varnish 5.2 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish52'
```
### Memory Limit
The default memory limit in Varnish is 256M. You may want to increase this, especially if you are using Varnish for Full Page Cache. You can do this by changing the value under VARNISH_STORAGE in the file /etc/varnish/varnish.params.

```bash
~]# grep VARNISH_STORAGE /etc/varnish/varnish.params
VARNISH_STORAGE="malloc,3G"
```
Please note Varnish will need a restart for this change to take effect.

### Pipe timeout
pipe_timeout is set to 60 seconds by default. This can cause time out issues when running exports in the Magento admin interface. You can increase this by adding the option:

-p pipe_timeout=600

Within the DAEMON_OPTS sections in the file /etc/varnish/varnish.params. You need to restart Varnish for this setting to take effect.

### Configuration Test
It's very important to run a configuration test before starting/restarting the Varnish service. You can run a configuration test with the following command:
```bash
~]# varnishd -C -f /etc/varnish/default.vcl
```
A successful output from this command will be the VCL displayed  on the terminal with no error message.

#### Start Varnish
You can start the Varnish service with the following command:
```bash
~]# systemctl start varnish
```
### Generate VCL
- Log in to the Magento Admin as an administrator.
- Click STORES > Settings > Configuration > ADVANCED > System > Full Page Cache.
- From the Caching Application list, click Varnish Caching.
- Click one of the export buttons to create a varnish.vcl you can use with Varnish.

You can now copy the file /var/www/vhosts/exmapledomain.com/htdocs/var/varnish.vcl to /etc/varnish/default.vcl. You may want to back up the default.vcl file:

```bash
~]# mv /etc/varnish/default.vcl /etc/varnish/default.vcl.backup
~]# cp /var/www/vhosts/exmapledomain.com/htdocs/var/varnish.vcl /etc/varnish/default.vcl
```
### Health Check
The Magento genereated VCL has the following healthcheck:
```bash
.probe = {
    .url = "/pub/health_check.php";
    .timeout = 2s;
    .interval = 5s;
    .window = 10;
    .threshold = 5;
    }
```
As we set the document root to pub you need to remove pub from the probe URL:

```bash
.probe = {
    .url = "/health_check.php";
    .timeout = 2s;
    .interval = 5s;
    .window = 10;
    .threshold = 5;
    }
```
The Varnish service needs to be reloaded in order for this to take effect.

### Cache Static Files
Static files are not cached by default in the Magento generated VCL. This is due to the assumption you have another service caching static files like a CDN. If you need Varnish to cache static files edit the section for static files in the VCL:

```bash
# Static files should not be cached by default
  return (pass);

# But if you use a few locales and don't use CDN you can enable caching static files by commenting previous line (#return (pass);) and uncommenting next 3 lines
  #unset req.http.Https;
  #unset req.http./*  */;
  #unset req.http.Cookie;
```
The Varnish service needs to be reloaded in order for this to take effect.

### Version Check
You can see the version of Varnish installed with the following command:
```bash
~]# varnishd -V
varnishd (varnish-4.1.11 revision 61367ed17d08a9ef80a2d42dc84caef79cdeee7a)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2019 Varnish Software AS
```

### HIT/MISS Headers
To test the caching of URLs in Varnish while Magento 2 is in producion mode you can add HIT/MISS headers to the VCL. Edit the vcl_deliver section in /etc/varnish/default.vcl and add the following:

```bash
if (obj.hits > 0) {
        set resp.http.X-Cache = "HIT";
        set resp.http.X-Cache-Hits = obj.hits;
    }
    else {
        set resp.http.X-Cache = "MISS";
    }
```

You need to reload Varnish for this change to take effect. Once done you can browse your website and check for these headers:

```bash
~]$ curl -sI https://exampledomain.co.uk/ | grep Cache
X-Cache: HIT
X-Cache-Hits: 4
```

### SSL Termination
Varnish does not support SSL-encrypted traffic, therefore we use Nginx for SSL termination. You need to remove the 443 listen from the server block in the Nginx vhosts configuration file and then add a new server block for 443. Example block:

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
