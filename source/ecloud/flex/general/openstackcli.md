# Installing the Openstack Command Line Client

This guide details how to install the Openstack command line tool and project-specific modules. The client is currently available on _most_ Linux distributions, Windows and MacOS. Every installation requires Python 2.7 or later.

## Installing Pip

### Ubuntu or Debian

```bash
# sudo apt install python-dev python-pip
```

### Red Hat Enterprise Linux, CentOS, or Fedora

```bash
# sudo yum install python-devel python-pip
```

### Microsoft Windows

```console
c:\> easy_install pip
```

```eval_rst
.. note::
   Ensure that the C:\Python27\Scripts directory is defined in the PATH environment variable, and use the easy_install command from the setuptools package.
```

### MacOS

```bash
# sudo easy_install pip
```

## Installing the Openstack client

Once `python-pip` and other dependencies have been installed, we can use pip to install the Openstack tools. Most tools that you will need to use will be in the default `python-openstackclient` package, however you are also able to install individual project packages (legacy) using the second command (using Glance as an example).

```bash
# pip install python-openstackclient
# pip install python-glanceclient
```

We recommend using a Python virtual environment for installing any Python modules, as this keeps all the dependencies together in one place and seperated from the system. You can find information about how to do this [here](https://docs.python.org/3/tutorial/venv.html).

## Upgrading / Removing clients

In order to upgrade your pip packages, run the `install` command with the `--upgrade` flag.

```bash
# pip install --upgrade python-openstackclient
```

To remove the openstackclient, run the `uninstall` command.

```bash
# pip uninstall python-openstackclient
```

If you'd like to find out more about the Openstack client, you can find more information [here](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html). We also have some documentation about [setting up environment variables](/ecloud/flex/general/settingvars) in order to authenticate with Keystone.

The next section of our documenation details managing the resources in your project, you can see more information about this below:

[Managing Resources](/ecloud/flex/resources/index)

```eval_rst
   .. title:: Installing the Openstack client
   .. meta::
      :title: Installing the Openstack client | UKFast Documentation
      :description: Details how to install the openstack command line client
      :keywords: openstack, ecloud, flex, ukfast, nova, swift, cinder, glance, keystone, heat, hosting, cloud, api, cli
```
