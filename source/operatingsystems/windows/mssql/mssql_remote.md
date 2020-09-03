## Connecting to MSSQL Instance remotely

In order to connect to a MSSQL instance from a remote source, The following is required;
```
- Check the port in which MSSQL is currently listening on (This is typically TCP port 1433)
- Outbound connectivity from the originating source to the destination server over the MSSQL port
- Firewall rules to allow inbound connectivity over the MSSQL port
- SSMS (SQL Server Management Services) To be installed on the remote client.
```
## How to check your servers MSSQL port

To check the port in which the SQL Server is configured to listen on, You would need to;
```
- Establish an RDP connection to the MSSQL server
- Open MSSQL Server Configuration manager
  - Open Start > Microsoft SQL Server {Version} > SQL Server {Version} Configuration Manager
- Expand SQL Server Network Configuration > Click Protocols for MSSQLSERVER > Right click "TCP/IP" > Properties > IP Addresses > Scroll down until you see your internal server IP and check "TCP port"
```
![Instance options](Images/mssql_remote/sql_configuration_manager.PNG)

## Opening the MSSQL Ports on your Firewall

Dependent upon on whether or not your server resides behind a dedicated or shared firewall, The following documentation will guide you through securely opening the MSSQL ports;

Dedicated Firewall: [https://docs.ukfast.co.uk/network/firewalls/dedi\_lockdown.html](https://docs.ukfast.co.uk/network/firewalls/dedi_lockdown.html)

Shared Firewall: [https://docs.ukfast.co.uk/network/firewalls/shared\_lockdown.html](https://docs.ukfast.co.uk/network/firewalls/shared_lockdown.html)

## Troubleshooting connectivity to your MSSQL Server

To check if your able to communicate both outbound from your network over the required MSSQL port. The following Powershell cmdlet can be utilised (Please note the TcpTestSucceeded indicates if the port is accessible);
```
Test-Netconnection {RemoteServerAddress} -port {MSSQLPORT}
```
Example;

![Instance options](Images/mssql_remote/tnc.png)

To further test connectivity to your instance, The following method can be used;

On your remote client > Go to start > Notepad.exe > File > Save As;

Filename: ConnectionTest.udl
Save As type: All Files (\*.\*)

![Instance options](Images/mssql_remote/udl_test.png)

Open the UDL File and enter the following information;

- Server name: Server IP
- User a specific username…: SQL Server Credentials
- Select the database on the server: Select the DB you would like to connect to
- Test connection.

## Installing SSMS and connecting to your instance

The latest SSMS client can be downloaded here: [https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15)

![Instance options](Images/mssql_remote/ssms.png)

In order to connect to the Instance, you will need to enter the correct connection details in to the "Connect to Server" pane as has been demonstrated above.

Please note that Windows Authentication may not be enabled on your Instance, if this is the case, you will need to use the "SA" Credentials to authenticate instead. in order to do this, you simply need to select the arrow next to the "Authentication" field, and select "SQL Server Authentication" then enter your SA credentials in the user name and password fields below.

```eval_rst
  .. title:: Setup Remote Access to MSSQL
  .. meta::
    :title: Setup Remote Access to MSSQL | UKFast Documentation
    :description: How to access an MSSQL instance between a client device and a MSSQL server
    :keywords: ukfast, mssql, windows, db, sql, remote, connection
```
