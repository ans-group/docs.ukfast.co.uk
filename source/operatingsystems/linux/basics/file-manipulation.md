# File Manipulation

This guide is only going to show an overview of the commands. To find out more about each command you can run the following command:

```bash
  man [command]
```

The following is the test directory structure we'll be using throughout the upcoming examples:

```console
[root@c7 test]# ll
total 4
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 directoryone
-rw-r--r-- 1 another  root        0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
-rw-r--r-- 1 root     root        0 Aug 11 14:41 filetwo.txt
```
`ll` is just an alias for `ls -l`.

## cp

`cp` is used to copy files and directories.
```console
[root@c7 test]# cp fileone.txt copyfileone.txt
[root@c7 test]# ll
total 4
-rw-r--r-- 1 root     root        0 Aug 11 14:46 copyfileone.txt
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 directoryone
-rw-r--r-- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
-rw-r--r-- 1 root     root        0 Aug 11 14:41 filetwo.txt
```
As you can see here, the file fileone.txt was copied to copyfileone.txt; however the permissions were set to be owned by root and part of the group root.
```console
[root@c7 test]# whoami
root
```
This is because we're logged in as the root user. If you want to maintain the permissions, you need to use the `-p` flag.
```console
[root@c7 test]# ll
total 4
-rw-r--r-- 1 another  another     0 Aug 11 14:41 copyfileone.txt
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 directoryone
-rw-r--r-- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
-rw-r--r-- 1 root     root        0 Aug 11 14:41 filetwo.txt
```
You can copy directories in the same manner but running just `cp directoryone copydirectoryone` will just copy the directory itself but none of its contents. To copy the contents as well you need to pass the `-R` flag. The `-p` and `-R` flag can be combined to the `-a` flag.
```console
[root@c7 test]# cp -a directoryone copydirectoryone
[root@c7 test]# ll
total 8
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 copydirectoryone
-rw------- 1 root     root        0 Aug 11 14:54 copyfileone.txt
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 directoryone
-rw------- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
-rw-r--r-- 1 root     root        0 Aug 11 14:41 filetwo.txt
```

## mv

The move command is used to move or rename a file.
```console
[root@c7 test]# mv filetwo.txt directoryone
[root@c7 test]# ll directoryone/
total 0
-rw-r--r-- 1 root root 0 Aug 11 14:41 filetwo.txt
```
Here filetwo.txt has been moved to directoryone.
```console
[root@c7 test]# mv copyfileone.txt renamedcopy.txt
[root@c7 test]# ll
total 8
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 copydirectoryone
drwxr-xr-x 2 root     root     4096 Aug 11 14:58 directoryone
-rw------- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
-rw------- 1 root     root        0 Aug 11 14:54 renamedcopy.txt
```
Here the file copyfileone.txt has been renamed to renamedcopy.txt

## rm
`rm` is used to delete files and directories.
```console
[root@c7 test]# rm renamedcopy.txt
rm: remove regular empty file ‘renamedcopy.txt'? y
[root@c7 test]# ll
total 8
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 copydirectoryone
drwxr-xr-x 2 root     root     4096 Aug 11 14:58 directoryone
-rw------- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
```
Here the file `renamedcopy.txt` is deleted. As you can see, there is a promt for this. This can be overridden with the `-f` flag.
```console
[root@c7 test]# rm -f renamedcopy.txt
[root@c7 test]# ll
total 8
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 copydirectoryone
drwxr-xr-x 2 root     root     4096 Aug 11 14:58 directoryone
-rw------- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
```
To delete a directory you need to pass the `-R` flag.
```console
[root@c7 test]# rm -R directoryone
rm: descend into directory ‘directoryone'? y
rm: remove regular empty file ‘directoryone/filetwo.txt'? y
rm: remove directory ‘directoryone'? y
```
Again, this prompts you. You can override this by using `-Rf`.
```console
[root@c7 test]# rm -Rf directoryone/
[root@c7 test]# ll
total 4
drwxr-xr-x 2 root     root     4096 Aug 11 14:45 copydirectoryone
-rw------- 1 another  another     0 Aug 11 14:41 fileone.txt
-rw-r--r-- 1 testuser testuser    0 Aug 11 14:41 filethree.txt
```
It is possible to add the `*` on the end of the `rm -Rf` command; however, we would advise you never to do this as if this command is run in the / folder on your server, this will cause all the contents of the server to be deleted. Instead, if you want to delete a directory, you should specify the directory.
```console
[root@c7 ~]# rm -Rf /root/test
```

```eval_rst
  .. title:: Manipulating files in Linux | UKFast Documentation
  .. meta::
     :title: Manipulating files in Linux | UKFast Documentation
     :description:  A guide to manipulating files on the Linux OS
     :keywords: ukfast, linux, copy, move, remove, server, virtual, vm, files, directory
