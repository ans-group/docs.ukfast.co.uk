# How to install or update an Application

FastDesk desktop sessions are non-persistent which means that upon reboot, they revert to the base image template. For example, Overnight. Therefore any applications that you wish to persist longer should be installed on an application layer. An application layer is a virtual machine (VM) that is designed for installing applications. Once applications have been installed, the app layer is powered off and pushed out to users. Applications are then stored as a layer that attaches to your profile upon login. The FastDesk team typically put all of your applications on one application. However, there are instances in which you may have multiple application layers.

```eval_rst
.. note::

   Your FastDesk profile comes equipped with a HomeDrive which is also persistant storage location. However this alone will not allow applications to persist. 
   
```

## Accessing the Application Layer

If you would like to install an application, you will need to contact the FastDesk support team to request an app layer to be opened. The FastDesk support team will let you know that the layer has been opened and they will provide you with the details needed to log in. Once the application layer is open, you will be able to connect to and access it so that you may perform your application installations or updates.

To access the app layer, you will need to log into your database user, this is accessed the same way as you would access your desktop when you login. From the FastDesk login page, enter the credentials for the database user (which will have been provided to you through email or ticket when your database machine or entire solution was setup).

![Image 1: Citrix Website OS options Download Page](files/Website_download.PNG "Image 1: Citrix website OS options download page")

Once you are logged in, please open up the database user desktop as usual. 

![Image 1: Citrix Website OS options Download Page](files/Website_download.PNG "Image 1: Citrix website OS options download page")

Once the desktop has launched, you should see a remote desktop application shortcut that has been created on the desktop. This will be called `"Application layer Shortcut"`. Alternatively, it may be called the name of the application you are looking to install. 

![Image 1: Citrix Website OS options Download Page](files/Website_download.PNG "Image 1: Citrix website OS options download page")

If you click on that shortcut you should be prompted to enter a password to login into the application layer. The password needed will be provided to yourself through the ticket system via a ticket that will be raised in regards to your application install or update. If additional information is needed such as a username or IP address of the application layer then they may also be provided in the ticket.

## Installing or Updating the Application(s)

Once the application layer has been launched, it will function as a normal desktop, please install or update any applications that you have requested be added. 

  ```eval_rst
.. warning::

   Please do not shut down or finalize the application layer. Doing this will make it inaccessible and will require us to open a new application layer for yourself.
   
```

Once complete, please sign out of the application layer. Refer to **image **

Once signed out, please inform the FastDesk team that you are ready to push this layer out to users. If you are installing an application for the first time, please state which users you want to have access to the application.

To allow for the updated application to come through on your desktop yourself, and other users looking for the updated application layer will need to sign out of your desktop, wait a few minutes and then sign back in. After doing so the updated or newly installed application will appear on your desktop.
 
**_This instruction guide should assist you in installing or updating an application layer. If you have any questions or still require assistance, please contact the FastDesk support team on 0800 923 0617_**.

 ```eval_rst
   .. meta::
      :title: Installing or Updating an Application | UKFast Documentation
      :description: Guide for users on how to install or update and application 
      :keywords: FastDesk, Citrix, VDI, Citrix Receiver, Windows, Workspace Application, Application Layer, Database, Installation, Updating, LOB, Line of Business
