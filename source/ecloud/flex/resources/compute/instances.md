# Managing and Launching instances

```eval_rst
.. warning::
   As with most of our Flex guides, we're going to assume that you've followed our guide on setting environment variables and installing the ``openstackclient``:

   - :doc:`/ecloud/flex/general/settingvars`
   - :doc:`/ecloud/flex/general/openstackcli`

   If you're not using this method of authentication, you may need to specify additional flags/options in the commands used in this article.
```

## Installation

The bundle of OpenStack management tools can all be found in `pip`, a package manager for python, so we'll first need to install that, along with a few dependencies that you'll be needing:

```bash
yum install python-pip python-devel gcc
apt install python-pip python-devel gcc
```

Now we're ready to install the whole suite of OpenStack CLI tools:

```bash
pip install python-openstackclient
```

We have a full page of documentation that details how to do this for various operating systems [here](/ecloud/flex/general/openstackcli).

## List instances

Starting with one of the more basic commands, we've got the following one to list all the instances you currently have. Running `openstack server list` will get you some output along these lines:

```console
[root@workstation ~]# openstack server list
+--------------------------------------+--------------------------+-----------+------------+-------------+----------------------------------+
| ID                                   | Name                     | Status    | Task State | Power State | Networks                         |
+--------------------------------------+--------------------------+-----------+------------+-------------+----------------------------------+
| c9911fee-7245-404c-a631-2d9b29f47395 | jump                     | active    | -          | running     | stnd=192.168.0.36, 46.37.172.05  |
| 5b2af436-e80d-4a29-aaaa-7a71250dfeef | ansible master           | ACTIVE    | -          | Running     | stnd=192.168.0.69, 46.37.172.04  |
| 69b1b7b7-77eb-4296-ba57-aa47890d146a | ansible slave-3          | ACTIVE    | -          | Running     | stnd=192.168.0.44, 46.37.172.03  |
| ac23d068-5b6d-4d4d-9615-b96be462c1b0 | ansible slave-4          | ACTIVE    | -          | Running     | stnd=192.168.0.15, 46.37.189.02  |
| 3b14dd96-7f05-4e57-ae9b-562e8d634691 | hosts                    | ACTIVE    | -          | Running     | stnd=192.168.0.50                |
| 04f961c5-8421-4198-9473-22b2289b89f0 | hubot                    | ACTIVE    | -          | Running     | stnd=192.168.0.68                |
| 47b55049-168a-4885-b8cd-ba431534022d | jamestest                | SUSPENDED | -          | Shutdown    | stnd=192.168.0.18                |
| df49a869-338b-441e-9e72-42ca4e51d242 | magento                  | SHUTOFF   | -          | Shutdown    | stnd=192.168.0.54                |
| 37ad0fc1-c01e-4c6b-804d-594d1bc20660 | rota                     | ACTIVE    | -          | Running     | stnd=192.168.0.24, 46.37.172.01  |
| 1bcf6b49-6f9b-4561-acda-fce135f646de | servera                  | ACTIVE    | -          | Running     | stnd=192.168.0.52                |
| 2a48ad36-84fd-4d12-b911-69f280d27588 | serverb                  | ACTIVE    | -          | Running     | stnd=192.168.0.53                |
| 3a86a28c-6338-4ce4-a79f-a6b28f1b0ffb | tower                    | ACTIVE    | -          | Running     | stnd=192.168.0.55                |
| a51c5773-722c-40b0-8a96-379701ea3698 | training                 | ACTIVE    | -          | Running     | stnd=192.168.0.34                |
+--------------------------------------+--------------------------+-----------+------------+-------------+----------------------------------+
```

One of the main reasons you may be running this command is to get access to the `uuid` used as the `ID` for each instance. Whilst most commands will accept the name of the instance as an argument, using the `ID` can be much less ambiguous when two instances have similar names and will help avoid some unwanted deletions in the future.

## Create instances

The syntax for creating new instances via the `openstack` CLI tool is as follows:

```bash
openstack server create --key-name development \
                        --image "Ubuntu 18.04" \
                        --flavor UKF2-small-1x1 \
                        --network local \
                        test-instance
```

Unless you've used it before though, you may be asking entirely reasonable questions like "How do I know what image to use?" and "What's up with the spelling of flavor?", so lets break it down a bit.

The first section `openstack server create` is relatively self explanatory, we're telling nova that we want to create a new instance, and the last argument `test-instance` is the name we want to give the instance once it's created.

`--key-name` is simply the name of the SSH keypair we want to use when authenticating with the server. If you know the name of your keypair already, then fire away, but if you'd like to check which ones you have available, the following `openstack keypair` argument will list them for you:

```console
  [root@workstation ~]# openstack keypair list
  +-----------------+-------------------------------------------------+
  | Name            | Fingerprint                                     |
  +-----------------+-------------------------------------------------+
  | development | 84:92:30:a6:d1:50:d3:43:3s:39:s8:4d:7a:e6:4f:51 |
  | default         | 1d:72:e6:e2:3z:9a:a9:s6:38:1b:11:88:40:38:7a:42 |
  +-----------------+-------------------------------------------------+
```

`--image` needs to be given a valid image name so that Flex knows which operating system or server image you want to create this new instance based on. If you've used the web interface for flex, you may know one off by heart, but chances are you'll need to check. For that, we need to talk to the image component of OpenStack, called `glance`. We can get a list of available images with `openstack image list` like so:

```console
  [root@workstation ~]# openstack image list
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

Your output to this command may very well be different, names may have been updated and the UUIDs have been changed in our examples on this page, so don't rely on the above content! Please refer to our other documentation for more information about [managing images](/ecloud/flex/resources/storage/managing-images).

The final part of that command is `--flavor`. American spelling aside, (it doesn't accept `--flavour` as an alias sadly, we've tried) `flavor` is the OpenStack parlance for 'size of instance'. It's the setting that controls how much RAM and CPU allocation you're giving the instance, along with which tier (i.e. `io`/`mem`/`std` of instance). We're back to the `openstack server` command for this one, with `openstack flavor list`:

```console
[root@workstation ~]# openstack flavor list
+--------------------------------------+----------------+-------+------+-----------+-------+-----------+
| ID                                   | Name           |   RAM | Disk | Ephemeral | VCPUs | Is Public |
+--------------------------------------+----------------+-------+------+-----------+-------+-----------+
| 2c3228cc-fd58-4d98-aec2-37f9c7821386 | UKF2-io-1x2    |  2048 |   60 |         0 |     1 | True      |
| 528498bd-254a-42f7-8729-21d20abebc20 | UKF2-io-2x4    |  4096 |   60 |         0 |     2 | True      |
| 56940ad3-6526-4f7e-8af8-ab9a3c2e59e8 | UKF2-io-4x8    |  8192 |   60 |         0 |     4 | True      |
| aedce3ce-6e6e-4bf7-84a7-b110f2eeb7be | UKF2-io-8x16   | 16384 |   60 |         0 |     8 | True      |
+--------------------------------------+----------------+-------+------+-----------+-------+-----------+
```

We are also able to view the available networks in our project. Every project in eCloud Flex is deployed with a pre-built network and router, so you should be able to plug in your default network. We have more information about networking in eCloud Flex [here](/ecloud/flex/resources/index).

```console
[root@workstation ~]# openstack network list
+--------------------------------------+-------+--------------------------------------+
| ID                                   | Name  | Subnets                              |
+--------------------------------------+-------+--------------------------------------+
| 7244b411-ee4a-483a-8383-4ee744ca9b75 | local | c9646849-0482-4616-9861-3520be09298d |
+--------------------------------------+-------+--------------------------------------+
```

With all that information, we're now in a better place to understand the command from earlier:

```bash
openstack server create \
    --key-name development \
    --image "Ubuntu 18.04" \
    --flavor UKF2-small-1x1 \
    --network local \
    test-instance
```

...and the output we receive from it:

```console
[root@workstation ~]# openstack server create --key-name development --image "Ubuntu 18.04" --flavor UKF2-small-1x1 --network local test-instance
+-----------------------------+-------------------------------------------------------+
| Field                       | Value                                                 |
+-----------------------------+-------------------------------------------------------+
| OS-DCF:diskConfig           | MANUAL                                                |
| OS-EXT-AZ:availability_zone |                                                       |
| OS-EXT-STS:power_state      | NOSTATE                                               |
| OS-EXT-STS:task_state       | scheduling                                            |
| OS-EXT-STS:vm_state         | building                                              |
| OS-SRV-USG:launched_at      | None                                                  |
| OS-SRV-USG:terminated_at    | None                                                  |
| accessIPv4                  |                                                       |
| accessIPv6                  |                                                       |
| addresses                   |                                                       |
| adminPass                   | oEp79VPqDZb5                                          |
| config_drive                |                                                       |
| created                     | 2019-08-13T12:11:22Z                                  |
| flavor                      | UKF2-small-1x1 (24bd8e8c-5575-439a-8f51-289c79e5175a) |
| hostId                      |                                                       |
| id                          | f1713d4d-eef1-4042-bd3e-cdc33c99ccfa                  |
| image                       | Ubuntu 18.04 (6f526ede-0b07-4e7f-be83-84f474ebcd2e)   |
| key_name                    | os-dev                                                |
| name                        | test-instance                                         |
| progress                    | 0                                                     |
| project_id                  | 7d86a2004a9d472681f18115dbd7b0a3                      |
| properties                  |                                                       |
| security_groups             | name='default'                                        |
| status                      | BUILD                                                 |
| updated                     | 2019-08-13T12:11:21Z                                  |
| user_id                     | db52babc4771498c96dc6b6e9f3ec0f2                      |
| volumes_attached            |                                                       |
+-----------------------------+-------------------------------------------------------+
```

Switching back to `openstack server list` again, we can check that the instance is showing as we'd expect:

```console
| f1713d4d-eef1-4042-bd3e-cdc33c99ccfa | test-instance | ACTIVE | local=2a02:22d0:9:2:f816:3eff:fe9e:d9f0, 10.0.0.16                  | Ubuntu 18.04                 | UKF2-small-1x1 |
```

## Deleting instances

So it turns out that the section on creating instances is quite big, but thankfully this one is a lot simpler. Using the `delete` argument and a name or ID, we can quickly delete instances like this:

```bash
openstack server delete f1713d4d-eef1-4042-bd3e-cdc33c99ccfa
```

If you want to delete a few at a time, just append their UUIDs onto the command:

```bash
openstack server delete f1713d4d-eef1-4042-bd3e-cdc33c99ccfa 4659bffc-923f-41b3-8dc0-8c24395b5add
```

```eval_rst
   .. title:: Controlling server actions on eCloud Flex
   .. meta::
      :title: Controlling server actions on eCloud Flex | UKFast Documentation
      :description: How to use the openstack CLI to manage server actions
      :keywords: openstack, ecloud, flex, ukfast, hosting, nova, openstackclient, openstack cli, instnace
```
