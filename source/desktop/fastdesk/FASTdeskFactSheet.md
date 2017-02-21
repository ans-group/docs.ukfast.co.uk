# FASTdesk Fact Sheet

## What are the differences between FASTdesk standard, pro and pro plus plans?

With the FASTdesk Standard plan, users are hosted on a shared XenApp server. Many users are assigned to one XenApp Virtual Machine and the resources are shared between these users.

With the FASTdesk Pro Plan, one user is assigned to their own dedicated XenDesktop Virtual Machine. The specification of this is 2 vCPU and 4GB RAM.

The FASTdesk Pro Plus plan is the same as the FASTdesk Pro Plan but with upgraded Virtual Machine specifications. The specification for this plan is  4 vCPU and 8GB RAM.

## What are __Line of Business Apps__?

Line of Business Applications are applications which are installed and maintained by FASTdesk Users and are not the default supported FASTdesk applications. The default FASTdesk applications are Microsoft Office 2016, ShareFile Drive Mapper, Adobe Acrobat and Google Chrome.

## What is included in 1st line Helpdesk Support and what hours do we support?

1st line Helpdesk Support is available to you from Monday to Friday between the hours of 9am and 6pm (Excluding UK Bank Holidays). Our support team will be available whilst working from within the FASTdesk environment. This means that our support covers the FASTdesk Microsoft Windows Virtual Desktop that you are working on, along with support for the default FASTdesk Applications, and other general end user issues that you may encounter. Support for your Line Of Business Applications is not provided. The Helpdesk telephone number is (+44) 0800 923 0617.

## Are my files backed up on FASTdesk?

Your home folder is backed up at file level and is available for 28 days. Virtual Machines are snapshotted at the storage level and are available for 28 days.

## How is security and encryption integrated into FASTdesk?

All FASTdesk data is encrypted via a 2048 bit RSA SSL. All connections into the environment are secured via Netscaler Gateways. FASTdesk is FIPS compliant and is encrypted end-to-end, meaning all communication within the environment is done over SSL.

## Can I supply my own Microsoft licenses on FASTdesk?

Yes, you can provide your own Microsoft licenses for applications such as Microsoft Office and SQL, providing that this has been pre-arranged before your solution is launched. Microsoft Windows operating system licenses cannot be provided. 

## What is a FASTdesk Application Server?

FASTdesk Application Servers are required when your Line Of Business Applications require a backend database engine running on a separate server. For example; you could have 20 x FASTdesk Standard Users, spread across a total of 4 x XenApp Servers, each with a Line Of Business Application installed that connects to a centralised database instance running on 1 x FASTdesk Application Server.

## Is Active Directory Federation Services (ADFS) supported?

Unfortunately, as FASTdesk is a multi-tenanted platform, we don't support the integration of any external Active Directory Domains, for security purposes.
