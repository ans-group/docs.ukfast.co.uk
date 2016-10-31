# Testing Websites

The easiest way to preview your website before making changes to DNS is through the modification of your hosts file on your PC/Server.

The hosts file is a computer file used by an operating system to map hostnames to IP addresses and can be used to bypass DNS.

The hosts file is located in: C:\Windows\System32\Drivers\etc\ and is named "hosts".

The formatting for the hosts file looks like this:

	127.0.0.1       domain.com
	::1             domain.com

Where the IP address on the left is the IP to resolve to and the entry on the right is the domain in question. In this instance with the entries above, when browsing to domain.com your machine would automatically direct you to domain.com hosted on 127.0.0.1
