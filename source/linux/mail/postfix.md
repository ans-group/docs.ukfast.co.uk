# Postfix

## Installation

Postfix is an opensource MTA (Mail Transfer Agent). It is the standard MTA that comes installed on CentOS servers by default. It is also the MTA used by the Plesk control panel. If this is not installed on your server, this can be done with the following:

```bash
  yum install postfix
```

and then started with:

```bash
  service postfix start
```

You can set this to start when the server comes online with the following command:

```bash
  chkconfig postfix on
```

The server is now ready to send emails. You can configure your websites to connect to localhost over port 25 and they will not require any authentication.

Please ensure that you have a valid hostname and rDNS set. See [the following article for details](/linux/mail/bounces.html)

## Where are the logs

Postfix logs are generally found in `/var/log/maillog` on Plesk servers. The log will show a variety of different information including mail sent, received and authentication attempts. The logging can be modified by making changes to the Postfix configuration file found in `/etc/postfix/main.cf`.  There are a variety of different configuration changes that can be made and it would be best to refer to the official documentation which is linked at the bottom of this guide.

## Queue Manipulation

You can use the below commands via SSH to help in debugging mail issues. To view the mail queue in Postfix you will need to use the below command.

```bash
  postqueue -p
```

This will display all mails in the queue including their ID, the sender and recipient address, the time and the reason that it is in the queue. Using the ID, you can view the contents of the email and the headers by using the below command where [ID] is the ID of the email.

```bash
  postcat -q [ID]
```

This will show a lot of information regarding the email and will help in investigating possible mail compromises such as whether the mail was sent through a logged in account, which would indicate a mail account has been compromised or through a PHP script which would indicate a malicious script has been uploaded to your server.

## Clearing the Postfix mail queue

You can use two methods to clear the queue. The first method is not guaranteed to clear the mail as it will attempt to send all of the mail in the queue. You would use this method if there a lot of mails in the queue due to a network issue or a blocked port for example.

```bash
  postfix -f
```

The second method would be to delete the mails in the queue. You would do this in an event such as the server was found to be sending spam mail and the queue is full of the spam mail. Once you have stopped the spam from sending then you would want to delete the contents of the queue. To do this, you can either delete mail using a mail ID or you can delete all of the mails in the queue.

To delete a specific mail from the queue you would use the below command where [ID] is the ID of the mail you wish to delete.

```bash
  postsuper -d [ID]
```

To delete all mail in the mail queue you would use the below command.

```bash
  postsuper -d ALL
```

## Official Postfix Documentation.

If your needs require specific tweaks or configurations additions, we suggest that you use the official Postfix documentation.

<http://www.postfix.org/documentation.html>
>>>>>>> devops/ukfast-docs-external-RickD
