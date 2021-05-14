# How to launch an instance

To launch an instance you have two options. Manually configuring an instance which includes configuring your own image, compute, storage and networking or launching a pre-configured instance using the marketplace with options such as Docker, Moodle and WordPress to quickly launch these applications.

## Launch instance manually

Select 'Instances' on the menu then click the 'Launch Instance' button.

Pick a distribution from:

* CentOS 7
* Ubuntu Server 20 LTS
* Debian 10
* Windows Server 2019

You will then need to decide which VPC this instance will be deployed into. The VPC you choose here will dictate which networks the instance can be assigned to.

### Compute

Your compute resources are how many vCPUs and how much RAM will be assigned to the instance.

### Storage

A volume will be created When you add storage to an instance. You can also create additional volumes later from the 'volumes' section on the menu, as well as being able to attach these to the instance. Select your required IOPS for the storage volume here as well.

### Networking

Which network this instance will be deployed to will depend upon which instance you selected. You will be able to select the VPC network and router here.

Selecting a floating IP will assign the instance a dedicated external IP address. The virtual machine will still be able to communicate with other devices on the internal network. It just won't be able to receive external traffic inbound if there is no floating IP assigned.

```eval_rst
.. warning::
    Floating IP's are charged even if they are not assigned to an instance.
```

### Backups

Decide if you want the instance to be backed up. 

```eval_rst
.. note::
   It is important to know that this currently can't be changed once the instance has been created.
```

Finally, give the instance an identifying name and click the 'Create Instance' button.

## Marketplace

You can quickly launch an instance with ready to go apps on your instance.

```eval_rst
   .. title:: Create an Instance
   .. meta::
      :title: Virtual Private Cloud | UKFast Documentation
      :description: Creating an Instance
      :keywords: ecloud, ecloudv2, instance, VPC, Virtual Private Cloud
```
