# Memcached security

Recently a new DDoS reflection attack technique using open memcached servers was found and used to perform the
largest recorded DDoS attack against the website Github.

The attack makes use of the UDP capabilities of memcached, but this has highlighted previously known issues
with memcached security where the service is open to the world with no authentication. This could potentially
expose sensitive information.

## Checking the security

To check if you have the tcp port open as well as no authentication, you can run the following command if you
have the netcat utility installed:

    $ echo  "stats items" | nc <server_ip> 11211
	
Please note you will need to run this from an external server to check.
	
If you see output in the form of "STAT items", you should consider reviewing the security of the memcached instance.

It's a little more difficult to review whether you have the UDP ports open and will require checking the firewall settings.
If you're unsure, feel free to ask support to check your firewall settings to see if udp port is open.

    Please note: This does not account for none-standard ports. You should still consider locking down non-standard ports.
	

## Securing memcached

You have multiple options to fix this security issue for memcached. You should always consider adding authentication
to the service, but it's understandable if for performance issues you wish to exclude that option. If you decide to go
without authentication then you *will* need to opt for one of the networking options instead.

### Networking

#### Bind to localhost

To bind memcached to localhost, you will need to modify your config with the appropriate options.
On debian based systems you can simply modify '/etc/memcached.conf' to include the following line:

    -l 127.0.0.1

For CentOS derivatives, modify '/etc/sysconfig/memcached' to include '-l 127.0.0.1' in the options variable. Here's an example:

    OPTIONS="-l 127.0.0.1"

Don't forget to also restart the memcached service to pick up these changes:

    service memcached restart
	
You should also verify that memcached is indeed only listening on the localhost with this command:

    netstat -plunt
	
#### Whitelist IP's on firewall

You can modify your firewall rules to block any IP's which are not listed. This can be done at a software firewall level or hardware firewall.
It's recommended you do it at the hardware firewall level. Here's guidance on configuring your firewalls with UKFast - https://docs.ukfast.co.uk/security/firewalls/

### Authentication

Guidance on implementing authentication can be found here - https://github.com/memcached/memcached/wiki/SASLAuthProtocol

It's not recommended that you run just authentication and keep the port open to the world but it should be more
secure than no authentication at all.

## Post checks

Once you've secured memcached, check it's secure! Re run the earlier command, all alternatively contact support and we can take a look for you.

 ```eval_rst
   .. meta::
      :title: Open Memcached Exploit | UKFast Documentation
      :description: Guidance on open memcached instances
      :keywords: ukfast, linux, security, vulnerability, memcached, hosting