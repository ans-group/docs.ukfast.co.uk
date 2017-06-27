# Getting Started

A Content Delivery Network (or CDN) is a network of highly-distributed servers that are specifically designed to deliver static content or streaming media. The servers are spread over a number of physical locations in order to bring the content as close as possible to the user requesting it.

The CDN sits between the client and the origin server and caches the content to reduce the number of requests to the origin  server and lower the latency to the end user easing the amount of bandwidth to the origin server. This is achieved by making use of anycast routing where each of the servers share the same IP address and a request for content is sent to one of many IP addresses. The IP address is announced through BGP (Boarder Gateway Protocol), so the client's request should hit the closet server to the client based on the client's geographical location.

For example, a user based in the USA streaming video from a server hosted in the UK could experience latency of 75ms or higher. However the same request for a video to a CDN server based in the USA in front of the origin server can be as little as 10ms.

Below is a list of what is required to ensure this content is cached:

* The type of request must be a GET or HEAD request
* The http response must be 200, 301, 206, this is only if you are setting how long content is cached at the cdn, otherwise we will just respect the Cache-Control header.

There are also a list of reason we will not cache the content or bypass something that is already cached:

* If there is a nocache cookie (Cache-Control: no-cache=Set-Cookie)
* Cache-Control headers are set to private
* Set-cookie is present in the request
* A nocache argument has been added to the request. (For example example.org/?nocache=true)
* If the Authorization http header is present in the request
* If the purge http header is present. This is not a standard header and is more likely to be used if you want to force the cdn server to fetch from the origin server (purge: something)

There are also some special cases you might want to aware of

* Once cachable content has been marked as expired the cdn will perform conditional GET request with the If-Modified-Since header. This saves bandwidth as the full item will only be fetched from the origin server if the file has been modified since the time recorded in the Last-Modified header
* There are a few situations that will mean stale content will be served from the CDN such as
   * http errors 500/502/503/504
   * if the origin server is unable to process a request
   * if cached content is currently being updated from the origin server this is to minimize the requests to the origin server
   * if the origin server times out to the request
* If there are multiple requests to something that isn't in the cache, only one request will be fetched from the origin server once cached the other requests will have it delievered from cache.

The CDN uses 4 values to decide what makes a request unique

* scheme
* host header
* request uri
* slice range

Put simply this means a request for
https://example.org/example.jpg
will be cached as normal, but if you made a request for the below the first request would not be cached. (All further requests would be)
http://example.org/example.jpg

The reason for this is that we cache 301's and if you are redirecting http to https we can cache the https request differently. (Only if MIME-type caching is disabled)

You might recognise the first three, but maybe not the forth. We use the slice range as we cut up larger files into chucks to allow for more efficent caching of large files such as video, so each range as cacheable. You can see the value of this by looking at the http range header

To help understand what happened to a request we add the header X-Proxy-Cache, and this can be seen in the response of the request these can be of the value.

* MISS
* BYPASS
* EXPIRED
* STALE
* UPDATING
* REVALIDATED
* HIT

MISS: The response was not found in the cache and so was fetched from an origin server. The response might then have been cached.
BYPASS: The response was fetched from the origin server instead of served from the cache, and the CDN was told to bypass any cache it might have had.
EXPIRED: The entry in the cache has expired. The response contains fresh content from the origin server.
STALE: The content is stale because the origin server is not responding correctly, so cached content deemed as expired was served.
UPDATING: The content is stale because the entry is currently being updated in response to a previous request.
REVALIDATED: The content was expired, but the current cached version is still valid.
HIT: Served from cache.

Finally there might be some occasions where you need to just tell the CDN to stop caching this and fetch from the origin. There are currently three ways this can be done

* As above with the bypass methods such as purge http header and the ?nocache=true arguments on the request
* Manual PURGE/DELETE http methods
* via my.ukfast.co.uk/ddosx

We have support for telling the CDN platform via a PURGE or a DELETE method to clear cache. For example using curl `curl -XPURGE example.org/example.jpg` This should response with an OK if this was successful. If you add a -I with this request to present the headers you should see something like `X-Purged-Count: 1` to show how many items were removed. This can also be done against `curl -XPURGE example.org/*` which will effectively clear everything. Cache is stored on each server locally, so this method will only clear the cache on the server it hits.

The final method is to use the my.ukfast.co.uk/ddosx interface. This will allow you to clear your items and effectively PURGE the content you want on each of the servers to fully clear it all out. You can also tell it specific URLs or any files ending in .jpg for example.
