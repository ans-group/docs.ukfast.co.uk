# How to use Let's Encrypt on Windows

`Windows` operating systems have a number of `ACME` clients available. Here are a couple that clients have found to be simple to use and feature rich.

## Certify the Web

[`Certify the Web`](https://certifytheweb.com/) is one of the most popular `Let's Encrypt` services available on `Windows` currently. This offers features such as;

* Automatic renewal
* `IIS` Integration
* Option to integrate alternative ACME certificate authorities

One downside to this product is that it does only offer a few certificates for free before requiring you to purchase an upgrade key.

For a complete guide on how to install this client and start issuing `Let's Encrypt` certificates, please see the following guide;

[Certify the Web - Docs](https://docs.certifytheweb.com/docs/intro)

```eval_rst
.. note:
  If you require assistance with installing this product, please raise a UKFast Support query via your https://portal.ans.co.uk client portal.

```
## Win-ACME

[`Win-ACME`](https://www.win-acme.com/) is a popular command line alternative for issuing and maintaining `Let's Encrypt` certificates. This offers the following features;

* `IIS` Integration
* A simple command line interface
* Support for alternative web servers, such as `Apache`
* Automatic renewal via an integrated scheduled task

For a complete guide on how to install and use this client, please see the following official documentation

[Win-ACME - Docs](https://www.win-acme.com/manual/getting-started)

## Posh-ACME

For `PowerShell` users, we recommend using [`Posh-ACME`](https://github.com/rmbolger/Posh-ACME) for your `Let's Encrypt` needs. This offers a feature set similar to `certbot`, and can be incorporated into environments that use APIs for DNS Challenges and automated certificate renewal.

### Installation

```eval_rst
.. note:
  If you require assistance with installing this product, please raise a UKFast Support query via your https://portal.ans.co.uk client portal.

```

To install this client, first open your `PowerShell` terminal and run the following, replacing `youruser` for the system user in question.

```powershell
Install-Module -Name Posh-ACME -Scope youruser
```

If you have elevated privileges and wish for this to be available for all system users, use the following syntax

```powershell
Install-Module -Name Posh-ACME -Scope AllUsers
```

Once installed, you will need to **import** the module

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Import-Module Posh-ACME
```

### Issuing a certificate

To issue a certificate for your chosen domain, run the following command, adjusting as per your specific requirements.

```powershell
New-PACertificate yourdomain.com -AcceptTOS  -Contact admin@yourdomain.com
```

This will default to using the **Manual** plugin, and prompt you to create a **TXT** record for the `DNS-01` challenge. Please be aware of your chosen DNS provider's DNS propagation time.

### Using a DNS Plugin

Please see the list of [**Available Posh-ACME DNS Plugins**](https://github.com/rmbolger/Posh-ACME/wiki/List-of-Supported-DNS-Providers) for a full list of available DNS Plugins for use with this software.

As an example, to use this with Route53, please see the following usage guide, which falls outside the scope of this article.

[Route53 Posh-ACME Guide](https://github.com/rmbolger/Posh-ACME/blob/main/Posh-ACME/Plugins/Route53-Readme.md)

```eval_rst
.. note:
  UKFast do not currently offer a DNS Plugin for use with Posh-ACME, but are open to contributions that integrate with the SafeDNS API. More information on this is available in the [UKFast Developer Centre](https://developers.ukfast.io/documentation/safedns)

```

```eval_rst
  .. title:: SSL | How to use Let's Encrypt on Windows
  .. meta::
     :title: SSL | How to use Let's Encrypt on Windows | ANS Documentation
     :description: How to use Let's Encrypt on Windows
     :keywords: ukfast, ssl, letsencrypt, let's encrypt, secure, security, windows, powershell, iis, server, guide, tutorial
```
