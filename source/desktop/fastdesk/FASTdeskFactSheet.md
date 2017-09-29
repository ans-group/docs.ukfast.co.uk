# General information / FAQs

## What are the differences between the various FASTdesk plans - Standard, Pro, ProPlus, and GPU?

**FASTdesk Standard** - runs on shared Citrix XenApp servers.  Multiple desktop users are assigned to a XenApp Virtual Machine (VM), with resources shared between these users.

**FASTdesk Pro** - runs on dedicated Citrix XenDesktop servers. Each desktop user has their own dedicated VM, with 2 vCPU and 4GB RAM.

**FASTdesk ProPlus** - runs on dedicated Citrix XenDesktop servers. Each desktop user has their own dedicated VM, with 4 vCPU and 8GB RAM.

**FASTdesk GPU** - runs on dedicated Citrix XenDesktop servers, with the addition of NVIDIA Grid Virtual Workstation and Tesla M10 GPUs. Each desktop user has their own dedicated VM, with 4vCPU, 8GB RAM, and 2GB GDDR5 memory ("graphics memory").

## What are Line of Business Applications?

The default FASTdesk applications are Microsoft Office 2016, ShareFile Drive Mapper, Adobe Acrobat and Google Chrome.  These come as standard with all FASTdesk desktops, and are supported by UKFast.  Line of Business Applications are any additional applications which are installed and maintained by FASTdesk customers.

## What is a FASTdesk Database Server?

FASTdesk Database Servers are recommended when your Line Of Business Applications require a backend database engine running on a separate server.  All your FASTdesk desktop users will be able to access these applications as necessary. For example: you could have 20 x FASTdesk Standard Users, spread across 4 x XenApp Servers, each with a Line Of Business Application installed that connects to a centralised database instance running on a single FASTdesk Database Server.

## Are my files backed up on FASTdesk?

Your home folder is backed up at file level and is available for 28 days. Virtual Machines are snapshotted at the storage level and are also available for 28 days.

## How is security and encryption integrated into FASTdesk?

All FASTdesk data is encrypted via a 2048 bit RSA SSL. All connections into the environment are secured via Netscaler Gateways. FASTdesk is FIPS-compliant and is encrypted end-to-end, meaning all communication within the environment is over SSL.

## Can I supply my own Microsoft licenses on FASTdesk?

Yes, you can provide your own licenses for Microsoft applications, providing that this has been pre-arranged with your licensing vendor/partner before your solution is launched.  Your Microsoft Volume Licensing agreement must include [Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-default.aspx), which allows you to use Microsoft licenses in a shared/multi-tenant or public cloud infrastructure environment.

We are currently unable to allow Office 365 licenses to run on FASTdesk. Additionally, License Mobility is not applicable to Windows Server, and therefore the Windows Server operating system needs to be licensed by UKFast under our SPLA agreement.

## Is Active Directory Federation Services (ADFS) supported?

As FASTdesk is a multi-tenanted platform, we don't support the integration of external Active Directory Domains for security purposes.

## What is included in 1st line Helpdesk Support?

1st line helpdesk support is available during office hours (Monday to Friday between 09.00 and 18.00 UK time, excluding UK Bank Holidays). This support covers the FASTdesk desktop, along with support for the default FASTdesk Applications, and other general desktop end user issues that you may encounter. Support for your Line Of Business Applications is not included. The Helpdesk telephone number is (+44) 0800 923 0617.


```eval_rst
.. meta::
     :title: General information about FASTdesk | UKFast Documentation
     :description: Guidance to help understand and use FASTdesk - desktop as a service from UKFast
     :keywords: fastdesk, desktop, applications, daas, desktop as a service
```
