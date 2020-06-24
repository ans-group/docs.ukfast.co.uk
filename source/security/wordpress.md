# Keeping WordPress secure

WordPress is a very common Content Management System (CMS), used by many websites and blogs.  As one of the most popular applications on the internet, it's also commonly targeted and exploited by bad actors.

```eval_rst
   .. warning::
      WordPress is third party software not provided by UKFast, therefore we cannot be responsible in the event of any security breaches due to the WordPress application itself, nor can we provide the in-depth forensics which may required should a breach occur.  

      The advice given here is provided on reasonable endeavours basis, and we recommend you do your own additional research.
```

The best way to address security problems is to make sure you've taken all the steps you can to prevent attacks in the first place. The [Hardening WordPress](https://codex.wordpress.org/Hardening_WordPress) guide in the WP Codex is the definitive guide to keeping your WordPress sites secure. It's maintained by the creators of WordPress, and covers all the elements you'll need to know.  We recommend you ready it in full, but below are the top five points as a summary:

- Use strong passwords, and if possible consider 2 step authentication.
- Keep your WordPress install, themes and plugins up to date, and remove any plugins you don't use.
- Do not use 777 file permissions.
- Find and use a good [security plugin](https://wordpress.org/plugins/tags/security/).
- Keep up-to-date backups of your site's files and database.

If you require additional security beyond the recommendations of WordPress, you could consider a [Web Application Firewall](/security/webapplicationfirewall/index) from UKFast.

### My WordPress site was hacked, what now?

In general the fastest way to get back online is to restore from backups prior to the incident, whether that's using UKFast provided backups or your own. You may also wish to first take a copy of the compromised site, should you need to have an investigation done at a later date.

Be aware that restoring from a backup might remove the malicious code, but it won't close the vulnerability which allowed your site to be compromised in the first place. To do that please do refer back to [Hardening WordPress Codex](https://codex.wordpress.org/Hardening_WordPress).

WordPress maintain [their own in-depth security guide](https://codex.wordpress.org/FAQ_My_site_was_hacked) with suggestions and recommended plugins which is worth a read should you find your site compromised.

We would also recommend running an on-demand virus scan just in case there's further issues beyond the compromised site. For Linux-based products we recommend [McAfee](/security/antivirus/index), or alternatively the open source [ClamAV](https://www.clamav.net).

And in all cases, we would always recommend getting a security expert to review and confirm your site is safe again.


```eval_rst
   .. title:: WordPress Security
   .. meta::
      :title: WordPress Security | UKFast Documentation
      :description: How to prevent the most common WordPress security problems
      :keywords:  ukfast, hosting, wp, wordpress, clamscan, security
```
