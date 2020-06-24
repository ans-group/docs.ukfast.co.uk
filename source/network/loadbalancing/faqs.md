# Frequently Asked Questions

A page dedicated to some of the more common questions related to our loadblancers.

## Why is all my traffic now coming from one IP?

Once you've moved behind a loadbalancer, you may notice that some of your analytics on your backend servers, along with your logs appear to break. Where you used to see a breakdown of all the visitors to your site, you now just see one persistent visitor. The numbers won't have changed, but the IP address will have.

This is down to the nature of the loadbalancer itself. Where visitors used to directly visit your server, they now visit the loadbalancer instead and it's the loadbalancer that makes requests to the backend server. As such, the only IP address you'll see in logs or analytics will likely be that of the loadbalancer.

This obviously isn't too great, but there's an easy fix. Whereas logs and analytics will usually derive the visitor IP from the requests source, they need to be directed to look at the standard `X-Forwarded-For` header instead. This is injected by the loadbalancer automatically, so should already be present.

How this is achieved will depend on what solution you're trying to work with. Here are a few examples:

### Apache

Apache has an optional module called `mod_rpaf` that handles the transition from source to `X-Forwarded-For`, so with it set up you shouldn't really notice any difference from that point onward.

It's not installed by default, so install it like so:

```bash
  yum install mod_rpaf
```

After that, edit `/etc/httpd/conf.d/mod_rpaf.conf` and put the following content in:

```apacheconf

  LoadModule rpaf_module modules/mod_rpaf-2.0.so

  RPAFenable On
  RPAFsethostname On
  RPAFproxy_ips 1.1.1.1 2.2.2.2 127.0.0.1
  RPAFheader X-Forwarded-For
```

Replace `1.1.1.1` and `2.2.2.2` with the ip address(es) your loadbalancer is sending traffic from and restart apache to put it all live:

```bash
  service httpd restart
```

### NGiNX

The comparable module for NGiNX is called `ngx_http_realip_module`: <http://nginx.org/en/docs/http/ngx_http_realip_module.html>

If your install of NGiNX was compiled with `--with-http_realip_module` then you should be able to make use of it like so in your `nginx.conf`:

```nginx
  set_real_ip_from 1.1.1.1;
  real_ip_header    X-Forwarded-For;
```

As mentioned for apache, `1.1.1.1` should be replaced with the IP address that's now sending all the traffic to your servers.

Then restart NGiNX to put it live:

```bash
  service nginx restart
```

```eval_rst
   .. title:: Load Balancing | Frequently Asked Questions
   .. meta::
      :title: Load Balancing | Frequently Asked Questions | UKFast Documentation
      :description: Information and guidance on using the CDN on DDoSX
```
