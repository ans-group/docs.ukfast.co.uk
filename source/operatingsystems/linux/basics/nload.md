# Monitoring current network usage

One utility to display the current network usage is `nload`. This can be useful when you need to monitor the ingress/egress bandwidth usage directly on Linux servers and this can be used for specific network devices.

## Installation

You can install `nload` through `yum` on Redhat/CentOS operating systems, with `apt` on Debian based distributions or `dnf` with Fedora . Here are several variations:

RHEL & CentOS
```bash
  sudo yum install nload
```

Debian & Ubuntu
```bash
  sudo apt install nload
```

Fedora
```bash
  sudo dnf install nload
```

The `nload` utility can be installed from the `epel` repository on Redhat/CentOS distributions.

If `epel` is not already installed on the RHEL & CentOS environment, this can be installed with:
```bash
  sudo yum install epel-release
```

## Live network bandwidth monitoring

Nload can be used with the command `nload` via a console or SSH session. This utility has several options that vary the output.

By default this will auto-detect devices and you can switch between devices with the left and right arrow keys.

The device displayed can be seen at the top of the `nload` output - for example:
```bash
Device lo [127.0.0.1] (1/2):
```

Or to show all devices (supressing traffic graphs), use the command `nload -m` - this will something similiar to this in the standard output:
```bash
Device eth0 [10.0.0.20] (1/2):
=============================================================================================================================
Incoming:                                                     Outgoing:
Curr: 13.44 kBit/s                                            Curr: 52.41 kBit/s
Avg: 48.49 kBit/s                                             Avg: 82.66 kBit/s
Min: 4.91 kBit/s                                              Min: 8.23 kBit/s
Max: 108.29 kBit/s                                            Max: 732.95 kBit/s
Ttl: 28.27 GByte                                              Ttl: 22.68 GByte

Device lo [127.0.0.1] (2/2):
=============================================================================================================================
Incoming:                                                     Outgoing:
Curr: 13.21 kBit/s                                            Curr: 13.21 kBit/s
Avg: 75.44 kBit/s                                             Avg: 75.44 kBit/s
Min: 2.31 kBit/s                                              Min: 2.31 kBit/s
Max: 671.77 kBit/s                                            Max: 671.77 kBit/s
Ttl: 21.72 GByte                                              Ttl: 21.72 GByte
```

The default time window is '300' milliseconds between average calculations. It can be set to a custom time window with `nload -a <time>` - for example to update this to 150 milliseconds you would perform the command:
```bash
nload -a 150
```

Modifying the default display interval is also possible - by default this value is 500 milliseconds. The flag to update the display interval is `-t` and can be used as follows:
```bash
nload -t 600
```

```eval_rst
.. warning::

   Please note that specifying refresh intervals shorter than about 100  milliseconds  makes  traffic  calculation very  unprecise.  Also  the display may flicker using such short refresh intervals.  nload tries to balance this out by doing extra time measurements, but this may not always succeed.
```

If there is a specific device(s) that needs to be monitored, you can specify this with the following:
```bash
nload devices device1 device2
```

In addition, the metrics in which the data is displayed can be customised - the default is adaptive to the amount of bandwidth being used but it can be forced with one of the subsequent variations:
```bash
nload -u K ## KByte/s
nload -u k ## KBit/s
nload -u M ## MByte/s
nload -u m ## KBit/s
nload -u G ## GByte/s
nload -u g ## GBit/s
```

```eval_rst
  .. title:: Monitoring current network usage with nload
  .. meta::
     :title: Monitoring current network usage with nload | UKFast Documentation
     :description:  A guide on how to monitor current network usage with nload
     :keywords: ukfast, server, nload, debian, rhel, centos, ubuntu, linux, performance, virtual, vm, activity, historic, monitoring
