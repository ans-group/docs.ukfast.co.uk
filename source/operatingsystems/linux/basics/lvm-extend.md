# Extending an LVM disk partition

When you purchase additional disk space - either in the form of additional hard disks, or an eCloud disk extension - there are some steps that need to be performed in order to make the additional disk space available.

There are two ways that the automation might present additional space to you. The default for Linux servers is to add a new virtual disk to your server, and then extend the LVM for your chosen partition with the new disk.

On Windows servers, the default is to change the size of the underlying virtual disk, which can sometimes be applied to Linux servers under certain conditions.

```eval_rst
.. warning::
   Please be aware that this article uses specific examples, such as *sdb* or */dev/mapper/eCloud-root*.

   You may have different requirements or configurations in terms of device names and volumes.

   Performing this incorrectly may make irreversible changes to your filesystem or cause data loss, so please proceed with care and caution.

   Once an extension has been started, it cannot be reverted.
```

## Identify the type of extension that was performed

As such, we must first identify which form of disk expansion has been applied to your virtual machine (VM).

Firstly we need to rescan the SCSI hosts:

```bash
[root@ssh ~]# for i in /sys/class/scsi_host/host*/scan; do echo "- - -" > $i; done
[root@ssh ~]# for i in /sys/class/scsi_device/*/device/rescan; do echo "1" > $i; done
```

Next, grab a list of the current physical volumes configured in LVM:

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize  PFree
  /dev/sda2  eCloud lvm2 a--   9.51g    0
  /dev/sdb   eCloud lvm2 a--  10.00g    0
[root@ssh ~]#
```

```eval_rst
.. seealso::
   Note that **/dev/sda1** is not supposed part of this list, as this contains your information for **/boot**.
```

Then, check whether there are any new disks of the requested additional size that have been created; or whether one of the disks has changed size:

### Example of resized disk

Here you can see that the `/dev/sdb` device is showing as 26.1G, while the output from `pvs` for `/dev/sdb` is only 10G.

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

**In this case, proceed with the [resized disk method](#resized-disk-method).**

---

### Example of additional disk

If you can't see a resized disk, a new disk has probably been added.

Check the output of `dmesg` for information about a new disk being added:

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

Then confirm that the disk that was added matches the size of the disk that you've purchased (`sdc` in this case):

```bash
root@ssh ~]# fdisk -l /dev/sdc

Disk /dev/sdc: 5368 MB, 5368709120 bytes, 10485760 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

[root@ssh ~]#
```

I added 5G to the VM, and this disk is ~5G in size, so we've identified where it was added.

**Now proceed with the [additional disk method](#additional-disk-method).**

---

# Resized disk method

We've identified that one of the disks has been resized - `sdb` in this case.

## Expand the partition if necessary

If the LVM PV refers to a partition on a disk (e.g. /dev/sdb3) rather than a complete disk (/dev/sdb), you'll first need to expand the partition to use the new space.   Use the :code:```growpart```  command to do this:

```growpart <disk> <partition number>```

for example

```growpart /dev/sdb 3```

Note that it is intentional that there is a space between the '/dev/sdb'  and '3'.  It's also important to note that this will only work if the partition number is the highest numbered on on the disk.  For example, if you had /dev/sdb1, /dev/sdb2, /dev/sdb3, /dev/sdb4, and your PV was /dev/sdb3,  you couldn't expand /dev/sdb3  because /dev/sdb4 would be in the way.   Contact support for advice if you find yourself in this situation.

The growpart command isn't always installed by default on a server, you may need to install it first using yum / apt  / dnf as appropriate.

## Resize the physical volume to use the new space

While the operating system (OS) can see the additional space, we've still got to make this usable.

First, you'll need to get LVM to recognise that the PV has changed size:

```bash
[root@ssh ~]# pvresize /dev/sdb
  Physical volume "/dev/sdb" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
[root@ssh ~]#
```

---

**Continue reading from the [final steps](#final-steps) section to complete the process.**

---

# Additional disk method

We've identified that a new disk was added - `sdc` in this case.

## Create a physical volume from the new device

We need to create a new physical volume for the new device (`sdc`) so that we can use it in LVM:

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

Then confirm that the VG shows the right total size:

```bash
[root@ssh ~]# vgs
  VG     #PV #LV #SN Attr   VSize  VFree
  eCloud   3   2   0 wz--n- 29.50g 5.00g
[root@ssh ~]#
```

---

**Continue reading from the [final steps](#final-steps) section to complete the process.**

---

# Final steps

Both methods of adding disk space to an eCloud VM are the same towards the end, so you can continue from here.

We need to grow the LV over the new free space - for most people this will be the `/` partition, but if you have more than one partition, take care to ensure you're resizing the right one:

```bash
[root@ssh ~]# lvs
  LV   VG     Attr       LSize    Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root eCloud -wi-ao----   18.53g
  swap eCloud -wi-ao---- 1000.00m
[root@ssh ~]#
```

In this case, we'll be doing the most common extension of `/`. Note the path in this command is `/dev/mapper/VG/LV` from the table above:

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

Then confirm that the disk shows the correct size in `df -h`.

```eval_rst
  .. title:: Extending LVM disk partition on Linux
  .. meta::
     :title: Extending LVM disk partition on Linux | ANS Documentation
     :description: A guide to extending an LVM disk partition on linux
     :keywords: ukfast, linux, extension, disk, server, virtual, vm, hard, drive
```
