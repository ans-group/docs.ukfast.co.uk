# Service Management on CentOS 7

CentOS 7 uses systemd for service management. Systemd is an alternative to older systems such as SysVinit which was used by [CentOS 6](/operatingsystems/linux/basics/services_centos6).

Here are a few changes that you need to be aware of.


## Check status of services

You can use the command below to check the status of your services.

```console
[root@centos ~]# systemctl status httpd
 httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2016-08-03 16:33:11 BST; 6 days ago
     Docs: man:httpd(8)
           man:apachectl(8)
  Process: 22622 ExecReload=/usr/sbin/httpd $OPTIONS -k graceful (code=exited, status=0/SUCCESS)
 Main PID: 7671 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
   Memory: 11.9M
   CGroup: /system.slice/httpd.service
           ├─ 7671 /usr/sbin/httpd -DFOREGROUND
           ├─22643 /usr/sbin/httpd -DFOREGROUND
           ├─22644 /usr/sbin/httpd -DFOREGROUND
           ├─22645 /usr/sbin/httpd -DFOREGROUND
           ├─22647 /usr/sbin/httpd -DFOREGROUND
           └─22658 /usr/sbin/httpd -DFOREGROUND

Aug 03 16:33:11 host-192-168-0-27 systemd[1]: Starting The Apache HTTP Server...
Aug 03 16:33:11 host-192-168-0-27 systemd[1]: Started The Apache HTTP Server.
Aug 07 03:38:31 centos systemd[1]: Reloaded The Apache HTTP Server.
Hint: Some lines were ellipsized, use -l to show in full.
```


## Restart your services

In this example, you will restart, stop and start the HTTPD services.

```bash
systemctl restart httpd
```

```bash
systemctl stop httpd
```

```bash
systemctl stop httpd
```


## Check list of all services enabled or disabled on boot

You can check the list of services by using the following command.

```console
[root@centos ~]# systemctl list-unit-files --type=service
UNIT FILE                                   STATE   
acpid.service                               enabled
arp-ethers.service                          disabled
auditd.service                              enabled
autovt@.service                             disabled
blk-availability.service                    disabled
brandbot.service                            static  
cloud-config.service                        enabled
cloud-final.service                         enabled
cloud-init-local.service                    enabled
cloud-init.service                          enabled
console-getty.service                       disabled
console-shell.service                       disabled
container-getty@.service                    static  
cpupower.service                            disabled
crond.service                               enabled
dbus-org.freedesktop.hostname1.service      static  
dbus-org.freedesktop.locale1.service        static  
dbus-org.freedesktop.login1.service         static  
dbus-org.freedesktop.machine1.service       static  
dbus-org.freedesktop.network1.service       invalid
dbus-org.freedesktop.NetworkManager.service enabled
dbus-org.freedesktop.nm-dispatcher.service  enabled
dbus-org.freedesktop.timedate1.service      static  
dbus.service                                static  
debug-shell.service                         disabled
dnsmasq.service                             disabled
docker.service                              enabled
dovecot.service                             enabled
dracut-cmdline.service                      static  
dracut-initqueue.service                    static  
```


You can also use the guide below for a quick conversion from SysVinit to systemd

[Conversion list](https://fedoraproject.org/wiki/SysVinit_to_Systemd_Cheatsheet)

```eval_rst
   .. title:: Service Management on CentOS 7
   .. meta::
      :title: Service Management on CentOS 7 | UKFast Documentation
      :description: Information on how to manage services on CentOS 7
```
