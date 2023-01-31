# Varnish

Varnish is recommended for Full Page Caching with Magento2. Website performance is greatly increased when using Varnish.

### Install Varnish

#### Version 6.5

Varnish 6.5 is available from the `varnishcache_varnish65` repository, you can install this repository and varnish with the following commands:

##### CentOS
```bash
curl -s https://packagecloud.io/install/repositories/varnishcache/varnish65/script.rpm.sh | sudo bash
```

```bash
yum install varnish --disablerepo='*' --enablerepo='varnishcache_varnish65,epel'
```

##### Ubuntu

```bash
curl -s https://packagecloud.io/install/repositories/varnishcache/varnish65/script.deb.sh | sudo bash
```

```bash
apt-get install varnish
```

##### `DAEMON_OPTS`

This is a template to be reviewed and modified to fit your needs:

```bash
systemctl edit --full varnish
```

Edit `ExecStart`:

```bash
ExecStart=/usr/sbin/varnishd \
        -a 10.0.0.16:80 \
        -f /etc/varnish/default.vcl \
        -s malloc,4G \
        -T 10.0.0.16:6082 \
        -p http_req_hdr_len=32768 \
        -p http_req_size=65536 \
        -p http_resp_hdr_len=131072 \
        -p http_resp_size=196608 \
        -p workspace_backend=280k \
        -p thread_pool_min=100 \
        -p thread_pool_max=3000 \
        -p timeout_linger=0.1 \
        -p cli_timeout=20 \
        -p thread_pools=2 \
        -p pipe_timeout=600
```

### Example `VCL`
You can view an example Magento2 UKFast `VCL` [here](ukfast_vcl)

### Configuration Test

It's very important to run a configuration test before starting / restarting the Varnish service. You can run a configuration test with the following command:

```bash
varnishd -C -f /etc/varnish/default.vcl
```

A successful output from this command will be the VCL displayed on the terminal with no error message(s).

### Start Varnish

You can start the Varnish service with the following command:

```bash
systemctl start varnish
```

##### Start On Boot

You can enable Varnish on boot after installing it with this command:

```bash
systemctl enable varnish
```

### Reload Varnish

You can reload the Varnish service with the following command:

```bash
systemctl reload varnish
```
### Restart Varnish

You can restart the Varnish service with the following command:

```bash
systemctl restart varnish
```

### Version Check

You can see the version of Varnish installed with the following command:

```bash
~# varnishd -V
varnishd (varnish-6.5.1 revision 1dae23376bb5ea7a6b8e9e4b9ed95cdc9469fb64)
Copyright (c) 2006 Verdens Gang AS
Copyright (c) 2006-2020 Varnish Software
```

### `Varnishlog`

The `varnishlog` command can be used to debug issues. Here are some examples which may assist you:

#### Monitor for Purge requests
This is very handy to see how frequently purge requests are being sent to Varnish:

```bash
varnishlog -g request -q 'ReqMethod eq "PURGE"'
```

#### Monitor HTTP response code (Example 503)
```bash
varnishlog -q 'RespStatus == 503' -g request
```

#### Filter `varnishlog` by IP address
If you wish to only see your own requests to Varnish you can filter with similar commands to:

```bash
varnishlog -q "ReqHeader eq 'X-Forwarded-For: ip.ip.ip.ip'"

varnishlog -q "ReqHeader eq 'DDOSX-Connecting-IP: ip.ip.ip.ip'"

varnishlog -q "ReqHeader eq 'X-Real-IP: ip.ip.ip.ip'"
```

### Generate VCL in Magento2

- Log in to the Magento Admin as an administrator.
- Click `STORES` > `Settings` > `Configuration` > `ADVANCED` > `System` > `Full Page Cache`.
- From the `Caching Application` list, click `Varnish Caching`.
- Click one of the export buttons to create a `varnish.vcl` you can use with Varnish.

You can now copy the file `/var/www/vhosts/exmapledomain.com/htdocs/var/varnish.vcl` to `/etc/varnish/default.vcl`. You may want to back up the `default.vcl` file:

```bash
mv /etc/varnish/default.vcl /etc/varnish/default.vcl.backup
cp /var/www/vhosts/exmapledomain.com/htdocs/var/varnish.vcl /etc/varnish/default.vcl
```
### Set Varnish for FPC in Magento2

- Log in to the Magento2 Admin as an administrator.
- Click `STORES` > `Settings` > `Configuration` > `ADVANCED` > `System` > `Full Page Cache`.
- From the `Caching Application` list, click `Varnish Caching`.

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

The Magento generated VCL has the following healthcheck:

```ini
.probe = {
    .url = "/pub/health_check.php";
    .timeout = 2s;
    .interval = 5s;
    .window = 10;
    .threshold = 5;
    }
```

As we set the document root to pub you need to remove `/pub` from the probe URL:

```ini
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

```vcl
# Static files should not be cached by default
  return (pass);

# But if you use a few locales and don't use CDN you can enable caching static files by commenting previous line (#return (pass);) and uncommenting next 3 lines
  #unset req.http.Https;
  #unset req.http./*  */;
  #unset req.http.Cookie;
```

The Varnish service needs to be reloaded in order for this to take effect.

### Too many restarts
Avoid the 'too many restarts' error by adding this configuration option to `vcl_recv`:

```vcl
if (req.restarts > 0) {
        set req.hash_always_miss = true;
    }
```

### HIT/MISS Headers

To test the caching of URLs in Varnish while Magento 2 is in production mode you can add `HIT`/`MISS` headers to the VCL. Edit the `vcl_deliver` section in `/etc/varnish/default.vcl` and add the following:

```vcl
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

### `cacheable="false"`

Cacheable and uncacheable are terms Magento uses to indicate whether or not a page should be cached at all. (By default, all pages are cacheable.) If any block in a layout is designated as uncacheable, the entire page is uncacheable.

If pages are not being cached we recommend you search for `cacheable="false"` with the below command:

```bash
cd /var/www/vhosts/domainname.com/htdocs/
find vendor app -regextype 'egrep' -type f -regex '.*/layout/.*\.xml' -not -regex '.*(vendor/magento/|/checkout_|/catalogsearch_result_|/dotmailer).*' | xargs grep --color -n -e 'cacheable="false"'
```

### Exclude Domain From Cache

If you have a domain you wish to exclude from cache you can add the following:

```vcl
  if (req.http.host ~ "exampledomain.com") {
    return (pass);
  }
```

This needs to go under the `vcl_recv` section of the VCL. Varnish will need a reload for this to take effect.

### Exclude URI From Cache

You may need to exclude a URI from being cached, like the `.well-known` folder for example when validating an SSL.

```vcl
  if (req.url ~ "^/.well-known/") {
      return (pass);
  }
```

This needs to go under the `vcl_recv` section of the VCL. Varnish will need a reload for this to take effect.

### HTTP -> HTTPS Redirect
To configure Varnish to perform the HTTP to HTTPS redirect add the following under the `vcl_recv` section of `/etc/varnish/default.vcl`:

All domains:

```vcl
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

 and then add the below under the `vcl_synth` section:

```vcl
    if (resp.status == 750) {
        set resp.http.location = req.http.location;
        set resp.status = 301;
        return (deliver);
    }
```

Varnish will need a reload for this to take effect.

```bash
varnishd -C -f /etc/varnish/default.vcl && systemctl reload varnish
```

### Custom 503 Error page
To configure a custom Varnish 503 error page you will have to follow these steps.

You will need to add this under the `vcl_deliver` section:

```vcl
    if (resp.status == 503) {
       return(restart);
    }
```

To configure the response you will have to add the below config to the `vcl_backend_response` section:

```vcl
    if (beresp.status == 503 && bereq.retries < 5 ) {
       return(retry);
    }
```

#### Custom error page for all sites

Upload custom error page here:

```bash
/etc/varnish/error503.html
```

Then you need to add this under the `vcl_backend_error` section (You may need to create the sub for `vcl_backend_error`):

```vcl
      if (beresp.status == 503 && bereq.retries == 5) {
          synthetic(std.fileread("/etc/varnish/error503.html"));
          return(deliver);
       }
```

The final change is to the `vcl_synth` section (You may need to create the sub for `vcl_synth`):

```vcl
    if (resp.status == 503) {
        synthetic(std.fileread("/etc/varnish/error503.html"));
        return(deliver);
     }
```

#### Custom error page for a single site

Upload site error page here:

```bash
/etc/varnish/maintenance/example.co.uk.html
```

Then you need to add this under the `vcl_backend_error` section (You may need to create the sub for `vcl_backend_error`):

```vcl
      if (beresp.http.host ~ "example.co.uk" && beresp.status == 503 && bereq.retries == 5) {
          synthetic(std.fileread("/etc/varnish/maintenance/example.co.uk.html"));
          return(deliver);
      }
```

The final change is to the `vcl_synth` section (You may need to create the sub for `vcl_synth`):

```vcl
      if (req.http.host ~ "example.co.uk" && resp.status == 503) {
          synthetic(std.fileread("/etc/varnish/maintenance/example.co.uk.html"));
          return(deliver);
      }
```

### Load balancing
You can define multiple backends in the `Varnish VCL` file (`/etc/varnish/default.vcl`) to load balance traffic between servers.

#### import directors
You will have to add this to the top of `VCL`:
```vcl
import directors;
```

#### Create/add backends:
```vcl
backend Web01 {
    .host = "REPLACEME";
    .port = "8080";
    .first_byte_timeout = 600s;
    .probe = {
        .url = "/health_check.php";
        .timeout = 2s;
        .interval = 5s;
        .window = 10;
        .threshold = 5;
   }
}

backend Web02 {
    .host = "REPLACEME";
    .port = "8080";
    .first_byte_timeout = 600s;
    .probe = {
        .url = "/health_check.php";
        .timeout = 2s;
        .interval = 5s;
        .window = 10;
        .threshold = 5;
   }
}
```

#### Directors
Beneath the backends create the `vcl_init` sub:
```vcl
sub vcl_init {
   new lbweb = directors.round_robin();
   lbweb.add_backend(web01);
   lbweb.add_backend(web02);
}
```

#### Set Backend
Within the `vcl_recv` sub you can now specify which director to use:
```vcl
set req.backend_hint = lbweb.backend();
```

### Purge Cache

Magento purges Varnish hosts after you configure Varnish hosts using the `magento setup:config:set` command. Ensure you run the Magento 2 CLI as the local system user defined in PHP-FPM and not root. Once configured, when you clean, flush, or refresh the Magento cache, Varnish purges as well.

```bash
php bin/magento setup:config:set --http-cache-hosts=10.0.0.17
```

You can also define more hosts if you have multiple web/varnish servers:

```bash
php bin/magento setup:config:set --http-cache-hosts=10.0.0.17,10.0.0.18,10.0.0.19
```

However you can purge the cache manually with the following command:

```bash
curl -I0 -X PURGE www.exampledomain.com -H "X-Magento-Tags-Pattern: .*"
```

Single URI:

```bash
curl -I0 -X PURGE www.exampledomain.com/client.css -H "X-Magento-Tags-Pattern: .*"
```

If the DNS for your domain does not point to Varnish you can use the IP address of your Varnish host:

```bash
curl -I0 -X PURGE http://158.228.105.80 -H "Host: www.exampledomain.com" -H "X-Magento-Tags-Pattern: .*"
```

By default, Varnish will not purge all static assets and will instead only purge PHP. This is due to Varnish only purging the assets with the X-Magento-Tags header. As this header is generated by Magento we need to adjust the `/etc/varnish/default.vcl` file if we want to purge everything including static assets.

In the `vcl_recv` section of the VCL and within the purge if statement you can add:

```bash
if (req.http.X-Magento-Tags-Pattern == ".*") {
   ban("req.url ~ .*");
}
```

### SSL Termination

Varnish does not support SSL-encrypted traffic, therefore we use NGINX for SSL termination. You need to remove the 443 listen from the server block in the NGINX vhosts configuration file and then add a new server block for 443. Example block:

```nginx
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

This block performs an SSL handshake and then sends traffic to port 80 which Varnish should be running on. You then need to ensure NGINX does not listen on port 80 by changing the listen from 80 to 8080:

```bash
server {
  listen 10.0.0.17:8080;
```

### SSL Offloading

If SSL is set to offloading like the above example you need to uncomment the following from the NGINX vhosts configuration file:

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

This tells Magento that although the connection is on port 80 -> 8080 it should be treated as a secure connection due to the header `x_forwarded_proto` containing https.

```eval_rst
  .. title:: Magento 2 Varnish
  .. meta::
     :title: Magento 2 Varnish | UKFast Documentation
     :description: A guide using Varnish with Magento 2
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento2, varnish, eCommerce
```
