# Configuring FTP passive mode

If you're having problems connecting to your server using FTP, and you are seeing any errors like the following examples, you may need to configure your server and firewall to correctly use FTP passive mode.

If you see an error similar to this, it's likely you need to set up passive ports:
```console
  Response:   227 Entering Passive Mode (123,123,123,123,174,209)
  Command:    MLSD
  Error:  Failed to retrieve directory listing
```

If you see an error similar to this, then your server is likely behind a firewall with NAT configuration, and you need to set up a Masquerade Address on your FTP server:
```console
"Server sent passive reply with unroutable address. Using server address instead."
```

How to do this is slightly different depending on what type of server you have, so we'll cover the most common ones here. In our examples we set up a range of 40000 to 40100.

## On WHM/cPanel servers

WHM/cPanel comes with two possible FTP servers built in, and the configuration is slightly different on each. To find out which one your server is using, log into WHM and navigate to  Home >> Service Configuration >> FTP Server Selection. You'll see either ProFTPD or Pure-FTPd selected.

For more information please do check out the [Official guide](https://documentation.cpanel.net/display/CKB/How+to+Enable+FTP+Passive+Mode).

### Pure-FTPd

- Log in via SSH and open the configuration file /var/cpanel/conf/pureftpd/local. If this file does not exist, create it.
- Add this line to set which ports your server should use.
```console
PassivePorts: 40000 40100
```
- If your server is behind a firewall and you are seeing unroutable address errors, add the following line, replacing 123.123.123.123 with your server's public IP:  
```console
  MasqueradeAddress: 123.123.123.123
```
- Restart PureFTP by running
```console
  /usr/local/cpanel/scripts/setupftpserver proftpd --force
```
- Allow inbound connections on the passive port range you selected to your server in your firewall.

### ProFTPd

- Log in via SSH and open the configuration file /var/cpanel/conf/proftpd/local. If this file does not exist, create it.
- Add this line to set which ports your server should use.
```console
  PassivePortRange: 40000 40100
```
- If your server is behind a firewall and you are seeing unroutable address errors, add the following line, replacing 123.123.123.123 with your server's public IP:  
```console
  ForcePassiveIP: 123.123.123.123
```
- Restart PureFTP by running
```console
  /usr/local/cpanel/scripts/setupftpserver pure-ftpd --force
```
- Allow inbound connections on the passive port range you selected to your server in your firewall.


## On Plesk servers

Plesk also uses the ProFTPd server, but the configuration is slightly different. For more information please do refer to the [official guide for Plesk](https://support.plesk.com/hc/en-us/articles/213902285-How-to-configure-passive-ports-range-for-ProFTPd-on-a-server-behind-a-firewall-).

- Log in via SSH, then followed the guide for your version of Plesk:

#### Plesk Onyx:
- Edit/create the file /etc/proftpd.d/55-passive-ports.conf
- Add the following configuration the that file:
```console
<Global>
PassivePorts 40000 40100
</Global>
```
- Restart the FTP service to pick up the changes:
```console
systemctl restart xinetd
```
- Allow inbound connections on the passive port range you selected to your server in your firewall.

#### Plesk 12.5 and older:
- Edit the file /etc/proftpd.conf
- Look for the existing <Global> tags, and add your port range in between them:
```console
<Global>
PassivePorts 40000 40100
</Global>
```
- Restart the FTP service to pick up the changes:
```console
systemctl restart xinetd
```
- Allow inbound connections on the passive port range you selected to your server in your firewall.

### Unroutable Address on Plesk

- If your server is behind a firewall and you are seeing unroutable address errors, look to see if that configuration already exists anywhere on your server:
```console
  grep -r Masq /etc/proftpd*
```
- Edit whichever file has this directive, and replace the IP with your server's public IP. If the MasqueradeAddress directive isn't found, add it in.
```console
  MasqueradeAddress: 123.123.123.123
```
- Restart the FTP service to pick up the changes:
```console
systemctl restart xinetd
```

## Opening ports on your firewall

If you are a UKFast customer, and you're not sure about how to open ports on your firewall, please do refer to our other guides on [how to manage your firewall](/security/firewalls/).

If you use any software firewalls, such as CSF, Plesk Firewall, IPtables, or firewalld, you'll need to make sure your passive port range is not blocked there either.

```eval_rst
  .. meta::
     :title: FTP Passive Configuration
     :description: A guide on how to set up FTP passive mode on your server
     :keywords: linux, ftp, transfer, file, protocol, passive, mode, plesk, cpanel, whm
```
