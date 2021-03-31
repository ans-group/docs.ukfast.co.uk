# Distributed Replicated Block Device (DRBD)

DRBD is utilised in our physical Business Continuity Platform (BCP) solutions to replicate data at block level between two or more servers. While not wholly comparable, you could think of it as resembling RAID1 being performed over the network on two volumes.

Generally, there are two DRBD volumes in each cluster:

 - `/dev/drbd0` mounted as `/var/www/vhosts`
 - `/dev/drbd1` mounted as `/var/lib/mysql`

 We connect DRBD to 10Gbps ports wherever possible, and otherwise make use of direct 10Gbps crossover cables to facilitate real-time replication between the member nodes. You'll see this listed as `p1p1` or `p1p2` when looking at the NICs connected to your server.

 DRBD is active / passive by nature, so only one node can be "primary" for the volume at a time - and therefore only one node can have the volume mounted at a time. If more than one node considers itself "primary", the cluster has likely become [split brain](/dr-ha/bcp/splitbrain).

 Given the above, don't be alarmed if `/var/www/vhosts` or `/var/lib/mysql` looks to be "missing" from one of your nodes, it is probably mounted elsewhere in the cluster.

 ## Viewing DRBD replication status

 To confirm that DRBD is synchronised, or that the node you're logged into is "secondary", you can run `cat /proc/drbd`:

 ```bash
 [root@acme-webdb-01 ~]# cat /proc/drbd
 version: 8.4.9-1 (api:1/proto:86-101)
 GIT-hash: 9976da086367a2476503ef7f6b13d4567327a280 build by akemi@Build64R7, 2016-12-04 01:08:48
  0: cs:Connected ro:Primary/Secondary ds:UpToDate/UpToDate C r-----
     ns:22341096 nr:4576 dw:22345672 dr:41373565 al:1464 bm:0 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:0
  1: cs:Connected ro:Secondary/Primary ds:UpToDate/UpToDate C r-----
     ns:15052 nr:37890252 dw:37905304 dr:40297 al:14 bm:0 lo:0 pe:0 ua:0 ap:0 ep:1 wo:f oos:0
 [root@acme-webdb-01 ~]#
 ```

 In this output the `0:` item denotes the DRBD device number, and `Primary/Secondary` shows the local node status first, then the remote node status. The `UpToDate/UpToDate` element follows the same format, and shows that DRBD is synchronised.

 If these show `WFConnection`, `Primary/Unknown`, or `StandAlone/Unknown`, please contact support immediately.

```eval_rst
   .. title:: Distributed Replicated Block Device (DRBD)
   .. meta::
      :title: Distributed Replicated Block Device (DRBD) | UKFast Documentation
      :description: Information on how to manage your FASTcloudbackup account
```
