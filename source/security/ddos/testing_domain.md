```eval_rst
.. meta::
   :title: Testing a domain on DDoSX\ :sup:`®` | UKFast Documentation 
   :description: A guide for testing your domain on  DDoSX\ :sup:`®` before enabling DNS
```

# Testing your domain on  DDoSX\ :sup:`®`

Before using ddosx it is strongly recommended that you test your web site first. This will 
help to find issues that might have affected your users if you went live with ddosx straight away. 

### Linux
Edit the file `/etc/hosts` to include your domain and subdomains and point these to the IP that has been assigned 
to your protected domain.  
Firstly open up the Terminal and then edit the file using your file editor of choice
```
$ sudo vi /etc/hosts
```
and enter `your ddosx ip` `example.org www.example.org` at the bottom of the file then save the file. You can now browse example.org and www.example.org and you will view the website as you would through ddosx. 

<b>Note: If you currently have AAAA record for your domain or subdomains you will also need to put the ddosx IPv6 address into your `/etc/hosts` file as well as your IPv4 address to ensure your IPv6 connection goes through ddosx as well.</b>  
<b>Note: If don't have the sudo command you can also run `su -` first and enter your root password before editing `/etc/hosts` with the `vi` command as per:</b>  
```
$ su -
Password: ********
# vi /etc/hosts
```

Alternatively if you don't have root access you can use the `curl` command for example:  
IPv4:
```
$ curl -H "Host: example.org" https://<replace_with_ddosx_ip>/ -k
```
IPv6:
```
$ curl -H "Host: example.org" https://<[replace_with_ipv6_ddosx_ip]>/ -gk
```
However this will return the site in plain html and might not give you a true representative of what your site looks like through ddosx compared to loading it via your web browser.

### mac osx
You need to open up the Terminal app and then run the command
```
$ sudo nano /private/etc/hosts
```
and enter `your ddosx ip` `example.org www.example.org` at the bottom of the file then save the file. You can now browse example.org and www.example.org and you will view the website as you would through ddosx. 

<b>Note: If you currently have a AAAA record for your domain or subdomains you will also need to put the IPv6 address into your `/private/etc/hosts` file to ensure your IPv6 connection goes through ddosx as well.</b>  

### windows 7/8/10

* Right click on notepad and open as the administrator
* Select File > Open
* Browser to `C:\Windows\System32\drivers\etc`
* At the bottom right change the file type to All Files
* Open the file called hosts
* Edit this file by adding `your ddosx ip` `example.org www.example.org` and save

<b>Note: You may need to run ipconfig /flushdns after making this changed before browsing the website</b>   
<b>Note: If you currently have a AAAA record for your domain or subdomains you will also need to put the IPv6 address into your `/private/etc/hosts` file to ensure your IPv6 connection goes through ddosx as well.</b>  
