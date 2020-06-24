# Resize an additional disk *(intermediate)*

This guide covers the process for getting Linux to recognize that one of the non-primary disks (not `/dev/sda`) has changed size, and to make that new space available for use.

```eval_rst
.. note::
   This article is for intermediate-level Linux administrators. If you're not comfortable with Linux and want to increase the amount of disk space assigned, the `add a new disk <add-disk.html>`_ method might be better for you.
```

Once you've resized one of the disks in MyUKFast on a virtual machine (VM), we can proceed to check which underlying volume this has altered. In most cases the mapping is similar to `Disk 1` in MyUKFast matching with `sda`, and so on.

## Rescan the SCSI hosts

Firstly we need to rescan the SCSI hosts to detect changes in disk size.

```bash
[root@ssh ~]# for i in /sys/class/scsi_host/host*/scan; do echo "- - -" > $i; done
[root@ssh ~]# for i in /sys/class/scsi_device/*/device/rescan; do echo "1" > $i; done
```

## Identifying the resized disk

Following this, we will need to compare the output of `pvs` and `fdisk -l` to see which disk has changed size. The `pvs` command will show old data, and `fdisk -l` will now be up-to-date.

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  eCloud lvm2 a--   9.51g    0
  /dev/sdb   eCloud lvm2 a--  10.00g    0
[root@ssh ~]#
```

```bash
[root@ssh ~]# fdisk -l

Disk /dev/sda: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x00001caf

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     1026047      512000   83  Linux
/dev/sda2         1026048    20971519     9972736   8e  Linux LVM

Disk /dev/mapper/eCloud-root: 19.9 GB, 19893583872 bytes, 38854656 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/eCloud-swap: 1048 MB, 1048576000 bytes, 2048000 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 16.1 GB, 16106127360 bytes, 31457280 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

[root@ssh ~]#
```

Here we can see that there is a 5G difference on `/dev/sdb`, which is the disk we expanded in MyUKFast.

## Resize the physical volume to use the new space

While the operating system (OS) can see the additional space, we've still got to make this usable.

First, you'll need to get LVM to recognize that the physical volume (PV) has changed size:

```bash
[root@ssh ~]# pvresize /dev/sdb
  Physical volume "/dev/sdb" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
[root@ssh ~]#
```

...then confirm that this is correct in `pvs`:

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  eCloud lvm2 a--   9.51g    0
  /dev/sdb   eCloud lvm2 a--  15.00g 5.00g
[root@ssh ~]#
```

## Extend the logical volume over the free space

```eval_rst
.. seealso::
   If you want to create a new partition from this disk - to have :code:`/` and :code:`/home` on separate partitions, for example - you would need to create a new Logical Volume instead of extending the existing one.

   This should only be performed by advanced users when absolutely required.

   For most use cases, a large :code:`/` partition will be all that is needed.

   As we've resized an underlying disk, you can only extend or create new volumes in the Volume Group with free space.
```

In this instance, we'll be doing the most common extension of `/`. Note the path in this command is `/dev/mapper/VG/LV` from the table above:

```bash
[root@ssh ~]# lvresize -l +100%FREE /dev/mapper/eCloud-root
  Size of logical volume eCloud-root changed from 18.53 GiB (4743 extents) to 23.53 GiB (6023 extents).
  Logical volume root successfully resized.
[root@ssh ~]#
```

Confirm that this has resized the logical volume (LV) as expected:

```bash
root@ssh ~]# lvs
  LV   VG     Attr       LSize    Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root eCloud -wi-ao----   23.53g                                                    
  swap eCloud -wi-ao---- 1000.00m                                                    
[root@ssh ~]#
```

## Resize the filesystem to make the new space available

Now that the disk and LV show the correct sizes, we can go ahead and resize the filesystem. Some servers use the `ext` filesystem type, and others user `xfs` - to identify which yours uses, run the following:

```bash
[root@ssh ~]# df -T
Filesystem              Type     1K-blocks    Used Available Use% Mounted on
/dev/mapper/eCloud-root xfs       19417088 2235516  17181572  12% /
devtmpfs                devtmpfs   1929244       0   1929244   0% /dev
tmpfs                   tmpfs      1939460       0   1939460   0% /dev/shm
tmpfs                   tmpfs      1939460    8656   1930804   1% /run
tmpfs                   tmpfs      1939460       0   1939460   0% /sys/fs/cgroup
/dev/sda1               xfs         508588  211732    296856  42% /boot
tmpfs                   tmpfs       387892       0    387892   0% /run/user/0
[root@ssh ~]#
```

In this example, the server is using `xfs`.

### Resizing XFS filesystems

To resize an `xfs` filesystem, run the following - noting the format of `/dev/mapper/VG-LV` on the device name:

```bash
[root@ssh ~]# xfs_growfs /dev/mapper/eCloud-root
```

Then confirm that the disk shows the correct size in `df -h`.

### Resizing EXT filesystems

To resize an `ext` filesystem, run the following - noting the format of `/dev/mapper/VG-LV` on the device name:

```bash
[root@ssh ~]# resize2fs /dev/mapper/eCloud-root
```

Then confirm that the disk shows the correct size in `df -h`

```eval_rst
  .. title:: Resizing an additional disk on an eCloud virtual server
  .. meta::
     :title: Resizing an additional disk on an eCloud virtual server | UKFast Documentation
     :description: An intermediate-level guide to resizing an additional disk on an eCloud virtual server
     :keywords: ukfast, linux, ecloud, cloud, server, disk, drive, resize, format, tutorial
