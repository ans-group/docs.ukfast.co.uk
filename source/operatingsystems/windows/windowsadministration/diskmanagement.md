# Windows Disk Management

In windows you can manage the hard disks within your computer by using the Windows Disk Management console, to access this, please follow the below guide

Open the server manager either by selecting the Taskbar shortcut, or by selecting start and selecting server manager from the list of applications.

Once you have opened server manager, please select "Tools", and select "Computer Management" from the list of options as below

![Server Manager](Images/diskmanagement/contextmenu.PNG)

you will now be presented with the computer management console, on the left hand side of the window, please pop out the storage section of the list, and select "Disk Management"
In the central field of the window, you should now be presented with the disk management console after a few seconds as below

![Disk Management](Images/diskmanagement/diskmanagement.PNG)

This console will provide you with information about your currently installed hard disk drives, and will also allow you to make changes to the partitioning and filesystems of those hard disks as well as carry out other functions such as extending and shrinking current partitions.
To view this information and to make changes, please select the disk of your choice, and right click to view the available options for that drive as below

![Options](Images/diskmanagement/diskmanagementcontextmenu.PNG)

## Extending A Partition

To extend a partition to make use of additional space, please follow the steps above to access the Disk Management console, and then follow the guide below.

When additional capacity is added to a Windows Server, the space needs to be either added to an existing partition, or used to create a new partition before it becomes usable. the below example shows how extra capacity will appear to you in the Disk Management console.

![Disk Management-With Extra Space](Images/diskmanagement/freespacevisible.PNG)

In this example, we would like to extend drive C: to make use of the additional 20GB of available disk space, to do this, right click on the drive C: partition as below and select "Extend Volume" from the context menu.

![Partition Options](Images/diskmanagement/rightclickpartition.PNG)

You will now be presented with the "Extend Volume Wizard" as below, please select "Next"

![Extend Wizard](Images/diskmanagement/extendwizard.PNG)

The "Select Disks" pane will now be displayed as below

![Select Disks](Images/diskmanagement/spaceselect.PNG)

This pane will already be configured correctly for you to use the maximum available amount of space on the disk, however 2 options are worth noting.

- Maximum available space in MB : This represents the total amount of extra space available
- Select the amount of space in MB : This section allows you to choose the amount of the extra space that you wish to add to the disk in question, in this case C:

If for example, you only wished to add 10GB of the 20GB available to drive C:, you would need to change the "Select the amount of space in MB" field to 10240. Once you have entered the correct details, please select next.

You will now be presented with the "Completed the Extend Volume Wizard" pane as below, please review the selected setting in the middle of the pane, and then select "Finish".

![Finish](Images/diskmanagement/complete.PNG)

You will now be returned to the Disk Management console, where you will see that Partition has been expanded as per the example below

![Space Added](Images/diskmanagement/diskmanwithspaceadded.PNG)

The additional space is now usable.
