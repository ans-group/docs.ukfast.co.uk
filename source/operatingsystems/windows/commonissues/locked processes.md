# How to identify which Windows Process is locking a File or Folder

When trying to delete, move or rename a file you may have experienced one of the following Windows System warning messages.

* Cannot delete file: Access is denied
* There has been a sharing violation
* The source or destination file may be in use
* The file is in use by another program or user
* Make sure the disk is not full or write-protected and that the file is not currently in use

## How to resolve the issue?

The easiest way to find handle locked files or folders is to use Microsoft’s Process explorer:
[MS Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)

By using process explorer there is a nice and easy way to find the problematic program that is using a file:

1.	Right click on procexp.exe and “run as administrator” 
2.	On the tool bar at the top click the icon that is a small black circle inside a larger black circle with arrows pointing inwards. 

![sight](commonissues/Files/sight.png)

3.	Drag the icon that appears and place it on the open file/folder that is locked.
4.	The executable that is using the file will then be highlighted from within process explorer displayed list.

How to identify which DLL or Handle is locking a file?

1.	Open file explorer as administrator
2.	Use CTRL + F to open the process explorer search function
3.	In the open search dialog box type in a name of a locked file/file of interest you
4.	Click the “Search” Button
5.	A list will then be generated with the search results (this may include a number of entries)

![search](commonissues/Files/explorersearch.png)

How to release the file/folder?

In order to release the lock on the file you will need to kill the process that is appropriately associated with the file. To kill an individual program or handle in the list provided by file explorer you do so via the following:

1.	Select the process/handle/program entry in the via the process explorer list

![list](commonissues/Files/processlist.png)

2.	Press the delete key to kill the process (this can also be achieved by right clicking on the process/handle/program entry and clicking “kill process”
