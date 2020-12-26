# TLS1.0 and TLS1.1 disabled on DDoSX<sup>®</sup>

The PCI Security Standards Council have set a deadline of 30th June 2018 for applications and websites to disable early SSL / TLS protocols in order to meet PCI Data Security Standards (PCI DSS), which are required for processing debit and credit card payments online.  This [blog post from the PCI Security Standards Council](https://blog.pcisecuritystandards.org/are-you-ready-for-30-june-2018-sayin-goodbye-to-ssl-early-tls) provides further information.

In accordance with this requirement, we **disabled both the TLS1.0 and TLS1.1 protocols on the UKFast DDoSX network on 14th May 2018**.  Whilst TLS1.1 is not yet strictly forbidden by the PCI Security Standards Council, they strongly recommended that TLS1.2 is used.  Therefore in order to help our customers both comply with the regulations and adhere to modern internet security standards, we disabled TLS1.1 at the same time as TLS1.0.

## Why have the PCI Security Council taken this step?

Please read the [PCI Security Standards Council blog post](https://blog.pcisecuritystandards.org/are-you-ready-for-30-june-2018-sayin-goodbye-to-ssl-early-tls) for a detailed explanation, but in summary there are serious security issues with early versions of the TLS protocol that have not been addressed retrospectively by the industry at large.  In recent years several large scale security breaches such as POODLE and BEAST originated due to weaknesses in early TLS and SSL being exploited.

Given that all modern web browsers (including those used on mobile devices) now support TLS1.2 as standard, the PCI Security Standards Council have decided to set this deadline for disabling early TLS protocols in the interest of all users of online eCommerce websites and applications.


## How is TLS1.0 and TLS1.1 traffic generated?

TLS1.0 and TLS1.1 traffic is generated primarily by users of older web browsers, particularly mobile devices running older versions of the Android and iOS operating systems.  This Wikipedia article is a [good source of information detailing web browser support for TLS versions](https://en.wikipedia.org/wiki/Transport_Layer_Security).


## The implications of TLS1.0 and TLS1.1 now being disabled on DDoSX<sup>®</sup>

If you are using the DDoSX network, whether it's for DDoS protection alone, or the additional Content Delivery Network (CDN) and Web Application Firewall (WAF), then your end users will be unable to connect to your websites and applications via TLS1.0 and TLS1.1.  This will impact people with older web browsers on their computers or mobile devices.

You may wish inform your end users with incompatible browsers or devices that they will no longer be able to access your websites or applications until they upgrade to a newer web browser.  It's highly likely these people will experience problems accessing many different websites over the next few months, as websites begin to comply with the mandate to disable early TLS protocols, and so whilst inconvenient it will not come as a surprise to your users.

If you need further help with this matter please either contact [your UKFast Account Manager](https://my.ukfast.co.uk/account/your-account-manager.php) or [raise a support ticket via MyUKFast](https://my.ukfast.co.uk/pss/add.php).


```eval_rst
.. meta::
     :title: Disabling early TLS protocols on DDoSX | UKFast Documentation
     :description: Guidance on UKFast's approach to disabling TLS1.0 and TLS1.1 on DDoSX for PCI DSS compliance
     :keywords: pci dss, pci, security, tls, early tls, ssl, browsers
```
