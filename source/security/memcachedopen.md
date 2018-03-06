# Memcached security concerns and reflection/amplification DDoS attacks

A DDoS attack method utilising memcached servers exposed to the public internet has come to light, and resulted in a number of extremely large DDoS attacks (this attack vector has been given the name "Memcrashed").  The root cause of this is vulnerable memcached servers that have been deployed without sufficient protection.  Attackers are able to utilise these vulnerable servers to launch large-scale reflection/amplification attacks at specific IP addresses.

The attack makes use of the UDP capabilities of memcached, but this has highlighted previously known issues
with memcached security where the service is open to the world with no authentication. This could also potentially
expose sensitive information.

## Checking your security

You should check if you have the TCP port open as well your level of authentication.  You can do this with following command if you
have the netcat utility installed:

    $ echo  "stats items" | nc <server_ip> 11211
	
Please note you will need to run this from an external server.
	
If you see output in the form of "STAT items", you should consider reviewing the security of the memcached instance.

It's a little more difficult to review whether you have the UDP ports open, to do this you'll need to check your firewall settings.
If you're unsure, please ask UKFast Support to check your firewall settings for you - just raise a support ticket in [MyUKFast](https://my.ukfast.co.uk/pss/).

```eval_rst
.. note::

   You should also consider checking and locking down non-standard ports.

```   
	

## Securing memcached

You have multiple options to fix this security issue for memcached. You should always consider adding authentication
to the service, but it's understandable if for performance issues you wish to exclude that option. If you decide to go
without authentication then you **will** need to opt for one of the networking options below instead.

### Authentication

Guidance on implementing authentication for memcached can be [found here](https://github.com/memcached/memcached/wiki/SASLAuthProtocol).

In addition to running authentication we do also recommend you remove public access to the ports on your server.

### Networking

#### Bind to localhost

To bind memcached to localhost, you will need to modify your config with the appropriate options.
On Debian-based systems you can simply modify '/etc/memcached.conf' to include the following line:

    -l 127.0.0.1

For CentOS derivatives, modify '/etc/sysconfig/memcached' to include '-l 127.0.0.1' in the options variable. Here's an example:

    OPTIONS="-l 127.0.0.1"

Don't forget to also restart the memcached service to pick up these changes:

    service memcached restart
	
You should also verify that memcached is indeed only listening on the localhost with this command:

    netstat -plunt
	
#### Whitelist IP's on your firewall

You can modify your firewall rules to block any IP's which are not listed. This can be done at a software firewall level or on a hardware firewall.
It is recommended you do this at the hardware firewall level. Please read [our guidance on configuring your firewalls with UKFast](/security/firewalls/)

## Post checks

Once you've secured memcached, double check that it is actually secure. Re-run the command outlined in [Checking your security](#checking-your-security), or alternatively contact [UKFast Support](https://my.ukfast.co.uk/pss/) and we can take a look for you.

 ```eval_rst
   .. meta::
      :title: Open memcached exploit | UKFast Documentation
      :description: Guidance on securing open memcached instances
      :keywords: ukfast, linux, security, vulnerability, memcached, hosting, ddos, udp, reflection, amplification
