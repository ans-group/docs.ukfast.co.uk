# Rebooting Your Server

Beyond kernel updates, there shouldn't really be much need to reboot your Linux server (we're not working with Windows after all), but it's still an important task to be able to carry out.

There are a few ways to do it:

```console
reboot
```

```console
shutdown -r now
```

Both those have the same effect on the system, the server will run through its shutdown scripts and then boot back up.

A more traditional way would be to put the system into runlevel 6:

```console
init 6
```

But there's really no reason to be using this method on modern systems above their built in reboot/shutdown commands, you may miss out on some of the self-documenting features implemented by these commands.

In some very niche situations, you may find that the above commands won't reboot your server. This is likely due you hitting a deadlock situation. In-depth explanations of this state are beyond the scope of a basic Linux reboot page, but there's a lot of good information in the book [Linux Kernel Development, Second Edition book](https://www.oreilly.com/library/view/linux-kernel-development/9780768696974/) (Chapter 8)

If you do find yourself in this situation, you can always send your server down for an immediate reboot with the following command:

```eval_rst
.. warning::

   This is not a recommended course of action for rebooting your server.
   Nothing is synced or unmounted, it's fairly similar to tearing the power cable out.
   If you use this method, please make sure you're know what you're letting yourself in for.
```

```console
echo b > /proc/sysrq-trigger
```

```eval_rst
  .. title:: Rebooting your Linux server
  .. meta::
     :title: Rebooting your Linux server | UKFast Documentation
     :description: A guide to rebooting a linux server
     :keywords: ukfast, reboot, linux, server, virtual, vm, shutdown, rebooting
```
