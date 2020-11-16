# How to set up a Multi-Protocol VPN Server using SoftEther

```eval_rst
.. meta::
    :title: Multi-Protocol VPN Server using SoftEther | UKFast Documentation
    :description: Detailed guidance on setting up a multi-protocol VPN server using SoftEther
```

## Set up the VPN server
### Introduction
This article explains how to install and configure a multi-protocol VPN server using the SoftEther package. We enable and configure OpenVPN, L2TP over IPSec and SSTP VPN Servers on Linux.

### What is SoftEther
SoftEther VPN is one of the world's most powerful and easy-to-use multi-protocol VPN software, made by the good folks at the University of Tsukuba, Japan. It runs on Windows, Linux, Mac, FreeBSD and Solaris and is freeware and open-source. You can use SoftEther for any personal or commercial use free of charge.

### Step 1: Create a Virtual Server
First, you need to create a CentOS 7 server. As mentioned in SoftEther's website, SoftEther will work on almost every Linux distro with kernel v2.4 or above; however, it's recommended to choose one of these distributions: CentOS, Fedora, or Red Hat Enterprise Linux.

Personally I have only tried it on CentOS 7 64-bit edition, but it has worked perfectly.

### Step 2: Update your Server Software
Using the command below, update and upgrade your server software packages to the latest version:

#### Debian / Ubuntu:
```
apt-get update && apt-get upgrade
```

#### CentOS / Fedora:
```
yum upgrade
```

### Step 3: Download SoftEther
You can download the latest SoftEther server package for Linux from their website:

<http://www.softether-download.com/en.aspx>

Unfortunately, there is no repository in place for getting the latest version of SoftEther, and so we'll need to download the latest version to use from their site. Therefore, you have to browse their website using a desktop browser to download the package.

First, browse their website on your own computer and choose the appropriate Component, Platform and CPU, then find the link to the appropriate package. This will download the latest stable version (at the time of writing) for Linux x86_64:

```
wget http://www.softether-download.com/files/softether/v4.20-9608-rtm-2016.04.17-tree/Linux/SoftEther_VPN_Server/64bit_-_Intel_x64_or_AMD64/softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz
```

### Step 4: Install and Configure SoftEther
Now we have to extract the package we received from the SoftEther download page and compile it. The package used in this tutorial is named **softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz** so we will extract it using the command below:

```
tar xzvf softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz
```

After extracting it, a directory named **vpnserver** will be created in the working folder. In order to compile SoftEther, the following tools and packages must be installed on your server:

```
make, gccbinutils (gcc), libc (glibc), zlib, openssl, readline, and ncurses
```

Make sure these are installed. You can install all the packages necessary to build SoftEther using the command below:

#### Debian / Ubuntu:
```
apt-get install build-essential -y
```

#### CentOS / Fedora:
```
yum groupinstall "Development Tools"
```

```eval_rst
.. note::

    On Fedora, I have found that the gcc package doesn't get installed using the command above so you have to install it manually using ``yum install gcc``.

```

Now that we have all the necessary packages installed, we can compile SoftEther using the following commands.

First **cd** into vpnserver directory:

```
cd vpnserver
```

And now run **make** to compile SoftEther into an executable file:

```
make
```

![pic1][]

SoftEther will ask you to read and agree with its License Agreement. Select **1** to read the agreement, again to confirm read, and finally to agree to the License Agreement.

SoftEther is now compiled and made into executable files (vpnserver and vpncmd). If the process fails, check if you have all of the requirement packages installed.

Now that SoftEther is compiled we can move the **vpnserver** directory to someplace else, here we move it to **/usr/local**:

```
cd ..
mv vpnserver /usr/local
cd /usr/local/vpnserver/
```

And then change the files permission in order to protect them:

```
chmod 600 *
chmod 700 vpnserver
chmod 700 vpncmd
```

If you like SoftEther to start as a service on startup create a file named **vpnserver** in **/etc/init.d** directory a follows.

First create and open the file using vi:

```
vi /etc/init.d/vpnserver
```

And paste the following into the file:

```
#!/bin/sh
# chkconfig: 2345 99 01
# description: SoftEther VPN Server
DAEMON=/usr/local/vpnserver/vpnserver
LOCK=/var/lock/subsys/vpnserver
test -x $DAEMON || exit 0
case "$1" in
    start)
        $DAEMON start
        touch $LOCK
        ;;
    stop)
        $DAEMON stop
        rm $LOCK
        ;;
    restart)
        $DAEMON stop
        sleep 3
        $DAEMON start
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
esac
exit 0
```

Finally save and close the file by pressing **esc** and typing **:wq** to close vim.

We have to make a directory at **/var/lock/subsys** if one does not exist:

```
mkdir /var/lock/subsys
```

Now change the permission for the startup script and start **vpnserver** using command below:

```
chmod 755 /etc/init.d/vpnserver && /etc/init.d/vpnserver start
```

Use the command below make it to run at startup:

#### Debian / Ubuntu:
```
update-rc.d vpnserver defaults
```

#### CentOS / Fedora:
```
chkconfig --add vpnserver
```

SoftEther VPN Server is now installed and configured to run at startup. Finally, we have to check if the VPN server is working:

```
cd /usr/local/vpnserver
./vpncmd
```

Now press **3** to choose **Use of VPN Tools** and then type:

```
check
```

If all of the checks pass, then your server is ready to be a SoftEther VPN server and you can move on to the next step. Type **exit** to exit **VPN Tools**.

There are two ways to configure SoftEther VPN server. You can use the Windows-based server manager to manage and configure any number of SoftEther VPN servers remotely, or use the built-in **vpncmd** tool to configure your servers.

You can download SoftEther Server Manager for Windows using their website and do the configuration using the GUI that it provides, which is a preferable way if you are a Windows user.

Here we will use **vpncmd** to configure our VPN server.

### Step 5: Generate a Let's Encrypt certificate

Let's Encrypt uses a package called **certbot** which you install on the VPN server, which automates the generation of the private key, the signing and downloading of the certificate. For that to work it requires that the server be accessible from the **Let's Encrypt** service on specific ports, as shown:

```eval_rst
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
|   Plugin   | Auth | Inst |                                                                                                            Notes                                                                                                           |             Challenge            |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
|   apache   |   Y  |   Y  |                                                        Automates obtaining and installing a cert with Apache 2.4 on Debian-based distributions with libaugeas0 1.0+.                                                       |         tls-sni-01 (443)         |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
|   webroot  |   Y  |   Y  |                                                                     Obtains a cert by writing to the webroot directory of an already running webserver.                                                                    |           http-01 (80)           |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
|    nginx   |   Y  |   N  |                                                               Automates obtaining and installing a cert with Nginx. Alpha release shipped with Certbot 0.9.0.                                                              |         tls-sni-01 (443)         |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| standalone |   Y  |   Y  | Uses a “standalone” webserver to obtain a cert. Requires port 80 or 443 to be available. This is useful on systems with no webserver, or when direct integration with the local webserver is not supported or not desired. | http-01 (80) or tls-sni-01 (443) |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
|   manual   |   Y  |   N  |                                                                  Helps you obtain a cert by giving you instructions to perform domain validation yourself.                                                                 |    http-01 (80) or dns-01 (53)   |
+------------+------+------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
```

Further reading: <https://certbot.eff.org/docs/using.html>

Install the certbot package from the EPEL repository as follows:
```
yum install epel-release
yum install certbot
```

Here we'll use the `standalone` option to create a temporary web server listening on port 80. We specify the challenge type **http-01** as the SoftEther will be listening on port 443

```
certbot certonly --standalone-supported-challenges http-01 --standalone -d ##fqdn.which.points.to.your.server##
```

If certbot managed to generate and validate your certificate, then you should receive a message like the following:

```
IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/##fqdn.which.points.to.your.server##/fullchain.pem. Your cert
   will expire on 2017-01-17. To obtain a new or tweaked version of
   this certificate in the future, simply run certbot again. To
   non-interactively renew *all* of your certificates, run "certbot
   renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

Certbot will have generated a number of files now including the private key, certificate, full certificate chain, etc. and stored them in `/etc/letsencrypt/live/##fqdn.which.points.to.your.server##`

We can now add the automatic renewal command into **cron** so that the certificate will be auto-renewed before it expires. You'll need to do this yourself, but the command to renew the certificate is:

```
certbot renew --quiet
```

### Step 6: Change Admin Password

Now that you have SoftEther VPN server installed, you have to assign an administrator password in order to use with SoftEther. You can do this using **vpncmd** which is SoftEther's command line based administration tool:

```
./vpncmd
```

Press **1** to select **Management of VPN Server or VPN Bridge**, then press **Enter** without typing anything to connect to the localhost server, and again press **Enter** without inputting anything to connect to server by server admin mode.

Then use command below to set the admin password:

```
ServerPasswordSet
```

Enter and then re-type your new password. You'll need this whenever you want to change the server-wide options, like the IPSEC PSK

### Step 7: Create A Virtual Hub

To use SoftEther we must first create a Virtual Hub. Here as an example we create a hub named **VPN**, in order to do that enter command below in the **vpncmd** tool:

```
HubCreate VPN
```

Next you will be asked to enter an **administrator password** for the hub. This password will be used whenever you are not logged in as **server admin** mode, and you want to manage that specific hub.

Now select the Virtual Hub you created using this command:

```
Hub VPN
```

### Step 8: Enable SecureNAT

There are two ways of connecting your hubs to the server network:
*  using a **Local Bridge** connection
*  using the **SecureNAT** function.

You can use each one separately, but using these two together will cause problems.

Here we use **SecureNAT**, which is very easy to setup and works pretty well in most situations. You could also use Local Bridge mode, but then you have to install and configure a DHCP Server too.

SecureNAT is a combination of Virtual NAT and DHCP Server function. By default, it will allocate the VPN clients from the subnet `192.168.30.0/24`, although this can be configured.

You can enable SecureNAT using the command below:

```
SecureNatEnable
```

If you require **split routing**, whereby all VPN client traffic will not be forced over the VPN, set the ```/GW:none``` option in the **DhcpSet** command. Unfortunately, you need to specify the full DHCP configuration again, so get the current values using DhcpGet first. Here's an example:

```
DhcpSet /START:192.168.30.10 /END:192.168.30.10 /MASK:192.168.30.10 /EXPIRE:7200 /GW:none /DNS:192.168.30.1 /DNS2:8.8.8.8 /DOMAIN:none /LOG:yes /PUSHROUTE:none
```

### Step 9: Create and Manage Users

Now we have to create users for our **Virtual Hub** to use the VPN. We can create users for our Virtual Hub using the command **UserCreate** and view the list of current users by using **UserList**. Users can be added to groups and can even have different types of authentication modes (including: Password, Certificate, RADIUS, NTLM, etc.).

By using command UserCreate we create a user named "test":
```
UserCreate test
```

The default type of authentication is **Password** but we can change it to a different type using commands below:
* ```UserNTLMSet``` for NT Domain Authentication
* ```UserPasswordSet``` for Password Authentication
* ```UserAnonymousSet``` for Anonymous Authentication
* ```UserRadiusSet``` for RADIUS Authentication
* ```UserCertSet``` for Individual Certificate Authentication
* ```UserSignedSet``` for Signed Certificate Authentication

In this tutorial we use Password as the user authentication mode for our **test** user, so using this command set a password for user test:
```
UserPasswordSet test
```

### Step 10: Setup L2TP/IPSec

To enable L2TP/IPsec VPN server you can use the command below:
```
IPsecEnable
```

After entering this command, you will be asked to configure the L2TP server functions:
*  **Enable L2TP over IPsec Server Function**: Choose yes to enable L2TP VPN over IPSec with pre-shared key encryption. Now you can make VPN connections to this server using iPhone, Android, Windows, and Mac OS X devices.
*  **Enable Raw L2TP Server Function**: This will enable L2TP VPN for clients with no IPSec encryption.
*  **Enable EtherIP / L2TPv3 over IPsec Server Function**: Routers which are compatible with EtherIP / L2TPv3 over IPsec can connect to this server by enabling this function.
*  **Pre Shared Key for IPsec**: Enter a pre-shared key to use with L2TP VPN.
*  **Default Virtual HUB in a case of omitting the HUB on the Username**: Users can specify the Virtual Hub they are trying to connect to by using **Username@TargetHubName** as their username when connecting. This option specifies which Virtual Hub to be used if the user does not provide such information. In our case enter **VPN**.

### Step 11: Setup SSTP/OpenVPN
The SoftEther can clone the functions of Microsoft SSTP VPN Server and OpenVPN Server. But before we enable these we have to import the SSL certificate and key from **Let's Encrypt**.

Here we use SoftEther's ServerCertSet command to point it to the SSL certificate and key for our server. Change the `##fqdn.which.points.to.your.server##` to the FQDN which you provided to Let's Encrypt's certbot tool, which should be the same one which points to your VPN server. It's imperative that it matches the one you will use long-term
```
ServerCertSet /LOADCERT:/etc/letsencrypt/live/##fqdn.which.points.to.your.server##/fullchain.pem /LOADKEY:/etc/letsencrypt/live/##fqdn.which.points.to.your.server##/privkey.pem
```

```eval_rst
.. note::

   SoftEther also comes with a built-in ``Dynamic DNS`` function, which can assign a unique and permanent hostname for your server. You can use the hostname assigned by this function for creating a SSL Certificate and connecting to your server.

```

```eval_rst
.. note::

   If you already have a SSL certificate or you have created one using ``openssl``, it can be added to the server using the command ``ServerCertSet`` as shown above, changing the paths to match where your files are.

```

Now that we have created and registered a SSL Certificate for our server, we can enable SSTP function with this command:
```
SstpEnable yes
```

And to enable OpenVPN:
```
OpenVpnEnable yes /PORTS:1194
```

* Note: OpenVPN's default port is 1194, but you can change it to any port you want by changing the ```/PORTS:1194``` part of the command above to your desired port or ports (yes it supports multiple ports).

After you enabled OpenVPN, you can download a sample configuration file for OpenVPN client. Here we create a sample OpenVPN configuration file and save it to **my_openvpn_config.zip**:
```
OpenVpnMakeConfig ~/my_openvpn_config.zip
```

Then you can download it using any SFTP client such as FileZilla and apply it to your OpenVPN clients.

SoftEther also provides a dedicated VPN Client software for both Windows and Linux. It supports a SoftEther specific protocol called **Ethernet over HTTPS** or **SSL-VPN** which is very powerful. It uses HTTPS protocol and port 443 in order to establish a VPN tunnel, and because this port is well-known, almost all firewalls, proxy servers and NATs can pass the packet. In order to use SSL-VPN protocol, you must download and install SoftEther VPN Client, which can be obtained from their website.

Alternatively, and what we'll do here, you can use the built-in VPN capabilities of Windows 7 or above.

### Step 12: Set up IP Forwarding
We have to query the sysctl kernel value ```net.ipv4.ip_forward``` to see if forwarding is enabled or not
```
sysctl net.ipv4.ip_forward
```

If it's not currently enabled, the output should be as follows. If the output is **1** then it is already enabled
```
net.ipv4.ip_forward = 0
```

Now edit the file ```/etc/sysctl.conf``` and add the following line:
```
net.ipv4.ip_forward = 1
```

Apply the configuration with the following command
```
sysctl -p
```

## Set up the VPN connection in Windows 7
### Step 1: Open Network and Sharing Center
Start by finding the network connections icon in the bottom right corner of the screen (near the clock). The icon can be in the shape of computer display or wireless signal meter. Right click on that icon.

![pic2][]

Select **Open Network and Sharing Center**. You can also get there by going through ```Start button``` > ```Control Panel``` > ```View network status and tasks```.

![pic3][]

### Step 2: Set up a new connection or network
Click **Set up a new connection or network**.

![pic4][]

### Step 3: Connect to a workplace
In the appeared window select **Connect to a workplace**, click **Next**.

![pic5][]

### Step 4: Set as VPN
Click **Use my Internet connection (VPN)**.

![pic6][]

### Step 5: Specify the VPN Server
**Internet address** is your server's FQDN which was used in ***Step 5 of "Set up the VPN server"***. It is not ```openstackvpn.calv.tk```, that is just an example. **Destination name** can be anything you like, for example OpenStack VPN.

Check **Don't connect now; just set it up so I can connect later** and click **Next**.

![pic7][]

### Step 6: Enter login credentials
Fill the **User name** and **Password** fields. In the ***Step 9 of "Set up the VPN server"*** we created the user **test**, so enter those details (or the ones you used instead). Check **Remember this password** and click **Create**.

![pic8][]

### Step 7: Create the connection
Click **Close**.

![pic9][]

### Step 8: Find the new connection
Click **Change adapter settings**.

![pic10][]

### Step 9: Enter connection properties
In the connections list find the **OpenStack VPN** connection, the description should be **WAN Miniport (IKEv2)**. Right click on it and select **Properties**.

![pic11][]

### Step 10: Set advanced options
Click **Security** tab, for **Type of VPN** select **Secure Socket Tunneling Protocol (SSTP)**. For **Data encryption** select **Require encryption (disconnect if server declines)**. Click **Advanced settings**. For **Authentication** select **Unencrypted password (PAP)** and **Microsoft CHAP Version 2 (MS-CHAP v2)**. Then click **OK**

![pic12][]

### Step 11: Start the VPN connection
Double click on the **OpenStack VPN** connection icon, or whatever you called yours.

![pic13][]

### Step 12: Verify / enter login details
It will show the connection window. Check **Save this user name and password for the following users** and leave **Me only** selected. Click **Connect** button.

![pic14][]

### Step 13: Check you're connected
After a few seconds it will connect and show you **Connected** status. You can also check the VPN status in the Network applet (the icon in your system tray at the bottom right). Click on that icon and you will see the connection list and their statuses.

![pic15][]

## Further Reading
*   <https://www.digitalocean.com/community/tutorials/how-to-setup-a-multi-protocol-vpn-server-using-softether>
*   <http://www.softether.org/4-docs/1-manual/3._SoftEther_VPN_Server_Manual>
*   <http://www.softether.org/4-docs/1-manual/7._Installing_SoftEther_VPN_Server>
* <http://www.softether.org/4-docs/2-howto/9.L2TPIPsec_Setup_Guide_for_SoftEther_VPN_Server/4.Windows_L2TP_Client_Setup>
* <https://letsencrypt.org/getting-started/>
* <http://www.ducea.com/2006/08/01/how-to-enable-ip-forwarding-in-linux/>

[pic1]: files/install_softether_vpn_server-1.png
[pic2]: files/install_softether_vpn_server-2.png
[pic3]: files/install_softether_vpn_server-3.png
[pic4]: files/install_softether_vpn_server-4.png
[pic5]: files/install_softether_vpn_server-5.png
[pic6]: files/install_softether_vpn_server-6.png
[pic7]: files/install_softether_vpn_server-7.png
[pic8]: files/install_softether_vpn_server-8.png
[pic9]: files/install_softether_vpn_server-9.png
[pic10]: files/install_softether_vpn_server-10.png
[pic11]: files/install_softether_vpn_server-11.png
[pic12]: files/install_softether_vpn_server-12.png
[pic13]: files/install_softether_vpn_server-13.png
[pic14]: files/install_softether_vpn_server-14.png
[pic15]: files/install_softether_vpn_server-15.png

```eval_rst
  .. title:: How to set up a Multi-Protocol VPN Server using SoftEther
  .. meta::
     :title: How to set up a Multi-Protocol VPN Server using SoftEther | UKFast Documentation
     :description: A guide to setting up a VPN server using SoftEther
     :keywords: ukfast, vpn, softether, multi, protocol, server, security
