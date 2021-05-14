# Create a network

If you didn't select the option for a default network when creating your VPC you can manually create a network and assign this to your VPC.

You will need to create a router before creating a virtual network as the network will then be attached to the router. You can assign 1 router per VPC but can have multiple networks per router.

Start be selecting 'Routers' on the left side menu and then give this router an identifying name and select your VPC you wish to assign this router to from the dropdown.

Once the router is created you can choose the bandwidth required. Bandwidth can be changed at a later time if needed. Pricing for the throughput can be found under the 'Cost Management' option.

To create the Network click 'Networks' from the menu which will take you to the create a network screen. Give your network an identifying name and select your VPC. The router you just created for the selected VPC will now also be available. Finally enter a subnet range you wish to use and click 'Create Network'.

Once the Network has been created this will be available to select when launching an instance.

```eval_rst
   .. title:: Create a network
   .. meta::
      :title: Virtual Private Cloud | UKFast Documentation
      :description: Creating a Network
      :keywords: ecloud, ecloudv2, instance, VPC, Virtual Private Cloud, Network
```