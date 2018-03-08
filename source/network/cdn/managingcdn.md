# Managing the cache

## Caching content

To ensure your content is cached:

* The type of request must be a GET or HEAD request
* The http response must be 200, 301 or 206 if you are setting how long content is cached by the CDN, otherwise we will respect the Cache-Control header.

There are also a number of reasons why content will not be cached:

* There is a nocache cookie (Cache-Control: no-cache=Set-Cookie)
* Cache-Control headers are set to private
* Set-cookie is present in the request
* A nocache argument has been added to the request. (For example example.org/?nocache=true)
* The Authorization http header is present in the request
* The purge http header is present. This is not a standard header and is more likely to be used if you want to force the CDN server to fetch from the origin server (purge: something)

## Special Cases

Once cachable content has been marked as expired, the CDN will perform a conditional GET request with the If-Modified-Since header. This saves bandwidth as the full item will only be fetched from the origin server if the file has been modified since the time recorded in the Last-Modified header.

There are a few situations that will mean stale content could be served from the CDN, such as:
* http errors 500/502/503/504
* the origin server is unable to process a request
* cached content is currently being updated from the origin server (this is to minimize the requests to the origin server)
* the origin server times out the request
If there are multiple requests to an item that isn't in the cache, only one request will be fetched from the origin server. Once cached, subsequent requests will be delievered from cache.

The CDN uses four values to decide what makes a request unique, and therefore uncached:

* scheme
* host header
* request uri
* slice range

Put simply, a request for **https:**//example.org/example.jpg will be cached as normal, but if a request was made for **http:**//example.org/example.jpg then the first request would not be cached, but subsequent requests would be.  This is because 301's are cached, and if you are redirecting http to https we can cache the https request differently. (Only if MIME-type caching is disabled)

You might recognise the first three values, but maybe not the fourth. The slice range is used to cut up larger files such as video into chucks and allow for more efficent caching, with each slice range being cached individually. You can see the value of this by looking at the http range header.

## X-Proxy-Cache Header

To help understand what happened to a request we add the header X-Proxy-Cache, which can be seen in the response of the request.  Possible values are:

**MISS**: The response was not found in the cache and so was fetched from an origin server. The response might then have been cached.

**BYPASS**: The response was fetched from the origin server instead of served from the cache, and the CDN was told to bypass any cache it might have had.

**EXPIRED**: The entry in the cache has expired. The response contains fresh content from the origin server.

**STALE**: The content is stale because the origin server is not responding correctly, so cached content deemed as expired was served.

**UPDATING**: The content is stale because the entry is currently being updated in response to a previous request.

**REVALIDATED**: The content was expired, but the current cached version is still valid.

**HIT**: Served from cache.

If you need help using the CDN or configuring your rules, please contact UKFast support by raising a ticket in [MyUKFast](https://my.ukfast.co.uk/pss/add.php) or by calling 0800 230 0032.

```eval_rst
  .. meta::
     :title: Managing the cache on CDN | UKFast Documentation
     :description: A guide to managing the content that is cached by CDN
     :keywords: ukfast, content delivery network, CDN, cache, Cache-Control, Cache headers, X-Proxy-Cache Header
