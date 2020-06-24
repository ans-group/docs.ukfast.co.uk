# Resize the primary disk *(advanced)*

If you need to resize the primary disk for some reason, you will need to create a new partition to utilise any additional space you assign to it. This is because the disk will have already been partitoned as follows:

```bash
[root@ssh ~]# fdisk -l /dev/sda

Disk /dev/sda: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x00001caf

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     1026047      512000   83  Linux
/dev/sda2         1026048    20971519     9972736   8e  Linux LVM

[root@ssh ~]#
```

Where `sda1` is `/boot`, and `sda2` is the first physical volume in the eCloud Volume Group (VG).

```eval_rst
.. warning::
   **This article is for advanced Linux administrators.** If you're not comfortable with Linux and want to increase the amount of disk space assigned to your server, the `add a new disk <add-disk.html>`_ method is recommended.
```

## Rescan the SCSI hosts

Firstly we need to rescan the SCSI hosts to detect changes in disk size.

```bash
[root@ssh ~]# for i in /sys/class/scsi_host/host*/scan; do echo "- - -" > $i; done
[root@ssh ~]# for i in /sys/class/scsi_device/*/device/rescan; do echo "1" > $i; done
```

## Extend an existing partition

For disks that have been extended using the eCloud control panel, you will use the `growpart` command to extend the last partition.

In the below example we can see that the last device partition number is `/dev/sda4`

```bash
[root@ssh ~]# fdisk -l

Disk /dev/sda: 118.1 GB, 118111600640 bytes, 230686720 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x0009cb29

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048      526335      262144   83  Linux
/dev/sda2          526336    41943006    20708335+  8e  Linux LVM
/dev/sda3        41943040   125829119    41943040   83  Linux
/dev/sda4       125829120   230686686    52428783+  83  Linux
```

Now that we have the partition number that we are going to extend, we will use the following command to grow the size of the last partition

```bash
[root@ssh ~]# growpart /dev/sda 4
CHANGED: partition=4 start=125829120 old: size=58720256 end=184549376 new: size=104857567,end=230686687
```

The output of `fdisk -l` will show the additional space is now present for /dev/sda4

Finish off by resizing the physical volume into the newly extended disk

```bash
root@ssh ~]# pvresize /dev/sda4
  Physical volume "/dev/sda4" changed
  1 physical volume(s) resized or updated / 0 physical volume(s) not resized
```

## Create a new partition

Alternatively, there is the option to create a new partition on `sda` to use the newly assigned disk space.

```eval_rst
.. note::
   The below uses a specific example of disk sizes and partition number. Please take care to ensure that your answers to these questions are accurate.
```

Here is an example of creating a new partition:

```bash
[root@ssh ~]# fdisk /dev/sda
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type:
   p   primary (2 primary, 0 extended, 2 free)
   e   extended
Select (default p): p
Partition number (3,4, default 3): 3
First sector (20971520-41943039, default 20971520):
Using default value 20971520
Last sector, +sectors or +size{K,M,G} (20971520-41943039, default 41943039):
Using default value 41943039
Partition 3 of type Linux and of size 10 GiB is set

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.

[root@ssh ~]#
```

If you want the above partition to form part of a Linux LVM, it would be recommended to use the `t` option to change the partition type to `8e`.

Following this, you can use the instructions in [add an additional disk](add-disk.html) to add this disk into an existing LVM, or make whatever more advanced changes you require with this additional partition.

**You may need to reboot your server for the new partition to be available.**

```eval_rst
  .. title:: Resizing the primary disk on an eCloud virtual server
  .. meta::
     :title: Resizing the primary disk on an eCloud virtual server | UKFast Documentation
     :description: An advanced-level guide to resizing the primary disk on an eCloud virtual server
     :keywords: ukfast, ecloud, cloud, disk, drive, resize, primary, server, virtual, linux
