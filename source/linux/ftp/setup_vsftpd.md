# vsftpd

## What is vsftpd?

vsftpd is a linux FTP server application. It runs on port 21 on most servers by default but you can also have FTPS enabled.

This service will allow you to access your filesystem using an FTP client like FileZilla.

## Add users for ftp usage

You can use the commands below to add the users and the passwords.

```bash
  useradd guest
```

```bash
  passwd guest
```


## Add attributes to the user

The users can be modified either through `/etc/passwd` or you can add attributes using the usermod command. The command below will disable SSH access for your user.

```bash
  usermod -s /sbin/nologin guest
```


## vsftpd configuration

Once you have applied the changes, you can set up the vsftpd configuration. The config below is going to be added into the `/etc/vsftpd/vsftpd.conf` at the bottom. This was tested with CentOS 7.


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
