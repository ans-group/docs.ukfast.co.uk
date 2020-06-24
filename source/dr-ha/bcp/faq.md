# Frequently asked questions

```eval_rst
   .. title:: BCP | Frequently Asked Questions
   .. meta::
      :title: BCP | Frequently Asked Questions | UKFast Documentation
      :description: Frequently asked questions on the UKFast Business Continuity Platform
```

Some of the most commonly asked questions by clients when receiving their first cluster, and a couple of recommendations for getting started quickly with BCP.

## Tips

- Before going live, read the documentation provided here, [attempt a failover](management) of your services, make sure you're confident with how you interact with the cluster and have an understanding of the architecture. This will save you time when you come to perform maintenance on your servers or application.

- Test thoroughly while you're not actively using this cluster; make sure your application works properly, make use of a [hosts file](/operatingsystems/windows/commonissues/testingwebsites) to simulate the live site prior to changing your DNS over.

- This is written several times in this documentation, but as it causes frequent issues: **do not use `service` or `systemctl` when managing clustered services** - this doesn't matter for services outside of the cluster (`vsftpd` for example), but might cause failover on a service managed by PCS.

- Make sure you're not currently inside a clustered volume (eg: `/var/www/vhosts`) before restarting a cluster group. An easy way to check is by running `pwd` or checking the "working directory" output on your FTP client.

***

## Common questions

### What IP address should I use for my A record?

Depending on the solution deployed, the answer to this will vary:

- If you have a solution containing a [Webcelerator](/webcel/), then you should use the VIP associated to that device.
- If you have a solution containing a [Load Balancer](/network/loadbalancing), then the VIP associated to the ruleset for this cluster should be used.
- If you have a [two node cluster with no edge device](generalinformation.html#two-node-active-passive-clusters), then the web VIP should be used.

If you have a solution to which more than one of the above is true, you should use whichever is the highest device in your solution diagram - usually this would be the Webcelerator or DDoS Mitigator.

***

### I can't see *"/var/www/vhosts"* or *"/var/lib/mysql"* on one of the nodes?

For volumes using DRBD to replicate between nodes, the mount point will only appear on the active node.

**[Read more →](drbd)**

***

### Running *"service servicename restart"* isn't working?

Clustered services do not always use the `systemd` script shipped with the package to start up. In the case of an `ocf:heartbeat:apache` resource (for example), the `httpd` service is started by a direct call to the binary rather than through a service startup.

However, the use of a `service` or `systemctl` command on a clustered service is discouraged, and should be managed through `pcs` instead.

**[Read more →](management)**

***

### What configuration should I use for MySQL in my application?

This depends on your solution:

- If you have a [two node cluster](generalinformation.html#two-node-active-passive-clusters) without 10GBPS switching, `10.1.0.3` should be used as the host, and the username and password you used when configuring your `GRANT` in MySQL would be used to connect.

- If you have a [two node cluster](generalinformation.html#two-node-active-passive-clusters) with 10GBPS switching, or a [four or more node cluster](generalinformation.html#four-node-active-active-clusters), the internal version of the VIP for MySQL should be used.

***

### There are two (or more) unexpected servers showing in MyUKFast

To enable the use of monitoring and backups on a VIP, we create a "placeholder" server which contains no specification but has the VIP as it's primary IP address. Normally these are configured to be inactive in our database, so aren't seen - but on occasion we need to set them active to perform certain functions.

These can be ignored for the most part, unless reviewing backups / monitoring associated to the "server", and are a for our administrative purposes only.

If in doubt, contact support for clarification.
