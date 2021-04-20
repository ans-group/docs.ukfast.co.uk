# Installation/Configuration of NGINX

## Install NGINX

NGINX probably isn't installed on your server, so we'll first need to get it.

We can install the latest version with `yum`. Firstly, create a file called /etc/yum.repos.d/nginx.repo and add in the below:

```console
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=0
enabled=1
```
Manually replace `$releasever` with either 5 (for 5.x), 6 (for 6.x), or 7 (for 7.x)depending upon your OS version.

Now we can install NGINX:

```console
yum install nginx
```

Most people will want their web server to start on boot, use `chkconfig` to make it so:

```console
chkconfig nginx on
```
For CentOS 7, use the below:
```console
systemctl enable nginx.service
```

## Configure a site

Where in Apache you have `Virtual Hosts` and in IIS you have `bindings`, in NGINX you have `server blocks`. Each block typically configures a site.

All config files ending in `.conf` in the `/etc/nginx/conf.d` directory will be parsed as NGINX configuration files at the end of the main `/etc/nginx.conf` file.

The following content, if added to a file called `/etc/nginx/conf.d/mywebsite.com.conf` will start NGINX listening on your default IP address for a site called `mywebsite.com` serving content out of `/var/www/vhosts/mywebsite.com/httpdocs/`.

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

With a standard setup like this, the files will need to be owned by the NGINX user and group:

```console
chown -R  nginx:nginx /var/www/vhosts/mywebsite.com
```

```eval_rst
.. note::
   If you opt for a ``PHP-FPM`` setup later, then you'll likely need to change that user and group to whatever user you specify in your ``PHP-FPM`` configuration
```

You're nearly good to go, the only thing you need now is some content. The NGINX directive `index` specifies which file is used as the default index file in a directory, and as you can see from that config, `index.php` and `index.html` were specified.

By that logic, if you create a file in `/var/www/vhosts/mywebsite.com/httpdocs` called `index.html` with some content, then that's what will display on `www.mywebsite.com`

```eval_rst
.. note::
   Don't forget to chown any website files to ``nginx:nginx`` as well
```

## Start it all up

```eval_rst
.. warning::
   If you haven't yet set up any php handler, then the above config won't start. Most people will be interested in having their website serve php, so you should carry on following the PHP-FPM guide:

   - :doc:`/operatingsystems/linux/php-fpm/phpfpmsetup`

   If you are just looking to serve static HTML, you'll have to comment out the upstream and php sections on the above NGINX config.
```

Before starting or restarting NGINX, it's always advisable to test your new config. Testing can be done with the command `service nginx configtest` and if all is well, it should spit out the following message:

```console
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

To start NGINX, the following command can be used:

```console
service nginx start
```

Or if it's already running, you can restart it:

```console
service nginx restart
```

## Going forward

Most sites now need more that just basic HTML, often using PHP to generate their dynamic content and some kind of database to store information.

As mentioned above, the NGINX config in this article is more geared towards PHP-FPM.

The following documents carry on the setup for those particular elements:

- [PHP-FPM Setup](/operatingsystems/linux/php-fpm/phpfpmsetup)
- [MySQL Installation](/operatingsystems/linux/mysql/installation)

```eval_rst
   .. title:: Installation and configuration of NGINX on Linux
   .. meta::
      :title: Installation and configuration of NGINX on Linux | UKFast Documentation
      :description: A guide to installing and configuring the NGINX web server on Linux
      :keywords: ukfast, linux, nginx, web, server, configuration, installation, guide, tutorial
```
