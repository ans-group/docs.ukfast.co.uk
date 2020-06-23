# Hostname

The hostname of a server is intended to provide a human readable name. Many services make use of the hostname. The mail service for example uses it to identify the server, if it's the default or wrong some mail servers may reject mail - It's important to get it right.

## View the Current Hostname

Most systems allow you to just type:

    $ hostname
    
However this may not be available in your operating system. In Centos 7 you are able to use the hostname command and:

    $ hostnamectl status
    
## What Hostname Should I Choose?

You must choose a suitable hostname for your server. If the server is only going to be used internally it may make sense just to give it a name based on its main service, for example a webserver could be named WEB. Generally people append a number on this in case they ever add extra server. If you are using a panel, you should opt for a FQDN, for example "mail.ukfast.co.uk" or "server.ukfast.co.uk" - This is due to the types of services which run on panels. Here is the requirements for setting a hostname in cPanel:

- Do **not** select a hostname that begins with www or a number, or that ends with a hyphen (-).

- The hostname **must** be a fully-qualified domain name (FQDN) that contains two periods (for example, hostname.example.com).

- Do **not** choose a hostname that that a cPanel account on your server will use.

It also notes the following:

- Do **not** select a socially-unacceptable hostname. The hostname will appear in mail headers.

- Only use lowercase letters in hostnames.


    
## Setting a New Hostname [SSH]

Different operating systems use different locations to set the hostname, if the following doesn't work it would be best to consult your individual operating systems documentation, however this should work for most.

If you use a panel on your server, it is recommended to skip this section and go to the Panel section.

Type the following on systems with the hostname binary:

    $ hostname <new-hostname>

Where <new-hostname> is the hostname you would like to use. This change is only temporary and will be written over next time you reboot. To make it permanent edit the '/etc/hostname' file with the hostname you would like to use.

Type the following on systems with the hostnamectl binary:

    $ hostnamectl set-hostname <new-hostname>
    
The next step is to check the changes were successful, this can be done by going back to the "View the Current Hostname" section.

Once you have completed this, it is recommended to also set the hosts file.

[//]: # (TODO: Create hosts article to cover general usage including on windows and mac)

```eval_rst
  .. title:: Hostnames in Linux | UKFast Documentation
  .. meta::
     :title: Hostnames in Linux | UKFast Documentation
     :description: Information on setting, viewing and using hostnames in the Linux OS
     :keywords: ukfast, linux, hostname, server, centos, cloud, virtual
