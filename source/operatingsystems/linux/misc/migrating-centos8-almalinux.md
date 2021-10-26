# Migrating from CentOS 8 to AlmaLinux

On December 31, 2021, CentOS 8 will reach end-of-life, meaning that Red Hat will no longer make security and maintenance updates to the OS. Since the announcement of this EOL date, several open-source RHEL (Red Hat Enterprise Linux) forks have been created, including AlmaLinux. This guide details the steps for migrating from CentOS 8 to AlmaLinux.

## Prerequisites

* Server running CentOS 8.3 or above. You can verify this by running `cat /etc/redhat-release`
* If you are a UKFast Backups customer, you can check on MyUKFast to ensure that you have a recent full backup.
* Once the migration is completed, the server will require a reboot.
* A minimum of 5GB free disk space
* Roughly 5m-2h time

## Downloading the AlmaLinux Migration Script

Firstly, [login to the server via SSH](/operatingsystems/linux/basics/connecting.html). From here, we will be downloading the almalinux-deploy.sh script from the AlmaLinux repo:


```bash
curl -O https://raw.githubusercontent.com/AlmaLinux/almalinux-deploy/master/almalinux-deploy.sh
```

With the script now downloaded, add the execute permission  using the `chmod` command:

```bash
chmod +x  almalinux-deploy.sh
```

## Starting the Migration

Once you are happy that you're on CentOS 8.3 or above, have backups in place, a minimum of 5GB free disk space and that you can reboot, run the **almalinux-deploy.sh** script to start the migration.

```bash
sudo bash almalinux-deploy.sh
```

The script has multiple stages. Initially, it does a pre-flight check to ensure compatibility and that the minimum requirements are met. After this, the script will begin to uninstall, reinstall and upgrade some packages from the AlmaLinux repository. The time the script takes to run can vary greatly, from anywhere between 60 seconds to 2 hours.

## Finishing the Migration

Once the script has finished running, it will display "Migration to AlmaLinux is completed". The last stage is to reboot the server, which will load the AlmaLinux Kernel.

```bash
sudo reboot
```

Once your server has rebooted, reconnect via SSH and confirm the version of AlmaLinux:

```bash
[root@example ~]$ cat /etc/redhat-release
AlmaLinux release 8.4 (Electric Cheetah)
```

```eval_rst
  .. title:: Migrating from CentOS 8 to AlmaLinux
  .. meta::
     :title: Migrating from CentOS 8 to AlmaLinux | UKFast Documentation
     :description: A guide on migrating from CentOS 8 to AlmaLinux
     :keywords: ukfast, centos, almalinux, migration, linux, eol, end-of-life
```
