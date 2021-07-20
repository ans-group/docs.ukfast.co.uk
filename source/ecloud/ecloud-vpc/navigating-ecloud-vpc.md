# Navigating eCloud VPC Control Panel

## Regions
An eCloud VPC region is an isolated and geographically separated area from other eCloud VPC regions.

Currently there are three; each of them currently have one availability zone available to create resources in. The regions are Amsterdam, London & Manchester. When you land on the eCloud VPC page for the first time, the default region will be Manchester.

Regions are selectable from the top of the left hand menu, the default is 'Manchester'

## Availability Zones
Coming Q3 2021, availability zones will allow resources to be distributed into the same geographical area but with segregation of some networking and power.

## Resource Status'
All of the resources within eCloud VPC have a status that can be one of the following four states:


The health of the resource is good 
![Status Complete](files/status-complete.PNG) 
The resource is currently being created, updated or deleted 
![Status In Progress](files/status-in-progress.PNG) 
The resource, for any number of reasons has failed to create, update or delete 
![Status Failed](files/status-failed.PNG) 
The resource has been successfully deleted and will not show after a refresh. 
![Status Deleted](files/status-deleted.PNG) 

## Cards
Most resources we display are shown as 'cards' on MyUKFast, with their display name in bold on the top-left and then the most relevant information for that resource shown below. In this example of a floating IP it displays its name and then the id, the VPC it belongs to, the actual IP, where it is assigned to and its status. The card can be clicked to view further information and make changes to the resource.
![eCloud VPC Card](files/vpc-card.PNG)


```eval_rst
   .. title:: Navigating eCloud VPC
   .. meta::
      :title: Navigating eCloud VPC Control Panel | UKFast Documentation
      :description: Navigating eCloud VPC Control Panel (MyUKFast)
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud
```
