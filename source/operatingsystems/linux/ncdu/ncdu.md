# Ncdu

### Install `Ncdu` (CentOS)
You can install `Ncdu` with the following command:

```bash
~]# yum install ncdu
```

### Install `Ncdu` (Ubuntu/Debian)
You can install `Ncdu` with the following command:

```bash
~]# apt install ncdu
```

#### Updating `Ncdu`
You can update `Ncdu` with the following command:

```bash
~]# yum update ncdu
```

#### Version Check
You can check the version of `Ncdu` installed with the following command:

```bash
~]# ncdu -v
ncdu 1.16
```

### Scan partitions and directories
`Ncdu` can be used to scan whole partitions, this will list the directories, with the largest at the top. To navigate through the `ncdu` screen, you use the arrow keys. To only scan one partition and omit the others, you would use the -x flag for this:

```bash
~]# ncdu -x /
```

This can also be done on specific directories, for example /root/:
```bash
~]# ncdu /root/
```

```eval_rst
   .. title:: Ncdu
   .. meta::
      :title: Ncdu | UKFast Documentation
      :description: A guide to using Ncdu
      :keywords: ukfast, linux, install, centos, cloud, server, virtual, ncdu
```
