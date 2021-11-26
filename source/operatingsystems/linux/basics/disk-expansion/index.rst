=======================
Disk expansion (eCloud)
=======================

This guide covers the process of expanding the size of your disks on our eCloud Public and Private platforms.

In MyUKFast, you will be presented with options to alter your allocation of storage to a virtual machine (VM):

.. toctree::
   :maxdepth: 1

   add-disk
   resize-primary-disk

As most customers have a simple large :code:`/` partition, the recommended option is to resize the primary disk on the server and perform a :code:`lvextend` on the :code:`/` volume to make it larger. This is the easiest to perform and doesn't require the creation of new partitions.

If you would like to add custom partitions to your server (to separate `/` and `/home` onto different volumes, for example), you can use ether the "add a new disk" method and then configure a new Volume Group, Logical Volume, and mount point. **This should only be performed by advanced users.**

Resizing disks should be done with care and if you are uncomfortable with resizing disk, you may also wish to add a new disk instead

.. warning::
   **For users without Commvault or UKFast Backup in place:**

   Before resizing any disk or performing any changes to the logical volume configuration on the server, please ensure that you have taken a backup of your data.


.. toctree::
   :maxdepth: 1
