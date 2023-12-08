# How to create a Microsoft SQL Server Database User

* In order to Create a Microsoft SQL Server database user, please follow the steps below. (For this guide, it is assumed that you have already created a database, and that you have access to SA credentials or Credentials with user creation privileges assigned to them)

Firstly, please log in to Microsoft SQL Management Studio using your SA (or Equivalent) credentials as below

![SA Login](Images/createuser/salogin.PNG)

Once logged in, drop out the Databases section within Object Explorer, then drop out the database which you wish to create a new user for.
You will now see a number of folders appear under your database in the object explorer, drop out the security section, followed by the users section.
A list of users will now be visible, right click on the Users object and select "New User" as below

![New User](Images/createuser/rightclickcontextnewuser.PNG)

You will now be presented with the Database User pane, Within this pane, you will see 5 pages under "Select a page" on the left hand side of the screen, and by default you should be currently on the "General" page as below. Within this page, please set the user type,
* Several options are listed in the "User Type" selector which are self explanatory, however for the purposes of this guide, we are going to use the "SQL user with login" option.

Enter a user name, and a login name, the user name will be the displayed user name within your database, and the login name will be used specifically for logging in to the SQL instance. Once you are happy with the details that you have entered, please select "Owned Schemas" from the "Select a page" menu on the left hand side of the pane.

![New Users General](Images/createuser/detailsentered.PNG)

On the owned schemas pane, you can select a variety of Different Schemas to assign this user to, an explanation of these schemas can be found at the link below, once you have made your selection, please select "Membership" from the "Select a page" menu on the left hand side of the pane.

* [MSSQL Schemas](https://technet.microsoft.com/en-us/library/ms191451(v=sql.90).aspx)

You will now be presented with the Database role membership selection pane as below, within this pane, you will need to select the appropriate Roles for your user, this is entirely your own choice, and should be set in accordance with what task the user will be carrying out.
For an explanation of the different roles and their functions, please visit the following link.

* [Database Roles](https://msdn.microsoft.com/en-GB/library/ms189121.aspx)

![Membership](Images/createuser/membership.PNG)

* Once you are happy with your choices, please select OK to create your user, you will now be returned to the MSSQL Management Studio, and you should be able to see your new user in the users list for your database as below

![New User](Images/createuser/uservisible.PNG)

```eval_rst
  .. title:: Creating a Microsoft SQL Server database user
  .. meta::
     :title: Creating a Microsoft SQL Server database user | ANS Documentation
     :description: A guide to creating a Microsoft SQL Server database user
     :keywords: ukfast, database, mssql, sql, sql server, windows, user, microsoft, server, cloud, tutorial
```
