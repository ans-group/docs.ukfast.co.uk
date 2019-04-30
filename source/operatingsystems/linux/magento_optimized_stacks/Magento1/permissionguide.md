# Magento 1 permission Guide

This guide is intended to show best practices for Magento 1 permissions. Ensuring that required directories are accessible whilst restricting access to others.

```eval_rst
.. seealso::
   Note:
     The following is for UKFast Magento 1 optimized stacks, which uses NGINX - this guide is for NGINX only.
     If your configuration is bespoke or does not use our native stack we would recommend proceeding with caution.

     In the case that you have any queries please consult UKFast support.
```

First, we need to establish the root directory for your Magento 1 instance.  Typically this can be viewed in the NGINX configuration file located under:
/etc/nginx/conf.d/

```bash
grep root /etc/nginx/conf.d/mage.ukast.co.uk.conf
  root /var/www/vhosts/mage.ukast.co.uk/htdocs;
```

Next, we need to verify which user and group should be used. This is important as if the domain is a Magento multi-store, typically the owner and group would be the same for each virtual host as the document root is shared.

In this case PHP-FPM is utilized - this is configured as an upstream within Nginx -

```bash
grep ".sock;" /etc/nginx/conf.d/mage.ukast.co.uk.conf
server unix:/var/run/php-fpm-mageukastcouk;

grep php-fpm-mageukastcouk /etc/php-fpm.d/*.conf
/etc/php-fpm.d/mageukastcouk.conf:listen = '/var/run/php-fpm-php-fpm-mageukastcouk'

egrep "^user|^group" /etc/php-fpm.d/mageukastcouk.conf
user = mage.ukast.co.uk
group = mage.ukast.co.uk
```

Using all the information provided above, we can then input this into the commands for changing the document roots permissions.

```eval_rst
.. warning::
   **Please ensure the getfacl command is run first, this means that we can revert your permissions back if required.**
```

```bash
getfacl -R /var/www/vhosts/mage.ukast.co.uk/htdocs > /var/www/vhosts/mage.ukast.co.uk/mage.ukast.co.uk-$(date +"%Y%m%d").acl
```

If this needs to be restored, the acl file can be used to restore the original permissions:

```bash
setfacl --restore=/var/www/vhosts/mage.ukast.co.uk/mage.ukast.co.uk-$(date +"%Y%m%d").acl
```

We can now proceed with updating the permissions. Please remember to change the root directory and user in accordance with the output of the previous commands.
```bash
chown -R mage.ukast.co.uk:mage.ukast.co.uk /var/www/vhosts/mage.ukast.co.uk/htdocs/
find /var/www/vhosts/mage.ukast.co.uk/htdocs/ -type f -exec chmod 440 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/ -type d -exec chmod 550 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/var/ -type f -exec chmod 660 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/media/ -type f -exec chmod 660 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/var/ -type d -exec chmod 770 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/media/ -type d -exec chmod 770 {} \;
chmod 770 /var/www/vhosts/mage.ukast.co.uk/htdocs/includes
chmod 660 /var/www/vhosts/mage.ukast.co.uk/htdocs/includes/config.php
```

If not already added, you can add Nginx to the group used by PHP-FPM - here is the command to do so - this only needs to be performed once
```bash
usermod -a -G mage.ukast.co.uk nginx
```

To verify that this has been added to the group
```bash
id nginx
uid=10(nginx) gid=10(nginx) groups=11(mage.ukast.co.uk)
```

If the Magento site has CSS merging on you need the following additional permissions:
```bash
find var/www/vhosts/mage.ukast.co.uk/media/css -type d -exec chmod 750 {} \;
```

Note that the above permissions do not allow the php-fpm user to write core Magento code.
However, when deploying new content the user needs to be able to write to the document root, therefore when deploying run the following.
```bash
chmod –R 770 /var/www/vhosts/mage.ukast.co.uk/htdocs/
```
Then deploy your content, once deployed revert the permissions back
```bash
chown -R mage.ukast.co.uk:mage.ukast.co.uk /var/www/vhosts/mage.ukast.co.uk/htdocs/
find /var/www/vhosts/mage.ukast.co.uk/htdocs/ -type f -exec chmod 440 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/ -type d -exec chmod 550 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/var/ -type f -exec chmod 660 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/media/ -type f -exec chmod 660 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/var/ -type d -exec chmod 770 {} \;
find /var/www/vhosts/mage.ukast.co.uk/htdocs/media/ -type d -exec chmod 770 {} \;
chmod 770 /var/www/vhosts/mage.ukast.co.uk/htdocs/includes
chmod 660 /var/www/vhosts/mage.ukast.co.uk/htdocs/includes/config.php
```

Now the permissions for the site should be correct. However, if you are unsure about any of the above then please do not hesitate to get in touch with UKFast support and we can assist you further.
