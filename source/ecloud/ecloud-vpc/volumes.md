# Volumes
eCloud Volumes are a storage entity that you can attach to a single instance (shared volumes will allow you to connect to multiple Instances, which is coming in Q3). 

### How our Volumes work
eCloud Volumes are created on our industry leading SANs from HPE 3Par, in eCloud VPC they are independent resources that can be moved between your instances should you need to.

### Creating a Volume
A volume will be created for you when you launch an instance or alternatively you can create one from the volumes area in the control panel or via the APIs/CLI tools. 

Once you’ve created a volume you can then attach this volume to the required instance so you can access it. 

### Deleting a Volume

Volumes that contain the operating system that are attached to an instance are deleted when the instance is deleted - for you, any additional volumes will be unattached. They will incur charges until you delete them so it’s best to check in the volumes section if the volume still exists if you need it or not.


```eval_rst
   .. title:: Volumes
   .. meta::
      :title: Volumes | UKFast Documentation
      :description: Managing your Volumes
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud
```