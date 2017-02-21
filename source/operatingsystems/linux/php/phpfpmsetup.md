# Installing and configuring php-fpm

php-fpm is a PHP module which will execute PHP code on behalf of a web server. Nginx is unable to natively execute PHP code so should be configured to pass all .php files over to php-fpm; Apache is able to execute PHP itself with mod_php but this is inefficient. Newer versions can now be confgured to pass .php files to php-fpm.

To install use the following command:

```console
  yum install php-fpm
```

This will create the file `/etc/php-fpm.d/www.conf`

You can now start php-fpm.

```console
  service php-fpm start
```

and set it to start on boot.

```console
  chkconfig php-fpm on
```

This will start a php-fpm server listening on port 9000. You can then pass all your PHP requests over to this port.

The above configuration will work fine and is ideal if you are running php-fpm on a separate server but if you're running php-fpm on the same server as your web server, it's a better idea to configure a socket to pass requests to. It's also a good idea to configure a php-fpm pool per site as this allows you to track how the sites are being used. Here is a samples configuration for a domain called domain.com

```console
[firstdomaincom]

listen = '/var/run/php-fcgi-firstdomaincom.sock'
;listen.backlog = -1
listen.allowed_clients = 127.0.0.1
listen.owner = apache
listen.group = apache
;listen.mode = 0666

user = firstdomainuser
group = firstdomainuser

pm = dynamic
pm.max_children = 300
pm.start_servers = 5
pm.min_spare_servers = 5
pm.max_spare_servers = 20
pm.max_requests = 2000
;pm.status_path = /status

;ping.path = /ping
;ping.response = pong

;request_terminate_timeout = 0
;request_slowlog_timeout = 0
slowlog = /var/www/vhosts/firstdomain.com/phpfpm-slow.log

;rlimit_files = 1024
;rlimit_core = 0

;chroot =

;chdir = /var/www

;catch_workers_output = yes

;env[HOSTNAME] = $HOSTNAME
;env[PATH] = /usr/local/bin:/usr/bin:/bin
;env[TMP] = /tmp
;env[TMPDIR] = /tmp
;env[TEMP] = /tmp

php_admin_value[error_log] =  /var/www/vhosts/firstdomain.com/phpfpm-error.log
php_admin_flag[log_errors] = on
```

This is configured to work with Apache. If you were configuring this with Nginx, you would replace these lines.

```console
listen.owner = nginx
listen.group = nginx
```

The php-fpm pool needs to run as its own Linux user.

```console
user = firstdomainuser
group = firstdomainuser
```

LINK TO CREATING USERS

You will then need to run a configuration test.

```console
 php-fpm -t
```

and then reload the configuration.

```console
  service php-fpm reload
```

You should now be able to see the php-fpm socket.

```console
  stat /var/run/php-fcgi-firstdomaincom.sock
  ```

 which should should show something like.

 ```console
   File: ‘/var/run/php-fcgi-firstdomaincom.sock’
  Size: 0               Blocks: 0          IO Block: 4096   socket
Device: 13h/19d Inode: 3108659     Links: 1
Access: (0666/srw-rw-rw-)  Uid: (   48/  apache)   Gid: (   48/  apache)
Access: 2016-08-10 13:15:26.968222080 +0100
Modify: 2016-08-10 13:15:26.968222080 +0100
Change: 2016-08-10 13:15:26.968222080 +0100
 Birth: -
```

The pm values in the configuration are there mainly to prevent the server from running out of memory; however, on higher servers with higher specification can be set to higher values.
