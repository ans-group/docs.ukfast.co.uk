# Information and guidance about .htaccess

The `.htaccess` file is used by Apache to allow configuration changes to be made per vhost without having to access the main Apache configuration files. You can have a `.htaccess` file in any folder of your web files but the minimum is usually to have one in your document root. Here are some `.htaccess` configuration examples.

## Lock down access to site/page

You can lock down pages completely, by source IP or with a password.

## Lock down completely

There may be some files that you want to lock down so nobody can access these via your web server. Here is an example to lock down access to a file called `xmlrpc.php`. This is used by some CMS' but can be used to brute force a site.

```apacheconf
  <Files xmlrpc.php>
    Order allow,deny
    Deny from all
  </Files>
```

## Lock down to specific IP(s)

You may want some files to be locked down to specific IPs. Here we lock down the `wp-admin.php` file to the IPs `123.123.123.121`, `123.123.123.122` and `123.123.123.123`.

```apacheconf
  <IfModule mod_rewrite.c>
    RewriteEngine on
    RewriteCond %{REQUEST_URI} ^(.*)?wp-login\.php(.*)$ [OR]
    RewriteCond %{REQUEST_URI} ^(.*)?wp-admin$
    RewriteCond %{REMOTE_ADDR} !^123\.123\.123\.121$
    RewriteCond %{REMOTE_ADDR} !^123\.123\.123\.122$
    RewriteCond %{REMOTE_ADDR} !^123\.123\.123\.123$
    RewriteRule ^(.*)$ - [R=403,L]
  </IfModule>
```

You can include as many IPs as you need in this example.

## Lock down using .htpasswd

You can use the `.htpasswd` file to hold usernames and passwords which can be referenced by the `.htaccess` file. First of all you need to create the `.htpasswd` file. Although a webserver should be configured not to deliver any file beginning with a dot, it is still good practice to create the `.htpasswd` file outside the document root. For example, for a site with document root `/var/www/vhosts/firstdomain.com/htdocs`, we will create the `.htpasswd` in the path `/var/www/vhosts/firstdomain.com/.htpasswd`.

This command will add a user to that file:

```bash
htpasswd -c /var/www/vhosts/firstdomain.com/.htpasswd admin
```

You will get prompted for the password. The command can be used for all subsequent users, replacing the user `admin` with the new user name.

To use this you then need to add the following to your `.htaccess` file.

```apacheconf
  ErrorDocument 401 "Denied"
  ErrorDocument 403 "Denied"
  <files wp-login.php>
    AuthType Basic
    AuthName "Password Protected Area"
    AuthUserFile /var/www/vhosts/firstdomain.com/.htpasswd
    Require valid-user
  </files>
```

```eval_rst
  .. title:: Information and guidance about htaccess
  .. meta::
     :title: Information and guidance about htaccess | ANS Documentation
     :description:  Information and guidance on locking down htaccess on Linux
     :keywords: ukfast, linux, htaccess, apache, server, virtual, vm, lockdown, IP, site, xmlrpc, access, apache
```
