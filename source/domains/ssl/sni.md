# Using Server Name Indication (SNI) with SSL certificates

```eval_rst
  .. title:: SSL | Using SNI with SSL certificates
   .. meta::
      :title: SSL | Using SNI with SSL certificates | UKFast Documentation
      :description: Information on Using Server Name Indication (SNI) with SSL certificates
```

Server Name Indication (SNI) technology can be used to present multiple SSL certificates on the same IP address and TCP port number. This represents a more efficient use of scarce <nospell>IPv4</nospell> addresses and is our recommended way of configuring SSL certificates. SNI has been supported by all the major web browsers for several years.

Assuming you already have the domains and SSL certificates in question, follow the steps below to configure your SSL-enabled domains to point to a single IP address.

## Pointing your domains to an IP address

If you're using SafeDNS from UKFast, follow the steps in [this article](/domains/safedns/addnewdomain) to add your domain, along with the IP address you wish to point the domain to. Repeat this for each of the domain.

## Configuring an SSL certificate using SNI

Next step is to configure your SSL certificates to work with SNI, which is simple providing you're using a supported operating system on your web server(s). Operating systems which support SNI include:

- Ubuntu - all in-life versions
- CentOS 6 and later
- Windows Server 2012 and later

Using your server control panel of choice (such as cPanel or Plesk), simply configure your web server for each domain you wish to SSL-enable and point them to the same IP address. As SNI is already integrated into your server's OS, it will automatically handle the process from this point.

Step-by-step guidance on working with SSLs and SNI is available here:

- [cPanel](https://documentation.cpanel.net/display/ALD/Install+an+SSL+Certificate+on+a+Domain#InstallanSSLCertificateonaDomain-SNIandmultiplecertificates)
- [Plesk](https://support.plesk.com/hc/en-us/articles/213944545-How-to-activate-the-SNI-support-on-the-Plesk-server-)

For more information on SNI and a full list of web browsers that support it, please see [this Wikipedia article](https://en.wikipedia.org/wiki/Server_Name_Indication)
