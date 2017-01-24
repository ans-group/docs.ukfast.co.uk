# SSL Certificates on a WebCelerator

As the WebCelerator acts as a reverse proxy to your backend servers, usually at the edge of your network, you'll probably need to consider how to handle SSL certificates for sites running through the WebCelerator.

There are three options for SSL configuration, depending on your needs:

- **SSL Passthrough** *(default)*: SSL traffic is passed directly to the backend by a Layer 4 proxy, and is therefore not cached. The SSL handshake occurs with the backend server directly, so traffic is encrypted until it reaches the backend. No caching will occur on HTTPS content.
- **SSL Offloading**: SSL traffic is decrypted when it enters the WebCelerator, so the SSL handshake actually happens with the WebCelerator rather than the backend. Any traffic which needs to be passed onto the backend is handled over HTTP. Caching will occur on HTTPS content.
- **Secure Origin Pull** *(recommended)*: SSL traffic is decrypted when it enters the WebCelerator, allowing inspection of the traffic, and querying of the cache. Any requests needing passing to a backend are re-encrypted and transmitted over HTTPS to the backend. Caching will occur on HTTPS content, and the backend will receive a normal HTTPS request on port 443 for uncached content.

We can configure your WebCelerator to handle SSL traffic on request, which may require a small period of downtime depending on the configuration you'd like to implement.

If you have multiple VIP's on your WebCelerator, we can configure more than one of these configuration options to suit a multi-tennant environment.

## Diagram of SSL configuration options

<center>![WebCel SSL Comparason](images/WebCel-SSL.png)</center>

## SSL Passthrough

When using SSL passthrough, we will transparrently proxy the HTTPS connection to your backend over layer 4.

All connections to the backend will be received on port 443, so your backend will continue to behave as normal in terms of redirection rules checking for HTTPS traffic; however as we can't inject headers into the request, the only IP you'll be able to retrieve is the WebCelerators IP address.

This allows your backend server to remain in control of the entire SSL handshake.

## SSL Offloading

When using SSL offloading, we decrypt and remove the SSL element of the request when it passes through the WebCel. To do this, we install your SSL certificate onto the WebCel and then handle all traffic from therein as HTTP.

Once the traffic is decrypted, we can inspect the request to determine whether it should be served from cache or piped to the backend server.

To allow you to identify from the backend whether the traffic originated as HTTPS or not, we add the `X-Forwarded-Proto` header onto the request which will be set to `https` if the request was originally HTTPS.

Further to this, we also add a `X-Forwarded-For` header onto the request containing the originating IP address of the request, which will allow you to retrieve the client IP in your applcication rather than the WebCelerator IP.

### Apache HTTPS redirection fix

Some clients have found that adding the following to the top of their `.htaccess` file fixes issues with redirection loops:

```
SetEnvIf X-Forwarded-Proto https HTTPS=on
```

### NGINX HTTPS redirection fix

Some clients have found that adding the following to their NGINX configuration for a domain fixes issues with redirection loops:

```
if ($http_x_forwarded_proto = "https") {
    set $fastcgi_https "on";
}
```

## Secure Origin Pull

With the secure origin pull configuration, traffic is first "offloaded" at WebCel level to allow us to inspect the traffic and serve requests from cache; however any requests needing to be passed to the backend are re-encrypted before leaving the WebCelerator and arrive to the backend over port 443.

This means that the backend is (for all intents and purposes) unaware that the traffic has passed through a reverse proxy device. As such, it can behave normally in terms of redirection and shouldn't require any modification to your configuration.

That being said, requests will still appear as though they originated from the WebCelerator - with the actual client IP being passed under the `X-Forwarded-For` header.

While this has a small performance overhead from the two encryption steps, this is negligable on modern hardware, and the benefit of having the WebCelerator as a "drop-in" solution to caching static content on your site outweighs this in most instances.
