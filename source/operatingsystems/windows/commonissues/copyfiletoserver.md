# How to Transfer Files to and from a Server

Depending on the size of the file, Windows offers a few different methods of transferring data between two devices.

## Remote Desktop clipboard

For your convenience, before attempting to establish a remote desktop session with your server, please carry out the below steps, as they cannot be changed while a session is established.

To configure Remote desktop clipboard, please open the Remote Desktop Connection application. If you are unsure on how to do this, please see our guide **Connecting to a server via remote desktop**.

You should now be presented with the Remote Desktop Connection application which will look like this.

![mstsc](Files/rdpfilecopy/MSTSCoptions.PNG)

From this window, please select the "Options" button in the bottom left hand corner of the window. This will expand the window and provide you with a number of options which were previously not visible.

Select the "Local Resources" tab and ensure that the "Clipboard" option is ticked as below

![Clipboard option](Files/rdpfilecopy/RDPclipboardoption.PNG)

With the above option set, establish your connection.

You will now find that you can copy and paste files between your local workstation and the server, either by using the keyboard shortcuts (Copy) `ctrl+c` and (Paste) `ctrl+v` to copy and paste respectively, or by simply right clicking files and selecting the copy / paste options, as you would on your local workstation. For example

![rdpcopy](Files/rdpfilecopy/rdpcopy.png)

![rdpcopy](Files/rdpfilecopy/rdppaste.png)


If you're copying a large file, or a large number of files, you may find FTP meets your requirements better.

## FTP (File Transfer Protocol)

### FTP Server Installation

Before FTP file transfer can be used, an FTP server such as FileZilla will need to be installed on your Windows server. FileZilla is open source software and is available for free from this link:

[FileZilla Server](https://filezilla-project.org/download.php?type=server)

The installation of FileZilla FTP server is fairly simple. However, there are a few steps which need to be highlighted.

Upon beginning the installation, you will be presented with a licence agreement, select "I Agree".

The installation wizard will then progress to the "Choose Components" pane. In this pane you will need to choose the components which you wish to install, and select next

![FileZilla component selection](Files/ftpserveranduser/choosecomponentstrimmed.png)

You will now be prompted to choose the install location for FileZilla Server. This will be set by default to `C:\Program Files (x86)\FileZilla Server\`, which is perfectly fine, but you can change this if you prefer.

Once you have chosen the installation location, click Next.

The next pane will ask you to choose the startup options for FileZilla Server. By default this is set to "Install as service, started with Windows", which is the recommended option.

You will also be asked to provide an `Admin Port`, which will be used to remotely administrate the FileZilla Server. This will be set to port `14147` by default, but again, can be changed to your preference.

The final option on this pane is to decide if you want FileZilla to start once the setup process has been completed.

![FileZilla server settings](Files/ftpserveranduser/startupsettingstrimmed.png)

The next pane asks to you to select 2 further options before the installation begins. These options are related to the server interface.

The first option is to choose how the server interface starts. By default, this option is set to "Start if user logs on, apply to all users". This option can be set to your preference, and can be changed to start manually if you choose.

The second option is to choose if you would like the server interface to be started once the setup process has been completed. Once you have made your selection, click Install to begin the installation process.

![FileZilla server settings 2](Files/ftpserveranduser/startupsettings2trimmed.png)

Once the installation has completed, you will be presented with a screen similar to the one below. Once the completed notice is presented, you can select the Close button.

![FileZilla install complete](Files/ftpserveranduser/installcompletetrimmed.png)

### FTP User Creation

Now that the FTP Server has been installed, you will need to create a user account to work with. This section will guide you how to do this for FileZilla specifically, although the process is very similar in other FTP servers also.

First of all, you will need to open the FileZilla Server interface. Depending on your chosen options during the installation process, the interface may open automatically for you, but if not, you can launch it by selecting Start and selecting "FileZilla Server interface", as below.

![FileZilla Server interface start](Files/ftpserveranduser/ftpserverinstance.PNG)

You should now be presented with the FileZilla Server interface as below. This window will be pre-populated with the host `localhost`, meaning the server you are working on, and the admin port which you have chosen during the installation process.

The password field will be blank. This is as expected and does not matter at this point as a password has not yet been configured. Once you are sure that the details are as expected, click "Connect"

![FileZilla Server interface login](Files/ftpserveranduser/serverentrypane.PNG)

You will now be logged in to your FTP server, and will be presented with an FTP console as below.

![FileZilla Server interface logged in](Files/ftpserveranduser/serveropen.PNG)

From this pane, select "Edit" and "Users" to open the "Users" pane.

![Edit/Users](Files/ftpserveranduser/edituserstrimmed.png)

You will now be presented with the Users pane. Within this menu, select "Add" on the right hand side of the pane. This will present the "Add user account" pane Enter a user name in the text field, and select "Ok"

![Add User](Files/ftpserveranduser/usersgeneraltrimmed.png)

Following the last step, you will have returned to the "Users" pane, and you should now be able to see your new user account listed in the users pane to the right of the window.

![User Added](Files/ftpserveranduser/useraddedtrimmed.png)

Select your new user account in the Users section, and select the "password" tick box to enable a password for this account. Once you have done this, enter your choice of password into the text field next to the password option. Once done, select OK. Your new account is now protected.

Re-enter the Users pane, if you are unsure how to do this, use the steps above as a reference.

Once you have navigated back to the users pane, select "Shared folders" from the left hand "Page" menu. In this pane, you can add the directories which you would like your user to be able to access via FTP.

To do this, select "Add" under the "Shared folders" section of the pane. You will now be presented with a file browser pane. Navigate to your chosen folder and select OK.

```eval_rst
.. note:: You can only select single directories in this menu, and you will need to repeat this step for each directory that you wish to grant access to.
```

![Add Share](Files/ftpserveranduser/sharedfoldersaddsharetrimmed.png)

You will now be returned to the Shared folders page of the Users pane, and you will be able to see the share(s) which you have added. To the right hand side of this, you will see 2 small options sections named "Files" and "Directories". These are the permission options which will be granted to the user.

By default the Files section will contain the Read permission, which will allow the user to read files in your chosen directories, and the directories section will contain the list and `+ subdirs` permissions which will allow the user to list files in your chosen directories and subdirectories thereof.

You can grant extra permissions as per your requirements by ticking the appropriate boxes as below. Once you are happy with the permissions, select OK and the permissions will now be granted to your user and the account will be ready to use.

```eval_rst
.. note:: These permissions are set on a per directory and per user basis, in order to set appropriate permissions for other users, you will need to first select the user on the Users Pane, and then select the share for that user which you wish to change the permissions for.
```

![FTP permissions](Files/ftpserveranduser/shareaddedtrimmed.png)

### FTP Client Installation

Before FTP file transfer can occur between a client machine and your server, an FTP client such as FileZilla must be installed on your client machine. The FileZilla client is open source software and is available to download for free from this link

* [FileZilla Client](https://filezilla-project.org/download.php?type=client)

As with the FileZilla Server, the installation of the FileZilla client is fairly simple, but again, has a few steps which need to be highlighted.

Upon beginning the installation, you will be presented with a licence agreement, select "I Agree".

![Licence agreement](Files/ftpclient/installationpane1trimmed.png)

You will then be presented with the installation options. This pane will ask you if you would like to make this software available to all users or just yourself. Select your preference and click Next

![Installation options](Files/ftpclient/installationoptionstrimmed.png)

The next window will present you with the choice of components which you would like to install. Select the options which you require and select next.

![components](Files/ftpclient/choosecomponentstrimmed.png)

You will now be asked to choose an installation location as below. The default location is `C:\Program Files\FileZilla FTP Client`, however you can choose your own installation location should you wish to. Once you have selected the installation location, please select Next.

![install location](Files/ftpclient/chooseinstalllocationtrimmed.png)

The next window will ask you if you would like to create a start menu folder. This is entirely optional, however, I would recommend doing so as it will make it easier to locate the FileZilla shortcut down the line, should you need it. Once you have made this choice, please select Install to begin the installation process.

Once the installation has completed you will be presented with the window shown below. By default, the option to start FileZilla now is enabled. If you do not wish to start FileZilla straight away, please untick the box and select finish.

![Install complete](Files/ftpclient/installationcompletetrimmed.png)

* The FTP client is now installed and ready to use

### Connecting to your FTP Server

Depending on the options which you selected during the installation stage, your FileZilla client should now be open. However, if you did not opt to start FileZilla following installation, you can start it manually by selecting the Start menu, and selecting the FileZilla icon

![Ftp Client start](Files/ftpclient/startmenufilezilla.png)

Once you have opened the FileZilla client, you should be presented with the FTP console. In this console, you will notice 4 blank text fields across the top of the window, `Host`, `Username`, `Password` and `Port`. You will need to enter the details of your FTP server and account in to these fields.

![Ftp console](Files/ftpclient/ftpclient.png)

Once you have entered the details, as demonstrated above, please select Quick Connect. Once selected, you should begin to see a number of status updates being presented in the top field of the console window. Once the connection has been fully negotiated, your chosen shares should be visible in the Remote Site section of the window, and your connection is now active as below.

![Ftp connected](Files/ftpclient/ftpclientconnected.png)

Your connection is now active and you will be able to move files between the "Remote Site" field, and the "Local Site" field. Local site refers to your workstation, and remote site refers to the remote server.

If you are unable to move files in a particular direction, review your permissions for that file and its directory on your FileZilla Server. If you are unsure how to do this, please review the steps above on setting permissions.

```eval_rst
  .. title:: Transferring Files to/from a Server
  .. meta::
     :title: Transferring Files to/from a Server | ANS Documentation
     :description:  A guide with common errors with uploading files via ftp and remote desktop
     :keywords: ukfast, windows, ftp, rdp, files, uploading, remote, server, virtual, vm, webserver, website
```
