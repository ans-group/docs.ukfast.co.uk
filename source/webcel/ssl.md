# SSL Certificates on a WebCelerator

As the WebCelerator acts as a reverse proxy to your backend servers, usually at the edge of your network, you'll probably need to consider how to handle SSL certificates for sites running through the WebCelerator.

There are three options for SSL configuration, depending on your needs:

- **SSL Passthrough** *(default)*: SSL traffic is passed directly to the backend by a Layer 4 proxy, and is therefore not cached. The SSL handshake occurs with the backend server directly, so traffic is encrypted until it reaches the backend. No caching will occur on HTTPS content.
- **SSL Offloading**: SSL traffic is decrypted when it enters the WebCelerator, so the SSL handshake actually happens with the WebCelerator rather than the backend. Any traffic which needs to be passed onto the backend is handled over HTTP. Caching will occur on HTTPS content.
- **Secure Origin Pull** *(recommended)*: SSL traffic is decrypted when it enters the WebCelerator, allowing inspection of the traffic, and querying of the cache. Any requests needing passing to a backend are re-encrypted and transmitted over HTTPS to the backend. Caching will occur on HTTPS content, and the backend will receive a normal HTTPS request on port 443 for uncached content.

