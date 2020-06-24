# Adding an SSL Certificate in nginx

A lot of guides on setting up SSL configuration with nginx will have you create a completely separate server block for your `https` content.

Whilst this works fine, it duplicates future work when making configuration changes, as you now have two near-identical server blocks that need to be updated.

So unless you have a particular need for separate blocks (such as needing different nginx configuration for your https content), I'd reccomend simplifying and using the following method.

## Configuration

Taking our example configuration from the previous nginx installation guide, we previously had the following:

```nginx

    upstream php {
            server 127.0.0.1:9000;
    }

    server {

            listen 80;
            server_name mywebsite.com www.mywebsite.com;
            root /var/www/vhosts/mywebsite.com/httpdocs;


            index index.php index.html;

            location / {
                    try_files $uri $uri/ /index.php?$args;
            }

            location ~ \.php$ {
                    include fastcgi.conf;
                    fastcgi_intercept_errors on;
                    fastcgi_pass php;
            }

            location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
                    expires max;
                    log_not_found off;
            }
    }
```

To adapt this for SSL connections, we only need to tell the configuration to listen on port `443` and then point it at our SSL certificate files.

To do that, we need to add the following lines:

```nginx

   listen 443 ssl;
   ssl_certificate     /var/path/to/certficate.crt;
   ssl_certificate_key /var/path/to/key.key;
```

Paths to your certificate and key would need to be replaced with something that wasn't fictitious.

```eval_rst
.. note::

   Your CA bundle should be included at the end of your certificate file, there's no separate directive required with nginx
```

With all that in place, your configuration should now look like this:

```nginx

    upstream php {
            server 127.0.0.1:9000;
    }

    server {

            listen 80;
            listen 443 ssl;

            ssl_certificate     /var/path/to/certficate.crt;
            ssl_certificate_key /var/path/to/key.key;

            server_name mywebsite.com www.mywebsite.com;
            root /var/www/vhosts/mywebsite.com/httpdocs;


            index index.php index.html;

            location / {
                    try_files $uri $uri/ /index.php?$args;
            }

            location ~ \.php$ {
                    include fastcgi.conf;
                    fastcgi_intercept_errors on;
                    fastcgi_pass php;
            }

            location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
                    expires max;
                    log_not_found off;
            }
    }
```

Now it's just a matter of testing your configuration and then restarting nginx to put it all live:

```console
  service nginx configtest
```

```console
  service nginx restart
```

```eval_rst
  .. title:: Adding an SSL certificate in Nginx
  .. meta::
     :title: Adding an SSL certificate in Nginx | UKFast Documentation
     :description: A guide to adding an SSL certificate to Nginx on Linux
     :keywords: ukfast, linux, ssl, security, nginx, web, server, install, tutorial, configuration
