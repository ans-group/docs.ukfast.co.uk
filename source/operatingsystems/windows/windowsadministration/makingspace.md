# How to free up hard disk space on your Windows Server

* If you are running low on disk space on your Windows Server, there are a number of different locations which are known to accumulate data which can be reviewed to remove unneeded files and free up space. to do this, please follow the below guide.

The most common locations of data which is potentially not required are 
* Users Desktops and My Documents folders
* Log Folders i.e. C:\inetpub\logs, C:\Windows\Logs
* Custom Backup Folders
* User Recycle Bins
* An unhealthy WBEM Repository directory
* MSSQL SQL Logs (Located in the MSSQL Log Directory)
    

If you are unable to discover what is responsible for the space consumption,You can use a tool such as TreeSize which is a disk space analyser that can be downloaded for free from 
[TreeSize](http://www.jam-software.de/treesize_free/?language=EN)

* If you have found large log file directories but cannot delete these due to compliance requirements, it would be advisable that these files were simply moved to a different drive with more free space where they can be stored for as long as required.

```eval_rst
  .. title:: Freeing up hard disk space on Windows Server | UKFast Documentation
  .. meta::
     :title: Freeing up hard disk space on Windows Server | UKFast Documentation
     :description: Instructions on how to free up hard disk space on a Windows Server
     :keywords: ukfast, windows, server, cloud, drive, disk, free, empty, space, full, remove, tutorial
