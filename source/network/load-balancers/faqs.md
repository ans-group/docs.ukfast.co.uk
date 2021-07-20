# FAQs

Here are some of the most frequently asked questions we get about our load balancers to help save you time.

## How do I replace an expired certificate?

This is covered in our [common changes](common-changes.html#replacing-an-expired-ssl-certificate) page.

## How do I drain traffic from a particular target server?

This is covered in our [common changes](common-changes.html#drain-traffic-from-a-particular-target-server) page.

## How can I temporarily take a server out of load to run updates / maintenance?

This is covered in our [common changes](common-changes.html#temporarily-remove-a-target-server-from-behind-the-load-balancer) page.

## Why is all my traffic now coming from one IP?

Once you've moved behind a load balancer, you may notice that some of your analytics on your backend servers, along with your logs appear to break. Where you used to see a breakdown of all the visitors to your site, you now just see one persistent visitor. The numbers won't have changed, but the IP address will have.

This is down to the nature of the load balancer itself. Where visitors used to directly visit your server, they now visit the load balancer instead and it's the load balancer that makes requests to the backend server. As such, the only IP address you'll see in logs or analytics will likely be that of the load balancer.

There's an easy fix. Whereas logs and analytics will usually derive the visitor IP from the source of the request, they need to be directed to look at the standard `X-Forwarded-For` header instead. This is injected by the load balancer automatically, so should already be present. If you have HTTPS passthrough enabled or are using TCP mode then you will need to enable the PROXY protocol on the edit target group screen for this to work. This also requires additional setup on your web / application servers.

How this is achieved will depend on what solution you're trying to work with. Here are a few examples:

**Apache:**

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

Replace `1.1.1.1` and `2.2.2.2` with the IP address(es) your load balancer is sending traffic from and restart Apache to put it all live:

```bash
  service httpd restart
```

**NGINX:**

The comparable module for NGINX is called `ngx_http_realip_module`: <http://nginx.org/en/docs/http/ngx_http_realip_module.html>

If your install of NGINX was compiled with `--with-http_realip_module` then you should be able to make use of it like so in your `nginx.conf`:

```nginx
  set_real_ip_from 1.1.1.1;
  real_ip_header    X-Forwarded-For;
```

As mentioned for Apache, `1.1.1.1` should be replaced with the IP address that's now sending all the traffic to your servers.

Then restart NGINX to put it live:

```bash
  service nginx restart
```

```eval_rst
   .. title:: Load Balancers | Frequently Asked Questions
   .. meta::
      :title: Load Balancers | Frequently Asked Questions | UKFast Documentation
      :description: FAQs about UKFast load balancers
```

### I'm getting a redirect loop when redirecting to HTTPS, how can I fix this?

In some configurations, performing a HTTP->HTTPS redirect from a server behind a load balancer may result in your website experiencing a redirect loop. As the HTTPS connection is terminated at the load balancer, the backend servers only see HTTP connections and continually try to redirect the client to a HTTPS URL.

Ideally you should perform your HTTP->HTTPS redirects directly on the load balancer using the option available in the Listener configuration section, however if this is not an acceptable solution, you can confirm if a client is using HTTPS connections to the load balancer by checking the X-Forwarded-Proto header. This header will be present and contain the value https when connections to the load balancer are occurring over HTTPS. You can check this header to perform conditional redirects to HTTPS on you backend servers, for example:

**Apache:**

```bash
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301,NE]
```

**NGINX:**

```nginx
if ($http_x_forwarded_proto = "http") {
    return 301 https://$server_name$request_uri;
}
```
