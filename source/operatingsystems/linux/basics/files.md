# File Reading and Editing

This guide is only going to show an overview of the commands. To find out more about each command you can run the following:

```bash
  man [command]
```

There are several ways to output a file in Linux.

Here are two test files and their content, we'll be using these in the upcoming examples.

fileone.txt
```console
one
two
three
four
five
```

filetwo.txt
```console
ONE
TWO
THREE
FOUR
FIVE
```

## cat
`cat` is mostly used today to output a file to the screen.
```console
[root@c7 ~]# cat fileone.txt
one
two
three
four
five
```
It was originally to combine the output of two files.
```console
[root@c7 ~]# cat fileone.txt filetwo.txt
one
two
three
four
five
ONE
TWO
THREE
FOUR
FIVE
```
It can be used to add content to a file.
```console
[root@c7 ~]# cat > filethree.txt
new file content
^C
[root@c7 ~]# cat filethree.txt
new file content
```
After the `cat > filethree.txt` command, press enter and enter the text you want to add to your file. End this with a new line and `ctrl + c`.
N.B. This command will NOT tell you if the file already exists so it's very easy to overwrite a file.

## less
For very large files less will allow you to scroll up and down a file. Search the file with the `/searchterm` keys. Use the `n` key to keep searching.

## head
By default `head` will show the top 10 lines of a file. This can be adjusted with the `-n` flag.
```console
[root@c7 ~]# head -n 2 fileone.txt
one
two
```

## tail
By default `tail` will show the bottom 10 lines of a file. This can adjusted with the `-n` flag.
```console
[root@c7 ~]# tail -n 2 fileone.txt
four
five
```
If your file is changing, you can watch the output. This is best used on logs like mail logs.
```console
[root@c7 ~]# tail -f /var/log/maillog
Aug 10 00:00:21 c7 sSMTP[31684]: Unable to locate mail
Aug 10 00:00:21 c7 sSMTP[31684]: Cannot open mail:25
Aug 10 11:10:44 c7 postfix/postqueue[23404]: fatal: Cannot flush mail queue - mail system is down
Aug 10 11:10:54 c7 postfix/postfix-script[23546]: starting the Postfix mail system
Aug 10 11:10:54 c7 postfix/master[23548]: daemon started -- version 2.10.1, configuration /etc/postfix
Aug 11 00:00:07 c7 sSMTP[25365]: Unable to locate mail
Aug 11 00:00:07 c7 sSMTP[25365]: Cannot open mail:25
Aug 11 11:17:21 c7 postfix/smtpd[9292]: connect from localhost[::1]
Aug 11 11:18:32 c7 postfix/smtpd[9292]: lost connection after CONNECT from localhost[::1]
Aug 11 11:18:32 c7 postfix/smtpd[9292]: disconnect from localhost[::1]
```

```eval_rst
  .. title:: Reading and editing files on Linux
  .. meta::
     :title: Reading and editing files on Linux | UKFast Documentation
     :description:  A guide to reading and editing files on Linux
     :keywords: ukfast, linux, reading, editing, files, server, virtual, vm, tail, head, vi, vim, less, head
