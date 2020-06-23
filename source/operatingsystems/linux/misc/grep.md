# The grep command

The grep command's main use is to search through files or filter output. 

As per other commands, it's best demonstrating its use with examples. Here is the contents of the file test.txt which we are going to use:

```console
[root@c7 ~]# cat test.txt
line 1
line 2
line 3
Line 4
newline 5
NEWline 6
NEWLINE 7
new line 8
```

First of all we're going to search the file for the word 'line':

```console
[root@c7 ~]# grep line test.txt
line 1
line 2
line 3
newline 5
NEWline 6
new line 8
```

As you can see, all lines wre displayed apart from line 7. This is because that line contains the word 'LINE' rather than 'line'. We can tell grep to ignore the letter case with the -i flag:

```console
[root@c7 ~]# grep -i line test.txt
line 1
line 2
line 3
Line 4
newline 5
NEWline 6
NEWLINE 7
new line 8
```

This displayed all lines. Here is another example using -i:

```console
[root@c7 ~]# grep -i LiNe test.txt
line 1
line 2
line 3
Line 4
newline 5
NEWline 6
NEWLINE 7
new line 8
```

Again, all lines were displayed.

To narrow this down further we could run:

```console
[root@c7 ~]# grep 'line 1' test.txt
line 1
```

The single quotes allowed us to search for the exact phrase 'line 1'.

# Using grep with a pipe

Filtering output is another common use for grep. Again, here is what we get if we cat out the test.txt file:

```console
[root@c7 ~]# cat test.txt
line 1
line 2
line 3
Line 4
newline 5
NEWline 6
NEWLINE 7
new line 8
```

The | symbol can be used to pipe the output of the last command into another command. We are going to pipe it into grep:

```console
[root@c7 ~]# cat test.txt | grep line
line 1
line 2
line 3
newline 5
NEWline 6
new line 8
```

As you can see, this gives us the exact same output as 'grep line test.txt':

```console
[root@c7 ~]# grep line test.txt
line 1
line 2
line 3
newline 5
NEWline 6
new line 8
```

Here we will use the command to filter out php modules for the xml module:

```console
[root@c7 ~]# php -m | grep xml
libxml
xml
```

As you can see this matched two modules.

```eval_rst
  .. title:: Using the grep command in Linux | UKFast Documentation
  .. meta::
     :title: Using the grep command in Linux | UKFast Documentation
     :description: A guide to using the grep command to search or filter in the Linux OS
     :keywords: ukfast, linux, grep, search, server, find, pipe, cloud, centos, virtual
