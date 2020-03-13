# Default Configuration for Windows Servers

## Pre-Launch Questionaire
With every dedicated server on your order form you will receive your Pre-Launch Questionnaire (PLQ). The PLQ give you the ability to verify the configuration for each server, firewall, or other configurable products on your order before we begin the launch process.

Once you are satisfied with your installation settings, please press the "Launch solution" button so that we can get your servers to you as quickly as possible. You will receive your PLQ within 15 minutes of your order form being processed.

To ensure that your order meets its scheduled launch date, the questionnaire will automatically close 24hrs after your order being processed and your server will meet the below default configuration. If you need more time to pre-configure your solution, you may extend the deadline by up to one week online, but please note that this may delay the delivery of your solution.

Please note that some of our more complex solutions may require you to complete additional documentation in order for us to gather as much information as possible to meet your requirements.

If you have a question about your order or our pre-launch process? You can call your Account Management Team on 0161 637 9321.


## Partitions
Please find below the UKFast Default Partitions configured as part of your solution. Default Partitions can be customised using your online Pre-Launch Questionnaire.

Partition | Size or % | Example (2x 256GB RAID1)
------------ | ------------- | -------------
C: Drive | 100GB | 100GB
D: Drive | Remaining Space | 135GB

## Default Installed Software
Please find below the UKFast Default Software installed as part of your solution. Default Software can be customised using your online Pre-Launch Questionnaire.

Software | Default - Yes/No
------------ | -------------
FileZilla | Yes
hMail Server | Yes
IIS Web Server | Yes
MySQL | Yes
MySQL Workbench | Yes
PHP | Yes
UKFast Backup Agent | Yes
McAfee | Yes

## Monitoring

### Service Monitoring
Service Monitoring can be customised using your online Pre-Launch Questionnaire on a per server basis. The following service monitoring will be added across all servers in the solution by default:

Monitoring | Default
------------ | -------------
Ping | Enabled
SMTP | Enabled
POP | Enabled
HTTP | Enabled
FTP | Enabled

If additional optional monitoring is required for services not listed above please inform your Account Manager or request via the Priority Support system in the MyUKFast portal after launch to make configuration changes.

#### Example Additional Monitoring Options

Hostname | Port / Service / URL | Default
------------ | ------------- | -------------
e.g. http://example.com/status.apsx | e.g. URL | Not Enabled

### Capacity Threshold Monitoring 
The following CTM alerts will be configured on your Windows servers, where applicable:

Name | Acceptable Range | Alert Triggered When | Default
------------ | ------------- | ------------- | -------------
CPU Usage | 0% - 80% | CPU usage hits 81% | Enabled
Memory Usage | 0% - 80% | Memory usage hits 81% | Enabled
C Drive Space (free) | 15% - 100% | Free space hits 14%  | Enabled
D Drive Space (free) | 15% - 100% | Free space hits 14% | Enabled

### Specific Application Monitoring
As part of your solution, we will add Application specific monitoring. Depending on the application and configuration of your solution will depend on whether this is applicable.

Application | When Applicable
------------ | -------------
DFS-R | When Distributed File System Replication is configured across more than one servers this is enabled by default.
Hyper-V Replica  | When Hyper-V Replication is configured across more than one server this is enabled by default.
Active Directory  | When Active Directory is installed and replicating between more than one servers this is enabled by default.
Failover Cluster Manager | When Failover Cluster Manager is installed and contains one or more clustered services this is enabled by default.
Microsoft SQL Server | When Microsoft SQL Server is installed this will monitor the SQL Service.

## Anti-Virus
All Physical and Virtual Machines as part of your solution will come with McAfee Anti-Virus installed, this comes as part of your PROprotection package.
Below you will find a list of common questions related to Anti-Virus:

IS THIS INSTALLED ON ALL SERVERS IN MY SOLUTION?
> This will be included on all servers if you have purchased PROprotection, both Windows and Linux server. The only devices this does not apply to are UKFast Appliances and Magento Servers.

ARE ALL FILES SCANNED BY THE AV SOFTWARE?
> Yes, on-access scanning is enabled by default.

AT WHAT FREQUENCY ARE FILES SCANNED?
> On-access scanning and weekly full scan.

AT WHAT FREQUENCY IS THE AV SOFTWARE UPDATED?
> Daily DAT Updates and Agent updates when available.

WHAT ARE DAT FILES?
> Virus definition or DAT files contain virus signatures and other information that McAfee anti-virus products use to protect your computer against existing and new potential threats. DAT files are released on a daily basis.

ARE ANY OTHER AV BASED TOOLS OR ACTIVATES USED? (E.G. LOCAL FIREWALL)
> No, by default local firewalls are disabled and no other AV tools are installed or used by UKFast.

## Updates

By default single role Windows Servers will have the following Group Policy Configuration, please note that Windows Updates policy can be customised using your online Pre-Launch Questionnaire:

- Automatically download and install all updates
- This will be scheduled for Friday at 8am.
- You are also able to configure Windows Updates with the following options:
- Automatically download all updates, but allow me to manually install the update
- Notify me when there is an update before downloading, and allow me to manually install the update
- Never check for updates
- Install Preferences (Day and Time) 

Please keep in mind that updates may reboot your server automatically, so you should pick an appropriate time to install the updates.

### Example Update Schedule:

Group 1 (Friday @ 8am) | Group 2 (Saturday @ 8am)
------------ | ------------- |
DC-01 | DC-02
WEB-01 | WEB-02
SQL-01 | SQL-02

## Application Specific Default Configuration

### MS-SQL Database Configuration

MS-SQL Setup | Default
------------ | ------------- |
MSSQL Version | As per your Order Form
Listening TCP / IP Port | 1433/TCP
Instance Name(s) |  MSSQLSERVER
Collation | Latin1_General_CI_AS
Additional Features / Components | All Components
Configuration | Log, Data and Backups will all be configured on the large partition

### IIS Web Configuration

IIS Setup | Default
------------ | ------------- |
Installed Version | Latest Version
Installed Components | Web-Server, Web-Basic-Auth, Web-ISAPI-Ext, Web-Scripting-Tools, Web-Http-Redirect, Web-Windows-Auth, Web-ISAPI-Filter, Web-DAV-Publishing, Web-CGI Web-Net-Ext, Web-Mgmt-Console, Web-Custom-Logging, Web-Http-Logging, Web-Includes, Web-Mgmt-Tools, Web-Stat-Compression, Web-Filtering, Web-ASP, Web-Asp-Net, Web-Asp-Net4 [2012 only], Web-Net-Ext45 [2012 only]

### Remote Desktop Services
Below outlines how the proposed configuration will be configured for an RDS Farm.
 
IMPORTANT NOTE: UKFast will configure each role, add the SSL certificate (if purchased through UKFast) and ensure each role is able to communicate with the others.
 
UKFast are **not** responsible for configuring users, Group Policies or RDS Collection Groups. This is the responsibility of the client to administer, although UKFast Support is on-hand if any guidance is required.

NetBIOS Name | Role | Role Services Installed | Installed Applications
------------ | ------------- | ------------- | -------------
RDSGW1 | RDS Web Access, Connection Broker & Gateway | RDS Web Access, Connection Broker & Gateway | None
RDSSH1 | RDS Session Host | RDS Session Host | Web Browser & Purchased Applications (I.E. Microsoft Office)
RDSSH2 | RDS Session Host | RDS Session Host | Web Browser & Purchased Applications (I.E. Microsoft Office)

### Citrix
Below outlines how the proposed virtual machines will be configured for an Citrix Farm.

NetBIOS Name | Role | Software / Features Installed
------------ | ------------- | ------------- 
CTXADC01 / CTXNS | Citrix Netscaler ADC | NetScaler ADC Appliance
CTXSF01 | Citrix StoreFront | Citrix StoreFront, Citrix Receiver & IIS
CTXDC01 | Citrix Delivery Controller & Citrix Studio | Citrix Delivery Controller, Citrix Studio & Citrix Receiver
CTXMISC01 | Citrix Licencing & Citrix Database Host | Citrix Licencing, Citrix Receiver & Microsoft SQL
CTXXENAPP01 | Citrix XenApp Host | Purchased Apps (I.E. Microsoft Office)
CTXXENAPP02 | Citrix XenApp Host | Purchased Apps (I.E. Microsoft Office)

```eval_rst
  .. meta::
      :title: UKFast Default Configuration Of A Windows Server | UKFast Documentation
      :description: Default Configuration for Windows Servers at deployment. 
      :keywords: ukfast, hosting, windows, server, virtual

