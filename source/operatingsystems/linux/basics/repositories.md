# Repositories

To install packages on a Linux server then the packages will need to be available in the enabled repositories on the server. On a RedHat based server, you can see the installed repositories by viewing the files located in the below directory.

```bash
  /etc/yum.repos.d/
```

Even though these repositories are installed on the server this does not definitively mean that they are enabled on the server. On a RedHat based server you will be able to see whether or not the repository is enabled by viewing the file with a text viewer such as less.

```bash
  less /etc/yum.repos.d/centos-base.repo
```

You will then be able to see whether or not it is enabled by viewing the value for the `enabled` configuration. If it is set to `0` then it is disabled and if it is set to `1` then it is enabled.

You can also enable a repository while attempting to install by adding the `--enablerepo` to the yum command. For example, to enable the epel repository you can use the below command.

```bash
  yum update --enablerepo=epel
```

## Install other repositories

There are a variety of different methods available to install other repositories. As this is a basic guide it will only glance over two methods with are yum and wget. This guide will explain how to install the `epel` repository using both methods.

To use yum to install the `epel` repository you can simply use the below command.

```bash
  yum install epel-release
```

To use wget to install the `epel` repository, you will need to ensure that you are installing the correct repository for the correct OS version. For example, if you are using CentOS 6, you will need to ensure that you are installing the epel repository for CentOS 6. The first command below downloads the rpm package for epel and then the second command installs the repository using the rpm file.

```bash
  wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
```
```bash
  rpm -uvh epel-release-6-8.noarch.rpm
```
