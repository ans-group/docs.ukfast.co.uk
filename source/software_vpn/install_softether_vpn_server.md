#How to set up a Multi-Protocol VPN Server using SoftEther
##Set up the VPN server
###Introduction
This article explains how to install and configure a multi-protocol VPN server using the SoftEther package. We enable and configure OpenVPN, L2TP over IPSec and SSTP VPN Servers on Linux.

###What is SoftEther
SoftEther VPN is one of the world's most powerful and easy-to-use multi-protocol VPN software, made by the good folks at the University of Tsukuba, Japan. It runs on Windows, Linux, Mac, FreeBSD and Solaris and is freeware and open-source. You can use SoftEther for any personal or commercial use free of charge.

###Step 1: Create a Virtual Server
First, you need to create a CentOS 7 server. As mentioned in SoftEther's website, SoftEther will work on almost every Linux distro with kernel v2.4 or above; however, it's recommended to choose one of these distributions: CentOS, Fedora, or Red Hat Enterprise Linux.

Personally I have only tried it on CentOS 7 64-bit edition, but it has worked perfectly.

###Step 2: Update your Server Software
Using the command below, update and upgrade your server software packages to the latest version:

####Debian / Ubuntu:
```bash
apt-get update && apt-get upgrade
```

####CentOS / Fedora:
```bash
yum upgrade
```

###Step 3: Download SoftEther
You can download the latest SoftEther server package for Linux from their website:

http://www.softether-download.com/en.aspx

Unfortunately, there is no repository in place for getting the latest version of SoftEther, and so we’ll need to download the latest version to use from their site. Therefore, you have to browse their website using a desktop browser to download the package.

First, browse their website on your own computer and choose the appropriate Component, Platform and CPU, then find the link to the appropriate package. This will download the latest stable version (at the time of writing) for Linux x86_64:

```bash
wget http://www.softether-download.com/files/softether/v4.20-9608-rtm-2016.04.17-tree/Linux/SoftEther_VPN_Server/64bit_-_Intel_x64_or_AMD64/softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz
```

###Step 4: Install and Configure SoftEther
Now we have to extract the package we received from the SoftEther download page and compile it. The package used in this tutorial is named **softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz** so we will extract it using the command below:

```bash
tar xzvf softether-vpnserver-v4.20-9608-rtm-2016.04.17-linux-x64-64bit.tar.gz
```

After extracting it, a directory named **vpnserver** will be created in the working folder. In order to compile SoftEther, the following tools and packages must be installed on your server:

> make, gccbinutils (gcc), libc (glibc), zlib, openssl, readline, and ncurses

Make sure these are installed. You can install all the packages necessary to build SoftEther using the command below:

####Debian / Ubuntu:
```bash
apt-get install build-essential -y
```

####CentOS / Fedora:
```bash
yum groupinstall "Development Tools"
```

> Note: On Fedora, I have found that the gcc package doesn't get installed using the command above so you have to install it manually using `yum install gcc`.

Now that we have all the necessary packages installed, we can compile SoftEther using the following commands.

First **cd** into vpnserver directory:

```bash
cd vpnserver
```

And now run **make** to compile SoftEther into an executable file:

```bash
make
```

SoftEther will ask you to read and agree with its License Agreement. Select **1** to read the agreement, again to confirm read, and finally to agree to the License Agreement.

SoftEther is now compiled and made into executable files (vpnserver and vpncmd). If the process fails, check if you have all of the requirement packages installed.

Now that SoftEther is compiled we can move the **vpnserver** directory to someplace else, here we move it to **/usr/local**:

```bash
cd ..
mv vpnserver /usr/local
cd /usr/local/vpnserver/
```

And then change the files permission in order to protect them:

```bash
chmod 600 *
chmod 700 vpnserver
chmod 700 vpncmd
```

If you like SoftEther to start as a service on startup create a file named **vpnserver** in **/etc/init.d** directory a follows.

First create and open the file using vi:	

```bash
vi /etc/init.d/vpnserver
```

And paste the following into the file:

```bash
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

```bash
mkdir /var/lock/subsys
```

Now change the permission for the startup script and start **vpnserver** using command below:

```bash
chmod 755 /etc/init.d/vpnserver && /etc/init.d/vpnserver start
```

Use the command below make it to run at startup:

####Debian / Ubuntu:
```bash
update-rc.d vpnserver defaults
```

####CentOS / Fedora:
```bash
chkconfig --add vpnserver 
```

SoftEther VPN Server is now installed and configured to run at startup. Finally, we have to check if the VPN server is working:

```bash
cd /usr/local/vpnserver
./vpncmd
```

Now press **3** to choose **Use of VPN Tools** and then type:

```bash
check
```

If all of the checks pass, then your server is ready to be a SoftEther VPN server and you can move on to the next step. Type **exit** to exit **VPN Tools**.

There are two ways to configure SoftEther VPN server. You can use the Windows-based server manager to manage and configure any number of SoftEther VPN servers remotely, or use the built-in **vpncmd** tool to configure your servers.

You can download SoftEther Server Manager for Windows using their website and do the configuration using the GUI that it provides, which is a preferable way if you are a Windows user.

Here we will use **vpncmd** to configure our VPN server.

###Step 5: Generate a Let’s Encrypt certificate

Let’s Encrypt uses a package called **certbot** which you install on the VPN server, which automates the generation of the private key, the signing and downloading of the certificate. For that to work it requires that the server be accessible from the **Let’s Encrypt** service on specific ports, as shown:

| Plugin | Auth | Inst | Notes | Challenge types (and port) |
| --- | --- | --- | --- | --- |
| apache | Y | Y | Automates obtaining and installing a cert with Apache 2.4 on Debian-based distributions with libaugeas0 1.0+. | tls-sni-01 (443) |
| webroot | Y | N | Obtains a cert by writing to the webroot directory of an already running webserver. | http-01 (80) |
| nginx | Y |	Y | Automates obtaining and installing a cert with Nginx. Alpha release shipped with Certbot 0.9.0. | tls-sni-01 (443) |
| standalone | Y | N | Uses a “standalone” webserver to obtain a cert. Requires port 80 or 443 to be available. This is useful on systems with no webserver, or when direct integration with the local webserver is not supported or not desired. | http-01 (80) or tls-sni-01 (443) |
| manual | Y | N | Helps you obtain a cert by giving you instructions to perform domain validation yourself. | http-01 (80) or dns-01 (53) |


