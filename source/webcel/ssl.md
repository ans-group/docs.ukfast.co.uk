# Configuring SSL

As the Webcelerator acts as a reverse proxy to your backend servers, usually at the edge of your network, you'll probably need to consider how to handle SSL certificates for sites running through it.

There are three options for SSL configuration, depending on your needs:

- **SSL Passthrough** *(default)*: SSL traffic is passed directly to the backend by a Layer 4 proxy, and is therefore not cached. The SSL handshake occurs with the backend server directly, so traffic is encrypted until it reaches the backend. No caching will occur on HTTPS content.
- **SSL Offloading**: SSL traffic is decrypted when it enters the Webcelerator, so the SSL handshake actually happens with the Webcelerator rather than the backend. Any traffic which needs to be passed onto the backend is handled over HTTP. Caching will occur on HTTPS content.
- **Secure Origin Pull** *(recommended)*: SSL traffic is decrypted when it enters the Webcelerator, allowing inspection of the traffic, and querying of the cache. Any requests needing passing to a backend are re-encrypted and transmitted over HTTPS to the backend. Caching will occur on HTTPS content, and the backend will receive a normal HTTPS request on port 443 for uncached content.

Configuring the Webcelerator to handle SSL may require a small period of downtime depending on the option you'd like to implement.

If you have multiple VIPs on your Webcelerator, we can set up more than one of these configuration options to suit a multi-tenant environment.

## Diagram of SSL configuration options

<center>![Webcel SSL Comparison](images/WebCel-SSL.png)</center>

## Comparison of SSL configuration options

<table>
  <thead>
    <tr>
      <th></th>
      <th>Pro's</th>
      <th>Con's</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>SSL Passthrough</th>
      <td>
        <ul>
          <li>SSL certificate is controlled by the backend.</li>
          <li>No SSL-encrypted content is cached by the Webcel.</li>
          <li>No additional configuration is required at Webcel level.</li>
          <li>Redirection loops as a result of implementing the Webcel are unlikely.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Any traffic sent over HTTPS will not be cached.</li>
          <li>If all traffic is HTTPS, the Webcel will not cache anything.</li>
          <li>If the backend goes offline, HTTPS traffic will receive a "connection refused" error.</li>
          <li>We are unable to manipulate or alter the flow of traffic through the Webcel, other than it's destined backend.</li>
          <li>All requests will appear as being from the Webcel's IP in access logs. We are not able to pass the client IP through to the backend</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>SSL Offloading</th>
      <td>
        <ul>
          <li>HTTPS traffic can be cached and served from cache.</li>
          <li>Slight performance increase on the backend from no longer needing to perform the SSL handshake.</li>
          <li>Support for more modern SSL technologies (HTTP2, TLS 1.2, etc).</li>
          <li>Ability to interact with and manipulate HTTPS traffic flowing through the Webcel.</li>
          <li>Client IP will be passed onto the backend with the <code>X-Forwarded-For</code> header.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Traffic passed to the backend will be sent over HTTP.</li>
          <li>As a result of the above, any force-HTTPS redirects not checking <code>X-Forwarded-Proto</code> might cause redirection loops.</li>
          <li>If configured to do so, and depending on the application, this might result in some session-related information being cached.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>Secure Origin Pull</th>
      <td>
        <ul>
          <li>HTTPS traffic can be cached and served from cache. Plus all of the benefits of offloading.</li>
          <li>Traffic is re-encrypted before leaving the device, so never traverses the network in plain text.</li>
          <li>Traffic is sent to the backend over port 443 in HTTPS, so shouldn't encounter redirection loops.</li>
          <li>The most "drop-in" configuration for a Webcel with HTTPS and caching in place.</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Slightly increased latency for any request passed to the backend as a result of the overhead of decrypting and re-encrypting the traffic.</li>
          <li>The SSL needs installing on both the Webcelerator and the backend server for this to work.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## SSL Passthrough

When using SSL passthrough, we will transparently proxy the HTTPS connection to your backend over layer 4.

All connections to the backend will be received on port 443, so your backend will continue to behave as normal in terms of redirection rules checking for HTTPS traffic; however as we can't inject headers into the request, the only IP you'll be able to retrieve is the Webcelerator's IP address.

This allows your backend server to remain in control of the entire SSL handshake.

## SSL Offloading

When using SSL offloading, we decrypt and remove the SSL element of the request when it passes through the Webcel. To do this, we install your SSL certificate onto the Webcelerator and then handle all traffic from therein as HTTP.

Once the traffic is decrypted, we can inspect the request to determine whether it should be served from cache or piped to the backend server.

To allow you to identify from the backend whether the traffic originated as HTTPS or not, we add the `X-Forwarded-Proto` header onto the request which will be set to `https` if the request was originally HTTPS.

We also add a `X-Forwarded-For` header onto the request containing the originating IP address of the request, which will allow you to retrieve the client IP for use in your application.

### Apache HTTPS redirection fix

Some clients have found that adding the following to the top of their `.htaccess` file fixes issues with redirection loops:

```apache
SetEnvIf X-Forwarded-Proto https HTTPS=on
```

Alternatively, some clients have found that placing the following `RewriteRule` into their `.htaccess` file has worked:

```apache
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]
```

### NGINX HTTPS redirection fix

Some clients have found that adding the following to their NGINX configuration for a domain fixes issues with redirection loops:

```nginx
if ($http_x_forwarded_proto = "https") {
    set $fastcgi_https "on";
}
```

Alternatively, some clients have found that placing the following into a `server { }` block configured to `listen 80;` has worked:

```nginx
if ($http_x_forwarded_proto != "https") {
    return 301 https://example.com$request_uri;
}
```

## Secure Origin Pull

With the secure origin pull configuration, traffic is first "offloaded" at Webcelerator level to allow us to inspect the traffic and serve requests from cache; however any requests needing to be passed to the backend are re-encrypted before leaving the Webcelerator and arrive to the backend over port 443.

This means that the backend is basically unaware that the traffic has passed through a reverse proxy device. As such, it can behave normally in terms of redirection and shouldn't require any modification to your configuration.

That being said, requests will still appear as though they originated from the Webcelerator - with the actual client IP being passed under the `X-Forwarded-For` header.

While this has a small performance overhead from the two encryption steps, this is negligible on modern hardware, and the benefit of having the Webcelerator as a "drop-in" solution to caching static content on your site outweighs this in most instances.
