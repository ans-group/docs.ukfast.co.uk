# Testing your domain on DDoSX

Before using DDoSX it is strongly recommended that you test your web site first. This will
help to find issues that might have affected your users if you went live with DDoSX straight away.

### Linux

Edit the file `/etc/hosts` to include your domain and subdomains and point these to the IP that has been assigned to your protected domain.

Firstly open up the Terminal and then edit the file using your file editor of choice

```console
sudo vi /etc/hosts
```

Enter `your DDoSX IP` `example.org www.example.org` at the bottom of the file then save the file. You can now browse `example.org` and `www.example.org` and you will view the website as you would through ddosx.

```eval_rst
.. note::
   If you currently have AAAA record for your domain or subdomains you will also need to put the DDoSX IPv6 address into your ``/etc/hosts`` file as well as your IPv4 address to ensure your IPv6 connection goes through DDoSX as well.
```

```eval_rst
.. note::
   If don't have the sudo command you can also run ``su -`` first and enter your root password before editing ``/etc/hosts`` with the ``vi`` command as per:
```

```console
su -
```

```console
Password: ********
```

```console
vi /etc/hosts
```

Alternatively if you don't have root access you can use the `curl` command for example:

IPv4:
```console
curl -H "Host: example.org" https://<replace_with_ddosx_ip>/ -k
```

IPv6:
```console
curl -H "Host: example.org" https://<replace_with_ipv6_ddosx_ip>/ -gk
```

However this will return the site in plain HTML and might not give you a true representative of what your site looks like through DDoSX compared to loading it via your web browser.

### macOS

You need to open up the Terminal app and then run the command

```console
sudo nano /private/etc/hosts
```

Enter `your DDoSX IP` `example.org www.example.org` at the bottom of the file then save the file. You can now browse example.org and www.example.org and you will view the website as you would through DDoSX.

```eval_rst
.. note::
   If you currently have a AAAA record for your domain or subdomains you will also need to put the IPv6 address into your ``/private/etc/hosts`` file to ensure your IPv6 connection goes through DDoSX as well.
```

### Windows 7/8/10

* Right click on Notepad and click Run As Administrator
* Select File > Open
* Browser to `C:\Windows\System32\drivers\etc`
* At the bottom right change the file type to All Files
* Open the file called hosts
* Edit this file by adding `your DDoSX IP` `example.org www.example.org` and save. For example:

```console
1.2.3.4 example.org www.example.org
```

```eval_rst
.. note::
   You may need to run ``ipconfig /flushdns`` after making this changed before browsing the website.
```

```eval_rst
.. note::
   If you currently have a AAAA record for your domain or subdomains you will also need to put the IPv6 address into your ``/private/etc/hosts`` file to ensure your IPv6 connection goes through DDoSX as well.
```

```eval_rst
  .. title:: Testing a domain on DDoSX
  .. meta::
    :title: Testing a domain on DDoSX | UKFast Documentation
    :description: A guide for testing your domain on  DDoSX before enabling DNS
```
