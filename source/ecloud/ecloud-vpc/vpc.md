## VPC  
An eCloud Virtual Private Cloud (VPC) is a logical collection of resources defined by its networking.

### How a VPC works
A VPC is much like a traditional data centre where you can (virtually) create your networking (routers and networks) and then create resources attached to those networks to consume. On creation we add a DHCP server to the VPC and some other minor administrative jobs to get going, there is no charge for a VPC by itself.

You can filter by VPC by selecting the VPC from the left hand menu (set to ‘Show All’ by default.)

### How to create a VPC

Select the region you want to create the VPC in using the dropdown on the left hand menu and press the Create VPC button.  
![VPC Listview](files/vpc-listview.PNG)

You will be asked to enter a name, if you wish to have the default networking created for you then leave the check box (this will create a router on our free tier & a network CIDR of 10.0.0.0/24). There is also the option to allow advanced networking, this enables east-west firewalling between network segments – note that this can only be done on VPC creation but does incur additional costs for instances.

Tick the terms and conditions check box and create the VPC.
![VPC Listview](files/vpc-listview-setup.PNG)

 
Automation is then triggered to configure your VPC in the background (should be almost instant). Automation does the following tasks (depending on what you set);   

1.	Creates a router in the default Availability Zone (if there is only one, otherwise you can pick your AZ). *The routers throughput is set to 25Mb/s by default.*  
2.	Creates a 10.0.0.0/24 CIDR Network  
3.	Creates default firewall rules (if you selected ‘Create default networking’) to allow common communication ports with your network and further restrict inbound access to your network  

The VPC is then available for you to start adding resources to.  
![VPC Listview with card](files/vpc-listview-card-example.PNG)
 

### Deleting your VPC

To delete your VPC you must ensure that there are no resources that are linked to your VPC, this includes:

Instances, dedicated hosts, Networks, Routers & Floating IP addresses.

Note, currently networks can take up to several minutes to delete – please ensure they no longer show before deleting the router and then the VPC



```eval_rst
   .. title:: Virtual Private Cloud (VPC)
   .. meta::
      :title: Virtual Private Cloud (VPC) | UKFast Documentation
      :description: Virtual Private Cloud (VPC)
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud
```