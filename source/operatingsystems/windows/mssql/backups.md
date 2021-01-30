# Creating MSSQL Backups

* In order to create a backup of your database/s, please follow the below instructions, for the purposes of this guide, it is assumed that you are already logged in to your MSSQL instance.

Please select the database which you wish to backup from within your MSSQL instance, right click the database, select tasks, and you will be able to see a "Back up" option, as below, please select this

![Backup context menu](Images/backups/rightclickcontext.PNG)

You will now be presented with the "back up database" window, within this window, you will see at the top of the window, a source section, please select the database that you wish to backup, and choose the backup type which you wish to carry out
Further down this window, you will see the Destination section, please select add, and select the ```...``` button from the right hand side of the pane, now choose the location where would like the backup file to be placed and select Ok, you will now be returned to the Select backup Destination pane, please select OK again to confirm your selection.
The selection that you have chosen will now be displayed in the Destination field of the "Back Up Database window as below.

![Backup General Options](Images/backups/generaloptions.PNG)

From the left hand side of the Back Up Database window, within the "Select a Page" section, please select the "Media Options". You will be presented with a number of options related to the behaviour of the backup such as whether to verify the backup, or overwrite existing backup sets as below, please set the options which best suit your requirements, once you have done so, please select "Backup Options" from the "select a page" section.

![Media Options](Images/backups/mediaoptions.PNG)

The Backup Options window which is shown below, allows you to set several secondary options such as a backup expiry date and if you would like for the database backup to be compressed to reduce its storage footprint, please configure these options and select Ok to confirm your choices.

![Backup Options](Images/backups/backupsoptions.PNG)

* Your backup will now begin, and you will be presented with a confirmation once it has completed. You will now be able to retrieve the backup from the location which you specified while configuring the backup.

```eval_rst
  .. title:: Creating Microsoft SQL Server backups
  .. meta::
     :title: Creating Microsoft SQL Server backups | UKFast Documentation
     :description: A guide to backing up Microsoft SQL Server databases
     :keywords: ukfast, backup, mssql, microsoft, sql server, database, create, tutorial, guide, cloud, server
```
