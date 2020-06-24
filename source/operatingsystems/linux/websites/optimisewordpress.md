# Optimize WordPress

As WordPress is a popular Content Management System (CMS), and as such we regularly receive requests to ensure WordPress installations are running optimally. In this article we will discuss what could be implemented to enhance the websites performance and improve load times.

```eval_rst
.. seealso::.. If you haven't yet installed WordPress please follow this prerequisite guide:
[Wordpress Install](/websites/wordpress)
```

An essential metric to any website is the page load time. It's a well-known fact that users want to consume data fast and will typically leave a website after just three seconds if the website fails to load. Googles SEO rankings also prefer speedier websites and so it's even more important to consider what can be done to optimize website performance.
An excellent tool that can be used to understand the website's performance is [GTmetrix](https://gtmetrix.com/). For the most accurate user results use test server region of London, UK and enable "stop test onload".

## Up To Date Software
It's important to keep on top of updating WordPress and its plugins to minimize risk from unpatched vulnerabilities, and updates may also include performance enhancements.

Automatic updates for themes and plugins are disabled by default but can be [enabled in the wp-config.php file](https://wordpress.org/support/article/configuring-automatic-background-updates/). This may not always be the preferred solution as the new versions could contain breaking changes that may impact the website. Available updates are visible through the WordPress admin panel and can be updated manually as they are released. 

In addition to updating the application software, making sure that the server is running the latest software is also important for both security and performance reasons. This includes the Operating System, Apache/NGINX/IIS, MySQL/MariaDB/MSSQL and PHP. 

```eval_rst
.. seealso::..If the website is running PHP5.X and your application supports PHP7.X, it may be worthwhile upgrading as PHP7.X is generally more performant.
```

## Load
Server load is a major factor in the systems ability to handle requests quickly. `Load average` represents how many processes are queued waiting for compute resources, the higher the load average the slower the website will likely perform. 

Identifying and blocking malicious traffic from accessing the server will reduce its impact on the servers load. WordPress [brute force attacks](https://wordpress.org/support/article/brute-force-attacks/) are typical in the industry and are easily mitigated by using a [.htpasswd](https://wordpress.org/support/article/brute-force-attacks/#password-protect-wp-login-php) or a security plugin like [All In One](https://wordpress.org/plugins/all-in-one-wp-security-and-firewall/).

## Cache
Using a caching layer will temporarily store data in memory, meaning future requests for that content will be served from cache, resulting in a faster page load - in turn improving the user experience and reducing server load. Utilizing a plugin like [W3 Total Cache](https://en-gb.wordpress.org/plugins/w3-total-cache/), WP Rocket, or WP Super Cache will provide the ability to cache static content and other features like "minifying" JS and CSS, as well as integrations into CDN platforms.

To take this to the next level, pairing these plugins with an in-memory datastore like `redis` or `memcached` can be very powerful. Feel free to contact support to discuss installing an in-memory cache on your server.

For clients running WordPress on Windows, take a look at [IIS tuning](/operatingsystems/windows/iis/tuning).

Installing `php-opache` on the server will improve PHP's performance by storing precompiled bytecode in memory. Windows Servers can also look at [Wincache](https://www.php.net/wincache).

```eval_rst
.. seealso::.. Speak with our specialist team on 0800 953 0645 to discuss a solution to caching using a Webcelerator and/or DDOSX CDN
```

## Themes & Plugins
It's fair to say that minimal, lightweight themes out-perform more complex graphic-heavy themes. It's recommended that before choosing a WordPress theme, you first consider the impact it will have on the sites performance. A solid indicator of the quality are the:
* `Ratings`
* `Reviews`
* `Documentation` 
* `Support` options provided

When talking about the homepage, it's ideal to avoid heavy content both in terms of CPU time and in download time. The homepage is best kept minimal and ideally most (if not all) of the content being static files served via cache.

The more plugins that are installed and active, the more likely it is that the website will run slowly. Start by deactivating and deleting any unnecessary plugins. Then selectively disable remaining plugins to measure the performance before and after and see the impact it makes on page load. *Is one plugin causing an obvious impact?* Dig into the plugin documentation and support forums to make sure its working correctly, or look at an alternate plugin that provides the same functionality.

## GZIP compression
Enabling `gzip` compression will reduce the size of the files sent from the server which increases the speed content is returned to the browser. When enabling compression you will notice the `TTFB` (Time To First Byte) will increase slightly. This is because the server is spending some time compressing the website files before the transfer, the overall page speed however should be quicker. For more information about `TTFB`, take a look at this [CloudFlare article](https://blog.cloudflare.com/ttfb-time-to-first-byte-considered-meaningles/).

## Optimize images
Images that haven't been optimized cause slower page load times, so it is recommended that these are optimized before use on your website.

- Use the correct file formats: `JPG/PNG/GIF`.
- Remove/crop white space around the images and instead use `CSS` for padding.
- Save images in the desired size to reduce the file size. 

"Lossless compression" is a method of compressing the size of a file without sacrificing image quality. This can be done using a plugin like [smush](https://en-gb.wordpress.org/plugins/wp-smushit/) (if suitable) or per image using an online [resizing tool](https://tinypng.com/). 

## Minify CSS & JavaScript
Minification is the action of removing white space and unnecessary characters from a file to reduce the total size of that file. When CSS and JavaScript are minified the page load time is decreased as the CSS and JS files are smaller.

## Defer JavaScript
By default, `JavaScript` blocks DOM render which delays the time it takes the browser to display the page. Some `JavaScript` execution is not necessary for the initial render and can be deferred to execute after the page has loaded. Also see [Parser Blocking vs. Asynchronous JavaScript](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/adding-interactivity-with-javascript#parser_blocking_versus_asynchronous_javascript) for details on loading JS asynchronously.

## Windows Application Pool 

To prevent memory leaks or unresponsive/idle worker processes within the application causing performance issues, its recommended to setup nightly [recycling](https://docs.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/add/recycling/) in the IIS application pool. In additional to `recycling`, requests to the application pool can be limited using the `Queue Length` parameter in the application pool settings. To prevent high demand causing degraded website performance there is an algorithm that can suggest the optimal queue length  `( Available memory in MB x number of processors x 10 ) / ( total number of application pools )`. 

## Database Tuning

WordPress on [MSSQL](https://docs.ukfast.co.uk/operatingsystems/windows/mssql/performancedashboard.html) 

Wordpress on [MySQL/MariaDB](https://docs.ukfast.co.uk/operatingsystems/linux/mysql/troubleshooting.html)

```eval_rst
  .. title:: Optimise your Wordpress installation
  .. meta::
     :title: Optimise your Wordpress installation | UKFast Documentation
     :description: An article that discusses all the ways to improve you wordpress installation and servers performance.
     :keywords: ukfast, windows, iis, web, site, guide, wordpress, linux, performance, seo, rankings, apache, nginx, faster
