# DDoSX® HTTP Request and Response Headers

Documentation of HTTP request and response headers DDoSX® will add to your requests.

## Request:

### `X-Forwarded-For`
This will have the connecting IP address appended to this header if the header is already present. If the header is missing it will just show the connecting IP address.

### `X-Forwarded-Proto`
This will provide the scheme `http` or `https` that was used when the connection hit the DDoSX® node. It is useful if your secure origin is set to `http`, so you can redirect your application accordingly based on this information.

### `DDOSX-Connecting-IP`
This header takes the IP address that hit the DDoSX® node. If this header was set during the original request it will be overwritten. This header is more trustworthy than the `X-Forwarded-For` header as it can't be sent to the origin with a forged IP address.

### `X-DDoSX-Country-Code`
This header will return the country of the connecting IP address in an Alpha-2 ISO Code format. You can get help mapping this to the name using https://www.iso.org/obp/ui/.

## Response:

### `X-DDoSX-Request-ID`
This header is used for diagnostics reasons and is useful for our support team and helps by giving us more detailed information about your request to track down potential issues in our logs.


```eval_rst
   .. title:: DDoSX® HTTP Request and Response Headers | UKFast Documentation
   .. meta::
      :description: HTTP request and response headers DDoSX® will add to your requests.
      :keywords: http, ddosx, headers, client ip, geo location, request, response
```