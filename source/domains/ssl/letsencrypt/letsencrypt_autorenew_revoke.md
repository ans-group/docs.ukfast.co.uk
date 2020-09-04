#  Auto-Renewing SSL Certificates with Certbot
Due to the short lifespan of `Let's Encrypt certificates, it introduces the risk of your certificates expiring at an inopportune time. Therefore you should look towards scheduling in **automatic renewal**.

There are two methods to achieve this: With a scheduled task (a cron job) or using an additional utility that comes with certbot.
## Cron Method
The `certbot` utility offers a *renew* option that will check your installed certificates and renew any that are within a 30 day expiration period.

You can test this feature using the 'dry-run' option
```
certbot renew --dry-run
```

As root, you can then add a cron task with either of the following commands

```
crontab -e
or
crontab -u root -e
```

In it you can then set your domains to be checked for renewal. In this example it checks twice a month and writes to a log

```
[root@server ~]# crontab -l
0 0  */15 * 6 /usr/bin/certbot renew >> /var/log/certbot.loC
```
This outputs information like...
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/docs.yourdomain.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Processing /etc/letsencrypt/renewal/p.yourdomain.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Processing /etc/letsencrypt/renewal/shop.yourdomain.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

The following certs are not due for renewal yet:
  /etc/letsencrypt/live/docs.yourdomain.com/fullchain.pem expires on 2020-10-05 (skipped)
  /etc/letsencrypt/live/p.yourdomain.com/fullchain.pem expires on 2020-10-05 (skipped)
  /etc/letsencrypt/live/shop.yourdomain.com/fullchain.pem expires on 2020-10-05 (skipped)
No renewals were attempted.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
``` 

## Certbot Timer Method

The `certbot` package comes with a **timer** service that you can leave to run and automatically update your certificates. This is a systemd service, and can be enabled with the following;

```
[root@ ~]# systemctl enable --now certbot-renew.timer
Created symlink from /etc/systemd/system/timers.target.wants/certbot-renew.timer to /usr/lib/systemd/system/certbot-renew.timer.

[root ~]# systemctl status certbot-renew.timer
● certbot-renew.timer - This is the timer to set the schedule for automated renewals
   Loaded: loaded (/usr/lib/systemd/system/certbot-renew.timer; enabled; vendor preset: disabled)
   Active: active (waiting) since Thu 2020-07-09 08:56:24 BST; 12s ago

```

# Revoking SSL Certificates with Certbot
To revoke a LetsEncrypt certificate, use the following command

```
certbot revoke (supply --cert-name or --cert-path)
```

You can obtain the cert-name/path with the 'certbot certificates' command, but this will usually be the domain name itself.

```eval_rst
  .. title:: SSL | Auto-Renewing & Revoking SSL certificates with Certbot
  .. meta::
     :title: SSL | Auto-Renewing & Revoking SSL certificates with Certbot | UKFast Documentation
     :description: Auto-Renewing & Revoking SSL certificates with Certbot
     :keywords: ssl, certbot, renew, autorenew, revoke, letsencrypt, let's encrypt, secure, security, linux, server, guide, tutorial
```
