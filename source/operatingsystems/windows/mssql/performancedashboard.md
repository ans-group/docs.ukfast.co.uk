# Microsoft SQL Performance Dashboard

In order to view the MSSQL Performance Dashboard, please follow the below steps.(Please note, this guide assumes that you already have MSSQL Management studio installed, and that you are connected to your database, 
if this is not the case, and you are unsure of how to go about this, please follow our respective guides on those subjects)

The Performance Dashboard is a Custom Report which is written by Microsoft specifically for use with Microsoft SQL to advise on performance improvements and best practice changes that could be made to your the databases.

The Performance Dashboard is not installed by default, however you can obtain it for free by visiting the following link
[MSSQL Performance Dashboard](http://www.microsoft.com/en-gb/download/details.aspx?id=29063)

Once the performance dashboard has been installed, before it can be used, you will need to run the setup script located in the Performance dashboard installation directory. by default this is located in C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Performance Dashboard, navigate to the directory and select "setup", this will initialise the Performance Dashboard on your SQL instance.

Now that the setup process for the performance dashboard has been compeleted,you will need to access it via MSSQL Management Studio, to do so, pop out the Databases tab in the object explorer, then right click on the database which you wish to run the performance dashboard for as below, and select Report, and Custom reports.

![Right click context](Images/performancedashboard/rightclickcontextreports.PNG)

You will now be presented with an "Open File" context box, please navigate to the location where Performance Dashboard has been installed, by default this is C:\Program Files(x86)\Microsoft SQL Server\110\Tools\Performance Dashboard and select the performance_dashboard_main.rdl as below

![Location](Images/performancedashboard/perdashlocation.PNG)

Once you have selected the performance_dashboard_main.rdl file, you will be presented with a context box named "Run Custom Report" this box will contain a warning as below, in this instance, please select Run.

![Warning](Images/performancedashboard/runreport.PNG)

The Performance Dashboard report will generate, and once complete should be presented in your main field of view

![Performance](Images/performancedashboard/perfdashboard.PNG)

* You can navigate the performance dashboard to review different pieces of information, generally, any information which is underlined, can be selected to provide further details specifically related to that title.

```eval_rst
  .. title:: Microsoft SQL Server performance dashboard
  .. meta::
     :title: Microsoft SQL Server performance dashboard | UKFast Documentation
     :description: A guide to the Microsoft SQL Server performance dashboard
     :keywords: ukfast, windows, sql, sql server, microsoft, mssql, database, performance, dashboard, cloud, server
