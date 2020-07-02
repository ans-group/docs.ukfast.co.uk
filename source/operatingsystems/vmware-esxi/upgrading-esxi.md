# Update or Upgrade Standalone ESXi servers

Standalone ESXi servers can also be updated or upgraded via SSH. You don't *need* to have a vCenter server, it just makes it easier.

It **will** require that all of the virtual machines on the ESXi server be powered off however, and the ESXi server will likely require a reboot.

The ESXi server will require an outbound internet connection to retrieve patches, and **a full backup of all servers is highly recommended**.

## Using Profiles

* Shut down and power off all virtual machines.
* Put the ESXi server into Maintenance Mode and enable SSH if it isn't already enabled.
* SSH onto the ESXi server itself.
* First allow outbound HTTPS access on the host firewall to access the repository.

```
esxcli system maintenanceMode set --enable true
esxcli network firewall ruleset set --enabled true --ruleset-id=httpClient
```

* Now run the following command to see what patch levels you can automatically patch the server to. You can replace the `ESXi-6.5` with the major version you want to get a list of (e.g. `5.0`, `5.1`, `5.5`, `6.0`, etc.):

```
esxcli software sources profile list \
    -d https://hostupdate.vmware.com/software/VUM/PRODUCTION/main/vmw-depot-index.xml | grep -i ESXi-6.5
```

```
ESXi-6.5.0-20170304001-no-tools   VMware, Inc.  PartnerSupported
ESXi-6.5.0-20170104001-standard   VMware, Inc.  PartnerSupported
ESXi-6.5.0-20170304001-standard   VMware, Inc.  PartnerSupported  <----
ESXi-6.5.0-20170301001s-no-tools  VMware, Inc.  PartnerSupported
ESXi-6.5.0-20170301001s-standard  VMware, Inc.  PartnerSupported
ESXi-6.5.0-20170104001-no-tools   VMware, Inc.  PartnerSupported
ESXi-6.5.0-4564106-standard       VMware, Inc.  PartnerSupported
ESXi-6.5.0-4564106-no-tools       VMware, Inc.  PartnerSupported
```

* Once you have decided which version you want to update / upgrade to, run the following command, substituting `ESXi-6.5.0-20170304001-standard` with the version you want to use.

```
esxcli software profile update \
    -p ESXi-6.5.0-20170304001-standard \
    -d https://hostupdate.vmware.com/software/VUM/PRODUCTION/main/vmw-depot-index.xml
```

* The server will now start updating itself to the patch level requested.
* Once it has finished, reboot the ESXi server.

```
esxcli system maintenanceMode set --enable false
esxcli system shutdown reboot \
    --reason "Software update to ESXi-6.5.0-20170304001-standard"
```

* Once the reboot has completed, take the server out of maintenance mode and bring the VMs back online.

## Using individual patches

If you have a specific patch you want to install, this can also be done via SSH. The recommendation is to do this with all of the virtual machines powered down and the host in Maintenance Mode.

You can either SCP the patch to the server, or you can retrieve it using `wget`. Here we'll retrieve it using `wget`.

* Ensure the host is in Maintenance Mode

```
esxcli system maintenanceMode set --enable true
```

* Find the path to the datastore on the server by using `df -h`.

* Download the update onto the VM Datastore as follows, replacing the URL and datastore name.

```
wget \
    -P /vmfs/volumes/vhost-01a-local-datastore \
    http://94.229.165.115/megaraid_sas-6.603.55.00-offline_bundle-1712343.zip
```

* Install the VIB from the download path

```
esxcli software vib install \
    -d /vmfs/volumes/vhost-01a-local-datastore/megaraid_sas-6.603.55.00-offline_bundle-1712343.zip
```

* Once the update has finished, reboot the server as follows, replacing comment part with something relevant.

```
esxcli system shutdown reboot -r 'Replace LSI Logic Megaraid driver to 6.603.55.00.1vmw on the VMware HCL'
```

* Then when the server is back online, take the server out of Maintenance Mode and start the VMs back up again.

```
esxcli system maintenanceMode set --enable false
```

```eval_rst
   .. title:: Update or Upgrade Standalone ESXi servers
   .. meta::
      :description: Information on how to upgrade standalone ESXi servers (without a vCenter server)
```
