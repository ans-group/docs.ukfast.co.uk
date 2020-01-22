# Creating An FTP Account In cPanel

You might need to create FTP accounts in cPanel, so that you and/or your developers can upload and download content from your website.  

In order to do this, start by logging into the cPanel account that you want to create the FTP account for. [You can find our guide on this here!](cpanel_connect.md)  

Now, navigate to:
```
Files >> FTP Accounts
```

You will be looking at this page:

![ImageToShowFTPAccountPage](LinkGoesHere)

Firstly, choose and input a username and password for your account.

The next box is for "Quota". This determines how much bandwidth the FTP account can use. By default, this can be left as unlimited.

The last box is "Directory". Unless the account you're adding should only be allowed to access a specific subdirectory of the site, this can be left as `public_html`

Now you can click "Create"