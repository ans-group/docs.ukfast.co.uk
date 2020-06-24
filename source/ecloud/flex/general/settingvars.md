# Setting Environment Variables for eCloud Flex

This guide is more of a springboard for the others in this category, getting your work environment set up in such a way that all the OpenStack tools we use work correctly out of the gate.

## The OpenStack RC file

The primary way in which we'll achieve this is via use of a file provided by OpenStack. This file is a list of pre-populated environment variables that will be used whenever you log into your shell session.

It's best explained through demonstration, so you can head to the following location to find the file:

<https://api.openstack.ecloud.co.uk/project/api_access/>

There's a button titled `Download OpenStack RC File v3`, which is the one you're after. Either save it directly onto your computer and then transfer it to whichever machine you're going to be using the tools from, or open it in a notepad and paste it into something called os.rc in a location you'll remember.

It should look something like this:

```bash
#!/usr/bin/env bash

# To use an OpenStack cloud you need to authenticate against the Identity
# service named keystone, which returns a **Token** and **Service Catalog**.
# The catalog contains the endpoints for all services the user/tenant has
# access to - such as Compute, Image Service, Identity, Object Storage, Block
# Storage, and Networking (code-named nova, glance, keystone, swift,
# cinder, and neutron).
#
# *NOTE*: Using the 3 *Identity API* does not necessarily mean any other
# OpenStack API is version 3. For example, your cloud provider may implement
# Image API v1.1, Block Storage API v2, and Compute API v2.0. OS_AUTH_URL is
# only for the Identity API served through keystone.
export OS_AUTH_URL=https://api.openstack.ecloud.co.uk:5000/v3

# With the addition of Keystone we have standardized on the term **project**
# as the entity that owns the resources.
export OS_PROJECT_ID=***********************
export OS_PROJECT_NAME="Project-*****"
export OS_USER_DOMAIN_NAME="Default"
if [ -z "$OS_USER_DOMAIN_NAME" ]; then unset OS_USER_DOMAIN_NAME; fi

# unset v2.0 items in case set
unset OS_TENANT_ID
unset OS_TENANT_NAME

# In addition to the owning entity (tenant), OpenStack stores the entity
# performing the action as the **user**.
export OS_USERNAME="joe.bloggs"

# With Keystone you pass the keystone password.
echo "Please enter your OpenStack Password for project $OS_PROJECT_NAME as user $OS_USERNAME: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT

# If your configuration has multiple regions, we set that information here.
# OS_REGION_NAME is optional and only valid in certain environments.
export OS_REGION_NAME="RegionOne"
# Don't leave a blank variable, unset it if it was empty
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi

export OS_INTERFACE=public
export OS_IDENTITY_API_VERSION=3
```

On the machine you're going to be running your OpenStack commands on, open up `~/.bash_profile` (adapt as appropriate if you're using an alternate shell) and add `source ~/.os.rc` to it, replacing `~/.os.rc` with wherever you saved the rc file, so that it looks somewhat like this:

```bash
  # .bash_profile

  # Get the aliases and functions
  if [ -f ~/.bashrc ]; then
      . ~/.bashrc
  fi

  source ~/.os.rc

  # User specific environment and startup programs

  PATH=$PATH:$HOME/bin

  export PATH
```

Either log out and back in, or type `source ~/.os.rc` to essentially run the file, setting all the necessary environment variables. The first thing you'll notice is that this causes a prompt to appear, asking for your OpenStack password. This is because it's not stored in the rc file by default, it sets it manually each time you log in so that it's not stored in plaintext on the filesystem.

```console
  [root@workstation ~]# source ~/.os.rc
  Please enter your OpenStack Password:
```

```eval_rst
.. warning::
  This won't actually validate the password, so if you put a bad password in at this point it won't flag it up, it'll just stop all the commands from working correctly.
```

From here on out, you should be good. You'll be prompted for your OpenStack password whenever you open a shell session, and once you've provided it you're able to authenticate with your project. The next section of our documenation details how to install the openstack client so you're able to manipulate resources in your project, you can see more information about this below:

[Installing the Openstack Command Line Client](/ecloud/flex/general/openstackcli)

```eval_rst
.. meta::
     :title: Setting Environment Variables for eCloud Flex
     :description: Details how to set necessary environment variables to connect to eCloud Flex
     :keywords: openstack, ecloud, flex, ukfast, nova, swift, cinder, glance, keystone, heat, hosting, cloud, api, variables
```
