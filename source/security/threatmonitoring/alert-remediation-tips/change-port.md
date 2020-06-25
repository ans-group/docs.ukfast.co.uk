# Changing common service ports

Most attacks are automated, utilising specially crafted scripts that crawl the internet looking for servers to attack. These scripts aim to find as many servers as possible and attack as many servers as possible in an attempt to find an insecure server that it can exploit. An effective way to prevent an attack from most of these scripts is to change the port that services like SSH and FTP use. This will stop all but the most advanced scripts. This can be a useful solution where IP Allow listing or a VPN is not an option.

Please note that changing service ports will not stop all brute force and exploit attacks, more advanced attackers and scripts utilise tools like Nmap, which can easily identify the ports for services, even when they have been changed from the defaults.

Feel free to follow the below steps to change the port for common services. If you do change your SSH or RDP port, please let UKfast know so we can update our database to ensure we can still provide support.

### SSH

Edit the file /etc/ssh/sshd_config using your prefered file editor.

`vi /etc/ssh/sshd_config`

Edit the following line

`# Port 2020`

Change it to the below, removing the hash and replacing [PORT] for your new SSH port.

`Port [PORT]`

Save the file.

Restart the sshd service with the below command.

`service sshd restart`

### FTP (ProFTPd)

Edit the file `/etc/proftpd.conf` with your preferred text editor.

`vi /etc/proftpd.conf`

Find the line `Port`. If it is commented out (prepended with a hash `#`) then remove the comment (hash `#`) and specify your port. If the line does not exist, you can create it by adding it to the bottom of the file.

For example:

`Port 321`

Save the file.

Restart the proftpd service
`$ /etc/init.d/proftpd restart`

### FTP (vsftpd)

Edit the file `/etc/vsftpd.conf` with your perfered text editor. Please note in some distrubutions this file is located at `/etc/vsftpd/vsftpd.conf`.

`vi /etc/vsftpd.conf`

Find the line `listen_port`. If it is commented out (prepended with a hash `#`) then remove the comment (hash `#`) and specify your port. If the line does not exist, you can create it by adding it to the bottom of the file.

For example:

`listen_port=321`

Save the file.

Restart the vsftpd service
`bash$ /etc/init.d/vsftpd restart`

### FTP (pure-ftpd/CPanel)

Pure-ftpd is commonly used on servers with CPanel, the below steps are for a server with CPanel, but they may apply to servers without Cpanel too, your mileage may vary.

Edit the file `/etc/chkserv.d/ftpd` with your preferred text editor.

`vi /etc/chkserv.d/ftpd`

This file will contain 1 line, this line is used to sell the server how to start the service. We can edit the port here. You can specify your port by replacing the current port with yours, this should be the number after the first `=` in the file. See below for an example.

Original:

`service[ftpd]=21,`

Modified:

`service[ftpd]=321,`

Save the file.

Restart the pure-ftpd service

`/etc/init.d/pure-ftpd restart`

Restart the cpanel service

`/etc/init.d/cpanel restart`

```eval_rst
.. meta::
     :title: Change service ports | UKFast Documentation
     :description: Useful threat remediation and prevention tips
     :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, UKFast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrustion detection, set up
