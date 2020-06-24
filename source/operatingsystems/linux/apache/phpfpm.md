
# Apache with php-fpm

By default Apache will run PHP as `mod_php`. This means that it will load the PHP libraries for every Apache process even when Apache is serving a static files such as an image or text. This can cause bloating of the Apache memory usage on your server. Another issue with running PHP as `mod_php` is that the Apache users needs to be able to read the files in your document root and any files it writes will be created with apache as the owner. This may be fine if you only have one or two sites on your server but may become an issue with more sites which may require other 3rd parties to access those files.

Apache version 2.4+ allows you to hand off PHP processing to `php-fpm` which runs as a separate process. You can check your Apache version with this command.

```bash
  httpd -V
```

This shows your version.

```console
  Server version: Apache/2.4.6 (CentOS)
```

Please see here on how to configure php-fpm: TODO

You will then need to add this section to your Apache configuration to pass .php files over to your php-fpm socket.

```apacheconf
    <FilesMatch "\.php$">
        SetHandler "proxy:unix:/var/run/php-fcgi-firstdomaincom.sock|fcgi://127.0.0.1"
    </FilesMatch>
    ProxyTimeout 600
```

Note the `ProxyTimeout` setting here. When Apache passes content to php-fpm for processing, it sees php-fpm as a proxy. If you have a long running PHP script, Apache may time out before it completes. On the other hand, you want to protect your server from running a PHP script indefinitely.

The `/var/run/php-fcgi-domaincom.sock` section needs to be the socket configured in your php-fpm configuration file.

Fully featured examples of this and other apache functionality can be found on the following page:

[Sample Vhosts](/linux/php/examplevhosts)

```eval_rst
  .. title:: Using Apache with PHP-FPM
  .. meta::
     :title: Using Apache with PHP-FPM | UKFast Documentation
     :description:  A guide to using PHP-FPM with the Apache web server.
     :keywords: ukfast, apache, php-fpm, server, linux, server, web, virtual, vm
