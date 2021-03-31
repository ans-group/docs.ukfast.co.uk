# Installing, updating, and configuring software

```eval_rst
   .. title:: BCP | Installing, Updating, and Configuring Software
   .. meta::
      :title: BCP | Installing, Updating, and Configuring Software | UKFast Documentation
      :description: How to install, update and configure software for BCP platforms
```

The only information replicated between the cluster is that stored in clustered volumes [DRBD](drbd), NFS, or SAN storage), and that which is copied over via [Unison](unison).

When it comes to software installed on the cluster, this is not replicated between the two.

As such, if you update the software on `acme-webdb-01`, you will also need to perform the same update on `acme-webdb-02`. The same goes for installing new software or replacing software.

If any new software installed on the server needs to be part of the cluster, consideration will need to be given to how this should be implemented; and is probably best discussed with our support team to make sure the implementation of additional clustered services doesn't impact your service in a failover scenario.

This includes the installation of Apache modules, PHP modules, or changing PHP versions.

A good example of additional clustered services is a requirement for a <nospell>Node.js</nospell> application that serves webhooks for your site, and needs to run on the same node as the web service - depending on the reliability and importance of the <nospell>Node.js</nospell> element, you might need to implement this into the cluster differently.

```eval_rst
.. warning::
   **If the software versions between cluster nodes are different, or you haven't synchronised the configuration between nodes, your sites may go offline in the event of a failover.**

   In these cases, the failover will be successful from PCS' perspective, but your application won't be able to connect to required software / use required PHP modules / use the correct PHP version / etc, so might show errors or not work at all.
```

## Checking whether your nodes match

To check whether the software versions match on both nodes, you can perform the following command (changing the hostname to match your solution):

```bash
[root@acme-webdb-01 ~]# diff <(rpm -qa | sort) <(ssh -p2020 acme-webdb-02 "rpm -qa | sort")
```

If there are any differences highlighted, you should seek to reconcile these so that both nodes have all software required to run your application.

## Adding new clustered software

As already mentioned, it is best to consult with support before adding new clustered services.

Some methods of adding services into the cluster:

- Add a new resource to the end of the `g_web` (for example) resource group so that the service starts with the web service each time. Then storing the files for this additional service in the related [clustered volume](drbd), or copy them over with [Unison](unison).

- Add a new resource group for this service, with either a new external VIP or an internal-only VIP running over the MySQL crossover cable, and copy the data between nodes using [Unison](unison). Then add resource constraints to prefer services run together or prefer to run on opposite nodes.

- Run the service standalone on both servers, and have the application look at localhost (127.0.0.1) when connecting to the service. This usually works for caching services like Redis - so the cache would need rebuilding in the event of a failover.

Notwithstanding, your service might not be compatible with the options listed above, however these should give a guide on what is possible.

```eval_rst
.. note::
   It is important that you ensure any configuration required for additional software (clustered or otherwise) is replicated between nodes. Otherwise, you risk having your site go offline in the event of a failover as a result of mismatched configuration between nodes or service startup failure.

   - :doc:`/dr-ha/bcp/unison`

```
