# Enabling and Disabling SSL/TLS Protocols in Windows

This section will detail how to add and remove TLS protocols and cipher suites, and provide links to further documentation.

Before making any changes, please check the Microsoft documentation on supported protocols for your operating system.

The protocols that can be supported will entirely depend on your operating system version.
Please also check:

* [Security Recommendations for Internet facing Web Servers](/operatingsystems/windows/tlsandschannel/webserverrecommendations)
* [Windows Server Software TLS Support](/operatingsystems/windows/tlsandschannel/softwareconsiderations)
* [.NET Framework TLS considerations](/operatingsystems/windows/tlsandschannel/dotnetsettings)

Microsoft list all the supported cipher suites for each operating system version. The external link is provided below:

[Cipher Suites in Schannel by OS](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374757(v=vs.85).aspx)

```eval_rst
.. warning::
  Editing protocol and cipher compatibility requires making changes to the registry. Always make a backup by exporting the registry keys before making any changes. **Incorrect changes to the registry can cause operating system instability.**
```

### Automated with IIS Crypto

[IIS Crypto](https://www.nartac.com/Products/IISCrypto) (external link) is a popular 3rd-party tool by Nartac Software, which simplifies the process of managing SSL/TLS protocols and ciphers, without having to manually edit the registry.

The use of IIS Crypto will not be discussed further here, but if you want to learn more, then you can following the link above to find out how it works.

### Manual

Manually enabling and disabling TLS protocols will require modifying the following registry key:

```none
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols
```

You may see sub-keys under this entry, one for each protocol version. Please note that the absence of any protocol key does not mean that it is disabled. Enabled protocols are implicitly defined by operating system version, unless explicitly defined in the registry.

Please refer to the official [Microsoft Documentation](https://docs.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) for further information on the TLS registry settings.

## Cipher Suite Ordering

In most cases you will not have to edit the order of cipher suites on a Windows server. Microsoft generally does a good job of ensuring the most secure ciphers are prioritised over the weaker ones. Occasionally, Windows updates can add additional support for ciphers, or reorder them, so we recommend frequent update schedules.


Cipher suite order can be defined by group policy on supported operating systems.

```none
Computer Configuration\Administrative Templates\Network\SSL Configuration Settings\SSL Cipher Suite Order
```

Setting the above policy setting in Windows Server 2012 R2 will modify the following registry key setting:

```none
HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Cryptography\Configuration\SSL\0010002
```

```eval_rst
   .. title:: Windows TLS Configuration
   .. meta::
      :title: Windows TLS Configuration | ANS Documentation
      :description: TLS and Schannel configuration
      :keywords: SSL, TLS, ukfast, Schannel, IIS, security, windows, IIS Crypto
```
