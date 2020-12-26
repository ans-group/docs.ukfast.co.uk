# Managing Volumes

```eval_rst
.. warning::
  As with most of our Flex guides, we're going to assume that you've followed our guide on setting environment variables and installing the openstackclient:

  :doc:`/ecloud/flex/general/settingvars`

  :doc:`/ecloud/flex/general/openstackcli`

  If you're not using this method of authentication, you may need to specify additional flags/options in the commands used in this article.
```

[Volumes](https://wiki.openstack.org/wiki/Cinder) are block storage devices that you attach to instances to enable persistent storage. Volumes can only be attached to one instance at a time, however you are able to detach a volume and attach it to a different instance whenever. You are able to manage your volumes within the [Horizon dashboard](https://api.openstack.ecloud.co.uk/project/volumes/), however this guide will detail how to manage your volumes using the Openstack command line client.

## Viewing Volumes

You can simply list all the volumes in your project using the `openstack volume list` command.

```console
root@dev:~# openstack volume list
+--------------------------------------+------------------+--------+------+----------------------------------------+
| ID                                   | Name             | Status | Size | Attached to                            |
+--------------------------------------+------------------+--------+------+----------------------------------------+
| e17dc8ec-e126-4883-803e-343ac444fbc1 | backups          | in-use |   50 | Attached to development on /dev/vdc    |
| e39c26b5-96a6-44ce-94be-3a57006e6bca | mail-backups     | in-use |   50 | Attached to mail-server on /dev/vdb    |
| 34179604-8d2c-44b5-b728-e8f991304hb3 | disk-ext         | in-use |   50 | Attached to gitlab-runner on /dev/vdb  |
| 4525d38b-195b-4ad7-92ea-dd4c0fa7912c | home-directory   | in-use |  100 | Attached to development on /dev/vdb    |
+--------------------------------------+------------------+--------+------+----------------------------------------+
```

You can also see more information about individual volumes by running `openstack volume show <volumeid>`.

```console
root@dev:~# openstack volume show 4525d38b-195b-4ad7-92ea-dd4c0fa7912c
+------------------------------+---------------------------------------+
| Field                        | Value                                 |
+------------------------------+---------------------------------------+
| attachments                  | <redacted>                            |
| availability_zone            | nova                                  |
| bootable                     | false                                 |
| consistencygroup_id          | None                                  |
| created_at                   | 2019-04-02T12:55:45.000000            |
| description                  |                                       |
| encrypted                    | False                                 |
| id                           | 4525d38b-195b-4ad7-92ea-dd4c0fa7912c  |
| multiattach                  | False                                 |
| name                         | home-directory                        |
| os-vol-tenant-attr:tenant_id | 183c303baa5d45e68dfded1595d94019      |
| properties                   | attached_mode='rw', readonly='False'  |
| replication_status           | None                                  |
| size                         | 100                                   |
| snapshot_id                  | None                                  |
| source_volid                 | None                                  |
| status                       | in-use                                |
| type                         | Ceph-P1-M5-ssd                        |
| updated_at                   | 2019-06-18T10:55:18.000000            |
| user_id                      | a2b72b6b45694b81b8879bes6c827742      |
+------------------------------+---------------------------------------+
```

## Creating Volumes

Creating new volumes is very simple. The below command is an example of creating a 20GB SSD volume named `test-volume`.

```bash
openstack volume create --size 20 \
                        --type Ceph-P1-M5-ssd \
                        test-volume
```

`--size` flag is the size of the volume in GB.
`--type` flag required the _type_ of the volume. Currently in eCloud Flex, we have 3 types of volume:

* **SATA / Ceph-P1-M5-sata** volumes offer up to 500 IOPS, and are recommended for storage of large files which are accessed infrequently, or for log files
* **SSD / Ceph-P1-M5-ssd** volumes will perform in excess of 5,000 IOPS, and are recommended for frequently accessed files, databases and web files
* **PCIe / Ceph-P1-M5-pcie** volumes bring performance of over 50,000 IOPS, and are recommended for high performance databases and applications

The `--source` flag allows you to create volumes from images, if you specify the image ID.

## Attaching / Detaching Volumes

Your new volumes can be attached to your instances easily, by running `opensack server add volume <instanceid> <volumeid>`.

```bash
opensack server add volume 0579f09b-c1e2-4551-9e8d-8e1997302dd6 \
                           8a5ce311-f5cd-447e-ae19-08a75412c7a5 \
                           --device /dev/vdb
```

The `--device` flag allows you to specific the internal device name for the volume.

Volumes are also removed simply by running `openstack server remove volume <instanceid> <volumeid>`.

```bash
openstack server remove volume 0579f09b-c1e2-4551-9e8d-8e1997302dd6 \
                               8a5ce311-f5cd-447e-ae19-08a75412c7a5
```

## Resizing Volumes

A volume must be in an `available` state in order to be resized (ie. it cannot be attached to an instance). You can use the `openstack volume set <volumeid>` command to do this:

```bash
openstack volume set 8a5ce311-f5cd-447e-ae19-08a75412c7a5 --size 30
```

## Managing Snapshots

A snapshot in eCloud Flex is a point in time version of a volume. You can create volume snapshots by running the `openstack volume snapshot create` command:

```bash
openstack volume snapshot create --volume 8a5ce311-f5cd-447e-ae19-08a75412c7a5 volsc1
```

You are able to manage your snapshots by using the `openstack volume snapshot delete|list|set|show|unset` commands.

## Deleting Volumes

It's very simple to remove a volume in eCloud Flex, by using the `openstack volume delete <volumeid>` command:

```bash
openstack volume delete 8a5ce311-f5cd-447e-ae19-08a75412c7a5
```

If you face any problems with volumes in eCloud Flex, please raise a support ticket via [MyUKFast](https://my.ukfast.co.uk/pss/create), or call support directly on 0800 230 0032.

```eval_rst
.. meta::
   :title: Managing Volumes in eCloud Flex | UKFast Documentation
   :description: A guide detailing how to manage volumes in eCloud Flex.
   :keywords: ecloud, flex, storage, hosting, cloud, vm, volumes, images, snapshots, sysadmin
```
