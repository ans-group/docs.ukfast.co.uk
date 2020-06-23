# Viewing Microsoft SQL Activity Monitor

* Should you be facing performance issues with your database, The Activity Monitor can be a useful tool to help diagnose the root cause of the issue, to access it, please follow the below guide.

Firstly, you will need to log in to the Microsoft SQL Management Studio, to so this, please select start, and select all programs, now select Microsoft SQL Server management studio from the list of available applications as below

![SSMS open](Images/activitymonitor/startssmsopen.PNG)

You will now be presented with a log in box, you will need to enter the appropriate details in to this box to gain access to your MSSQL instance. once you have entered the correct details, please select "Connect"

![Login](Images/activitymonitor/logintrimmed.png)

Once you have logged in, you should be able to view your MSSQL instance in the object explorer to the left hand side of the window as below

![Object explorer](Images/activitymonitor/loggedin.PNG)

From this view, please select your instance (in this case named WINDOWS2012R2\SQLEXPRESS) and right click it, you should now see additional options for your instance including "Activity Monitor" as below. please select this from the list.

![Instance options](Images/activitymonitor/rightclickcontext.PNG)

You will now be presented with the SQL Server Activity Monitor which will provide you with a selection of performance related information. You can use this to identify any performance issues and find the root cause of those issues.

![Activity Monitor](Images/activitymonitor/activitymonitor.PNG)

```eval_rst
  .. title:: Microsoft SQL Server Activity Monitor | UKFast Documentation
  .. meta::
     :title: Microsoft SQL Server Activity Monitor | UKFast Documentation
     :description: Viewing the Microsoft SQL Server activity monitor
     :keywords: ukfast, windows, mssql, sql server, microsoft, database, activity, monitor, tutorial, cloud, server
