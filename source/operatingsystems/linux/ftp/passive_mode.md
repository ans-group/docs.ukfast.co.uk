# Configuring FTP passive mode

This guide will help you configure your server and firewall correctly in order to connect using FTP passive mode.

If you see an error similar to this when trying to connect to your server via FTP, it's likely you need to set up passive ports:

```console
Response:   227 Entering Passive Mode (123,123,123,123,174,209)
Command:    MLSD
Error:  Failed to retrieve directory listing
```

If you see an error similar to this, then your server is likely behind a firewall with NAT configuration, and you need to set up a `Masquerade Address` on your FTP server:

```console
"Server sent passive reply with unroutable address. Using server address instead."
```

The steps to set this up differ depending on your server, so below you will find guides based on some common server types. These examples are based upon setting up a range of 40000 to 40100.

## WHM/cPanel servers

WHM / cPanel comes with two possible FTP servers built in, and the configuration is slightly different on each. To find out which one your server is using, log into WHM and navigate to `Home >> Service Configuration >> FTP Server Selection`. You'll see either `ProFTPD` or `Pure-FTPd` selected.

For more information please do check out the [official cPanel guide](https://documentation.cpanel.net/display/CKB/How+to+Enable+FTP+Passive+Mode).

### Pure-FTPd

- Log in via SSH and open the configuration file `/var/cpanel/conf/pureftpd/local`. If this file does not exist, then create it.
- Add this line to set which ports your server should use.

```console
  PassivePortRange: 40000 40100
```

- If your server is behind a firewall and you are seeing unroutable address errors, add the following line, replacing `123.123.123.123` with your server's public IP:

```console
  ForcePassiveIP: 123.123.123.123
```

- Restart `Pure-FTPd` by running:

```console
  /usr/local/cpanel/scripts/setupftpserver pure-ftpd --force
```

- On your firewall, allow inbound connections on the passive port range you selected (in our example `40000` to `40100`).  If necessary please read our [guide on opening firewall ports](/network/firewalls/index).


### ProFTPD

- Log in via SSH and open the configuration file `/var/cpanel/conf/proftpd/local`. If this file does not exist, then create it.
- Add this line to set which ports your server should use.

```console
PassivePorts: 40000 40100
```

- If your server is behind a firewall and you are seeing unroutable address errors, add the following line, replacing `123.123.123.123` with your server's public IP:

```console
MasqueradeAddress: 123.123.123.123
```

- Restart ProFTPD by running:

```console
/usr/local/cpanel/scripts/setupftpserver proftpd --force
```

- On your firewall, allow inbound connections on the passive port range you selected (in our example `40000` to `40100`).  If necessary please read our [guide on opening firewall ports](/network/firewalls/index).

## Plesk servers

Plesk also uses the ProFTPD server, but the configuration is slightly different. For more information please do refer to the [official guide for Plesk](https://support.plesk.com/hc/en-us/articles/213902285-How-to-configure-passive-ports-range-for-ProFTPd-on-a-server-behind-a-firewall-).

- Log in via SSH, then followed the guide for your version of Plesk:

#### Plesk Onyx:

- Edit/create the file `/etc/proftpd.d/55-passive-ports.conf`
- Add the following configuration this file:

```console
<Global>
PassivePorts 40000 40100
</Global>
```

- Restart the FTP service to pick up the changes:

```console
systemctl restart xinetd
```

- On your firewall, allow inbound connections on the passive port range you selected (in our example `40000` to `40100`).  If necessary please read our [guide on opening firewall ports](/network/firewalls/index).

#### Plesk 12.5 and older:

- Edit the file `/etc/proftpd.conf`
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

- On your firewall, allow inbound connections on the passive port range you selected (in our example `40000` to `40100`).  If necessary please read our [guide on opening firewall ports](/network/firewalls/index).

### Unroutable Address on Plesk

- If your server is behind a firewall and you are seeing unroutable address errors, look to see if that configuration already exists anywhere on your server:

```console
grep -r Masq /etc/proftpd*
```

- Edit whichever file has this directive, and replace the IP with your server's public IP. If the `MasqueradeAddress` directive isn't found, add it in.

```console
MasqueradeAddress: 123.123.123.123
```

- Restart the FTP service to pick up the changes:

```console
systemctl restart xinetd
```

## Opening ports on your firewall

If you are a UKFast customer and you're not sure about how to open ports or manage other aspects of your firewall configuration, please do refer to our other guides on [managing your firewall](/network/firewalls/index).

If you use any software firewalls, such as CSF, Plesk Firewall, IPTables, or firewalld, you'll need to make sure your passive port range is not blocked there either.

```eval_rst
   .. title:: FTP Passive Configuration
   .. meta::
      :title: FTP Passive Configuration | UKFast Documentation
      :description: A guide on how to set up FTP passive mode on your server
      :keywords: linux, ftp, transfer, file, protocol, passive, mode, plesk, cpanel, whm, ukfast
```
