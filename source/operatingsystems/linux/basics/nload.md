# Monitoring current network usage

One utility to display the current network usage is `nload`. This can be useful when you need to clearly see the ingress/egress bandwidth usage directly on a Linux server.

## Installation

You can install `nload` through the `yum` on Redhat/CentOS operating systems or with `apt` on Debian based distributions. Here are both variations:

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

The `nload` utility can be installed from the `epel` repository on Redhat distributions.

If you do not already have `epel` on a RHEL & CentOS operating system, you can install this with:
```bash
  sudo yum install epel-release
```

## Live network monitoring

Load can be used with the command `nload` via a console or SSH session. This utility has a number of options that vary the data that is provided.

By default this will auto-detect devices and you can switch between devices with the left and right arrow keys.

The device being displayed can be seen at the top of the `nload` output - for example:
```bash
Device lo [127.0.0.1] (1/2):
```

Or you can show all devices (supressing traffic graphs) with the command `nload -m` - this will something similiar to this in the standard output:
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

The default time window is '300' milliseconds between average calculations. You can set a custom time window with `nload -a <time>` - for example to update this to 150 milliseconds you would perform the command:
`nload -a 150`

You can also modify the default display interval - by default this value is 500 milliseconds. The flag to update the display interval is `-t` and can be used as follows:
`nload -t 600`

```eval_rst
.. warning::
PLEASE NOTE: Specifying refresh intervals shorter than about 100  milliseconds  makes  traffic  calculation very  unprecise.  Also  the display may flicker using such short refresh intervals.  nload tries to balance this out by doing extra time measurements, but this may not
always succeed.
```

If you have a specific device(s) that you want to monitor you can specify this with the following:
`nload devices device1 device2`

In addition the metrics in which the data is display can be changed - the default is adaptive to the amount of bandwidth being used but you can force this with:

```nload -u K ## KByte/s```   
```nload -u k ## KBit/s```   
```nload -u M ## MByte/s```   
```nload -u m ## KBit/s```   
```nload -u G ## GByte/s```   
```nload -u g ## GBit/s```   

## Basic historic monitoring

The nload utility also allows historic server monitoring. To do this you will need to use the below command.

```bash
  nload -r
```

This will look the same as the live monitoring but will start from the start of the current log, which is generally midnight of the current day. To step ahead in the log you will need to type `t` which will take you one step ahead in the configured logging period. To take a step backwards, you will need to type `T`. You can also specify a specific time by typing `b` followed by the desired time.

```eval_rst
  .. meta::
     :title: Monitoring current network usage with nload | UKFast Documentation
     :description:  A guide on how to monitor current network usage with nload
     :keywords: ukfast, server, nload, debian, rhel, centos, ubuntu, linux, performance, virtual, vm, activity, historic, monitoring
