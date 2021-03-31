# Managing Images

OpenStack Glance is the project that manages images within eCloud Flex. UKFast manage a range of images that are available publicly to our clients so you should be able to get on your feet without having to manage any of your own images, however this documentation details how to view and create your images if you were so inclined.

```eval_rst
.. warning::
  As with most of our Flex guides, we're going to assume that you've followed our guide on setting environment variables and installing the ``openstackclient``:

  :doc:`/ecloud/flex/general/settingvars`

  :doc:`/ecloud/flex/general/openstackcli`

  If you're not using this method of authentication, you may need to specify additional flags/options in the commands used in this article.
```

## Viewing Images

You can see a full list of your images (along with the public UKFast-managed images) by running `openstack image list`:

```console
root@dev:~# openstack image list
+--------------------------------------+----------------------------------------+-------------+
| ID                                   | Name                                   | Status      |
+--------------------------------------+----------------------------------------+-------------+
| 2daa747f-7225-4975-9173-fe3430a41483 | CentOS 6                               | active      |
| 47ac8b2c-9922-4ef9-9add-04580f080b89 | CentOS 7                               | active      |
| edae902c-df4e-4be8-b87a-72d5553e8f28 | Debian 8                               | active      |
| 574f21df-29e9-4209-a70b-a230b479ddb0 | Debian 9                               | active      |
| a277e3d1-da07-4a1e-8078-c097bb93838c | Ubuntu 16.04                           | active      |
| 6f526ede-0b07-4e7f-be83-84f474ebcd2e | Ubuntu 18.04                           | active      |
| 102fdfb2-2f1a-4547-882e-a8bc84590760 | Windows Server 2008 R2                 | active      |
| 7c823d29-a1e0-4b8f-ae18-0c7a78d37331 | Windows Server 2012 R2                 | active      |
| 09fc9015-cca1-4a76-b0ce-c9f250f42c8d | Windows Server 2016                    | active      |
| c9ab888e-9b28-4ef8-8d90-cd4508552c4b | Windows Server 2019                    | active      |
+--------------------------------------+----------------------------------------+-------------+
```

When viewing the list of images, we suggest piping the output into grep to refine your search. For example, if we wanted to see all the active Windows images:

```console
root@dev:~# openstack image list | grep -E 'Windows.*active'
| 102fdfb2-2f1a-4547-882e-a8bc84590760 | Windows Server 2008 R2                 | active      |
| 7c823d29-a1e0-4b8f-ae18-0c7a78d37331 | Windows Server 2012 R2                 | active      |
| 09fc9015-cca1-4a76-b0ce-c9f250f42c8d | Windows Server 2016                    | active      |
| c9ab888e-9b28-4ef8-8d90-cd4508552c4b | Windows Server 2019                    | active      |
```

You are also able to view the properties of each image, by running `openstack image show <imageid>`:

```console
root@dev:~# openstack image show 47ac8b2c-9922-4ef9-9add-04580f080b89
+------------------+---------------------------------------------------------------------------+
| Field            | Value                                                                     |
+------------------+---------------------------------------------------------------------------+
| checksum         | 78c715b10f00d61e5d72a0ecfac9cbf7                                          |
| container_format | bare                                                                      |
| created_at       | 2019-07-01T04:35:36Z                                                      |
| disk_format      | raw                                                                       |
| file             | /v2/images/47ac8b2c-9922-4ef9-9add-04580f080b89/file                      |
| id               | 47ac8b2c-9922-4ef9-9add-04580f080b89                                      |
| min_disk         | 0                                                                         |
| min_ram          | 512                                                                       |
| name             | CentOS 7                                                                  |
| owner            | 113bf558c22948b3ab156c10600070ba                                          |
| properties       | <redacted>                                                                |
| protected        | True                                                                      |
| schema           | /v2/schemas/image                                                         |
| size             | 2684354560                                                                |
| status           | active                                                                    |
| tags             |                                                                           |
| updated_at       | 2019-07-01T05:04:58Z                                                      |
| virtual_size     | None                                                                      |
| visibility       | public                                                                    |
+------------------+---------------------------------------------------------------------------+
```

## Creating / Modifying Images

Creating images in eCloud Flex is simple, and uses the `openstack image create <imagename>` command as you might expect.

```console
root@dev:~# openstack image create test-image
+------------------+------------------------------------------------------+
| Field            | Value                                                |
+------------------+------------------------------------------------------+
| checksum         | None                                                 |
| container_format | bare                                                 |
| created_at       | 2019-08-14T16:28:21Z                                 |
| disk_format      | raw                                                  |
| file             | /v2/images/a4ffe635-4d3b-472f-ae5b-910f82e52ac5/file |
| id               | a4ffe635-4d3b-472f-ae5b-910f82e52ac5                 |
| min_disk         | 0                                                    |
| min_ram          | 0                                                    |
| name             | test-image                                           |
| owner            | 7d86a2004a9d472681f18115dbd7b0a3                     |
| properties       | locations='[]'                                       |
| protected        | False                                                |
| schema           | /v2/schemas/image                                    |
| size             | None                                                 |
| status           | queued                                               |
| tags             |                                                      |
| updated_at       | 2019-08-14T16:28:21Z                                 |
| virtual_size     | None                                                 |
| visibility       | shared                                               |
+------------------+------------------------------------------------------+
```

However, an empty image isn't too handy. We need to pass this command various parameters in order to make this image _useful_.

```bash
openstack image create --disk-format qcow2 \
                       --file ubuntu-image.qcow2 \
                       --private \
                       --protected \
                       ubuntu-image
```

In the above example, we created an image called `ubuntu-image`, as can be seen in the final argument. Various flags can be used to control the properties of the image, and we suggest running `openstack image create --help` in order to see the full description for each flag.

You are also able to update the properties of your existing images, by using the `openstack image set [--flag] <id>` command.

```bash
openstack image set --unprotected ubuntu-image
```

## Deleting Images

The command for deleting images in your project is simple as you would expect.

```bash
openstack image delete <imageid>
```

If you would like to learn more about managing images in eCloud Flex, please refer to the [OpenStack documentation](https://docs.openstack.org/glance/pike/user/index.html).

```eval_rst
   .. title:: Managing Images in eCloud Flex
   .. meta::
      :title: Managing Images in eCloud Flex | UKFast Documentation
      :description: A guide detailing how to manage images in eCloud Flex.
      :keywords: ecloud, flex, storage, hosting, cloud, vm, volumes, images, snapshots, sysadmin
```
