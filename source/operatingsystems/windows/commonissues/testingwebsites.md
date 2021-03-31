# Testing Websites

The easiest way to preview your website before making changes to DNS is through the modification of your hosts file on your PC/Server.

The hosts file is a computer file used by an operating system to map hostnames to IP addresses and can be used to bypass DNS.

The hosts file is located in `C:\Windows\System32\Drivers\etc\hosts`. You need to be an administrator to update this file. Right-click on Notepad and click "Open as Administrator", then browse to the file and open it.

The formatting for the hosts file looks like this:

```console
127.0.0.1       domain.com
::1             domain.com
```

Where the IP address on the left is the IP to resolve to and the entry on the right is the domain in question. In this instance with the entries above, when browsing to `domain.com` your machine would automatically direct you to `domain.com` hosted on `127.0.0.1`.

On Linux and macOS the file is located in `/etc/hosts`, and it is in the same format as above.

You can test your hosts file is working by running a `ping` against the domain in question.

```eval_rst
  .. title:: Testing websites on Windows
  .. meta::
     :title: Testing websites on Windows | UKFast Documentation
     :description: Information on testing websites on Windows by modifying the hosts file
     :keywords: ukfast, windows, testing, websites, cloud, server, web, tutorial, guide
```
