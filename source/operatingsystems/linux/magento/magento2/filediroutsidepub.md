# Magento 2 File/Directory Outside /pub

If you have a file/directory you want to be accessible but is outside of the Magento 2 pub directory you need to edit your domains Nginx configuration (Example: /etc/nginx/conf.d/example.com.conf). 

For this example we the sitemap.xml located in /var/www/vhosts/example.com/htdocs/. This file will produce a 404 as it's not located in the pub directory (/var/www/vhosts/example.com/htdocs/pub/):

```bash
 ~]$ curl -I www.example.com/sitemap.xml
 HTTP/1.1 404 Not Found
```

You can add the following to the domains Nginx configuration file anywhere within the server block:

```bash
~]$ vim /etc/nginx/conf.d/example.com.conf

# Alias to run sitemap.xml outside of the pub folder
location /sitemap.xml {
    alias /var/www/vhosts/example.com/htdocs/sitemap.xml;
}
 ```

To implement this change you need to reload the Nginx service. First perform a configuration test with the following command:

```bash
 ~]$ nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

If there are no errors in the configuration test, proceed to reload the Nginx service with the following command:

```bash
 ~]$ nginx -s reload
```

You should now be able to access sitemap.xml without any issues:

```bash
 ~]$ curl -I www.example.com/sitemap.xml
 HTTP/1.1 200 OK
```

```eval_rst
  .. meta::
     :title: Magento 2 File/Directory Outside /pub | UKFast Documentation
     :description: A guide to adding Files/Directories to run outside /pub in Nginx
     :keywords: ukfast, linux, permissions, nginx, install, centos, cloud, lamp, server, virtual, Wordpress, Magento
