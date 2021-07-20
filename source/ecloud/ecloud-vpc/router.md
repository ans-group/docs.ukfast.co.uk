# VPC
An eCloud Virtual Private Cloud (VPC) is a logical collection of resources defined by its networking.

### How a VPC works
## Routers
Routers are the entry and exit point for your networking within your VPCs, within a VPC you can have multiple routers if you require that can each be configured individually.

### How our Router works
The routers are connected to the internet at the speed defined in the router properties.  North-South firewalling is applied on the router, this is why the firewall policies are within the router section (if you use MyUKFast to manage your routers)

### Create a Router
In most cases where a single router suffices in your VPC, you would typically have created this by default when launching your VPC, there is the option to add more which you can do from the router section - set the option to create the router from the menu and then also set the bandwidth, note that the bandwidth is chargeable above the free tier.

### Delete a Router
Routers cannot be deleted unless they have no networks attached to them, once they have none then you can delete with either the trash can or button on the page like all other resources.


```eval_rst
   .. title:: Routers
   .. meta::
      :title: Routers | UKFast Documentation
      :description: Managing your routers in eCloud VPC
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud, Router
```