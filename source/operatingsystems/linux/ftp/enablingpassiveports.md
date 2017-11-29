# Enabling Passive Ports for FTP

## Opening ports on the firewall

In order to open the correct ports on the firewall, you will first have to log into MyUKFast.

Navigate to:

```path
    Products and Services >> Firewalls >> FirewallName
	
### Shared Firewalls

If you are on a Shared Firewall, navigate to the "Port Config" section and click on the "Add port" option on the Outgoing list.

Now click on the drop down and change "Port Number" to "Port Range".

Add the range of ports: 40000 - 40100.

Now click on the "Save Changes" button and this part is complete.

### Dedicated Firewalls

If you are on a Dedicated Firewall, navigate to the "Access List" page and choose the port group that you need to edit (usually "linux.ports.fromoutside.tcp")

Click on the "Add port" button at the bottom of the list.

Click the drop down and change "Port Number" to "Port Range".

Now click on the "Save Changes" button and this part is complete.


## Configuring FTP server

### cPanel Servers

The cPanel documentation site has a very good page with information on enabling passive ports on a cPanel server.

It has a guide for configuring passive ports for Pure-FTPd and ProFTPd servers.

https://documentation.cpanel.net/display/CKB/How+to+Enable+FTP+Passive+Mode


### VSFTPd

In order to configure passive mode for VSFTPd, first, you will have to set some parameters in the vsftpd.conf file that can be found in "/etc/vsftpd/".

```config
  pasv_enable=Yes
  pasv_max_port=40000
  pasv_min_port=40100
```

If you are using IPTables, you will want to add the following line to the list of rules:

```iptablesrule
  iptables -I INPUT -p tcp --destination-port 40000:40100 -j ACCEPT
```

Then, you will want to save the config with:

```bash
  service iptables restart
```

Finally, you will want to restart the FTP service by using:

```bash
  service vsftpd restart
```

```eval_rst
  .. meta::
     :title:
     :description: 
     :keywords:
