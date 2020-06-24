# Fencing / STONITH

In order to recover from failure and file-level locks when performing a failover, the cluster is able to send a STONITH ("Shoot The Other Node In The Head") command to a problem node and force a reboot.

For example: If you attempted to move `g_web` between nodes, but a process was holding one of the files in `/var/www/vhosts` open, the passive node could send a STONITH command to reboot the active node and forcibly takeover it's resource.

This allows the resource to come back online without manual intervention, and helps prevent the situation where the cluster becomes [split brain](splitbrain).

## Common causes of accidental fencing

There are a number of occasions where fencing can be accidentally triggered, which are worth being mindful of:

1. **Performing a restart of `g_web` while your `cwd` is within `/var/www/vhosts`.**

    It is quite common for clients to accidentally trigger a fence by being `cd`'ed into `/var/www/vhosts`, or are performing an SFTP operation to the directory, and running a `pcs` command on the `g_web` service. PCS will attempt to dismount `/var/www/vhosts` and fail because there is a file-level lock on the device. To resolve this issue, the cluster will send a STONITH to the node and reboot it.

    The same stands for restarting any clustered service which has a filesystem as part of the resource group in PCS.

2. **Performing an operation on a clustered service outside of `pcs`.**

    If you attempt to start / stop / restart one of the clustered services via the `service` or `systemctl` command, PCS will not be aware that it is an expected action and will assume something is wrong. This could result in failover and possible fencing of the node.

3. **Full disk on the server or DRBD.**

    When a disk becomes full, services will likely start to throw errors that they can't operate. For example, if `/` became full, MySQL might shutdown because it can't write to its log file. As this was not anticipated by PCS, it might failover or fence the node.

4. **Rebooting one of the nodes.**

    Normally PCS can handle the rebooting of one of its member nodes, but if you don't perform a graceful reboot, there is a chance that a fence command will also be sent in attempt to bring the node back online.
