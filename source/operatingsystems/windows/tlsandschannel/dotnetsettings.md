# TLS Considerations for .NET Client connections

Windows Schannel will also handle the client-side TLS negotiation and cipher suite selection for any applications using the .NET Framework. The version of .NET that your application is targeted for will dictate which protocols are supported.


.NET applications will usually be the "client" in the TLS handshake. A good example of this would be a 3rd party payment gateway.

1. When a user visits a website, their device will be the "TLS client", and the webserver will be the "TLS server". A TLS connection will be established between these endpoints.

2. If the webserver then connects to a payment gateway when the user makes a payment, the webserver must initiate another TLS connection from the webserver to the payment gateway API. For this part of the process, the webserver will act as the "TLS client", and the payment gateway will be the "TLS Server".

---

### .NET Framework Versions
There are a few caveats to keep in mind when dealing with .NET Framework versions:

* Any changes made to Schannel protocols and ciphers, through registry or group policy, will also apply to applications using the .NET Framework. For example, if client-side TLS 1.0 is disabled in the registry then no .NET applications will be able to negotiate TLS 1.0 connections.

* Application developers can explicitly specify through code which security protocols to use, providing that the security provider (Schannel) supports it. This is not considered good practice for production applications, but can be used in testing. Microsoft recommend that applications should always let the .NET Framework decide which protocols to use.

* Applications compiled for .NET Framework 4.6 and higher will use the following security protocols by default:

    - TLS 1.2
    - TLS 1.1
    - TLS 1.0


* Applications compiled for .NET Framework 4.0 to .NET Framework 4.5.2 will use the following security protocols by default. Administrators can override this with the `SchUseStrongCrypto` registry value specified [here](https://docs.microsoft.com/en-us/security-updates/SecurityAdvisories/2015/2960358).:

    - TLS 1.0
    - SSL 3

* Applications compiled for .NET Framework 2 to 3.5 will use the following security protocols by default. Administrators can install an update and set a registry value to override this (detailed below):

    - TLS 1.0
    - SSL 3

* Windows Updates are available to enable support for TLS 1.1 and TLS 1.2 for legacy applications compiled for .NET 2.0 - 3.5. Once installed, you will need to add the registry value for `SystemDefaultTLSVersions` as mentioned in the articles below:

    - Windows Server 2008 - [KB3154517](https://support.microsoft.com/en-gb/help/3154517/support-for-tls-system-default-versions-included-in-the-net-framework) (Ensure that TLS 1.1 and TLS 1.2 are enabled first)
    - Windows Server 2008 R2 - [KB3154518](https://support.microsoft.com/en-gb/help/3154518/support-for-tls-system-default-versions-included-in-the-net-framework) (Ensure that TLS 1.1 and TLS 1.2 are enabled first)
    - Windows Server 2012 - [KB3154519](https://support.microsoft.com/en-gb/help/3154519/support-for-tls-system-default-versions-included-in-the-net-framework)
    - Windows Server 2012 R2 - [KB3154520](https://support.microsoft.com/en-gb/help/3154520/support-for-tls-system-default-versions-included-in-the-net-framework)
    - Windows Server 2016 - No update required. Registry value for `SystemDefaultTLSVersions` will still need added manually.


Microsoft provide an excellent article on their TLS best practices, which can be found at the external link [here](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls).

```eval_rst
   .. title:: .NET Framework TLS Settings
   .. meta::
      :title: .NET Framework TLS Settings | ANS Documentation
      :description: Considerations for .Net Framework applications
      :keywords: SSL, TLS, Schannel, IIS, security, windows, dotnet, framework
```
