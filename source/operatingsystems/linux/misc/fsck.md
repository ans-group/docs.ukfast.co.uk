# Filesystem Check

If the server suffers an issue relating to data integrity, the server can go into read only mode where the OS stops any disk writes from happening to preserve data integrity. A filesystem check will need to be ran on the server to fix any issues before any data can be written to the filesystem. The server will need to first be booted into single user mode before the filesystem check can take place as it must not be mounted.

To boot into single user mode you must first reboot the server. When the GRUB screen appears in the boot process you must press any key in which you will then see a list of available kernels to boot from. You will need to press `e` on the kernel version you wish to boot from which will then allow you to edit the boot configuration. You will need to add the word `single` to the boot line. You can then press `enter` and then `b` to proceed with the boot.

Once the server has booted you will be logged in as the root user and will be able to run the filesystem check. To start the filesystem check you will need use the `fsck` command followed by the partition you wish to run the check against. You can also use the `-y` flag which will then attempt to fix any detected issues on the filesystem. An example on how to run this a filesystem check on the / partition is below.

```bash
  fsck -y /
```

Once the filesystem check has finished you can then reboot the server. Once the server has booted you should be able to write files to the filesystem.

```eval_rst
  .. title:: Checking the Linux filesystem for errors | UKFast Documentation
  .. meta::
     :title: Checking the Linux filesystem for errors | UKFast Documentation
     :description: A guide to checking for errors on the Linux filesystem
     :keywords: ukfast, files, filesystem, fsck, boot, data, integrity, cloud, linux
