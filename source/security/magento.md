# Keeping Magento secure

Magento is a popular e-commerce platform, used by a large number of online shops. As a popular platform, it is often targeted by malicious actors, so it's important to keep your Magento installations secure.

```eval_rst
.. warning::
   Magento is third party software not provided by UKFast, therefore we cannot be responsible in the event of any security breaches due to the Magento application itself, nor can we provide the in-depth forensics which may required should a breach occur.

   The advice given here is provided on reasonable endeavours basis, and we recommend you do your own additional research.
```

If you plan on using Magento as your e-commerce platform, the following resources should provide all the information you need to stay secure:

The official [Magento Security Center](https://magento.com/security) is provided by Magento, and includes all security updates directly from them. They also have many guides and further information, such as [Magento Security Best Practices](http://docs.magento.com/m1/ce/user_guide/magento/magento-security-best-practices.html) and [Protect your Magento Installation from Password Guessing](https://magento.com/security/best-practices/protect-your-magento-installation-password-guessing-new-update).

3rd party tools such as [MageReport Scanner](https://www.magereport.com/) let you run scans on your sites, which should help you find and fix potential vulnerabilities, before they become problems.

Some of the key points to consider in order to keep your Magento site secure are:

- Keep Magento and any extensions up to date, and make sure to install any security updates available
- Change the default "admin" username, and use a strong password. Consider adding a 2-factor authentication extension for added security
- [Change your default Admin URL](http://docs.magento.com/m1/ce/user_guide/configuration/url-admin-custom.html).
- Consider securing your file permissions. Magento provide guides for [Magento 1.x](http://devdocs.magento.com/guides/m1x/install/installer-privileges_after.html) and [Magento 2.0](http://devdocs.magento.com/guides/v2.0/config-guide/prod/prod_file-sys-perms.html). Do bear in mind that the file permissions you should use depend on which version of Magento you're running, and whether you're running on a dedicated Magento host or a shared environment like WHM/cPanel or Plesk. Please do refer to the appropriate official documentation for your setup before making changes.
- Have a disaster recovery plan, and make sure to take regular backups which you can restore your site from, should you be attacked.  Speak to your [UKFast account manager](https://my.ukfast.co.uk/account/your-account-manager.php) or [raise a support ticket via MyUKFast](https://my.ukfast.co.uk/pss/add.php) if you need help with establishing an appropriate backup regime.

### My Magento site was hacked, what now?

In general the first thing you'll want to do is take the site offline so no further damage can be inflicted. You may wish to first take a copy of the compromised site, should you need to have an investigation done at a later date.

Then the fastest way to get back online is to restore from backups prior to the incident, whether that's using UKFast-provided backups or your own. Be aware that restoring from a backup might remove the malicious code, but it won't close the vulnerability which allowed your site to be compromised in the first place.

We would also recommend running an on-demand virus scan just in case there are further issues beyond the compromised site. For Linux-based products we recommend [McAfee](/security/antivirus/index), or alternatively the open source [ClamAV](https://www.clamav.net).

And in all cases, we would recommend getting a security expert to review and confirm your site is safe again.

```eval_rst
   .. title:: Magento Security
   .. meta::
      :title: Magento Security | UKFast Documentation
      :description: How to prevent the most common Magento security problems
      :keywords:  ukfast, hosting, magento, mage, clamscan, security, hacking, ecommerce
```
