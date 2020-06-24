# SSL Certificates

To allow users to connect to your site over HTTPS you need to install mod_ssl.

```bash
  yum install mod_ssl
```

This will add the file `/etc/httpd/conf.d/ssl.conf` . If you're configuring separate vhosts per site (as suggested above), it's best to delete or comment out the contents of this file underneath this section.

```apacheconf
  ##
  ## SSL Virtual Host Context
  ##

  <VirtualHost _default_:443>

  # General setup for the virtual host, inherited from global configuration
  #DocumentRoot "/var/www/html"
  #ServerName www.example.com:443
```

You then need to add the following section to your vhost configuration:

```apacheconf
    SSLEngine on
    SSLProtocol all -SSLv2 -SSLv3 -TLSv1
    SSLCipherSuite ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:ECDHE-ECDSA-DES-CBC3-SHA:ECDHE-RSA-DES-CBC3-SHA:EDH-RSA-DES-CBC3-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA:!DSS
    SSLCertificateFile /etc/pki/tls/certs/firstdomain.com.crt
    SSLCertificateKeyFile /etc/pki/tls/private/firstdomain.com.key
```

N.B The recommended cipher suites and protocols are constantly changing. This site is useful to generate these.

<https://mozilla.github.io/server-side-tls/ssl-config-generator/>

If you have a signed (paid for) certificate, this needs to be added to the `/etc/pki/tls/certs/firstdomain.com.crt` file. Your certificate issuer should have provided you with a CA bundle. This needed to be added underneath your certificate in the same file.

Your private key will need to be added to the `/etc/pki/tls/private/firstdomain.com.key` file. This file should have its permissions change to be 600.

```bash
  chmod 600 /etc/pki/tls/private/firstdomain.com.key
```

so it can only be read and edited by the root user on your server.

You then need to test the configuration.
```bash
  httpd -t
```

and then reload it.

```bash
  service httpd reload
```

Fully featured examples of this and other apache functionality can be found on the following page:

[Sample vhosts](/operatingsystems/linux/apache/examplevhosts)

```eval_rst
  .. title:: Using SSLs with Apache
  .. meta::
     :title: Using SSLs with Apache | UKFast Documentation
     :description:  A guide on how to set up mod_ssl to allow Apache to use SSLs
     :keywords: ukfast, ssl, apache, mod_ssl, website, encryption, bash, tls, server, virtual, vm
```
