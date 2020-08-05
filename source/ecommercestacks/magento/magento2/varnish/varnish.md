# Varnish

### Install Varnish
#### Version 5.2
Varnish 5.2 is available from the varnishcache_varnish52 repository, this repository can be installed with the following command:
```bash
~]# curl -s https://packagecloud.io/install/repositories/varnishcache/varnish52/script.rpm.sh | sudo bash
```

Varnish 5.2 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish52,epel'
```

##### Start On Boot
You can enable Varnish on boot after installing it with this command:

```bash
~]# systemctl enable varnish
```

#### Version 6.3
Varnish 4.1 is available from the varnishcache_varnish41 repository, this repository can be installed with the following command:
```bash
~]# curl -s https://packagecloud.io/install/repositories/varnishcache/varnish63/script.rpm.sh | sudo bash
```

Varnish 4.1 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish63,epel'
```

##### Start On Boot
You can enable Varnish on boot after installing it with this command:

```bash
~]# systemctl enable varnish
```

### Version Check

You can see the version of Varnish installed with the following command:
```bash
~]# varnishd -V
varnishd (varnish-4.1.11 revision 61367ed17d08a9ef80a2d42dc84caef79cdeee7a)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2019 Varnish Software AS
```

### DAEMON_OPTS
DAEMON_OPTS can be defined in the /etc/varnish/varnish.params file. Here is an example that we use:

```bash
DAEMON_OPTS=" -p http_req_hdr_len=12000 -p http_resp_hdr_len=12000 -p thread_pool_min=100 -p thread_pool_max=3000 -p timeout_linger=0.1 -p pipe_timeout=600"
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

### Header Size
If you have this error message in Nginx: 

```bash
[error] 110200#110200: *102122 upstream sent too big header while reading response header from upstream
```

You may need to increase http_resp_hdr_len and http_resp_size. You can do this by adding:

```bash
-p http_resp_hdr_len=983044 \
-p http_resp_size=983044 \
```

To the DAEMON_OPTS sections in the file /etc/varnish/varnish.params. You need to restart Varnish for this setting to take effect.

### Configuration Test
It's very important to run a configuration test before starting/restarting the Varnish service. You can run a configuration test with the following command:
```bash
~]# varnishd -C -f /etc/varnish/default.vcl
```
A successful output from this command will be the VCL displayed  on the terminal with no error message(s).

#### Start Varnish
You can start the Varnish service with the following command:
```bash
~]# systemctl start varnish
```
#### Reload Varnish
You can reload the Varnish service with the following command:
```bash
~]# systemctl reload varnish
```
#### Restart Varnish
You can restart the Varnish service with the following command:
```bash
~]# systemctl restart varnish
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
### Set Varnish for FPC in Magento2
- Log in to the Magento2 Admin as an administrator.
- Click STORES > Settings > Configuration > ADVANCED > System > Full Page Cache.
- From the Caching Application list, click Varnish Caching.

You can also set this via the Magento2 CLI

```bash
php bin/magento config:set system/full_page_cache/caching_application 2
```

To check this has been set correctly:

```bash
php bin/magento config:show system/full_page_cache/caching_application
```

With the expected outcome being 2.

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

#### Health Check Status
You can check the health check status of all defined backends with the following command:

```bash
~]# varnishadm backend.list
Backend name                   Admin      Probe
boot.default                   probe      Healthy (no probe)
```

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

### cacheable="false"
Cacheable and uncacheable are terms Magento uses to indicate whether or not a page should be cached at all. (By default, all pages are cacheable.) If any block in a layout is designated as uncacheable, the entire page is uncacheable.

If pages are not being cached we recommend you search for cacheable="false" with the below command:

```bash
~]$ cd /var/www/vhosts/domainname.com/htdocs/
~]$ find vendor app -regextype 'egrep' -type f -regex '.*/layout/.*\.xml' -not -regex '.*(vendor/magento/|/checkout_|/catalogsearch_result_|/dotmailer).*' | xargs grep --color -n -e 'cacheable="false"'
```

### Exclude Domain From Cache
If you have a domain you wish to exclude from cache you can add the following:

```bash
if (req.http.host ~ "exampledomain.com") {
    return (pass);
   }
```
This needs to go under the vcl_recv section of the VCL. Varnish will need a reload for this to take efect.

### Exclude URI From Cache
You may need to exclude a URI from being cached, like the .well-known folder for example when validating an SSL.

```bash
if (req.url ~ "^/.well-known/") {
      return (pass);
   }
```

This needs to go under the vcl_recv section of the VCL. Varnish will need a reload for this to take efect.

### HTTP -> HTTPS Redirect
To configure Varnish to perform the HTTP to HTTPS redirect add the following:

All domains:
```bash
if (req.http.X-Forwarded-Proto !~ "https") {
        set req.http.location = "https://" + req.http.host + req.url;
        return (synth(750, "Permanently moved"));
    }
```

Single domain:
```bash
if (req.http.host ~ "exampledomain.com" && req.http.X-Forwarded-Proto !~ "https") {
        set req.http.location = "https://" + req.http.host + req.url;
        return (synth(750, "Permanently moved"));
    }
```

Under the vcl_recv section of /etc/varnish/default.vcl and:

```bash
if (resp.status == 750) {
        set resp.http.location = req.http.location;
        set resp.status = 301;
        return (deliver);
    }
```

Under vcl_synth. Varnish will need a reload for this to take efect.

### Purge Cache
Magento purges Varnish hosts after you configure Varnish hosts using the magento setup:config:set command (Ensure you run the Magento 2 CLI as the local system user defined in PHP-FPM and not root). Once configured when you clean, flush, or refresh the Magento cache, Varnish purges as well. 

```bash
~]$ php bin/magento setup:config:set --http-cache-hosts=10.0.0.17
```
You can also define more hosts if you have multiple web/varnish servers:
```bash
~]$ php bin/magento setup:config:set --http-cache-hosts=10.0.0.17,10.0.0.18,10.0.0.19
```

However you can purge the cache manually with the following command:

```bash
~]$ curl -I0 -X PURGE www.exampledomain.com -H "X-Magento-Tags-Pattern: *"
```

Single URI:
```bash
~]$ curl -I0 -X PURGE www.exampledomain.com/client.css -H "X-Magento-Tags-Pattern: *"
```

If the DNS for your domain does not point to Varnish you can use the IP address of your Varnish host:

```bash
curl -I0 -X PURGE http://158.228.105.80 -H "Host: www.exampledomain.com" -H "X-Magento-Tags-Pattern: *"
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

This block performs an SSL handshake and then sends traffic to port 80 which Varnish should be running on. You then need to ensure Nginx does not listen on port 80 by changing the listen from 80 to 8080:

```bash
server {
  listen 10.0.0.17:8080;
```

#### SSL Offloading
If SSL is set to offloading like the above example you need to uncomment the following from the Nginx vhosts configuration file:

```bash
 # Enable for SSL offloading
  set $my_https off;
  set $my_port 80;
  
  if ($http_x_forwarded_proto = https) {
    set $my_https on;
    set $my_port 443;
  }
  
  fastcgi_param HTTPS $my_https; # Uncomment the below for SSL offloading
  fastcgi_param SERVER_PORT $my_port; # Uncomment the below for SSL offloading
```

This tells Magento that although the connection is on port 80 -> 8080 it should be treated as a secure connection due to the header x_forwarded_proto containing https. 

```eval_rst
  .. title:: Magento 2 Varnish
  .. meta::
     :title: Magento 2 Varnish | UKFast Documentation
     :description: A guide using Varnish with Magento 2
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, varnish, eCommerce
