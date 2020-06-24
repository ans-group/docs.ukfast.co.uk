# Managing your cluster

```eval_rst
   .. title:: BCP | Managing Your Cluster
   .. meta::
      :title: BCP | Managing Your Cluster | UKFast Documentation
      :description: Information on how to manage your BCP luster
```

When moving from a standard Linux server with a LAMP stack (for example), there are a number of differences in how you manage the server and its services. Further to this, consideration to the cluster architecture should be given before adding new services or applications onto your nodes.

We utilize of the RedHat clustering suite, which uses Pacemaker (`pcs`) as the cluster manager.

```eval_rst
.. seealso::
   Further reading about PCS on RedHat for those interested:

   - `RedHat Pacemaker documentation <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/High_Availability_Add-On_Administration>`_
   - `ClusterLabs Pacemaker documentation <http://clusterlabs.org/doc/>`_
```

## Service management

Services which are managed by the cluster should only be started / stopped / restarted by the cluster manager (PCS) - **not through the use of the `service`, `systemctl`, or `/etc/init.d/` commands**. Performing these actions via the aforementioned commands does not inform PCS that the service status was intended to change, and may result in the node being [fenced](fencing).

For any services which PCS is not aware of, you can continue to use conventional methods of restarting them. If in doubt, it's always best to check with our support team for clarification.

When performing commands on clustered services, it is usually best to run them on the service group (eg: `g_mysql`) rather than an individual resource (eg: `r_mysql_ip`).

### Clustered service status

To view the current clustered services, their status, and the node they're running on, use the `pcs status` command:

```bash
[root@acme-webdb-01 ~]# pcs status
Cluster name: acme-webdb
Stack: corosync
Current DC: acme-webdb-02 (version 1.1.15-11.el7_3.5-e174ec8) - partition with quorum
Last updated: Fri Jul 14 13:01:21 2017          Last change: Wed Jul 12 12:20:00 2017 by root via crm_resource on acme-webdb-01

2 nodes and 15 resources configured

Online: [ acme-webdb-01 acme-webdb-02 ]

Full list of resources:

 acme-webdb-01-stonith   (stonith:fence_idrac):  Started acme-webdb-02
 acme-webdb-02-stonith   (stonith:fence_idrac):  Started acme-webdb-01
 Clone Set: ping-clone [ping]
     Started: [ acme-webdb-01 acme-webdb-02 ]
 Master/Slave Set: ms_web_drbd [r_web_drbd]
     Masters: [ acme-webdb-01 ]
     Slaves: [ acme-webdb-02 ]
 Resource Group: g_web
     r_web_fs   (ocf::heartbeat:Filesystem):    Started acme-webdb-01
     r_web_ip   (ocf::heartbeat:IPaddr2):       Started acme-webdb-01
     r_web_httpd        (systemd:httpd):        Started acme-webdb-01
 Master/Slave Set: ms_mysql_drbd [r_mysql_drbd]
     Masters: [ acme-webdb-02 ]
     Slaves: [ acme-webdb-01 ]
 Resource Group: g_mysql
     r_mysql_fs (ocf::heartbeat:Filesystem):    Started acme-webdb-02
     r_mysql_ip (ocf::heartbeat:IPaddr2):       Started acme-webdb-02
     r_mysql_int_ip     (ocf::heartbeat:IPaddr2):       Started acme-webdb-02
     r_mysql    (ocf::heartbeat:mysql): Started acme-webdb-02

Daemon Status:
  corosync: active/enabled
  pacemaker: active/enabled
  pcsd: active/enabled
[root@acme-webdb-01 ~]#
```

The above shows that the `g_web` group contains: the web VIP, web filesystem, and `httpd` service. It is started and running on the `acme-webdb-01` node. The `g_mysql` service is running on `acme-webdb-02`, and contains: the MySQL external VIP, the MySQL crossover VIP, the MySQL filesystem, and the `mysqld` service.

If any services show as failed, you would normally receive information about the errors encountered at the end of this output.

To view more detailed information about the configuration of the individual resources in the group, use the `pcs config show` command.

At the very top of the output, the `acme-webdb-01-stonith` and `acme-webdb-02-stonith` resources are listed and running on the opposing node to their name. These are used to send [fence](fencing) commands to recover a node from failure.

If you think that the output from `pcs status` is inaccurate, you can run `pcs resource cleanup` to re-check the status of all the resources in the cluster - or `pcs resource cleanup r_mysql_int_ip` (for example) to re-check an individual resource.

### Stopping clustered services

To stop a clustered service, you should issue the following command swapping `g_mysql` for the group you want to stop):

```bash
[root@acme-webdb-01 ~]# pcs resource disable g_mysql
```

This will shut down the service on it's active node, and instruct the passive node not to take over, and should be considered equivalent to running `service mysqld stop`.

```eval_rst
.. note::
   Services are started in-order in PCS, so if you disable a resource in the middle of a group (`r_mysql_ip` for example), it will also stop all the services following it in the list (eg: `r_mysql_int_ip` and `r_mysql` would also stop).

   Simlarly, if one of the resources in a group fails, the whole group will attempt to recover on the other node or stop.
```

### Starting clustered services

To start a service which you've disabled in the cluster, run the following (swapping `g_mysql` for the group you want to start):

```bash
[root@acme-webdb-01 ~]# pcs resource enable g_mysql
```

This will update the PCS configuration to mark the resource enabled, and it might take a few seconds before the cluster actually starts the group up. You can monitor the output of `pcs status` to see it start up with the following:

```bash
[root@acme-webdb-01 ~]# watch -n1 "pcs status"
```

Press `CTRL + C` to exit this watch screen.

### Restarting clustered services

To restart a cluster service, run the following command (swapping `g_mysql` for the group you want to restart):

```bash
[root@acme-webdb-01 ~]# pcs resource restart g_mysql
```

It is best to restart whole resource groups where possible to prevent unexpected behavior.

### Moving a cluster service to another node

When performing maintenance for a node, you might want to move the resources running there onto its counterpart. To do that, we will use the `pcs resource move` command, however this has a caveat.

The way PCS "moves" a resource is by creating a `ban` constraint for the node it is running on at the moment. For example, if `g_mysql` was running on `acme-webdb-02` and you issued a move command, PCS would add a constraint which prevents `g_mysql` from starting on `acme-webdb-02` any more.

When PCS next checks the status of the cluster, it will reconcile the rule that is now being violated (`g_mysql` is running on `acme-webdb-02`, which is is banned from) by stopping the service and starting it on `acme-webdb-01`.

However, if you left the cluster in this state, you would not be able to move the service back to `acme-webdb-02`. If `acme-webdb-01` were to fail at this point, `g_web` would move over to `acme-webdb-02`, but `g_mysql` would fail to start and enter a stopped state.

As such, you should perform the following steps:

1. Issue a `pcs resource move` command to add the `ban` constraint:

    ```bash
    [root@acme-webdb-01 ~]# pcs resource move g_mysql
    ```
2. Watch the output of `pcs status` until you've confirmed the group has fully moved over:

    ```bash
    [root@acme-webdb-01 ~]# watch -n1 "pcs status"
    ```
3. Issue a `pcs resource clear` command to remove the `ban` constraint:

    ```bash
    [root@acme-webdb-01 ~]# pcs resource clear g_mysql
    ```

This will not move the resource group back over unless a `prefers` or `colocation` constraint is now being violated (which in most cases it would not be); however the resource group is now free to be moved again in the future, or failover as needed.

### Putting a node into standby

You can temporarily disable a node in the cluster by running the following command **on the node that you want to disable**:

```bash
[root@acme-webdb-01 ~]# pcs cluster standby
```

This will move any resources running on the node off to other members, essentially putting the node into a "maintenance mode" of sorts.

```eval_rst
.. note::
   We have found that putting a node into standby mode can cause the DRBD volumes to be disconnected by PCS, which can prevent DRBD replication from taking place while the node is in standby. As such, having standby enabled for long periods of time is discouraged.

   If you're unsure about using ``pcs cluster standby``, make use of the ``pcs resource move`` commands instead to make a node passive.
```

### Taking a node out of standby

To put a node back into service after `pcs cluster standby` has been performed on it, run the following **on the node you want to enable**:

```bash
[root@acme-webdb-01 ~]# pcs cluster unstandby
```

Resources will not move back over to the node unless a `prefers` or `colocation` constraint are currently being violated, so you might want to manually perform a `pcs resource move` to balance services out again.

## Resource constraints

Constraints are used to define 'rules' which define where resources are started up within the cluster. These are also used by some PCS commands to facilitate certain functions, such as the `pcs resource move` command.

### Viewing configured constraints

You can view the current constraints configured on the cluster with the following:

```bash
[root@acme-webdb-01 ~]# pcs constraint show --full
Location Constraints:
  Resource: acme-webdb-01-stonith
    Enabled on: acme-webdb-02 (score:INFINITY) (id:location-acme-webdb-01-stonith-acme-webdb-02-INFINITY)
  Resource: acme-webdb-02-stonith
    Enabled on: acme-webdb-01 (score:INFINITY) (id:location-acme-webdb-02-stonith-acme-webdb-01-INFINITY)

[...]

Ticket Constraints:
[root@acme-webdb-01 ~]#
```

These should be managed carefully as an incorrect constraint cause unexpected behaviour, and you might take the resources offline.
