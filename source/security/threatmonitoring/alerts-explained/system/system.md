# System Events

## Three failed attempts to run sudo

*What does this mean?*


This rule tells you that there have been 3 incorrect password attempts on syslog within the space of a few minutes. This could be someone forgetting their passwords. Usually, this is an administrator or someone who has access to the system.

This does not discount an attacker from triggering this rule. Some investigation should be done to make sure that this is a valid authorised user completing these actions.

*What program/service does this rule relate to?*


This relates to user management and permissions management. The `sudo` program allows users to act as root when performing actions that directly relate to the system. This allows the users to start and stop services, modify configuration files and access restricted parts of the file system.

This program is also very locked-down to specific individuals. The program needs the authorization to allow a user to use it. This is meant as an administration tool, to allow the root account login to be disabled.

*How can I fix this?*


Finding out which user triggered this alert would be useful. It should be listed on our alert to you. This would allow you to investigate to see what they have been doing.

If the user is not meant to be able to use the `sudo` command then looking through their `.bash_histroy` files by looking in their home directory,  `/home/<user>` usually. This file lists all the commands the user has run on the system. If it is a system user that has tried to this, a ClamAV scan or a McAfee scan would be a good idea to make sure that a program is not a virus or malware.


## SCSI RAID ARRAY ERROR, drive failed

*What does this mean?*


This tells you that one or more of the drives in RAID array have failed, this is usually because the drive has been in operation for a long while so is suffering from general wear and tear. This needs to be looked at immediately.

**NOTE**: This does not indicate an attack. This is caused by a disk physically failing in the server.

*What does this rule relate to?*


This can affect everything in your server. Anything which needs to access data on that disk will error out and fail. This is a serious issue. Mostly RAIDs are used to store data, so the operating system of the server is unlikely to be affected by a disk failure.

*How can I fix this?*


Contact the providers of your server. Make sure your backups are as up to date as they can be, and work with them to get everything back up and running. Keeping an open dialogue with them, so that you are informed of any updates and developments would be good too.

Other than that, there isn't much you can do. Getting the drive replaced, and your RAID array rebuilt is the only solution. If you are using RAID as a redundancy, not a backup, then there may not be a lot of downtimes as your RAID array will fail over.

A good backup solution is also a must in these situations, as if the array does become completely corrupted, then your data is still kept safe, in a backup. Running daily backups is a recommended configuration.

## Possible Disk failure. SCSI controller error.

*What does this mean?*


This means that there is a failure on the hard drive or an error with the SCSI controller. This is usually caused by normal wear and tear of the server, and can often lead to data loss, if not monitored carefully.

Linux and Windows Servers will do some monitoring of Hard Disks and some SCSI controllers. This will generally do this through the general system logs (syslog) via its own Health Checking systems. These alerts trigger when the drive is approaching unusability. This means that you will still have time to recover all data from usable sectors.

This does not mean that an attack is taking place. This is a hardware alert which is generated to inform the user of hardware that is about to fail.

*How can I fix this?*


A replacement hard drive will be necessary to preserve all the data. Migrating data from onto a new drive is the best way to not lose data. Please contact your technical team, or our support staff to help you with this.

**NOTE**: If you are dealing with a RAID array, please seek the advice of our support staff or another experienced IT professional for the best way to replace disks in a RAID array.


To find out more about the health of your hard drives on Linux run the command replacing the `<device_id>` with the device you wish to run it against, such as `sda` or `sdb`.


`smartctl -a /dev/<device_id>`


On Windows open PowerShell and type in:


`wmic`

`diskdrive get status`



This will return 'Status OK' if the drive is all good, or an error message. This error message will indicate problems with your hard drive.

```eval_rst
.. meta::
     :title: System Rules Explained | UKFast Documentation
     :description: Our Threat Monitoring ruleset explained
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
