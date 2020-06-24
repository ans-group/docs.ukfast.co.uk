# Unison file-level replication

```eval_rst
   .. title:: BCP | Unison File-Level Replication
   .. meta::
      :title: BCP | Unison File-Level Replication | UKFast Documentation
      :description: Information abotu Unison file-level replication on BCP platforms
```

In order to keep configuration files and credentials synchronized between all nodes in the cluster, we run a regular [cron job](/operatingsystems/linux/basics/cron) to check on the files specified in the Unison configuration.

## Configuring Unison

We release clusters with a basic configuration that will keep the configuration files for your chosen webserver and database server in sync between the nodes. If you store your configuration files somewhere non-standard, or would like to have more files synchronized and available on both nodes at the same time (eg: `/etc/sysconfig/memcached` to ensure memcached is configured the same way on all nodes), you will need to modify the Unison settings.

To configure Unison, edit the `/root/.unison/default.prf` file with your favourite text editor *(to avoid arguments, `vim` is the correct answer to that question)*.

```eval_rst
.. note::
   The configuration file for Unison is different on all nodes in your cluster, so you will need to update all of them when making changes.
```

For solutions with more than two nodes, the configuration on each node might be located in `/root/.unison/hostname.prf`, where "hostname" is replaced with the hostname of each of the nodes you're syncing with (eg: `/root/.unison/acme-web-01.prf`, `/root/.unison/acme-web-02.prf`, and `/root/.unison/acme-web-03.prf`).

The configuration will look something like this:

```
root = /
root = ssh://acme-webdb-02//

path = var/spool/cron/
path = etc/passwd
path = etc/shadow
path = etc/group
path = etc/motd
path = etc/drbd.conf
path = etc/cluster/cluster.conf
path = etc/php.ini

ignore = Name access.log*
ignore = Name error.log*
```

To add more files into Unison, add another `path =` line to the file, using a full path to the file omitting the leading `/`.

Directories are denoted by the trailing `/` at the end of the path, and will be recursively copied.

Once this file has been saved, it will take effect from the next run of the [cron job](/operatingsystems/linux/basics/cron), which should be configured similar to the following as the `root` user:

```
* * * * * /usr/bin/file_sync.sh
```

If that cron is not configured, Unison replication will not work.

```eval_rst
.. warning::
   **Please note that some of the paths configured in Unison are used to ensure proper functioning of the cluster, so check with support before removing any lines from the default Unison configuration.**

   Also, Unison will not work if the default SSH keys for the root user are changed. As such, if you regenerate these keys for some reason, please ensure that the nodes each have the public keys in their ``authorized_keys`` file for the root user.
```

## Manually performing a synchronization

You can force Unison to perform a sync by running the following command:

```bash
[root@acme-webdb-01 ~]# /usr/bin/file_sync.sh
```

However, as this doesn't provide a verbose output, you can use the following to see what Unison is doing:

```bash
[root@acme-webdb-01 ~]# /usr/bin/unison -sshargs "-p 2020"
```
