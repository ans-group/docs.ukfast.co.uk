# Resize the primary disk *(suggested)*

If you need to resize the primary disk, you will need to grow your partition on the disk and then tell LVM to recognise the new space.

```eval_rst
.. warning::
   **This article is for those comfortable with Linux administration** If you're not comfortable with Linux and want to increase the amount of disk space assigned to your server, UKFast customers may raise a support ticket.
```
### Resize the disk in MyUKFast

You may start off with a VM like so:

```bash
[root@ssh ~]# lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda               8:0    0   15G  0 disk
├─sda1            8:1    0  512M  0 part /boot
└─sda2            8:2    0 14.5G  0 part
  ├─eCloud-root 253:0    0 13.5G  0 lvm  /
  └─eCloud-swap 253:1    0    1G  0 lvm  [SWAP]
```

In this example, we can see that the disk `/dev/sda` is 15G in size. 

The first step from here is to resize the disk in the MyUKFast portal. This can be done by visiting:

```bash
MyUKFast -> eCloud -> Public/Private/Hybrid -> [Click the server]
```
## Rescan the SCSI hosts

Following this, we need to rescan the SCSI hosts to detect changes in disk size.

```bash
[root@ssh ~]# for i in /sys/class/scsi_host/host*/scan; do echo "- - -" > $i; done
[root@ssh ~]# for i in /sys/class/scsi_device/*/device/rescan; do echo "1" > $i; done
```

## Extend an existing partition

Once the disk has been extended using the eCloud control panel, you will use the `growpart` command to extend the last partition.

In the below example we can see that the last device partition number is `/dev/sda2`

Note now how the size of `/dev/sda` is now 20G whereas previously this was 15G

```bash
[root@id116041 ~]# lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda               8:0    0   20G  0 disk
├─sda1            8:1    0  512M  0 part /boot
└─sda2            8:2    0 14.5G  0 part
  ├─eCloud-root 253:0    0 13.5G  0 lvm  /
  └─eCloud-swap 253:1    0    1G  0 lvm  [SWAP]
```
We can see in this example that our LVM drive is on `/dev/sda2` so this is the partition that we need to expand.

Now that we have the partition number that we are going to extend, we will use the following command to grow the size of the last partition

```bash
[root@ssh ~]# growpart /dev/sda 2
CHANGED: partition=2 start=1050624 old: size=30406623 end=31457247 new: size=40892383 end=41943007
```

Going back to `lsblk` we can now see the size of the partition has now also changed to around 20G:

```bash
[root@ssh ~]# lsblk
NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda               8:0    0   20G  0 disk
├─sda1            8:1    0  512M  0 part /boot
└─sda2            8:2    0 19.5G  0 part
  ├─eCloud-root 253:0    0 13.5G  0 lvm  /
  └─eCloud-swap 253:1    0    1G  0 lvm  [SWAP]
```
Now we need to resize the physical volume into the newly extended disk

```bash
[root@ssh ~]# pvresize /dev/sda2
  Physical volume "/dev/sda2" changed
  1 physical volume(s) resized or updated / 0 physical volume(s) not resized
```

...then confirm that this is correct in `pvs`:

```bash
[root@ssh ~]# pvs
  PV         VG     Fmt  Attr PSize   PFree
  /dev/sda2  eCloud lvm2 a--  <19.50g 5.00g
```

## Extending the logical volume onto the increased volume group

```eval_rst
.. seealso::
   If you want to create a new partition from this disk - to have / and /home on separate partitions, for example - you would need to create a new Logical Volume instead of extending the existing one.

   This should only be performed by advanced users when absolutely required.

   For most use cases, a large / partition will be all that is needed.

   As we've resized an underlying disk, you can only extend or create new volumes in the Volume Group with free space.
```

In this instance, we'll be doing the most common extension of `/`. Note the path in this command is `/dev/mapper/VG-LV` from the table above:

```bash
[root@ssh ~]# lvresize -l +100%FREE /dev/mapper/eCloud-root
  Size of logical volume eCloud/root changed from <13.50 GiB (3455 extents) to <18.50 GiB (4735 extents).
  Logical volume eCloud/root successfully resized.
[root@ssh ~]#
```

Confirm that this has resized the logical volume (LV) as expected:

```bash
root@ssh ~]# lvs
  LV   VG     Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root eCloud -wi-ao---- <18.50g
  swap eCloud -wi-ao----   1.00g
[root@ssh ~]#
```

## Resize the filesystem to make the new space available

Now that the disk and LV show the correct sizes, we can go ahead and resize the filesystem. Some servers use the `ext` filesystem type, and others user `xfs` - to identify which yours uses, run the following:

```bash
[root@ssh ~]# df -T
Filesystem              Type     1K-blocks    Used Available Use% Mounted on
[...]
/dev/mapper/eCloud-root ext4      13800600 1378772  11776020  11% /

[root@ssh ~]#
```

In this example, the server is using `ext4`.

### Resizing EXT4 filesystems

To resize an `ext4` filesystem, run the following - noting the format of `/dev/mapper/VG-LV` on the device name:

```bash
[root@ssh ~]# resize2fs /dev/mapper/eCloud-root
resize2fs 1.42.9 (28-Dec-2013)
Filesystem at /dev/mapper/eCloud-root is mounted on /; on-line resizing required
old_desc_blocks = 2, new_desc_blocks = 3
The filesystem on /dev/mapper/eCloud-root is now 4848640 blocks long.
```

### Resizing XFS filesystems

To resize an `xfs` filesystem, run the following - noting the format of `/dev/mapper/VG-LV` on the device name:

```bash
[root@ssh ~]# xfs_growfs /dev/mapper/eCloud-root
```

```eval_rst
   .. title:: Resizing the primary disk on an eCloud virtual server
   .. meta::
      :title: Resizing the primary disk on an eCloud virtual server | UKFast Documentation
      :description: An advanced-level guide to resizing the primary disk on an eCloud virtual server
      :keywords: ukfast, ecloud, cloud, disk, drive, resize, primary, server, virtual, linux
```
