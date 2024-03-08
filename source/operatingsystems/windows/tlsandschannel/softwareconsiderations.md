# TLS Support for Windows Software

This section lists some things to be aware of before making changes to the Schannel security provider on Windows operating systems.

Schannel SSP configuration changes will affect the whole operating system. In other words, if you remove Schannel protocols in order to harden your web application, and that web application connects to a SQL instance on the same server, the Schannel changes will affect both the web application and the SQL instance.

## TLS Support for Microsoft SQL Server

Microsoft SQL Server has it's own set of compatibility considerations when it comes to SSL/TLS security.

A list of the SQL versions along with minimum patch requirements to support TLS 1.2 can be found at the external link below:

[TLS1.2 Support for Microsoft SQL](https://support.microsoft.com/en-us/help/3135244/tls-1-2-support-for-microsoft-sql-server)

## TLS support for Microsoft Exchange Server

Modern versions of Exchange will fully support TLS 1.2, providing, of course, that the Exchange environment has the necessary Cumulative Updates applied, and meets the minimum patch level.

You can read further information from the Microsoft Exchange Team's 3-part blog on TLS guidance, [here](https://blogs.technet.microsoft.com/exchange/2018/01/26/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/).

## TLS support for the Remote Desktop Services

There are some things to be aware of when it comes to RDS Farms.

The Remote Desktop Protocol (RDP) on Windows Servers 2012 R2 and newer fully supports TLS 1.2 encryption. If using an older operating system, such as Server 2008 R2, then you may need to apply Windows patches to [enable RDP to use TLS 1.1 and TLS 1.2](/operatingsystems/windows/tlsandschannel/webserverrecommendations/index#windows-server-2008-r2-2012).


### RDS Connection Broker TLS Compatibility
Administrators may find that when TLS 1.0 is disabled on the server running the Connection Broker role, the RDMS service can't start, and therefore users are not able to log into the Farm.

The reason for this is that, by default, the Connection Broker role will use a local Windows Internal Database (WID) to store session information. The WID does not currently support anything above TLS 1.0. This means that disabling this protocol will break connection broker and RDMS functionality.

More information on this can be found at the external link [here](https://support.microsoft.com/en-gb/help/4036954/disabling-tls1-0-can-cause-rds-connection-broker-or-rdms-to-fail).

The only way to migrate away from using the WID, is to configure the RDS deployment to use the connection broker in High Availability mode. This requires using a dedicated SQL Server to hold the Connection Broker information instead.

```eval_rst
   .. title:: TLS Support for Windows Software
   .. meta::
      :title: TLS Support for Windows Software | ANS Documentation
      :description: Considerations for TLS support of various applications
      :keywords: SSL, TLS, ukfast, Schannel, RDS, RDP, MSSQL, Exchange, windows
```
