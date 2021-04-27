# Virtual Private Cloud

A VPC is your Virtual Private Cloud. To create a VPC select the VPC option from the menu. Click the 'Create VPC' button which will take you to the setup page.

You can give your VPC an identifying name here and the region in which you want to create the VPC. The regions available are Manchester, Amsterdam or London.

After you have given the VPC a name and selected a region, you can choose either an automated network deployment which will automatically create a network for you, or deselect this option to manually create a network with more advanced settings.

# Default Network

During the VPC setup if you selected 'create default networking' you will have 1 network already created within your VPC overview available for you. This will provide you a default network which you can attach instances to. A router will also be created. It is important to note once the VPC has been setup with a default network the network cannot be changed afterwards with more advanced settings.

Each VPC can have 1 router which the virtual networks will be assigned to. If the router is created automatically with a default network, the polices and throughput can still be modified.

For more information on networking see the networks doc.

# Deleting a VPC

Before deleting the VPC you will have to delete the instances, network and router. Once these have been deleted you will then be able to delete the VPC.

To delete a VPC click the VPC you wish to delete from the VPC menu and click 'Delete VPC'. You will be asked to confirm if you want to delete this. If you are happy to delete the VPC confirm by clicking the 'Delete VPC' button.

```eval_rst
   .. title:: Virtual Private Cloud
   .. meta::
      :title: Virtual Private Cloud | UKFast Documentation
      :description: Creating a Virtual Private Cloud
      :keywords: ecloud, ecloudv2, instance, VPC, Virtual Private Cloud
```
