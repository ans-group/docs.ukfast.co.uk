# Restoring an MSSQL Database from backup

In order to Restore a database to your MSSQL Instance, please follow the below steps.(Please note, this guide assumes that you already have MSSQL Management studio installed, and that you are connected to your database,
if this is not the case, and you are unsure of how to go about this, please follow our respective guides on those subjects)

To Restore a copy of your database from a pre-made backup, firstly right click anywhere on or within the databases menu in object explorer to the left hand side of the Microsoft SQL management studio, and select Restore Database from the resulting context box as below

![context menu](Images/restoredb/rightclickcontextmenu.PNG)

* You will now be presented with the "Restore Database" pane, you will see a source field and a destination field in the centre of this pane, in the source filed, please select the "Device" option (this allows you to restore a backup file from your local hard disk drive)
* Once you have selected Device, please select the `...` button which will present the "Select backup devices" pane, ensure that the backup media type is set to file, and select "Add".
* Now navigate to the database backup and select the file which you wish to restore, once the file has been selected, select "OK".
* You will now be returned to the "Select backup devices" pane, once you are happy that all of the files which you wish to restore have been selected, please select "OK"

You will now be taken back to the "Restore Database" pane and it should look similar to the below example

![Restore Prepped](Images/restoredb/restoredatabase.PNG)

Now Select "OK" and the restore process will start, once completed a prompt will be displayed to inform you that the process has completed, and you should now be able to see your restored database in the databases section of MSSQL Management Studio as below

![Restore complete](Images/restoredb/databaserestored.PNG)

* The Restore process is now complete.

```eval_rst
  .. title:: Restoring a Microsoft SQL Server database from backup
  .. meta::
     :title: Restoring a Microsoft SQL Server database from backup | ANS Documentation
     :description: How to restore a Microsoft SQL Server database from a backup
     :keywords: ukfast, windows, mssql, sql, sql server, microsoft, database, restore, backup, cloud, server
```
