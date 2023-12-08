# Diagnostic Tools

This guide is only going to show an overview of the commands. To find out more about each command you can run the following:

```console
man [command]
```

## `netstat`

This command will show all the TCP and UDP ports listening on the server:

```console
netstat -tunap
```

Here's an example of it running.

```console
[root@c7 ~]# netstat -tunap
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1000/redis-server *
tcp        0      0 0.0.0.0:11211           0.0.0.0:*               LISTEN      995/memcached
tcp        0      0 127.0.0.1:6380          0.0.0.0:*               LISTEN      994/redis-server 12
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      26714/nginx: master
tcp        0      0 127.0.0.1:5910          0.0.0.0:*               LISTEN      4053/Xvnc
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      997/sshd
tcp        0      0 127.0.0.1:3350          0.0.0.0:*               LISTEN      987/xrdp-sesman
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      984/cupsd
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      23548/master
tcp        0      0 0.0.0.0:3389            0.0.0.0:*               LISTEN      988/xrdp
tcp        0      0 127.0.0.1:9000          0.0.0.0:*               LISTEN      23220/php-fpm: mast
tcp        0     64 192.168.0.97:22         81.201.139.52:60952     ESTABLISHED 2747/sshd: root@pts
tcp        0      0 192.168.0.97:3389       80.244.179.100:65397    ESTABLISHED 1905/xrdp
tcp        0      0 127.0.0.1:5910          127.0.0.1:43772         ESTABLISHED 4053/Xvnc
tcp        0      0 127.0.0.1:43772         127.0.0.1:5910          ESTABLISHED 1905/xrdp
tcp6       0      0 :::3306                 :::*                    LISTEN      1224/mysqld
tcp6       0      0 :::6379                 :::*                    LISTEN      1000/redis-server *
tcp6       0      0 :::11211                :::*                    LISTEN      995/memcached
tcp6       0      0 :::80                   :::*                    LISTEN      26714/nginx: master
tcp6       0      0 127.0.0.1:9200          :::*                    LISTEN      1008/java
tcp6       0      0 ::1:9200                :::*                    LISTEN      1008/java
tcp6       0      0 :::81                   :::*                    LISTEN      6624/httpd
tcp6       0      0 127.0.0.1:9300          :::*                    LISTEN      1008/java
tcp6       0      0 ::1:9300                :::*                    LISTEN      1008/java
tcp6       0      0 :::21                   :::*                    LISTEN      1001/vsftpd
tcp6       0      0 ::1:5910                :::*                    LISTEN      4053/Xvnc
tcp6       0      0 :::22                   :::*                    LISTEN      997/sshd
tcp6       0      0 ::1:631                 :::*                    LISTEN      984/cupsd
tcp6       0      0 ::1:25                  :::*                    LISTEN      23548/master
tcp6       0      0 :::443                  :::*                    LISTEN      6624/httpd
udp        0      0 0.0.0.0:68              0.0.0.0:*                           929/dhclient
udp        0      0 127.0.0.1:323           0.0.0.0:*                           659/chronyd
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           661/avahi-daemon: r
udp        0      0 0.0.0.0:40400           0.0.0.0:*                           661/avahi-daemon: r
udp        0      0 0.0.0.0:11211           0.0.0.0:*                           995/memcached
udp        0      0 0.0.0.0:22983           0.0.0.0:*                           929/dhclient
udp6       0      0 ::1:323                 :::*                                659/chronyd
udp6       0      0 :::5000                 :::*                                1050/java
udp6       0      0 :::11211                :::*                                995/memcached
udp6       0      0 :::48010                :::*                                929/dhclient
```

The most important information that can be gleaned from this is whether the socket is listening on all IPs or a specific IP, what port it's listening on and then that last part shows the Process ID (<nospell>PID</nospell>) and the service name.

## `lsof`

If you just run `lsof`, it will show all the open files on your server. This can be combined with the `grep` command to search for a specific file, e.g.

```console
[root@c7 ~]# lsof | grep access.log
nginx     26718                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26719                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26720                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26721                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26722                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
```

Will show all the files with `access.log` in the name.

If you run `lsof -ni:[x]`, this will show whether TCP port `[x]` is listening on your server. e.g.

```console
[root@c7 ~]# lsof -ni:80
COMMAND   PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
nginx   26714  root    6u  IPv4 3450218      0t0  TCP *:http (LISTEN)
nginx   26714  root    7u  IPv6 3450219      0t0  TCP *:http (LISTEN)
nginx   26715 nginx    6u  IPv4 3450218      0t0  TCP *:http (LISTEN)
nginx   26715 nginx    7u  IPv6 3450219      0t0  TCP *:http (LISTEN)
nginx   26716 nginx    6u  IPv4 3450218      0t0  TCP *:http (LISTEN)
nginx   26716 nginx    7u  IPv6 3450219      0t0  TCP *:http (LISTEN)
nginx   26717 nginx    6u  IPv4 3450218      0t0  TCP *:http (LISTEN)
nginx   26717 nginx    7u  IPv6 3450219      0t0  TCP *:http (LISTEN)
nginx   26718 nginx    6u  IPv4 3450218      0t0  TCP *:http (LISTEN)
```

This shows that NGINX is listening on port 80. The last part shows it `*:http` so listening on all IPs available on the server.

```console
[root@c7 ~]# lsof -ni:6379
COMMAND    PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
redis-ser 8056 redis    4u  IPv4 4640217      0t0  TCP 192.168.0.97:6379 (LISTEN)
```

This shows that the Redis service is listening on this port and it's listening on `192.168.0.97:6379`, which shows it's bound to a particular IP.

## `telnet`

`telnet` can be used to connect to a remote server via command line but it is useful to check connectivity to local and remote ports, e.g.

```console
[root@c7 ~]# telnet bbc.co.uk 80
Trying 212.58.244.22...
Connected to bbc.co.uk.
Escape character is '^]'.
```

This shows you are able to connect to `bbc.co.uk` from your server.

```console
[root@c7 ~]# telnet localhost 25
Trying ::1...
Connected to localhost.
Escape character is '^]'.
220 c7.novalocal ESMTP Postfix
```

This shows you're able to connect to the mail service on your own server.

You may come across a scenario where you're unable to connect to a specific server. You need to determine whether the connection is being blocked locally or on the remote end. This is an example of a blocked connection:

```console
[root@c7 ~]# telnet bbc.co.uk 3306
Trying 212.58.244.22...
telnet: connect to address 212.58.244.22: Connection timed out
```

There are specific servers that are set to listen on all ports and have no firewall restrictions in front of them. An example of this is `lee.io`. e.g.

```console
[root@c7 ~]# telnet lee.io 3306
Trying 178.62.56.193...
Connected to lee.io.
Escape character is '^]'.
Connected Successfully. Enter to quit
```

This shows the connection to `lee.io` over port `3306` was successful. Unless your firewall has specific firewall rules to block outbound access to specific IPs (unlikely as there's usually blanket bans to IPs and then specific IPs allowed rather than the other way round), you can assume that your server is able to connect outbound on port `3306`.

## `tcpdump`

`tcpdump` allows you to carry out a huge range of tests on your server. One of the most useful is to check activity on your network interface. First you need to check the interfaces on your machine.

```console
[root@c7 ~]# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    link/ether fa:16:3e:a2:ee:c9 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.97/24 brd 192.168.0.255 scope global dynamic eth0
       valid_lft 63133sec preferred_lft 63133sec
    inet6 fe80::f816:3eff:fea2:eec9/64 scope link
       valid_lft forever preferred_lft forever
```

The interface we want to check here is `eth0`. Here are some examples.

```text
[root@c7 ~]# tcpdump -Alnni eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:12.625803 IP 192.168.0.97.22 > 81.201.139.52.60952: Flags [P.], seq 2085181232:2085181440, ack 581399386, win 352, length 208
.e7.Q...]....dp..]X.~r...3@Q..?.f..Zp..L..!,*\.y. :...x,..!..~.T-r._.....{9.;u...............,T....H...."...K.J....s]+3.....h>.W...v.
11:28:12.626114 IP 192.168.0.97.22 > 81.201.139.52.60952: Flags [P.], seq 208:656, ack 1, win 352, length 448
E.....@.@..K...aQ..4....|IX.".sZP..`....E=...g.k..N`.f...M...rh..E.+h.-.#.....................NA.E.G......F..M....1.[..a.T..2....,@../.d.i.m..{.....!..y....iv...._.....J....        .Gg.v*.....XO.F.o.Ke6.l..D...N.we..U8.....g...Y.q0...~.....A$.16.L63v..'`.)....n....w.b6_..D\............{..R..Xt......X....\.  g..8(A.].O...-..g..=Xb..03.=!...=...g..D..xj.....#...3.^..&).....r]....|E...:A(..7............9:.x$..*.A......5.+S/H..(...4o
```

The above shows all activity on interface `eth0`. This will show you activity on `eth0` on port 80

```console
[root@c7 ~]# tcpdump -Alnni eth0 port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

This will show activity on `eth0` going to or coming from `54.65.7.81`

```console
[root@c7 ~]# tcpdump -Alnni eth0 host 54.65.7.81
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

This combines the 2 above examples so shows all traffic on `eth0` either coming from or going to `54.65.7.81` on port 80.

```console
[root@c7 ~]# tcpdump -Alnni eth0 port 80 and host 54.65.7.81
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

## `WinDump`

The program `WinDump` can be used on Windows with almost exactly the same syntax as `tcpdump`. Search Google to find the download page for this program.

One difference in the way this works is the selection of an interface. use the `-D` flag to list the interfaces:

```console
PS C:\Users\user1\Downloads> .\WinDump.exe -D
1.\Device\NPF_{3DD38385-E724-421A-B877-A44EEF5730C1} (VMware vmxnet3 virtual network device)
2.\Device\NPF_{FE51E730-F862-4E77-A733-0C5E88778135} (VMware vmxnet3 virtual network device)
```

You can then select the interface number:

```console
PS C:\Users\nick\Downloads> .\WinDump.exe -i 2
C:\Users\user1\Downloads\WinDump.exe: listening on \Device\NPF_{FE51E730-F862-4E77-A733-0C5E88778135}
10:28:33.106680 arp who-has 94.229.165.3.srvlist.ukfast.net tell 94.229.165.37.srvlist.ukfast.net
10:28:33.116382 IP test.com.3389 > 80.244.179.100.srvlist.ukfast.net.58832: P 2986157641:2986157998(357) ack 6594898
25 win 62990
10:28:33.130406 IP test.com.3389 > 80.244.179.100.srvlist.ukfast.net.58832: P 357:746(389) ack 1 win 62990
```

## `curl`

The man page of the `curl` command begins with an appropriate introduction:

```console
DESCRIPTION
       curl is a tool to transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, DICT, TELNET, LDAP or FILE).  The com-
       mand is designed to work without user interaction.

       curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file transfer resume  and  more.  As  you
       will see below, the number of features will make your head spin!
```

We'll try not to make your head spin but here are some of the most useful commands:

```console
[root@c7 ~]# curl www.ukfast.co.uk
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="shortcut icon" href="/favicon.ico">
```

This performed a `GET` request against the site `www.ukfast.co.uk`. As you can see, the site's source code was displayed. Apart from seeing that a response was retrieved, this isn't especially useful.

```console
[root@c7 ~]# curl -I www.ukfast.co.uk
HTTP/1.1 200 OK
Date: Mon, 06 Mar 2017 10:49:35 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Server: Apache
Set-Cookie: PHPSESSID=go5d65jm9jcp1slds2h7g5hfg3; path=/
Expires: Mon, 06 Mar 2017 11:49:20 GMT
Cache-Control: maxage=3600, public, must-revalidate, public
Pragma: no-cache
Last-Modified: Tue, 28 Feb 2017 16:05:01 GMT
Set-Cookie: marketing_campaign=eyJpZCI6MCwibmFtZSI6Ik5vbmUgLSBEaXJlY3QgVmlzaXRvciIsInBob25lIjoiMDgwMCA0NTggNDU0NSIsInBob25lX2dlbyI6IjAxNjEgMjE1IDM3MDAiLCJ1dWlkIjoiMTEzNTA5NjQ3NDU4YmQzZWIwNmMxZGQzLjYyNTcyODA4IiwidGltZXN0YW1wIjoxNDg4Nzk3MzYwfQ%3D%3D; expires=Tue, 06-Jun-2017 09:49:20 GMT; path=/; domain=ukfast.co.uk
X-Recruitment: Are you a superstar? Apply Now! http://ukfast.jobs
Vary: Accept-Encoding,User-Agent
Age: 0
Via: Webcelerate
Set-Cookie: SERVERID=web002; path=/
```

On the above example the `-I` flag was passed. This changes the request into a `HEAD` request which just retrieves the headers. As you can see, this gave a `200 OK` response. This also showed other information like cookies, expire headers, cache control information, etc.

```console
[root@c7 ~]# curl -I ukfast.co.uk
HTTP/1.1 301 Moved Permanently
Date: Mon, 06 Mar 2017 11:02:52 GMT
Content-Type: text/html; charset=iso-8859-1
Connection: keep-alive
Server: Apache
Location: http://www.ukfast.co.uk/
Cache-Control: max-age=0
Expires: Mon, 06 Mar 2017 11:02:37 GMT
Vary: Accept-Encoding
Accept-Ranges: bytes
Age: 0
Via: Webcelerate
Set-Cookie: SERVERID=web002; path=/
Cache-control: private
```

As you can see from the above example, we tested `ukfast.co.uk`. The response from this was a `301 Moved Permanently` redirect, and we can see the location of that is `http://www.ukfast.co.uk/`. We can add the flag `-L` which will tell `curl` to follow the redirect:

```console
[root@c7 ~]# curl -IL ukfast.co.uk
HTTP/1.1 301 Moved Permanently
Date: Mon, 06 Mar 2017 11:05:00 GMT
Content-Type: text/html; charset=iso-8859-1
Connection: keep-alive
Server: Apache
Location: http://www.ukfast.co.uk/
Cache-Control: max-age=0
Expires: Mon, 06 Mar 2017 11:04:45 GMT
Vary: Accept-Encoding
Accept-Ranges: bytes
Age: 0
Via: Webcelerate
Set-Cookie: SERVERID=web002; path=/
Cache-control: private

HTTP/1.1 200 OK
Date: Mon, 06 Mar 2017 11:05:00 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Server: Apache
Set-Cookie: PHPSESSID=vksgaspkjbm0b551nijb2g8il2; path=/
Expires: Mon, 06 Mar 2017 12:05:00 GMT
Cache-Control: maxage=3600, public, must-revalidate, public
Pragma: no-cache
Last-Modified: Tue, 28 Feb 2017 16:05:01 GMT
Set-Cookie: marketing_campaign=eyJpZCI6MCwibmFtZSI6Ik5vbmUgLSBEaXJlY3QgVmlzaXRvciIsInBob25lIjoiMDgwMCA0NTggNDU0NSIsInBob25lX2dlbyI6IjAxNjEgMjE1IDM3MDAiLCJ1dWlkIjoiMTc2ODI3Nzg1MDU4YmQ0MjVjMzIxNjQ2LjM3MzY5NDQwIiwidGltZXN0YW1wIjoxNDg4Nzk4MzAwfQ%3D%3D; expires=Tue, 06-Jun-2017 10:05:00 GMT; path=/; domain=ukfast.co.uk
X-Recruitment: Are you a superstar? Apply Now! http://ukfast.jobs
Vary: Accept-Encoding,User-Agent
Age: 0
Via: Webcelerate
Set-Cookie: SERVERID=web001; path=/
```

As you can see, we got the `301` response first and then the original `200` response when we ended up at `www.ukfast.co.uk`.

You may want to test a site against an IP before its DNS record has been changed. You could do this by [creating a hosts file entry](/operatingsystems/windows/commonissues/testingwebsites) or you can amend a header on your `curl` command with the `-H` flag. Here is a test against the domain `testdomain.com` - we don't own this. Here is the response:

```console
[root@c7 ~]# curl testdomain.com
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" data-adblockkey="MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKrfIMFkSaoTSqKmC+BrghK0CpDHc0MuVzmMHin8LIORhpXbped+iYhSnZurWnEO0zcKcVIrzp026LVc5pMB9bUCAwEAAQ==_k30gkd/zAhhXt9eui+IJt66Wl3Fl7A0MNcpds/Ub3yjgmHPt+tNYiJiutb7b9/liIU+l3dGaeXvBJ+OC21ynAA==">
```

We are now going to test this domain against a server with IP `46.37.172.196` and insert a Host header with the `-H` flag:

```console
[root@c7 ~]# curl 46.37.172.196 -H "Host: testdomain.com"
new testdomain server
```

Here is the same test without inserting the `Host` header:

```console
[root@c7 ~]# curl 46.37.172.196
<html>
        <head>
                <title>Under Maintenance</title>
```

As you can see, this gave us a different response. The reason for this is that there are multiple sites on `46.37.172.196` - using the `-H` flag and inserting a `Host` header allowed us to be more specific about what site we were requesting.

```eval_rst
  .. title:: Network diagnostic tools on Linux
  .. meta::
     :title: Network diagnostic tools on Linux | ANS Documentation
     :description: A guide to using network diagnostic tools in the Linux OS
     :keywords: ukfast, network, diagnostic, netstat, lsof, linux, telnet, ping
```
