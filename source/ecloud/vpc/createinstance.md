# How to launch an instance

To launch an instance you have two options. Manually configuring an instance which includes configuring your own image, compute, storage and networking or launching a pre-configured instance using the marketplace with options such as Docker, Moodle and WordPress to quickly launch these applications.

# Launch instance manually

Select 'Instances' on the menu then click the 'Launch Instance' button.

Pick a distribution from:

* `CentOS 7`
* `Ubuntu Server 20 LTS`
* `Debian 10`
* `Windows Server 2019`

You will then need to decide which VPC this instance will be deployed into. Which VPC you choose here will depend which network the instance can be assigned to.

Compute - Your compute resources are how many vCPUs and how much RAM will be assigned to the instance.

Storage - When adding the storage for a VM this will create a volume. You can also create additional volumes later from the 'volumes' section on the menu and attach these to the instance. Select your required IOPS for the storage volume here as well.

Networking - Which network this instance will be deployed to will depend upon which instance you selected. You will be able to select the VPC network and router here.

A floating IP will assign the instance a dedicated external IP address. The virtual machine will still be able to communicate internally with other devices on the network if this doesn't require a dedicated IP address.

```eval_rst
.. warning::
    Floating IP's are charged even if they are not assigned to an instance.
```

For backups it is important to know that this currently can't be changed once the instance has been created.

Finally give the instance an identifying name and click the 'Create Instance' button.

Marketplace:

You can quickly launch an instance with ready to go apps on your Virtual Machine.

```eval_rst
   .. title:: Create an Instance
   .. meta::
      :title: Virtual Private Cloud | UKFast Documentation
      :description: Creating an Instance
      :keywords: ecloud, ecloudv2, instance, VPC, Virtual Private Cloud
```