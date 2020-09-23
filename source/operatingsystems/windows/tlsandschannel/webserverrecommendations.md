# Security Recommendations for Internet facing Web Servers

A very popular online tool to determine which TLS protocols and cipher suites are supported by your Web server is [SSL Labs](https://www.ssllabs.com/index.html)(External Link). This platform will enumerate all available protocols and give you a rating based on the security of your supported suites. The requirements to get the best rating are reviewed frequently as newer vulnerabilities and exploits are found. This ensures that you will always get the most up-to-date recommendations and information. For example, starting from March 2018, any web server that does not support Perfect Forward Secrecy or AEAD suites, [is capped at a 'B' rating](https://blog.qualys.com/ssllabs/2018/02/02/forward-secrecy-authenticated-encryption-and-robot-grading-update). 

Mozilla also have an excellent page on [Server-Side TLS]( 
https://wiki.mozilla.org/Security/Server_Side_TLS).

_Below, we will take a look specifically at Windows Server operating systems. Linux web servers running Apache or Nginx, with OpenSSL as the security provider will be discussed later._

A good place to dive into the specifics of Microsoft's security implementation is the Microsoft Technet blog post on [Demystifying SChannel](https://blogs.technet.microsoft.com/askpfeplat/2017/11/13/demystifying-schannel/)

If the Windows web server is connecting directly to the Internet, and does not use a Webcelerator or Loadbalancer to terminate SSL/TLS connections, then please check the following for your relevant operating system. 

### Server-Side Protocol Support 

In order to complete a TLS handshake, both parties must support at least one common protocol and cipher suite. When discussing the TLS handshake we will use the terms server-side TLS and client-side TLS. 

 

**Server-Side TLS** - This will be a service, such as a web server which accepts requests and serves content. Webmasters and server administrators can configure the server settings to dictate which protocols the server will support for the TLS handshake.  The following section discusses this is detail

**Client-Side TLS** - This will be handled by a Web browser or user device, such as a smartphone. The client will _initiate_ the TLS handshake. Webmasters and developers will have no control over which protocols and ciphers a client will try to negotiate with. We can, however, influence the decision by disabling any protocols or ciphers at the server-side that we do not want to use. 


```eval_rst
+------------------------+---------------+----------+---------+----------+----------+
| Windows Version        | SSL 2         | SSL 3    | TLS 1.0 | TLS 1.1  | TLS 1.2  |
+========================+===============+==========+=========+==========+==========+
| Windows Server 2008    | Enabled       | Enabled  | Enabled | Disabled | Disabled |
+------------------------+---------------+----------+---------+----------+----------+
| Windows Server 2008 R2 | Enabled       | Enabled  | Enabled | Disabled | Disabled |
+------------------------+---------------+----------+---------+----------+----------+
| Windows Server 2012    | Disabled      | Enabled  | Enabled | Enabled  | Enabled  |
+------------------------+---------------+----------+---------+----------+----------+
| Windows Server 2012 R2 | Disabled      | Enabled  | Enabled | Enabled  | Enabled  |
+------------------------+---------------+----------+---------+----------+----------+
| Windows Server 2016    | Not Supported | Disabled | Enabled | Enabled  | Enabled  |
+------------------------+---------------+----------+---------+----------+----------+
```

## Windows Server 2016

Windows Server 2016, being the latest production version of Microsoft's server operating system, naturally provides support for the newest and most secure cipher suites. 

Notably, Server 2016 supports the `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` cipher (and the `AES_256` variant) which provides both Forward Secrecy (using ECDHE) and Authenticated Encryption (AEAD) while using RSA authentication. All earlier versions of Windows need to either use ECDSA authentication (by using an ECC certificate) or rely on the much slower DHE in order to provide both AEAD and PFS (Perfect Forward Secrecy).   

A full list of supported ciphers and protocols for Windows Server 2016, can be found [here](https://msdn.microsoft.com/en-us/library/windows/desktop/mt490158(v=vs.85).aspx)

As the table shows [above](#server-side-protocol-support), TLS 1.0 is still enabled by default on Windows Server 2016 for backwards compatibility. If you have no services that require this then you can go-ahead and disable the TLS 1.0 protocol. 


## Windows Server 2012 R2

In the table shown [above](#server-side-protocol-support), you can see that all protocols except SSLv2 are enabled by default. From these defaults,  we recommend that SSLv3 and TLS 1.0 are disabled, as these are considered cryptographically weaker than the latest TLS versions. 

If Windows Updates are being routinely applied to your Windows Server (and they should be!) then you should have the following Cumulative update installed on 2012 R2 servers already: 

[KB2919355 - Cumulative Update April 2014](https://support.microsoft.com/en-gb/help/2919355/windows-rt-8-1-windows-8-1-and-windows-server-2012-r2-update-april-201) 

This cumulative update installs
[KB2929781](https://support.microsoft.com/en-us/help/2929781/update-adds-new-tls-cipher-suites-and-changes-cipher-suite-priorities)
which adds 4 GCM ciphers to the Schannel provider and re-orders the cipher priority.

GCM ciphers offer Authenticated Encryption (AEAD) and currently provide the best encryption. Out of these additional ciphers, the 2 listed below also provide Perfect Forward Secrecy (PFS) through the use of the DHE_RSA key exchange: 


`TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`

`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`


You may notice in Microsoft documentation that these ciphers are near the top in the cipher order. This is partly because they remain the only ways to support PFS and AEAD when using RSA authentication on Windows servers prior to Server 2016. 

_In the real world, these 2 ciphers are rarely negotiated due to limited client-side support._ 

If you choose to use the DHE key exchange, you should ensure that the Diffie-Hellman keys for your server are strong enough. If you follow a regular Windows Update schedule [KB3174644](https://support.microsoft.com/en-us/help/3174644/microsoft-security-advisory-updated-support-for-diffie-hellman-key-exc) should already be installed to provide updated support for the Diffie-Hellman Key Exchange. Once this patch is installed, you will be able to define the length of the DH private key, up to a size of 4096 bits. 
Additional information provided [here](https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2016/3174644).

**Note:** The Ephemeral Diffie Hellman (DHE) key exchange using a secure key (at least 2048 bits) is much more computationally expensive on both the client and the server, and is therefore slower than the more modern Elliptic Curve Diffie Hellman (ECDHE) exchange. If you MUST support AEAD on Server 2012 R2 while using an RSA signature certificate then this is the only option. 

## Windows Server 2008 R2 / 2012

In the table shown [above](#server-side-protocol-support), you can see the default enabled SSL/TLS versions for these operating systems. From these defaults, we recommend that TLS 1.1 and TLS 1.2 are enabled if not already. We also advise that SSLv2, SSLv3 and TLS 1.0 are disabled, as these are considered cryptographically weaker than the latest TLS versions.

[Security  Advisory 3042058](https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2015/3042058) introduced 4 new ciphers suites to Server 2008 R2 and Server 2012. This now means that forward secrecy (PFS) with Authenticated Encryption (AEAD) is available on 2008 R2 and 2012 when using a standard RSA authentication by prioritising these 2 ciphers: 

`TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`

`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`

_In the real world, these 2 ciphers are rarely negotiated due to limited client-side support._ 

As mentioned above, you will need to ensure that [KB3174644](https://support.microsoft.com/en-us/help/3174644/microsoft-security-advisory-updated-support-for-diffie-hellman-key-exc) is installed to provide updated support for the Diffie-Hellman Key Exchange.

**Note:** The DHE key exchange using a secure key (at least 2048 bits) is much more computationally expensive on both the client and the server, and is therefore slower than the more modern ECDHE exchange. If you MUST support AEAD on Server 2008 R2 or Server 2012 while using an RSA certificate then this is the only option. 

---

_If you are running a production web server with SSL/TLS being terminated directly on the 2008 R2 or 2012 server, we recommend looking to either upgrade your operating system, or implementing a Webcelerator/Loadbalancer solution to terminate the secure connection. Both these options will make available newer, more secure cipher suites, which provide both authenticated encryption and forward secrecy._

---


### Add RDP support for TLS 1.1 and TLS 1.2 on Server 2008 R2
On Server 2008 R2, the Remote Desktop Protocol will use TLS 1.0, by default (if negotiated). If you are attempting to disable support for older TLS protocols such as TLS 1.0, you will need to ensure that the following update is applied first to [enable RDP to support TLS 1.1 and TLS 1.2](https://support.microsoft.com/en-gb/help/3080079/update-to-add-rds-support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind)



## Windows Server 2008 
In the table shown [above](#server-side-protocol-support), you can see the default enabled SSL/TLS versions for this operating system. Before you disable insecure protocols (SSL2, SSL3 and TLS1.0), you will need to ensure you have no applications such as old versions of SQL server which requires them. 

Due to the age of this operating system, TLS 1.1 and 1.2 are not supported by default.  Support can be added for TLS1.1 and 1.2 by installing the following Windows update: 

[KB4019276](https://support.microsoft.com/en-ca/help/4019276/update-to-add-support-for-tls-1-1-and-tls-1-2-in-windows)

On systems that have a regular update schedule, it is possible that this patch has been supersceded by a more recent update. You can check this by ensuring that the **schannel.dll** file is at least version **6.0.6002.24129** by running the following command from an elevated CMD Prompt: 

`wmic datafile where Name="c:\\Windows\\System32\\schannel.dll" get Description,Version`

Once support for TLS 1.2 has been enabled, you will need to install [KB4074621](https://support.microsoft.com/en-gb/help/4074621/add-rds-support-for-tls-1-1-and-tls-1-2-in-windows-server-2008-sp2) to enable the use of TLS1.1 and 1.2 for RDP connections before disabling any of the older suites.


---

_Windows Server 2008 has very limited support for newer and more secure cipher suites. We strongly advise looking to upgrade your operating system if you are hosting public facing web sites._ 

---

## Loadbalancer, WAF, and Webcelerator solutions
In order for a device, such as a load balancer, to inspect HTTPS Web traffic, it must be able to decrypt any packets between the client's browser and the backend web server. The same applies to a Webcelerator - If the Webcel cannot decrypt the traffic then it will be unable to cache any static content for future requests. This means that either SSL Offloading or Secure Origin Pull should be used and the TLS connection terminated at the device. More information on this is provided [here](/webcel/generalinformation)

If HTTPS traffic to your Web server is terminated at one of these edge devices, then you can get in touch with our Support Team to adjust the supported TLS protocols and cipher suites per your requirements.

The next thing to look at is [how .NET Framework applications interact with Schannel](/operatingsystems/windows/tlsandschannel/dotnetsettings).

```eval_rst
   .. title:: Web Server Recommendations
   .. meta::
      :title: Web Server Recommendations | UKFast Documentation
      :description: Security considerations for IIS Web servers
      :keywords: SSL, TLS, ukfast, Schannel, IIS, security, windows
```
