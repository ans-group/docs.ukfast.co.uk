# Basic nova CLI tool usage

```eval_rst
.. warning::
  As with most of our Flex guides, we're going to assume that you've followed our guide on setting environment variables:

  :doc:`/flex/general/settingvars`

  If you're not using this method of authentication, you may need to specify additional flags/options in the commands used in this article.
```

Nova is the compute element of Openstack, basically the main chunk that handles the instance/server creation. As such, the tool for interacting with this is also called `nova`. This guide will cover some basic operations that can be carried out with this tool.

## Installation

The bundle of openstack management tools can all be found in `pip`, a package manager for python, so we'll first need to install that, along with a few dependencies that you'll be needing:

```bash
  yum install python-pip python-devel gcc
```

As the version of `pip` provided by yum is likely outdated, an update is in order:

```bash
  pip install --upgrade pip
```

The same goes for a library we're going to need to install the tools:

```bash
  pip install --upgrade setuptools
```

Now we're ready to install the whole suite of openstack cli tools:

```bash
  pip install python-openstackclient
```

## List instances

Starting with one of the more basic `nova` commands, we've got the following one to list all the instances you currently have. Running `nova list` will get you some output along these lines:

```console
  [root@workstation ~]# nova list
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

The syntax for creating new instances via the `nova` cli tool is as follows:

```bash
  nova boot --key-name default --image CentOS7_2016-01 --flavor UKF1-io-1x2 novatest
```

Unless you've used it before though, you may be asking entirely resonable questions like "How do I know what image to use?" and "What's up with the spelling of flavor?", so lets break it down a bit.

The first section `nova boot` is relatively self explanatory, we're telling nova that we want to boot (create) a new instance, and the last argument `novatest` is the name we want to give the instance once it's created.

`--key-name` is simply the name of the SSH keypair we want to use when authenticating with the server. If you're creating windows servers, you can skip this. If you know the name of your keypair already, then fire away, but if you'd like to check which ones you have available, the following `nova` argument will list them for you:

```console
  [root@workstation ~]# nova keypair-list
  +-----------------+-------------------------------------------------+
  | Name            | Fingerprint                                     |
  +-----------------+-------------------------------------------------+
  | ansibletraining | 84:92:30:a6:d1:50:d3:43:3s:39:s8:4d:7a:e6:4f:51 |
  | default         | 1d:72:e6:e2:3z:9a:a9:s6:38:1b:11:88:40:38:7a:42 |
  +-----------------+-------------------------------------------------+
```

`--image` needs to be given a valid image name so that flex knows which operating system or server image you want to create this new instance based on. If you've used the web interface for flex, you may know one off by heart, but chances are you'll need to check. For that, we need to talk to the image component of Openstack, called `glance`. Using the predictably named `glance` command that we installed earlier with all the other openstack tools, we can get a list with `glance image-list` like so:

```console
  [root@workstation ~]# glance image-list
  +--------------------------------------+--------------------------------+
  | ID                                   | Name                           |
  +--------------------------------------+--------------------------------+
  | b2316be1-6353-460d-b9ed-f890bdd8791b | Alpine-3.4_2016-09_Unsupported |
  | 9160f6b3-293d-4dfa-b07b-e1e84d30633f | CentOS6_2016-04                |
  | 2c739802-d864-4d36-ae09-78e326825518 | CentOS7_2016-01                |
  | fa13d75c-0d90-4e4d-b5d7-194445106ed8 | CentOS_Atomic_7_2016-05        |
  | a6df9578-e4e3-481b-affb-c6e1fb2a8652 | coreos_557.2.0_stable          |
  | 19ci820e-d6ed-463a-8452-713dff99f844 | Debian8_2015-12                |
  | faeof599-cab5-4db3-85b9-5a4ffa2051cb | gentoo                         |
  | 6bfo502f-dff5-44f4-996e-dbdae74da40b | Ubuntu1404_2016-01             |
  | 66cp8de3-9i39-46c6-94a3-de64226bea1f | Ubuntu1604_2016-04-r2          |
  +--------------------------------------+--------------------------------+
```

Your output to this command may very well be different, names may have been updated and the UUIDs have been changed in my examples on this page, so don't rely on the above content!

The final part of that command is `--flavor`. American spelling aside, (it doesn't accept `--flavour` as an alias sadly, I've tried) `flavor` is the openstack parlance for 'size of instance', so it's the setting that controls how much RAM and CPU allocation you're giving the instance, along with which tier (IO/mem/std). We're back to the `nova` command for this one, with `nova flavor-list`:

```console
  [root@workstation ~]# nova flavor-list
  +--------------------------------------+---------------+-----------+------+-----------+------+-------+-------------+-----------+
  | ID                                   | Name          | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
  +--------------------------------------+---------------+-----------+------+-----------+------+-------+-------------+-----------+
  | 238047d3-1428-4672-94dc-6640ab181029 | UKF1-std-1x0  | 512       | 20   | 0         |      | 1     | 65.0        | True      |
  | 36d82687-679a-499b-9c58-26a47bd27ea8 | UKF1-mem-8x64 | 65536     | 160  | 0         |      | 8     | 4160.0      | True      |
  | 37757dcf-4aeb-43ec-bda3-fb1fe517c320 | UKF1-io-8x16  | 16384     | 160  | 0         |      | 8     | 2080.0      | True      |
  | 4aa4f348-dc8a-4f8c-af9c-a2972c465203 | UKF1-mem-4x32 | 32768     | 120  | 0         |      | 4     | 2080.0      | True      |
  | 547288c5-c0dc-4277-804a-2f6b9cf4ca93 | UKF1-std-1x1  | 1024      | 30   | 0         |      | 1     | 1.0         | True      |
  | 7a71df69-080f-4a94-9ee9-33efe414f21a | UKF1-std-4x4  | 4096      | 60   | 0         |      | 4     | 520.0       | True      |
  | 97b8ac1c-e78a-451c-95ee-85cf728a0fdc | UKF1-io-2x4   | 4096      | 80   | 0         |      | 2     | 520.0       | True      |
  | 9bc640a8-b35f-4c9d-9116-269f49d8170d | UKF1-io-1x2   | 2048      | 40   | 0         |      | 1     | 260.0       | True      |
  | a8df2a5b-be54-4518-a1a9-69ae98923e57 | UKF1-mem-2x16 | 16384     | 80   | 0         |      | 2     | 1040.0      | True      |
  | d5a592eb-1f44-4b64-b19b-1d80886ae1e0 | UKF1-std-8x8  | 8192      | 80   | 0         |      | 8     | 1040.0      | True      |
  | d8da0f9d-c912-43d5-8b5d-ad072298fb1a | UKF1-mem-1x8  | 8192      | 40   | 0         |      | 1     | 520.0       | True      |
  | e0cc93bf-dcb1-4bb4-a45e-c9cee92df76a | UKF1-std-2x2  | 2048      | 40   | 0         |      | 2     | 260.0       | True      |
  | fa6ea278-5524-4342-9b90-03104ab6a869 | UKF1-io-4x8   | 8192      | 120  | 0         |      | 4     | 1040.0      | True      |
  +--------------------------------------+---------------+-----------+------+-----------+------+-------+-------------+-----------+
```

With all that information, we're now in a better place to understand my command from earlier, `nova boot --key-name default --image CentOS7_2016-01 --flavor UKF1-io-1x2 novatest` and the output we receive from it:

```console
  [root@workstation ~]# nova boot --key-name default --image CentOS7_2016-01 --flavor UKF1-io-1x2 novatest
  +--------------------------------------+--------------------------------------------------------+
  | Property                             | Value                                                  |
  +--------------------------------------+--------------------------------------------------------+
  | OS-DCF:diskConfig                    | MANUAL                                                 |
  | OS-EXT-AZ:availability_zone          |                                                        |
  | OS-EXT-STS:power_state               | 0                                                      |
  | OS-EXT-STS:task_state                | scheduling                                             |
  | OS-EXT-STS:vm_state                  | building                                               |
  | OS-SRV-USG:launched_at               | -                                                      |
  | OS-SRV-USG:terminated_at             | -                                                      |
  | accessIPv4                           |                                                        |
  | accessIPv6                           |                                                        |
  | adminPass                            | 9LoVzXbuSkEm                                           |
  | config_drive                         |                                                        |
  | created                              | 2016-10-05T11:54:25Z                                   |
  | flavor                               | UKF1-io-1x2 (91c640a8-b45f-4c8d-9z16-269f49da170d)     |
  | hostId                               |                                                        |
  | id                                   | 7805d590-2n13-4la7-8k27-612k1f7207a2                   |
  | image                                | CentOS7_2016-01 (2c739a02-d364-4v36-ai09-78e326o25518) |
  | key_name                             | default                                                |
  | metadata                             | {}                                                     |
  | name                                 | novatest                                               |
  | os-extended-volumes:volumes_attached | []                                                     |
  | progress                             | 0                                                      |
  | security_groups                      | default                                                |
  | status                               | BUILD                                                  |
  | tenant_id                            | 13f9asiud3289734sdkeizxch7bcc9dc                       |
  | updated                              | 2016-10-05T11:54:25Z                                   |
  | user_id                              | f6727383839djfhasdnvk90be7e9d270                       |
  +--------------------------------------+--------------------------------------------------------+
```

Switching back to `nova list` again, we can check that the instance is showing as we'd expect:

```console
  | 7805d590-2n13-4la7-8k27-612k1f7207a2 | novatest                 | ACTIVE    | -          | Running     | stnd=192.168.0.57                |
```

## Deleting instances

So it turns out that the section on creating instances is quite big, but thankfully this one is a lot simpler. Using the `delete` argument and a name or ID, we can quickly delete instances like this:

```console
  [root@workstation ~]# nova delete novatest
  Request to delete server novatest has been accepted.
```

We could also have given it the uuid ID of the instance, like so:

```console
  [root@workstation ~]# nova delete 7805d590-2n13-4la7-8k27-612k1f7207a2
  Request to delete server 7805d590-2n13-4la7-8k27-612k1f7207a2 has been accepted.
```

If you want to delete a few at a time, just append their names on:

```console
  [root@workstation ~]# nova delete serverb tower
  Request to delete server serverb has been accepted.
  Request to delete server tower has been accepted.
```
