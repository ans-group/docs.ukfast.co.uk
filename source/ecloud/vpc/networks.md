# Networks
eCloud VPC networks are blocks of private address spacing that you can create attached to a router in your VPC, denoted by their CIDR identifier.

### How do the Networks work
Both class A (10.0.0.0) & class B ( 172.16.0.0) private IP ranges are available to use across the platform which need to be unique subnets per router. By default you are given the 10.0.0.0/24 if you selected 'create default networking' when you create a VPC.

### Create a Network
To create a network write a name, select the VPC & Router you wish to have the network connected to and write the CIDR block including the subnet in the final box. There is validation applied when trying to create to ensure that you do not overlap any other address spacing, you can only create blocks inside class A & class B ranges, the class C range is reserved for ANS use.

###  Delete a Network
Instance NICs are a dependency of networks so it will always block you from deleting the network if there are instances attached to it, ensure all Instances are deleted first before deleting your networks.

Note:  Networks can currently take up to 5 minutes (in certain regions) to delete due to how busy the workers are and the priority of other jobs in the queue.

```eval_rst
   .. title:: Networks
   .. meta::
      :title: eCloud VPC Networks | ANS Documentation
      :description: eCloud VPC Networks
      :keywords: ecloud, ecloud VPC, ANS Portal, VPC, Virtual Private Cloud, Networks
```
