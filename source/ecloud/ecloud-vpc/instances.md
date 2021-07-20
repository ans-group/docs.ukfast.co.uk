# Instances
These are traditional compute servers for running windows and linux operating systems to host most workloads.

### How do Instances work
Our instances use either UKFast managed images or you can create private images from our managed images to run either a vanilla operating system or an image with pre-defined software installed. When launching an instance, you will select the VPC, router and network to connect it to and also define the compute & storage that exactly fits your needs (no flavours here).

### Launching an Instance (not from marketplace)

Choose your image, the most commonly used images will be displayed at the top under 'Distributions', set a name for your instance if required and select the VPC you wish the instance to be connected to, this will filter your router & network options).

Set the CPU, memory and disk space for your instance, pricing can be found on the pricing page (note that once storage is created it can only be increased and not shrunk). If you require the instance to be able to route out from your network then select that it requires a floating IP on top of defining which router & network to connect it to.

Check over the details and then press the launch instance button, in around a minute the 
instance should be ready for you use.
![Instances](files/instance-create.PNG)

Whilst your instance is being built you will see the following banner and the instance will be locked from changes whilst it is being built.
![Instances](files/instance-building.PNG)


Once your instance has finished building you will notice it now has a volume and NIC associated with it at the bottom of the form.
![Instances](files/instance-launched.PNG)

 
### Power
There are a number of power options available for your instance; 
•	Power on, Reset and Power off are all akin to physical operations of a server such as physically pressing the power off button
•	Restart and Shutdown are operating system level commands and will try to cleanly restart or shutdown your instance 
![Instances](files/instance-power.PNG)

### Instances -> Resize

Here you can change the following items: vCPU & RAM

Change with the slider or the entry box on the right for any item you wish to change and then press the resize button, changes to your instance may incur additional charges 

There will be a note when the changes affect the pricing of your instance: 
![Instances](files/instance-resize.PNG)

Whilst your instances size is changing, a banner will be shown and you will locked from making further changes until the request completes, once the request completes, you will be able to make further actions on your instance.
![Instances](files/instance-resize-complete.PNG)


### Instances -> Credentials

Here you will find the instances credentials, press the eye to show the password.
![Instances](files/instance-credentials.PNG)

### Delete Instances
You can delete your instances like all other resources using the trash can icon or form within the resource itself, note though if there is a floating IP or additional volumes attached these will be detached and still incur charges unless you clear them up also, the volume that the operating system sits on will always be deleted. This is slightly different behaviour to some of the other resources where it will error and prevent you from deleting, although the other resources will eventually do this too.

### Instance Console
If you wish to see what your instance is doing via it's (virtual) console (post launch), you can launch the console for the instance from the Instances list view by clicking the '>_ ' from the instances card. This will create an hour long session for you, note though after 15 minutes of inactivity the session will be closed.
![Instances](files/instance-console.PNG)


```eval_rst
   .. title:: Instances
   .. meta::
      :title: Instances | UKFast Documentation
      :description: Managing Instances
      :keywords: ecloud, ecloud VPC, MyUKFast, VPC, Virtual Private Cloud, Instances
```
