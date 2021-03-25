# DDoSX® HTTP Request and Response Headers

Documentation of HTTP request and response headers DDoSX® will add to your requests.

## Request:

### `X-Forwarded-For`
This will have the connecting IP address appended to this header if the header is already present. If the header is missing it will be set to the connecting IP address.

### `X-Forwarded-Proto`
This will provide the HTTP scheme (`http` or `https`) that was used when the connection arrived to the DDoSX® node. It is useful if your secure origin is set to `http`. Use this in your application to detect if you needed to perform a redirect to HTTPS.

### `DDOSX-Connecting-IP`
This header takes the client IP address that hit the DDoSX® node. If this header was set during the original request it will be overwritten. This header is more trustworthy than the `X-Forwarded-For` header as it can't forged by would-be attackers.

### `X-DDoSX-Country-Code`
This header will return the country of the connecting IP address in an [Alpha-2 ISO Code format](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). You can get help mapping this to the name using [https://www.iso.org/obp/ui/](https://www.iso.org/obp/ui/).

## Response:

### `X-DDoSX-Request-ID`
This header is used for diagnostic reasons by our Support team and is used to trace the request in our logs, giving us more detailed information about your request.


```eval_rst
   .. title:: DDoSX® HTTP Request and Response Headers | UKFast Documentation
   .. meta::
      :description: HTTP request and response headers DDoSX® will add to your requests.
      :keywords: http, ddosx, headers, client ip, geo location, request, response
```
