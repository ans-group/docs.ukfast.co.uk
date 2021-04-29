# FastDesk Support Offering

This page is intended to provide generic and basic details on the FastDesk Security policy.

## Physical Security

The FastDesk solution is only ever housed in our government and ISO-certified, ultra-secure data centres managed by security cleared personnel. By design, all user files and apps used inside are stored inside FastDesk meaning unauthorised access to data through the loss of a user device is no longer an issue. The data centres are based in Manchester, GB. Physically, the perimeter of the Data Centre is secured by 2.8m prison grade fencing. 24hr CCTV is in place in all data centres and this is monitored via a live link in the guardhouse. Alongside this, they are staffed 24/7/365 by SIA-accredited UKFast Staff. To prevent entry into the facility a man trap, accompanied by a ram proof barrier is in place; visitors have to drive into the space between the two gates, provide their access code, name and the company they work for at the gate. Access to the data centre is restricted to data centre employees only. On the website, it is also possible to take a virtual tour to give you a better visual idea. For more specific information on the DCs please visit [Our Data centres](https://www.ukfast.co.uk/inside-our-data-centres.html)

## Accreditations & Certifications

We have a number of accreditations highlighting our commitment towards keeping data safe. These include but are not restricted to; ISO 27001:2013 Info Security Management, ISO 9001:2008 Quality, ISO 22301 and PCI DSS compliance. You can find the full list of certifications on the [UKFast website](https://www.ukfast.co.uk/certifications.html)

UKFast have twice yearly a penetration test which is conducted by a CHECK & Crest accredited penetration testing company in line with it receiving the Cyber Essentials Plus Certification. For evidence of this please click [Here](https://www.ukfast.co.uk/certifications.html) Alternatively, please visit: https://pdf.ukfast.co.uk/pdf/fastdeskcecert.pdf

## Data Security

Inside FastDesk, data is encrypted in transit. We use AES 256 encryption. We also use TLS 1.2 which protects from even more vulnerabilities from being exploited compared to the older ones. The data is not encrypted at rest. This allows to be able to see data. However, we encrypt the data on both the backup server and the host of the VM. The encryption is agent side meaning the backup data is encrypted before transmission and to store the encrypted data on the media. During restore operations, the client(hypervisor) decrypts the data. For more information on backups, please see the backups page.

On a user level, group policies and NTFS in windows can be used to lock down access to particular applications and files/folders. As default, passwords are set to expire every three months. The password policy is a minimum of 8 characters in length and contain at least 3 of the following: uppercase letters, lowercase letters, numbers, symbols and special characters e.g. ! " £. Two-Factor Authentication is also available as an optional extra.

```eval_rst
.. note::

  If you require a deviation from any of polices above or if you need information in more detail, please contact the FastDesk support team on 0800 923 0617.

```

```eval_rst
   .. title:: Security Information | FastDesk Documentation
   .. meta::
      :title: Guide on how to change your FastDesk Paswword | UKFast Documentation
      :description: Guide for users on how to change their FastDesk Password
      :keywords: FastDesk, Citrix, ukfast, VDI, Citrix Receiver, Windows, Workspace Application, File, Change, VM, Web, Portal, Commvault, SQL
```