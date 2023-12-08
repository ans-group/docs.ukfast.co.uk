# Fencing / STONITH

```eval_rst
   .. title:: BCP | Fencing
   .. meta::
      :title: BCP | Fencing | ANS Documentation
      :description: Information about what fencing is and common accidental causes
```

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

## eCloud Fence Agent

If you are hosting your BCP cluster within our eCloud environment, including eCloud VPC, you can optionally use our eCloud Fence Agent to perform STONITH operations on your VMs using the eCloud API.

Please follow the instructions below to install the fence agent on your distribution.

### CentOS 7 / AlmaLinux 8 / RHEL7 / RHEL8

You can run the following commands to enable the ANS repository and install the fence agent. You will require EPEL on CentOS 7 (`yum install epel-release`).

```shell
rpm --import https://repo.ans.uk/keys/RPM-GPG-KEY-ans
curl -sSLo /etc/yum.repos.d/ans-public.repo https://repo.ans.uk/ans-public.repo
yum install fence-ecloud
```

### Ubuntu 20.04 / 22.04

On Ubuntu, the following commands will enable the ANS repository and install the fence agent:

```shell
mkdir -p /etc/apt/keyrings
curl -sLo /etc/apt/keyrings/ans-public.asc https://repo.ans.uk/keys/RPM-GPG-KEY-ans
echo "deb [signed-by=/etc/apt/keyrings/ans-public.asc] https://repo.ans.uk/public/debs/ans ubuntu main" | sudo tee /etc/apt/sources.list.d/ans-public.list
apt update
apt install fence-ecloud
```

### Configuring Pacemaker

With the fence agent installed, you can configure Pacemaker to use the eCloud fence agent. These instructions should work for all distributions.

To do this you will need an API key for eCloud, which you can create by logging into the ANS Portal and going to 'API Applications'. Make sure the API key you create has Read/Write permissions for eCloud.

For the purposes of this example, we will assume that you have two nodes called `host1` and `host2`. Both hosts are eCloud VPC hosts, `host1` has an instance ID of `i-c6e2878c`, with `host2` being `i-dbb4ce6e`.

You should only need to run these commands on one of your Pacemaker nodes and it will set up STONITH on all of them, however in some circumstances this may not be enough - please speak with ANS support if you are unsure.

```shell
export $ECLOUD_API_KEY="<YOUR API KEY HERE>"
pcs stonith create ecloud_stonith fence_ecloud \
    apikey="$ECLOUD_API_KEY" \
    pcmk_host_check=static-list \
    pcmk_host_list=host1,host2 \
    pcmk_host_map="host1:i-c6e2878c;host2:i-dbb4ce6e" \
    retry_on=3 \
    op monitor interval=60s
```

Of importance in the above command is the option `pcmk_host_map` which maps the hosts to their instance IDs. This allows the fence agent to fence the correct node when requested by Pacemaker. Note that eCloud (not VPC) instance IDs are usually positive integers, e.g. `119283`, rather than identifiers starting with `i-`. The fence agent will use the correct API calls depending on if you are using VPC or non-VPC identifiers. Further information on the options presented can be found [here](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/high_availability_add-on_reference/s1-genfenceprops-haar).

Once you have configured STONITH, you can ask Pacemaker to fence one of your nodes to test that the STONITH configuration is working. Please be aware that this will reboot the target node.

```shell
pcs stonith fence host2
```
