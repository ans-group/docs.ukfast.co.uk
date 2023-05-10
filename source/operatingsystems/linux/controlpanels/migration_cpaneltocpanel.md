# Performing a cPanel to cPanel Migration

A guide on performing a cPanel to cPanel Migration

```eval_rst
.. note::
   cPanel requires the ability to connect to your other cPanel server via your defined SSH port and port ``2087`` BOTH inbound and outbound.
```

To begin your migration you first need to ensure you are logged into your WHM panel.
The migration can only be started via WHM, which is the server-wide control panel, as opposed to cPanel which is the domain specific panel for your sites.

```eval_rst
.. note::
   cPanel Migrations have to be initiated from the destination cPanel server
```

Once you are logged in to WHM, use the search box in the top left under the WHM logo to search for "Transfer Tool"
Click on "Transfer Tool" to be directed to the Transfer Tool page in which you can start your migration.

![cPanel Home Transfer](files/cpanel_searchtransfertool.PNG)

Now you are within the Transfer Tool section of WHM, fill in the details accordingly for the server you want to pull your data from.

![cPanel Transfer Tool Start](files/cpanel_transfertool1.PNG)

* Remote Server Address: The IP Address of the other server
* Remote SSH Port: The port SSH is bound to on the other server
* Root Password: The password for the root user on the other server

```eval_rst
.. note::
   UKFast Linux Servers listen on port 2020 for SSH by default
```
![cPanel Transfer Tool Details](files/cpanel_transfertool1withdetails.PNG)

Once you have filled in the server details as per the above screenshot, scroll down and select the Remote Server Type
Next, click the "Scan Remote Server" button which will have the migration tool connect to the remote server and scan for migratable accounts

![cPanel Transfer Select WHM](files/cpanel_transfertool2.PNG)

When the scan completes, select the accounts you want to transfer to your server.
After selecting what you want to transfer over, click the "Copy" button to start the migration

![cPanel Select scanned sites for migration](files/cpanel_transfertoolscannedplesk.PNG)

When the migration completes you will see the following page showing that both the transfer of data and restore of the account to your server is complete.

![cPanel Transfer Success](files/cpanel_transfertoolplesksuccess.PNG)

After the migration, you can go to the "List Accounts" page in WHM and you will be able to see the account you have just transferred.

![cPanel List accounts to see the transferred site](files/cpanel_transfertoollistaccounts.PNG)

You have successfully performed a cPanel to cPanel Migration!

Before amending your DNS to point to your new server, you can test your websites using a hosts file change
You can view more information on that [here](https://portal.ans.co.uk/safedns/index.php)

```eval_rst
  .. title:: Performing a cPanel to cPanel Migration
  .. meta::
     :title: Performing a cPanel to cPanel Migration
     :description:  A guide to performing a cPanel to cPanel Migration
     :keywords: ukfast, cpanel, migration, move, website, transfer, whm
```
