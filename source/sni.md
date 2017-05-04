# Using Server Name Indication (SNI) with SSL certificates

Server Name Indication (SNI) technology can be used to present multiple SSL certificates on the same IP address and TCP port number.  This represents a more efficient use of scarce IPv4 addresses and is our recommended way of configuring SSL certificates.  SNI has been supported by all the major web browsers for several years.

## How to configure an SSL certificate using SNI

Configuring your SSL certificates to work with SNI is very simple providing you're using a supported operating system on your web server(s), which include:

- Ubuntu - all in-life versions
- CentOS 6 onwards
- Windows Server 2012 onwards

Using your server control panel of choice (such as cPanel or Plesk), simply configure your web server for domain you wish to SSL-enable and point them to the same IP address.  As SNI is already integrated into your server's OS, it will automatically handle the process from this point.

For more information on SNI and a full list of web browsers that support it, please see [this Wikipedia article](https://en.wikipedia.org/wiki/Server_Name_Indication)
