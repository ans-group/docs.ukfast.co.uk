# EXIM mail transfer agent

Exim is an open source mail transfer agent. It is most commonly found on Web Host Monitor (WHM) /cPanel servers. You can configure Exim through the command line or through the cPanel itself. The guide below focuses on ways to configure Exim and the various ways you can parse logs.

## Where are the logs?

Exim logs are generally found in `/var/log/exim_mainlog` on cPanel servers. This can be modified by making changes to the Exim configuration file found in `/etc/exim.conf`. The variable that can be changed is shown below.

```console
  log_file_path = /var/log/$primary_hostname/exim_%slog
```

## Changing logging parameters.

To get more information out of the logs, you can change the parameters to add or remove information that is logged by Exim for mails that are delivered and received by your server. The variable is called the log_selector. You can modify it in the `/etc/exim.conf` file.

```console
  log_selector = +arguments -retry_defer
```

Here are some of the optional log items.

```console
        acl_warn_skipped             skipped warn statement in ACL
        arguments                    command line arguments
        connection_reject            connection rejections
        delay_delivery               immediate delivery delayed
        deliver_time                 time taken to perform delivery
        delivery_size                add S=nnn to => lines
        ident_timeout                timeout for ident connection
        incoming_interface           local interface on <= and => lines
        incoming_port                remote port on <= lines
        lost_incoming_connection     as it says (includes timeouts)
        outgoing_port                add remote port to => lines
        queue_time                   time on queue for one recipient
        pid                          Exim process id
        received_recipients          recipients on <= lines
        received_sender              sender on <= lines
        rejected_header              header contents on reject log
        retry_defer                  “retry time not reached”
        return_path_on_delivery      put return path on => and ** lines
        sender_on_delivery           add sender to => lines
        sender_verify_fail           sender verification failures
        skip_delivery                delivery skipped in a queue run
        smtp_confirmation            SMTP confirmation on => lines
        smtp_connection              incoming SMTP connections
        smtp_incomplete_transaction  incomplete SMTP transactions
        smtp_mailauth                AUTH argument to MAIL commands
        smtp_no_mail                 session with no MAIL commands
        smtp_protocol_error          SMTP protocol errors
        smtp_syntax_error            SMTP syntax errors
        subject                      contents of Subject: on <= lines
        tls_certificate_verified     certificate verification status
        tls_cipher                   TLS cipher suite on <= and => lines
        tls_peerdn                   TLS peer DN on <= and => lines
        tls_sni                      TLS SNI on <= lines
        unknown_in_list              DNS lookup failed in list match
        all                          all of the above
```

## Parsing logs.

Here are some basic commands that you can use to look through the mail queue. These are especially useful if your mail queue has a large amount of emails. A mail queue with a lot of emails could point to a misconfiguration or a compromise on the server with malicious code causing the server to generate spam out. Here are a few of the basic commands that you can use through SSH to look at the details of your mail queue.

View the mail queue.

```console
  exim -bpc
```

View the mail queue with email IDs.

```console
  exim -bp
```

Force delivery for a single mail in the mail queue.

```console
  exim -M [ID]
```

Start sending mail out from the queue to clear it.

```console
  exim -qf
```

Force a queue out with frozen emails.

```console
  exim -qff
```

Check the emails individually. The `l` stands for log, the `b` stands for body, the `h` stands for header.

```console
  exim -Mvb [ID]
  exim -Mvl [ID]
  exim -Mvh [ID]
```

## Digging deeper into the logs.

Some of the commands below can allow you to find the source of spam or identify a single user sending a lot of mail out. This is particularly useful during compromise investigations.

The following helps to spot spammers sending mail from their `/home/` directory.

```console
  zegrep 'cwd=/home' `ls -tr /var/log/exim_mainlog*` | awk '{print $3}' | cut -d '/' -f3 | sort -bg | uniq -c | sort -bgr | head -n20
```

The command below is used to identify the directory it's coming from for that account.

```console
  grep cwd /var/log/exim_mainlog | grep -v /var/spool | awk -F"cwd=" '{print $2}' | awk '{print $1}' | sort | uniq -c | sort -n
```

The following also helps to find if a particular user is sending a lot of mail.

```console
  zegrep -oh 'A=dovecot[^ ]+' `ls -tr /var/log/exim_mainlog*` | sort | uniq -c | sort –n
```

## Clearing the Eximstats database.

You can use the following command from the MySQL CLI to clear the eximstats database in case the size is getting too large.

This is a one liner that will remove parts of the eximstats database.

```SQL
  use eximstats;delete from sends;delete from smtp;delete from failures;delete from defers;
```


## How to clear the Exim mail queue.

Here is a one liner that will allow you to clear the entire mail queue. This is especially useful if you have a large number of spam mails in the mail queue.

```console
  exim -bp | exiqgrep -i | xargs exim -Mrm
```

You can also delete mail from a specific sender using the command below. This is useful if you have a single user generating spam.

```console
  exiqgrep -ir email@domain.com | xargs exim -Mrm
```

## Permissions/ownership issues on WHM/cPanel servers

Occasionally, Exim running under WHM/cPanel will encounter problems with file permissions that present a wide array of unusual problems. This is a common enough issue that WHM provide an excellent repair script via the WHM web panel. When encountering any email problem on an WHM server, this script is a great place to start investigating: Home > Email > Repair Mailbox Permissions

## Official Exim Documentation.

If your needs require specific tweaks or configuration additions, we suggest that you use the [official Exim documentation](http://www.exim.org/exim-html-current/doc/html/spec_html/index.html) maintained by the University of Cambridge.



```eval_rst
  .. meta::
     :title: Using EXIM on Linux | UKFast Documentation
     :description: A guide to using the EXIM mail transfer agent on Linux servers
     :keywords: ukfast, linux, mail, email, exim, guide, tutorial, whm, cpanel, mysql
