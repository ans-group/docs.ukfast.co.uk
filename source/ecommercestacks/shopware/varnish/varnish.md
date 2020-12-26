# Varnish

### Install Varnish
#### Version 4.1
Varnish 4.1 is available from the varnishcache_varnish41 repository, this repository can be installed with the following command:
```bash
~]# curl -s https://packagecloud.io/install/repositories/varnishcache/varnish41/script.rpm.sh | sudo bash
```

Varnish 4.1 can then be installed with the command:
```bash
~]# yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish41,epel'
```
##### Start On Boot
You can enable Varnish on boot after installing it with this command:

```bash
~]# systemctl enable varnish
```

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

### Memory Limit
The default memory limit in Varnish is 256M. You may want to increase this, especially if you are using Varnish for Full Page Cache. You can do this by changing the value under VARNISH_STORAGE in the file /etc/varnish/varnish.params.

```bash
~]# grep VARNISH_STORAGE /etc/varnish/varnish.params
VARNISH_STORAGE="malloc,3G"
```
Please note Varnish will need a restart for this change to take effect.

### Pipe timeout
pipe_timeout is set to 60 seconds by default. This can cause time out issues when running exports in the Shopware admin interface. You can increase this by adding the option:

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
### Shopware VCL
The Shopware VCL can be downloaded [here](https://developers.shopware.com/sysadmins-guide/varnish-setup/#varnish-configuration-(vcl))

Copy the file vcl to /etc/varnish/default.vcl. You may want to back up the default.vcl file:

```bash
~]# mv /etc/varnish/default.vcl /etc/varnish/default.vcl.backup
~]# cp /var/www/vhosts/exmapledomain.com/htdocs/var/varnish.vcl /etc/varnish/default.vcl
```

### Version Check
You can see the version of Varnish installed with the following command:
```bash
~]# varnishd -V
varnishd (varnish-4.1.11 revision 61367ed17d08a9ef80a2d42dc84caef79cdeee7a)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2019 Varnish Software AS
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

This tells Shopware that although the connection is on port 80 -> 8080 it should be treated as a secure connection due to the header x_forwarded_proto containing https.

```eval_rst
  .. title:: Shopware Varnish
  .. meta::
     :title: Shopware Varnish | UKFast Documentation
     :description: A guide using Varnish with Shopware
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Shopware, varnish, eCommerce
