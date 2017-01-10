# Setting up the FASTcloudbackup agent

## Downloading the agent

Login to the [FASTcloudbackup web console](https://fcb.ukfast.co.uk) and click `Download Center` (apologies for the US spelling!).  

![download centre](files/download centre.PNG)

Find the appropriate Windows or Linux agent and click `Download`.  The agent will download based on your web browser's usual download process.  

![download agent](files/download agent.PNG)

## Installing the agent - Windows

Find the agent in your browser's download folder and open it.  Follow the instructions given to install the agent.

![download agent](files/windows-install01.png)

Select where to install the FASTcloudbackup agent. By default this will be to C:\Program Files\FASTcloudbackup\ContentStore

![download agent](files/windows-install02.png)

The installer will proceed to install the FASTcloudbackup agent on your computer.

![download agent](files/windows-install03.png)

You will be asked to name your computer, this will be the computer name displayed in your FASTcloudbackup console. By default, this will be the local hostname of the computer running the install, though you can change this to make it easier to identify the computer in the console. It is recommended to keep the Client Name and Host Name as the same value.

![download agent](files/windows-install04.png)

When you come to a screen called CommServe Authentication, you should enter the same User Name and Password that you used to log in to the FASTcloudbackup web console.

![download agent](files/windows-install05.png)

The installation will the complete and you can begin to manage backups of this computer in the FASTcloudbackup web console.

## Installing the agent - Linux

Once downloaded to your Linux client, extract the .tar file to any directory. Browse to the extracted directory and run "cvpkgadd" to begin the installer

'''
fastcloudbackup_linux_x86-64]# ./cvpkgadd
'''


## Checking the agent is set up correctly

Once you've installed the agent on your computer or server, you can check it's been set up properly by heading back to the [FASTcloudbackup web console](https://fcb.ukfast.co.uk).  From the home page click `My Data` and you'll be taken to a page called Computers.  On here you will see the computer(s) and server(s) you have installed the FASTcloudbackup agent on to.

![Computers installed](files/Computers installed.PNG)
