# Extracting Client IP

Since all requests to your web servers will now be coming directly from the Webcelerator, your log files on your server will show that every request comes from the same IP address. If you're using something like Google Analytics for visitor stats, this shouldn't matter. If you're using log file processing tools like AWStats or Webalizer, you won't be able to extract meaningful data from your logs anymore.

If you are also extracting the client's IP address to use in your website or application, e.g. using `$_SERVER['REMOTE_ADDR']` in PHP, then the IP reported will also now be the Webcelerator's IP.

To solve these problems, the Webcelerator will place the client's IP address into an `X-Forwarded-For` HTTP header.

We can make your web server log this as the client's IP instead by applying a platform-dependent fix. If you need this please speak with us and we can apply the appropriate fixes to your solution. (Including `mod_rpaf` for Apache, an `ISAPI filter` for IIS, and the `HTTPRealIPModule` for NGINX).

## PHP Overwrite

For your web application and code you should begin inspecting the `X-Forwarded-For` header instead of the IP where the request came from. Here's some example PHP code you could use to overwrite the `REMOTE_ADDR` variable.

```php
if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
$_SERVER['REMOTE_ADDR'] = $_SERVER['HTTP_X_FORWARDED_FOR'];
}
```

Also note that if you have other devices in your solution that already forward on the `HTTP_X_FORWARDED_FOR` header then the Webcelerator will add these to the header so you receive a comma separated list of IPs.

To always extract the client IP you would then need to apply to the above example code.

```php
$_SERVER['REMOTE_ADDR'] = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
$_SERVER['REMOTE_ADDR'] = trim($_SERVER['REMOTE_ADDR'][0]);
```

```eval_rst
  .. title:: Finding the Client IP when using Webcelerators
  .. meta::
     :title: Finding the Client IP when using Webcelerators | UKFast Documentation
     :description: How to currectly identify the client IP with Webcels
     :keywords: webcel, client ip, php
```
