# Troubleshooting

This section contains help relating to problems you may run in to.

## Problems installing the FASTcloudbackup agent

(Oli please could you write this section)

## Add New Computer button doesn't work

There is an button on the Computers page labelled `Add New Computer`.  

![computer](files/computer.PNG)

You should not use this to add new computers or servers to be backed up - instead follow the instructions shown on [Setting up the FASTcloudbackup agent](link) - this will guide you through installing the agent so you can run and manage backups.

## Problems browsing file structure

FASTcloudbackup runs as a system service and so cannot pre-select or utilise shortcuts to folders such as Documents or Photos.  In order to find the folders you wish to backup you'll need to navigate through the full path - for example `C:\Users\[username]\Documents\[foldername]`

To make navigation simpler for folders you access regularly you can set up Favourite folders - see [Favourite folders](link) for instructions.

## The amount of data backed up is larger than the total of my files and folders

You may notice that the total amount of data backed up within FASTcloudbackup is larger than the size of the files and folders on the computer or server being backed up.  This will typically be because of any hidden files or metadata that has also been included in the backup process.

## Backups taking a long time to run

The first time a computer or server is backed up, a full backup of all selected files and folders needs to take place.  This can take a while, depending on the total amount of data.  Subsequent backups will be incremental, meaning that only files that have been changed or created since the last backup will be processed, making the backup quicker to run.

The speed of your network connectivity will also affect the time a backup takes to run.

You can set up an alert so you are notified if a single backup job exceeds 24 hours - see the [Alerts](link) section for details.

You can "kill" a backup job at any point through the [FASTcloudbackup web console](https://fcb.ukfast.co.uk).  When a backup job is in progress, click `Kill` in the Schedules area to stop the backup from running.

![kill](files/kill.PNG)

## Failed backups



## Showing Live Machine data and Network Share data









