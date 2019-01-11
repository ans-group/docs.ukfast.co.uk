# HTTP Error Codes

Having a Webcelerator in front of your solution can present you with new error codes to deal with and understand, next to the usual 404s and 500s you normally see. These are as follows:

- **502 Bad Gateway** – The backend web server returned a response that the cache was unable to handle or was invalid. This usually indicates a problem on the web servers rather than something wrong with the Webcelerator. If you see this message, you should attempt to repeat your request to the backend server itself and see if it's returning a valid response (you can do this with a [hosts file change](gettingstarted) if you've already pointed your DNS through the Webcelerator).

- **503 Service Unavailable** – All backend web servers are offline. If you see this message, the Webcelerator is unable to communicate with any of your web servers, thus it returns this message. By default, the Webcelerator will attempt to make a backend connection five times before returning this status code. Seeing this message usually indicates that an error is occurring on your web servers that needs investigating.

- **504 Gateway Timeout** – The backend web server did not respond fast enough. If you have a page that performs a lot of processing before returning a result, you might see this error. It can also indicate a performance problem on the web servers. We can increase timeouts on the Webcelerator in order to prevent this message from occurring.
