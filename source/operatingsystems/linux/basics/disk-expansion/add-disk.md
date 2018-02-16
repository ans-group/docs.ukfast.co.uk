# Add a new disk to the server *(recommended approach)*

When increasing the amount of disk space assigned to an eCloud virtual machine (VM), the simplest method is to add a new disk to the VM via [MyUKFast](https://my.ukfast.co.uk), and then add that disk into the Volume Group and Logical Volume for the `/` partition.

```eval_rst
.. warning::

   Please be aware that this article uses specific examples, such as :code:`sdc` or :code:`/dev/mapper/eCloud-root`.

   You may have different requirements or configurations in terms of device names and volumes.

   Performing this incorrectly may make irreversible changes to your filesystem or cause data loss, so please proceed with care and caution.

   Once an extension has been started, it cannot be reverted.
   
   If you're unsure of anything or need some help, please contact UKFast Support, by raising a ticket in MyUKFast or calling 0800 230 0032.
   
```

## Identifying new disk

From MyUKFast, you will need to first add a new disk to your VM using the eCloud interface for your required VM. This will hot-add a new disk to your server.

To identify the label for this disk, check `dmesg` for lines about a new device being added:

```bash
[root@ssh ~]# dmesg
[13955.155726] scsi 2:0:2:0: Direct-Access     VMware   Virtual disk     1.0  PQ: 0 ANSI: 2
[13955.157712] sd 2:0:2:0: Attached scsi generic sg3 type 0
[13955.159156] sd 2:0:2:0: [sdc] 10485760 512-byte logical blocks: (5.36 GB/5.00 GiB)
[13955.159210] sd 2:0:2:0: [sdc] Write Protect is off
[13955.159214] sd 2:0:2:0: [sdc] Mode Sense: 61 00 00 00
[13955.159293] sd 2:0:2:0: [sdc] Cache data unavailable
[13955.159296] sd 2:0:2:0: [sdc] Assuming drive cache: write through
[13955.161472]  sdc: unknown partition table
[13955.161769] sd 2:0:2:0: [sdc] Attached SCSI disk
```

In this case, the new disk is labeled `sdc`.

You should confirm that this is not already configured as a physical volume in LVM:

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  eCloud lvm2 a--   9.51g    0
  /dev/sdb   eCloud lvm2 a--  10.00g    0
[root@ssh ~]#
```

Above shows that `/dev/sda2` and `/dev/sdb` are currently configured as physical volumes; but the `/dev/sdc` device is not listed.

## Create a physical volume from the new disk

We need to create a new physical volume (PV) for the new device (`sdc`) so that we can use it in LVM:

```bash
[root@ssh ~]# pvcreate /dev/sdc
  Physical volume "/dev/sdc" successfully created
[root@ssh ~]#
```

Then confirm that it shows up in `pvs`:

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  eCloud lvm2 a--   9.51g    0
  /dev/sdb   eCloud lvm2 a--  15.00g    0
  /dev/sdc          lvm2 ---   5.00g 5.00g
[root@ssh ~]#
```

## Add the new physical volume into the volume group

So that we can assign the new disk space to the logical volume, we need to first add the physical volume into the volume group:

```bash
[root@ssh ~]# vgextend eCloud /dev/sdc
  Volume group "eCloud" successfully extended
[root@ssh ~]#
```

Then confirm that the volume group (VG) shows the right total size:

```bash
[root@ssh ~]# vgs
  VG     #PV #LV #SN Attr   VSize  VFree
  eCloud   3   2   0 wz--n- 29.50g 5.00g
[root@ssh ~]#
```

We need to grow the logical volume (LV) over the new free space - for most people this will be the `/` partition, but if you have more than one partition, take care to ensure you're resizing the right one:

```bash
[root@ssh ~]# lvs
  LV   VG     Attr       LSize    Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root eCloud -wi-ao----   18.53g                                                    
  swap eCloud -wi-ao---- 1000.00m                                                    
[root@ssh ~]#
```

## Extend the logical volume over the free space

```eval_rst
.. seealso::
   If you want to create a new partition from this disk - to have :code:`/` and :code:`/home` on separate partitions, for example - you would need to create a new Logical Volume instead of extending the existing one.

   This should only be performed by advanced users when absolutely required.

   For most use cases, a large :code:`/` partition will be all that is needed.
```

In this instance, we'll be doing the most common extension of `/`. Note the path in this command is `/dev/mapper/VG/LV` from the table above:

```bash
[root@ssh ~]# lvresize -l +100%FREE /dev/mapper/eCloud/root
  Size of logical volume eCloud/root changed from 18.53 GiB (4743 extents) to 23.53 GiB (6023 extents).
  Logical volume root successfully resized.
[root@ssh ~]#
```

Confirm that this has resized the LV as expected:

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
.. meta::
     :title: Adding new disks to an eCloud virtual server | UKFast Documentation
     :description: A guide on adding a new disk to an eCloud virtual server
     :keywords: ukfast, linux, ecloud, cloud, disk, drive, virtual, vm, server, tutorial
```
