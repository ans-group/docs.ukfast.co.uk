# Adding an IP Address

```eval_rst
.. note::

   You should speak with your account manager to have an IP address assigned to
   you before adding IPs to your server.
```

The quickest way to add an IP on either CentOS or Ubuntu would be to use the `ip` command as follows:

```bash
   ip addr add 10.10.10.10/28 brd + dev eth0
```

That example would add an IP of `10.10.10.10` with a netmask of `255.255.255.240` (CIDR `/28`) onto the interface `eth0`.

Although there's nothing wrong with that command, the IP won't persist beyond a reboot.

For that, we'll need to add it the respective network configuration file for our operating system.

## CentOS

On CentOS 5, 6 and 7, IP addresses are added in files in the following directory:

```console
   /etc/sysconfig/network-scripts
```

Files should be created with the name `ifcfg-ethX` and have the following content:

```console
   DEVICE=eth0:1
   ONBOOT=yes
   BOOTPROTO=static
   IPADDR=192.168.0.1
   NETMASK=255.255.255.0
```

Once you've added the your configuration file, bring the interface up with the `ifup` command:

```bash
ifup eth0:1
```

## Ubuntu

On Ubuntu, all the network config is typically stored in one file:
`/etc/network/interfaces`

This file should already exist as it'll have your existing network configuration in place.

Additional IP addresses should be added underneath the existing configuration with the following syntax:

```console
   auto eth0:1
   iface eth0:1 inet static
      address 192.168.0.1
      netmask 255.255.255.0
```

Again, the interface can be brought up with `ifup`, as so:

```bash
   ifup eth0:1
```

```eval_rst
  .. title:: Adding an IP Address
  .. meta::
     :title: Adding an IP Address | ANS Documentation
     :description:  A guide on how to add an IP address in CentOS or Ubuntu
     :keywords: ukfast, ip, address, netmask, server, linux, centos, ubuntu, network, web, config, configuration
```
