## Keeping WordPress secure

WordPress is a very common CMS (Content Management System), and many sites use this CMS. As it's a well known CMS, it's also commonly exploited and hacked.

As WordPress is third party software not provided by UKFast, we cannot be responsible in the event of any security breaches due to the WordPress application, nor can we provide the in-depth forensics which may required should a breach occur. All advice given here is on best endeavors and we recommend you do your own research. If you have any doubt, consult a security expert!

With that said, there are things we can advise to help keep your sites safe! The best way to address security problems is to make sure you've taken all the steps you can to prevent attacks in the first place. The [Hardening WordPress](https://codex.wordpress.org/Hardening_WordPress) guide in the WP Codex is the definitive guide to keeping your WordPress sites secure. It's maintained by the creators of WordPress, and covers all the elements you'll need to know.

*Please do read it in full, but if you want the most basic breakdown, here are the top 5 points to keep you safe from the most common exploits:*

- Use strong passwords, and if possible consider 2 step authentication.
- Keep your WordPress install, Themes and Plugins up to date, and remove any plugins you don't use.
- Do not use 777 file permissions.
- Find and use a good [security plugin](https://wordpress.org/plugins/tags/security/).
- Keep up-to-date backups of your site files and database.

If you require additional security beyond the recommendations of WordPress, we offer a [Web Application Firewall](security/webapplicationfirewall/).

### My WordPress site was hacked, what now?

In general the fastest way we'd suggest to get you back online is to restore from backups prior to the incident, whether that's using UKFast backups or your own. You may also wish to first take a copy of the compromised site, should you need to have an investigation done at a later date.

Be aware that restoring from a backup might remove the malicious code, but it won't close the vulnerability which allowed your site to be compromised in the first place. To do that please do refer back to the [Hardening WordPress Codex](https://codex.wordpress.org/Hardening_WordPress).

We would also recommend running an on-demand virus scan just in case there's further issues beyond the compromised site. For Linux products we recommend [McAfee](/security/antivirus/), or alternatively the open source [ClamAV](www.clamav.net).

And in all cases, we would always recommend getting a security expert to review and confirm your site is safe again.

```eval_rst
   .. meta::
      :title: WordPress Security | UKFast Documentation
      :description: How to prevent the most common WordPress problems.
      :keywords:  ukfast, hosting, wp, wordpress, clamscan
