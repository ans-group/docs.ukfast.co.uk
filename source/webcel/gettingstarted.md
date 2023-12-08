# Getting started

Once your Webcelerator is ready, you will receive a virtual IP address (VIP) from our launch team (also known as a floating IP). If you have more than one Webcelerator, these VIPs will keep traffic moving through the active Webcelerator, even if one is offline. Web traffic hitting your VIP will pass through the cache before being sent through the firewall, onto the backend web server to request any missing assets.

```eval_rst
.. note::
   You can have multiple VIPs that each point to a different set of backend web servers, e.g.

   * VIP1 -> Web server1 & Web server2
   * VIP2 -> Web server2 & Web server3
```

## Testing with a hosts file

To begin with, we recommend performing a test from a local machine or server by changing the hosts file to point your domain to one of the Webcelerator's VIPs. This allow you to test your Webcelerator configuration without affecting the live site. Please see the following guide for information about how to change your host file within [Windows, Mac or Linux](http://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/).

For example, if your VIP was `198.51.100.200` and your domain was `www.example.com` you would add the following to your hosts file (which is the same for every operating system):

```console
198.51.100.200 example.com www.example.com
```

It's important that you put any required subdomains on the same line as well, especially the www subdomain (even if you normally redirect to remove it). On Windows, you may need to flush your DNS cache too by running the following command:

```console
ipconfig /flushdns
```

Now when browsing to your site via this machine, your request and website will be served through the Webcelerator. At first your cache will be empty, so you're not going to see much performance benefit, but browse around using your browser's developer tools and your response times for static content like images and CSS should dropping. These items are starting to be served from the cache rather than your web servers.

Now you're ready to start the testing phase; ensuring your [SSL is configured correctly](/webcel/ssl), and your client IP address handling is present and correct.

```eval_rst
   .. title:: Webcelerator | Getting Started
   .. meta::
      :title: Webcelerator | Getting Started | ANS Documentation
      :description: Getting started with a UKFast Webcelerator
```
