# Time To First Byte (TTFB)

Time to first byte (TTFB) is a measurement to show the responsiveness of your Magento website. TTFB measures the time from the end user making an HTTP request to the first byte of the page being received by the end user's browser. Magento can show a slower TTFB as it does not send any bytes until PHP has rendered the whole page (Unless there are cache mechanism in place).

### Server Time To First Byte

You can test the response time of the server with a simple PHP info page. This will show you the speed of which the network, server, webservice and PHP-FPM response:

```bash
 ~]$ curl -o /dev/null -s -w "Time: %{time_total} \n" https://exampledomain.com/info.php
Time: 0.197
```

### Magento Time To First Byte

Comparing the same test when accessing Magento will provide an indication of server response time versus Magento response time:
```bash
 ~]$ curl -o /dev/null -s -w "Time: %{time_total} \n" https://exampledomain.com/index.php
Time: 2.034
```

The key to having a lower TTFB with Magento is to optimise Magento to reduce the load time. Some recommendations on improving TTFB:

- Implement Full Page Cache (Ideally with Varnish)
- Memory based session management (Redis)
- Disable/Remove unused modules in Magento
- Optimise code in theme .phtml files
- Ensure Magento is on the latest version
- Optimise static content (Reduce image sizes, minify js/css)

```eval_rst
  .. title:: Magento Time To First Byte
  .. meta::
     :title: Magento Time To First Byte | UKFast Documentation
     :description: A guide to investigate time to first byte
     :keywords: ukfast, linux, nginx, install, centos, cloud, server, virtual, Magento, ttfb

