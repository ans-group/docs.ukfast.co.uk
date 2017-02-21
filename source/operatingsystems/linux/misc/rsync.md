# Transferring files with rsync

rsync is a utility that can be used for both file transfers and file synchronisation. rsync uses the SSH protocol to transfer files. This utility can be used to transfer from a local computer to a server, the server to a local computer and also between remote server. This guide will go explain how to transfer files between remote servers.

You will need to have working server credentials for both the origin and the destination server. You will need to login to the origin server via SSH and then you will be able to start with the transfer. The syntax will need to follow the example below.

```bash
  rsync /path/to/origin/dir root@ip.ip.ip.ip:/path/to/dir/destination/server
```

There are a lot of flags that can be added to this command that would can be found by reading the man pages for the rsync command. The below example command will use archive mode to preserve permissions, verbose output, compress the data during transfer and output information in a human readable format. The `-e` flag also allows the specification of a port to use, which in this case is 2020.

```bash
  rsync -avzPh -e"ssh -p2020" /path/to/dir root@ip.ip.ip.ip:/new/location/for/dir
```
