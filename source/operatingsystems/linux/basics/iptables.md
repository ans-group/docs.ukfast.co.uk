# Linux software firewall


`iptables` is the name of the software firewall bundled with most UKFast Linux servers.

Whilst we recommend that you use your hardware firewall for most things, it may still be helpful/necessary to be able to use iptables for quickly blocking IP addresses or closing ports.

As with most Linux packages, the man pages are a good place to start to learn more about the package and its usage, but if you're just looking to get up and running quickly, here are a few examples:

## Command Structure
```console
   iptables -I OUTPUT -p tcp -s 192.168.0.1 --dport 2020 -j ACCEPT
```

The individual elements of the above commands are explained below

* **iptables**

   The command itself.


* **-I**

   Insert the new rule at the top of the chain.

   iptables rules are read in sequentially, so the order the rules are in is very important. If the rule you're adding doesn't need to be the first, can you alternatively use `-A` to append it to the bottom of the chain or `-I {CHAIN} {LINE NUMBER}` to insert it at a particular line number.


* **OUTPUT**

   The chain name.

   There are 2 main chains that you'll likely be interested in, `INPUT` and `OUTPUT`. Simply put, rules in `INPUT` affect inbound traffic and rules in `OUTPUT` affect outbound.


* **-p**

   The protocol that the rule relates to.

   Valid protocols are `tcp`, `udp` or `icmp`


* **-s**

   Source IP address that the rule pertains to.

   Can also be written longhand as `--source` or `--src`.

   Inversely, destination ip addresses can be specified with `-d`, `--destination` or `--dst`.

   Can also be given a range such as `192.168.0.0/24` or `192.168.0.0/255.255.255.0`.


* **--dport**

   Destination port that the rule relates to.

   Can also be written as `--destination-port`.

   Alternatively, source port can be specified with `--sport` or `--source-port`.

   Ranges of ports can be specified with a `:`, for example `1096:2999`.


* **-j**

   Chain to jump to when previous elements have been matched.

   Basic chains that can be used here are `ACCEPT`, `DROP` and `REJECT`.

   `ACCEPT` will accept packet, `REJECT` will deny packet and `DROP` will result in it being silently dropped.

## List current rules

```bash
   iptables -vnL
```

## Blocking a port

```bash
   iptables -I INPUT -p tcp --dport 6667 -j REJECT
```

## Blocking an ip

```bash
   iptables -I INPUT -p tcp -s 1.2.3.4 -j DROP
```

## Blocking a port for a particular ip

```bash
  iptables -I OUTPUT -p tcp -s 192.168.0.1 --dport 25 -j DROP
```  

```eval_rst
.. note::

   The site http://iptabl.es can be used to generate iptables rules without having to memorise the above syntax. Usage is explained on the frontpage, but a few examples are below:

   curl iptabl.es/drop/2020/8.8.8.8

   http://iptabl.es/accept/25
```

```eval_rst
  .. title:: Linux software firewall
  .. meta::
     :title: Linux software firewall | UKFast Documentation
     :description: Information and guidance on using iptables in linux
     :keywords: ukfast, linux, firewall, iptables, security, software, waf, application, server, virtual, vm
