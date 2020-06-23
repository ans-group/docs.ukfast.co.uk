# Linux Backups with Duply + eCloud Vault

eCloud vault, with it's S3 compatible API provides a great, cheap, way to store large amounts of data. Backups and other long term storage are a great use-case for this, but manually pushing/pulling files from Vault can be a bit arduous.

Enter [Duply](http://duply.net/), a wrapper for [Duplicity](http://duplicity.nongnu.org/).

Once configured correctly, duply allows you to send encrypted incremental backups to various remote storage platforms, Vault amongst them.

## Installing Duply

First things first, we need to get `duply` onto your server. It can be found in the `epel` repository, so if you don't have it then install it like so:

```shell
yum install epel-release
```

You can then install `duply` and all related packages with this command:

```shell
yum install duply --enablerepo=epel
```

For it's encryption, `duply` uses the venerable GPG suite. Explanation of how GPG does what it does is a bit beyond the scope of this article, but it's worth reading up on if you're interested. All you really need to know here is that you'll need a gpg keypair for `duply` to work with, which you can generate with the following command:

```shell
gpg --gen-key
```

Follow the prompts through to create the pair, the default values should be fine. Make sure to use a nice strong passphrase and commit it to memory.

```eval_rst
.. note::
  This command can take quite a while to complete. You can either wait it out, or install ``rngd`` with ``yum install rng-tools`` and run the following command to generate some entropy and speed up the generation:

  ``rngd -f -r /dev/urandom``

  You can check your current entropy like so:

  ``cat /proc/sys/kernel/random/entropy_avail``
```

With your key generated, grab the id of the key from the output of the following command:

```shell
gpg --list-keys

/root/.gnupg/pubring.gpg
------------------------
pub   2048R/FE9414F1 2015-06-01
uid                  duply (duply) <duply@duply.fake>
sub   2048R/BE1CCF23 2015-06-01
```

In the above example, we want the `pub` line, with our id being the part after the `/`. So our key id would be `FE9414F1`

## Configuring a backup

With the pre-requisites out of the way, we can move onto creating our backup. I'm using the name `demobackup` throughout this document, but you can of course call it whatever you want.

Run the following command to get `duply` to create your backup:

```shell
duply demobackup create
```

This will create a config file in the following location:

```shell
/etc/duply/demobackup/conf
```

Open it with the editor of your choice (`vim` of course) and replace all the contents with something like this:

```shell
GPG_KEY='FE9414F1'
GPG_PW='pryhaerdr7TIbra'
GPG_OPTS='--compress-algo=bzip2 --personal-cipher-preferences AES256,AES192'
TARGET='s3://vault.ecloud.co.uk/sambackup/docs/'
export AWS_ACCESS_KEY_ID='8ASJQWEKJ8DHJFKSHEUV'
export AWS_SECRET_ACCESS_KEY='e3NozpAdkjfiwhnvpwjvkhz6GHJ43a8chji4bnmG'
SOURCE='/'
MAX_AGE=1M
TEMP_DIR=/tmp
```

There are a few settings you'll want to change:

* `GPG_KEY` should be replaced with the key ID you generated in the previous step
* `GPG_PW` should be replaced with the passphrase specified earlier
* `TARGET_USER` should be switched out for your eCloud Vault access key
* `TARGET_PASS` should be changed for your eCloud Vault secret key

You may also want to change `MAX_AGE`. This refers to how long backups are kept for. The default in my example is 1 month, but can be increased/decreased as you see fit.

Now onto the `excludes` file to specify what we do and don't want to back up. You can find it here:

```shell
/etc/duply/demobackup/excludes
```

For the purpose of my example, I'm only backing up 1 directory, `/etc/testdir`. In that directory, I have a logs directory that has files I don't want to backup, so I'll be excluding that. With that in mind, my `excludes` file looks like this:

```none
- /etc/testdir/logs
+ /etc/testdir
**
```

```eval_rst
.. note::
   You can add as many lines as you need, just make sure that `**` remains as the last line, and that your exclusions are above your inclusions.
```

## Running a backup

Now for the main event, actually running a backup and getting those files somewhere safe.

If you did all the previous steps correctly, this should just be a case of running the following command:

```shell
duply demobackup backup
```

Depending on what you're backing up, this may take a while. This can be sped up somewhat by allowing asynchronous uploads (allowing duply to prepare the next file whilst it uploads the current one). The command with this option looks like this:

```shell
duply demobackup backup --asynchronous-upload
```

Once it completes, you'll get quite a bit of output, but the main bit you're interested in looks like this:

```shell
--------------[ Backup Statistics ]--------------
StartTime 1433165073.54 (Mon Jun  1 14:24:33 2015)
EndTime 1433165088.51 (Mon Jun  1 14:24:48 2015)
ElapsedTime 14.96 (14.96 seconds)
SourceFiles 6
SourceFileSize 567550046 (541 MB)
NewFiles 6
NewFileSize 567550046 (541 MB)
DeletedFiles 0
ChangedFiles 0
ChangedFileSize 0 (0 bytes)
ChangedDeltaSize 0 (0 bytes)
DeltaEntries 6
RawDeltaSize 567537701 (541 MB)
TotalDestinationSizeChange 35710 (34.9 KB)
Errors 0
-------------------------------------------------

--- Finished state OK at 14:24:53.136 - Runtime 00:00:20.545 ---
```

There aren't any errors there, so our files are now backed up.

## Running backups automatically

No-one wants to log in every day and start a backup running, that's not efficient at all, so we'll turn to our good friend `cron` to carry this out regularly.

```eval_rst
.. seealso::
   If you're new to `cron`, you may want to read our page on it here:

   :doc:`/operatingsystems/linux/basics/cron`
```

The following bash script will run duply jobs on a nightly basis and email the output to the email address you specify:

```shell
#!/bin/sh
SRVNAME=$(hostname)

STARTDATE=$(date "+%Y-%m-%d %H:%M:%S")
DUPLYOUT=$(/usr/bin/duply demobackup backup --asynchronous-upload 2>&1)
EXITCODE=$?
ENDDATE=$(date "+%Y-%m-%d %H:%M:%S")

echo -e "To: email@me.com\nSubject: [${SRVNAME}] Duply Backup Complete\n\nExit code: ${EXITCODE}\nStart: ${STARTDATE}\nEnd: ${ENDDATE}\n\n${DUPLYOUT}" \ | /usr/sbin/sendmail -f duply@myserver.net email@me.com
```

Save that to a file on your server (`/usr/bin/duplyback.sh` in my case), change the email addresses and make it executable with `chmod +x /usr/bin/duplyback.sh`

With that done, it's just a matter of adding it into crontab. Open crontab with `crontab -e` and use something like this, adjusting the timing to suit you:

```shell
1 2 * * * /usr/bin/duplyback.sh
```

## Restoring files using duply

Here's the bit that you don't really want to have to do. It's worth testing out before you really need to do it so that you're familiar with the process.

To check what backups you have available, the following command is useful:

```shell
duply demobackup status
```

It might generate quite a lot of noise, but the following bit is what you're after:

```none

Number of contained backup sets: 2
Total number of contained volumes: 2
Type of backup set:                            Time:          Number of volumes:
                Full                Mon Jun  1 14:41:45 2015                   1
                Incremental         Mon Jun  1 14:51:38 2015                   1
```

In this basic example, we only have 2 backups from the same day, but you may very well have months worth. This will be useful to know later.

To restore the latest version of everything that duply has, run this:

```shell
duply demobackup restore /etc/restore
```

You can use whatever directory you like in place of `/etc/restore`. This will generate an entire clone of the directory structure that duply has a copy of, like so:

```shell
[root@duplytest ~]# cd /etc/restore/etc/testdir/
[root@duplytest testdir]# ll
total 4
-rw-r--r-- 1 root root 37 Jun  1 14:14 important.txt
drwxr-xr-x 2 root root 20 Jun  1 14:14 logs
```

Of course you don't always want a copy of everything, it's often just one file. In that case, the `fetch` command is the one you want:

```shell
duply demobackup fetch etc/testdir/important.txt /etc/testdir/important.txt
```

It's important to note that the first `/` is intentionally missing in that command, as it refers to the `SOURCE` variable configured earlier in your duply configuration file.

## Going forward

If you're thinking of backing up MySQL data using this, you may want to read our accompanying article on this topic to ensure you're taking consistent backups:

[Linux Database Servers](linuxdbservers.html)

```eval_rst
.. title:: Linux Backups with Duply and eCloud Vault | UKFast Documentation
.. meta::
   :title: Linux Backups with Duply and eCloud Vault | UKFast Documentation
   :description: Linux Backups with Duply and eCloud Vault
```

