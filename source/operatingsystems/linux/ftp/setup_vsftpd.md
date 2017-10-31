# vsftpd

## What is vsftpd?

vsftpd stands for Very Secure File Transfer Protocol Daemon and is a Linux FTP server application. It is much more secure than regular FTP due to the use of encryption.

On most servers, the default port for connecting to vsftpd is port 21. 

The vsftpd service will allow you to access the files on your server using an FTP client such as FileZilla.

## Add users for ftp usage

In order to create an account for FTP usage, you will first have to create a user for them on the server. You can do this by using the "useradd" command, then specifying the name of the user, as shown below:

```bash
  useradd guest
```

Now that you have created a user, you will want to make the account secure by adding a password. You can do this with the "passwd" command:

```bash
  passwd guest
```

## Add attributes to the user

In order to allow the user that you have created the correct permissions to use FTP, you will want to use the "usermod" command in order to edit its attributes. The command below disables SSH access to your for the specified user:

```bash
  usermod -s /sbin/nologin guest
```
Note, you can also achieve this by editing the "/etc/passwd" file.

## vsftpd configuration

Once you have made the attribute changes to the user, you will want to edit the vsftpd config file. The file that needs editing is `/etc/vsftpd/vsftpd.conf` file. 

The below configuration was tested with CentOS 7 and will need to be added to the vsfrpd configuration file.


```console
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
anonymous_enable=NO
chroot_local_user=YES
rsa_cert_file=/etc/ssl/private/vsftpd.pem
rsa_private_key_file=/etc/ssl/private/vsftpd.pem
ssl_enable=YES
allow_anon_ssl=NO
force_local_data_ssl=YES
force_local_logins_ssl=YES
ssl_tlsv1=YES
ssl_sslv2=NO
ssl_sslv3=NO
require_ssl_reuse=NO
ssl_ciphers=HIGH
pasv_enable=YES
pasv_min_port=8443
pasv_max_port=8443
allow_writeable_chroot=YES
```
