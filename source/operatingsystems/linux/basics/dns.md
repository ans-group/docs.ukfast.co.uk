# Domain Name Service (DNS)

This guide is only going to show an overview of the commands. To find out more about each command you can run the following:

```bash
  man [command]
```

## dig

`dig` is used to query DNS servers. N.B. `dig` will query the nameservers defined in the `/etc/resolv.conf` file. If you are running a DNS server on your own server, this command will query that DNS server by default - this may not be what is being seen globally. See how to query an external nameserver further down.

Here are some examples.

```console
[root@c7 ~]# dig bbc.co.uk

; <<>> DiG 9.9.4-RedHat-9.9.4-29.el7_2.3 <<>> bbc.co.uk
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49328
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;bbc.co.uk.                     IN      A

;; ANSWER SECTION:
bbc.co.uk.              120     IN      A       212.58.244.22
bbc.co.uk.              120     IN      A       212.58.244.23
bbc.co.uk.              120     IN      A       212.58.246.79
bbc.co.uk.              120     IN      A       212.58.246.78

;; Query time: 17 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Aug 11 12:17:19 BST 2016
;; MSG SIZE  rcvd: 102
```

This will give you the `A` record entry for `bbc.co.uk`.

```console
[root@c7 ~]# dig www.bbc.co.uk

; <<>> DiG 9.9.4-RedHat-9.9.4-29.el7_2.3 <<>> www.bbc.co.uk
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4367
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;www.bbc.co.uk.                 IN      A

;; ANSWER SECTION:
www.bbc.co.uk.          173     IN      CNAME   www.bbc.net.uk.
www.bbc.net.uk.         105     IN      A       212.58.246.91
www.bbc.net.uk.         105     IN      A       212.58.244.67

;; Query time: 9 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Aug 11 12:36:48 BST 2016
;; MSG SIZE  rcvd: 100
```

This will give you the `A` record entry for `www.bbc.co.uk`. Most of the time the non-`www` and `www` record will be the same but it is always worth checking.

```console
[root@c7 ~]# dig mx bbc.co.uk

; <<>> DiG 9.9.4-RedHat-9.9.4-29.el7_2.3 <<>> mx bbc.co.uk
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11699
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;bbc.co.uk.                     IN      MX

;; ANSWER SECTION:
bbc.co.uk.              233     IN      MX      20 cluster1a.eu.messagelabs.com.
bbc.co.uk.              233     IN      MX      10 cluster1.eu.messagelabs.com.

;; Query time: 22 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Aug 11 12:39:13 BST 2016
;; MSG SIZE  rcvd: 107
```

This will give you the `MX` record for `bbc.co.uk`.

```console
[root@c7 ~]# dig spf bbc.co.uk +short
"v=spf1 ip4:212.58.224.0/19 ip4:132.185.0.0/16 ip4:78.136.53.80/28 ip4:78.136.14.192/27 ip4:78.136.19.8/29 ip4:89.234.10.72/29 ip4:89.234.53.236 ip4:212.111.33.181 ip4:78.137.117.8 ip4:84.45.18.216 ip4:46.37.176.74 ip4:194.74.182.201" " ip4:80.169.167.201 +include:sf.sis.bbc.co.uk +include:servers.mcsv.net +include:amazonses.com ?all"
```

This example gives the `SPF` record for `bbc.co.uk` but also contains the `+short` flag which will just output the actual record.

```console
[root@c7 ~]# dig bbc.co.uk @8.8.8.8

; <<>> DiG 9.9.4-RedHat-9.9.4-29.el7_2.3 <<>> bbc.co.uk @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 62442
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;bbc.co.uk.                     IN      A

;; ANSWER SECTION:
bbc.co.uk.              191     IN      A       212.58.244.22
bbc.co.uk.              191     IN      A       212.58.244.23
bbc.co.uk.              191     IN      A       212.58.246.79
bbc.co.uk.              191     IN      A       212.58.246.78

;; Query time: 9 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Aug 11 12:45:43 BST 2016
;; MSG SIZE  rcvd: 102
```

This queries the `A` record for `bbc.co.uk` but specifically queries the nameserver `8.8.8.8`

```eval_rst
  .. title:: DNS commands in Linux
  .. meta::
     :title: DNS commands in Linux | ANS Documentation
     :description:  A guide to the DNS commands in the Linux OS
     :keywords: ukfast, linux, dns, server, command, ttl, ip, address, dig
```
