# Getting started

So, as part of your expansion plans for improving your site, you've purchased a Webcelerator (or two, to be fully redundant) that will allow you to expand without adjusting the rest of your solution too much. Here's what to do next.

Once your Webcelerator is ready, you will receive your VIP from UKFast support (also known as a floating IP). If you have more than one Webcelerator, these VIPs will move between them as failover events occur, rerouting traffic through the working Webcelerator. Web traffic hitting your VIP will pass through the cache before being sent onto the backend web server if necessary.

You can have multiple VIPs that each point to a different set of backend web servers *(e.g. VIP1 -> Web server1 & Web server2, VIP2 -> Web server2 & Web server3, etc)*. We'll keep things simple for this example, but remember that the Webcelerator can be as flexible as you need it to be.

## Testing with a hosts file

To start with we recommend doing a test from a local machine or server, by changing the hosts file to point your domain to one of the webccelerator's VIPs that you were provided with. This lets you test your Webcelerator configuration without affecting the live site or any other visitors. Here are some links to help you change your hosts file appropriately:

* **[http://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/](http://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)**
* **[http://www.webhostinghub.com/help/learn/domain-names/dns-nameserver/modfiying-your-hosts-file](http://www.webhostinghub.com/help/learn/domain-names/dns-nameserver/modfiying-your-hosts-file)**
* **[https://support.apple.com/kb/TA27291?viewlocale=en_US&locale=en_US](https://support.apple.com/kb/TA27291?viewlocale=en_US&locale=en_US)**
* **[https://en.wikipedia.org/wiki/Hosts_%28file%29](https://en.wikipedia.org/wiki/Hosts_%28file%29)**

For example, if your VIP was `198.51.100.200` and your domain was `www.example.com` you would add the following to your hosts file (which is the same for every operating system):

```
 198.51.100.200 example.com www.example.com
```

It's important that you put any required subdomains on the same line as well, especially the www subdomain (even if you normally redirect to remove it). On Windows, you may need to flush your DNS cache too – see the link above.

```
C:\> ipconfig /flushdns
```

Now when browsing to your site via this machine, your request and website will then be served through the Webcelerator. Doesn't look any different, does it? At first your cache will be empty, so you're not going to see much performance benefit as you begin to move around your site. Browse around for a bit using Firebug or Chrome Developer Tools and watch your response times for static content like images and CSS. Generally you'll see response times dropping as these items are served from the cache rather than your web servers.

Now you're ready to start the testing phase; ensuring your [SSL is configred correctly](/webcel/ssl.html), and your client IP address handling is present and correct!
