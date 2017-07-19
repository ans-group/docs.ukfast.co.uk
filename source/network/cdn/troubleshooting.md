# Troubleshooting

## Why am I getting a X-Proxy-Cache: MISS

If you have configured Respect Origin Cache-Control headers in [ddosx](https://my.ukfast.co.uk/ddosx), you need to make sure that you have Cache-Control headers set and to something that doesn't fall under the catagory of not cacheable as per [manage cdn](https://docs.ukfast.co.uk/network/cdn/managingcdn.html#caching-content)

The distributed nature of the servers in each pop has a trade off that means cache is stored locally at each server, so you might find requests with a HIT will next return a MISS, this is entirely possible until the cache has been stored by each server.

If you have configured Custom there are two cases where you might get a MISS, this is if in the response header there is a `Set-Cookie` or the special `Vary: *` header has been set. The reason behind this is caching content with `Set-Cookie` if mis configured might lead to content that is supposed to be user specific from being cached for another user. Also the Vary header if ignored could mean that content that is meant to be cached differently from others might not be.

For example if the `Vary: Accept-Encoding` header is sent in the response, this tells the CDN that compressed and none compressed content should be cached independantly. If we ignore this header this could leave to compressed content being cached and delivered cache to clients that haven't sent Accept-Encoding in the request headers to get back compressed content.

Please make sure that the Content-Type matches the mime-types that have been selected in [ddosx](https://my.ukfast.co.uk/ddosx/). You can do this using curl and request the content with a HEAD request:
curl -I example.org/image.png

and confirm the Content-Type header that is returned matches the mime type that has been configured.
