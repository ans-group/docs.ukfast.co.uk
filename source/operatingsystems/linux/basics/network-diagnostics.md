# Diagnostic Tools

This guide is only going to show an overview of the commands. To find out more about each command you can run the following:

```console
  man [command]
```

## netstat

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

The most important information that can be gleaned from this is whether the socket is listening on all IPs or a specific IP, what port it's listening on and then that last part shows the PID (Process ID) and the service name.

## lsof

If you just run `lsof`, it will show all the open files on your server. This can be combined with the grep command to search for a specific file. e.g.

```console
[root@c7 ~]# lsof | grep access.log
nginx     26718                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26719                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26720                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26721                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
nginx     26722                       nginx    5w      REG                8,2     19160    4942997 /var/log/nginx/access.log
```

Will show all the files with access.log in the name.

If you run `lsof -ni:[x]`, this will show whether TCP port x is listening on your server. e.g.

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

This shows that Nginx is listening on port 80. The last part shows it `*:http` so listening on all IPs available on the server.

```console
[root@c7 ~]# lsof -ni:6379
COMMAND    PID  USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
redis-ser 8056 redis    4u  IPv4 4640217      0t0  TCP 192.168.0.97:6379 (LISTEN)
```

This shows that the Redis service is listening on this port and it's listening on `192.168.0.97:6379` which shows it's bound to a particular IP.

## telnet

telnet can be used to connect to a remote server via command line but it is useful to check connectivity to local and remote ports. e.g.

```console
[root@c7 ~]# telnet bbc.co.uk 80
Trying 212.58.244.22...
Connected to bbc.co.uk.
Escape character is '^]'.
```

show's you are able to connect to the BBC site from your server.

```console
[root@c7 ~]# telnet localhost 25
Trying ::1...
Connected to localhost.
Escape character is '^]'.
220 c7.novalocal ESMTP Postfix
```

shows you're able to connect to the mail service on your own server.

You may come across a scenario where you're unable to connect to a specific server. You need to determine whether the connection is being blocked locally or on the remote end. e.g.

```console
[root@c7 ~]# telnet bbc.co.uk 3306
Trying 212.58.244.22...
telnet: connect to address 212.58.244.22: Connection timed out
```

There are specific servers that are set to listen on all ports and have no firewall restrictions in front of them. An example of this is lee.io. e.g.

```console
[root@c7 ~]# telnet lee.io 3306
Trying 178.62.56.193...
Connected to lee.io.
Escape character is '^]'.
Connected Successfully. Enter to quit
```

This shows the connection to lee.io over port 3306 was successful. Unless your firewall has specific firewall rules to block outbound access to specific IPs (unlikely as there's usually blanket bans to IPs and then specific IPs allowed rather than the other way round), you can assume that your server is able to connect outbound on port 3306.


## tcpdump

tcpdump allows you to carry out a huge range of tests on your server. One of the most useful is to check activity on your network interface. First you need to check the interfaces on your machine.

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

```
[root@c7 ~]# tcpdump -Alnni eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:12.625803 IP 192.168.0.97.22 > 81.201.139.52.60952: Flags [P.], seq 2085181232:2085181440, ack 581399386, win 352, length 208
.e7.Q...]....dp..]X.~r...3@Q..?.f..Zp..L..!,*\.y. :...x,..!..~.T-r._.....{9.;u...............,T....H...."...K.J....s]+3.....h>.W...v.
11:28:12.626114 IP 192.168.0.97.22 > 81.201.139.52.60952: Flags [P.], seq 208:656, ack 1, win 352, length 448
E.....@.@..K...aQ..4....|IX.".sZP..`....E=...g.k..N`.f...M...rh..E.+h.-.#.....................NA.E.G......F..M....1.[..a.T..2....,@../.d.i.m..{.....!..y....iv...._.....J....        .Gg.v*.....XO.F.o.Ke6.l..D...N.we..U8.....g...Y.q0...~.....A$.16.L63v..'`.)....n....w.b6_..D\............{..R..Xt......X....\.  g..8(A.].O...-..g..=Xb..03.=!...=...g..D..xj.....#...3.^..&).....r]....|E...:A(..7............9:.x$..*.A......5.+S/H..(...4o
```

This shows all activity on interface eth0.

```console
[root@c7 ~]# tcpdump -Alnni eth0 port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

This will show you activity on eth0 on port 80

```console
[root@c7 ~]# tcpdump -Alnni eth0 host 54.65.7.81
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

This will show activity on eth0 going to or coming from 54.65.7.81

```console
[root@c7 ~]# tcpdump -Alnni eth0 port 80 and host 54.65.7.81
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 65535 bytes
```

This combines the 2 above examples so shows all traffic on eth0 either coming from or going to 54.65.7.81 on port 80.
