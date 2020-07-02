# Navigating around a linux system

Navigating a Linux server using SSH for the first time can be a very daunting experience for those coming from a predominantly Windows/GUI background. The principal
difference from having a user interface is that you will not have a desktop, both in the visual sense and in that there is no common area to launch programs from in the way
that you may be used to.

Linux is primarily interacted with using the BASH shell. On logging in you will be in your user's home folder, for example if logging in as the user `graphiterack` you will
be in `/home/graphiterack`. The exception to this is the `root` user, root is akin to the administrator user in other operating systems and has permission to change
anything on the system and always logs in to `/root`.


You can always find your current location using the `pwd` command like so:

    [centos@arthas centos]# pwd
    /home/centos



## Getting around


`cd` will be your primary method of traversing the system, as you may have guessed `cd` stands for change directory. This command is used in conjunction with a filepath
to change to that directory, for example:


    cd /home/graphiterack/

`cd` can also be used to go up a folder in the system when used with two dots


    cd ..


Once you are in a directory you can view it's contents using the command `ls`.


    [cloud-user@arthas ~]$ ls
    python  sampleFile.txt  test


Extra details can be seen with the command `ls -l` which is commonly aliased to `ll` in RHEL/CentOS based systems.


     [cloud-user@arthas ~]$ ls -l
     total 12
     drwxr-xr-x. 3 cloud-user cloud-user 4096 Jan 15 12:55 python
     -rw-rw-r--. 1 cloud-user cloud-user  101 Apr  6 05:59 sampleFile.txt
     drwxrwxr-x. 2 cloud-user cloud-user 4096 Apr  6 07:19 test
     [cloud-user@arthas ~]$ ll
     total 12
     drwxr-xr-x. 3 cloud-user cloud-user 4096 Jan 15 12:55 python
     -rw-rw-r--. 1 cloud-user cloud-user  101 Apr  6 05:59 sampleFile.txt
     drwxrwxr-x. 2 cloud-user cloud-user 4096 Apr  6 07:19 test


As you can see here, both outputs are the same as it is a CentOS server.

## Viewing files


There are many way to view files in Linux, here we will cover the two most common ways that are found on the majority of Linux systems.

### cat


The `cat` utility can be used for a variety of operations, however in this article we will be using it in the most simple form `cat {filename}`. This will simply print
he contents of the file to the console window as so:


     [cloud-user@arthas ~]$ cat sampleFile.txt
     This is an example file
     There are many like it but this one is mine
     It has several lines
     and bacon.


`cat` is useful for quickly viewing small files that do not need to be edited.

### less


`less` is another common utility used to view the contents of files. `less` is useful for viewing files that are potentially very large and as such would not be easily
viewed with `cat`. Unlike `cat` which simply prints to standard output `less` is an interactive file viewer that will open the file for viewing in a new screen.
It can be opened with the command `less {filename}`.

When viewing a file in `less` it will be broken up into pages if the length of the file exceeds the size of your console window. These pages can be navigated with Page Up
and Page Down. The file can also be searched with `/` and `?` to search up and down the pages respectively.

## Creating files

The easiest way to create a file in any Linux directory is to use the `touch` command as follows:


     [cloud-user@arthas test]$ touch exampleFile.txt
     [cloud-user@arthas test]$ ls
     exampleFile.txt


This will create a blank file owned by the user that you are logged into the system with, these can then be edited with the text editor of your choice.

## Editing files


Linux has many text editors available for use, the most common two being `nano` and `vi`, each editor is worthy of an entire article to themselves however we will touch
upon the basics of each here.

### nano


To open a file in `nano` you simply need to type `nano` followed by the name of the file you wish to edit. In the following example I have used `nano sampleFile.txt`.

![nano](nano1.png)

You can interact with `nano` in the same was as any regular text editor, instructions for operations are outlined at the bottom of the window. These can be performed by
holding `Ctrl` and pressing the specified letter.

### vi


To open a file in `vi` is the same as `nano` simply type `vi {filename}`, however this is where the similarities end.

`vi` operates in two modes, command and input. The program will launch in command mode, to edit the file you will need to enter input mode. This can be done by pressing
`i`. Once in input mode you can edit text as you need to, to return to command mode hit `esc`. In command mode you can issue `:wq` to save your edits and exit the file.

```eval_rst
  .. title:: Navigating the Linux operating system
  .. meta::
     :title: Navigating the Linux operating system | UKFast Documentation
     :description: A guide on how to navigate through linux
     :keywords: ukfast, server, linux, cd, move, vi, virtual, vm, navigate, navigation
