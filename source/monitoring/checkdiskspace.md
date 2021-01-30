# Disk space

It's quite common to want to check the status of the various partitions/drives on your server to see how full they are. To do so run this command:

```bash
df -h
```

This will produce output similar to the following:

```console
[root@mail ~]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VolGroup-lv_root
                        19G  1.6G   16G   9% /
tmpfs                 245M     0  245M   0% /dev/shm
/dev/sda1             485M   47M  413M  11% /boot
```

In this basic example, we can see that the `/` partition only has 9% used.

For a more complex example that also covers using `df` to see various mountpoints, see below:

```console
[root@mail ~]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/VG-root   1.9T  1.7T   89G  95% /
/dev/mapper/VG-var    431G  145G  264G  36% /var
devtmpfs              7.8G  204K  7.8G   1% /dev
tmpfs                 7.8G  4.0K  7.8G   1% /dev/shm
/dev/md1              495M  126M  344M  27% /boot
ku.example.com:9421   2.5T  487G  2.0T  20% /mnt/test
tmpfs                 500M   86M  415M  18% /var/ngx_pagespeed_cache
```

In this example, we have a root partition that's 95% full along with an additional `/var` partition that's only 36% full.
It's got an external network mount of 2T that's mounted on `/mnt/test` and a `ramdisk`/`tmpfs` mount of 500M mounted on `/var/ngx_pagespeed_cache`.

```eval_rst
  .. title:: Checking Disk Space
  .. meta::
     :title: Checking Disk Space | UKFast Documentation
     :description: How to check disk space on your server
```
