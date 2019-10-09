# NFS

### Install NFS
You can install NFS with the following command:
```bash
~]# yum install nfs-utils nfs-utils-lib 
```

### Distributed Files/Folders
It's very important to only use NFS for files/folder which need to be distributed between multiple servers. We strongly advise against having the entire document root of your Magento website on NFS. For Magento2 the typical directories that need NFS are:

- pub/media
- pub/static

There are a number of ways in which you can achieve this.

#### Customize MAGE_DIRS
You can set MAGE_DIRS in any of the following ways:

##### Bootstrap Parameters
Please refer to the Magento guide on how to set the value of bootstrap parameters: [https://devdocs.magento.com/guides/v2.3/config-guide/bootstrap/magento-how-to-set.html](https://devdocs.magento.com/guides/v2.3/config-guide/bootstrap/magento-how-to-set.html)

##### Custom Entry Point Script
You can use a custom entry point script such as the following:
```bash
use Magento\Framework\App\Filesystem\DirectoryList;
use Magento\Framework\App\Bootstrap;

require __DIR__ . '/app/bootstrap.php';
$params = $_SERVER;
$params[Bootstrap::INIT_PARAM_FILESYSTEM_DIR_PATHS] = [
 	    DirectoryList::PUB => [DirectoryList::URL_PATH => '',
 	    DirectoryList::MEDIA => [DirectoryList::PATH => '/nfsshare/media', DirectoryList::URL_PATH => ''],
 	    DirectoryList::STATIC_VIEW => [DirectoryList::URL_PATH => 'static'],
 	    DirectoryList::UPLOAD => [DirectoryList::URL_PATH => '/nfsshare/media/upload'],
 	    DirectoryList::CACHE => [DirectoryList::PATH => '/nfsshare/cache'],
];
$bootstrap = \Magento\Framework\App\Bootstrap::create(BP, $params);
/** @var \Magento\Framework\App\Http $app */
$app = $bootstrap->createApplication('Magento\Framework\App\Http');
$bootstrap->run($app);
```

#### Direct Mount Point
You can directly mount NFS to the folder within your document root:

```bash
NFSSERVER/nfsshare/media -> /var/www/vhosts/magentodomain.com/htdocs/pub/media
```
You can do this with the following entry in /etc/fstab:

```bash
 ~]# cat /etc/fstab | grep -i nfs
NFSSERVER:/nfsshare/media /var/www/vhosts/magentodomain.com/htdocs/pub/media nfs rw,vers=3,noatime,nodiratime,async,timeo=1800 0 0
 ~]# mount /var/www/vhosts/magentodomain.com/htdocs/pub/media
```

#### Symlinks
You can symlink files/folders from your document root to the NFS mount point.

```bash
~]# ln -s /var/www/vhosts/magentodomain.com/htdocs/pub/media /nfsshare/media
```

### Open File Check
You can see all the NFS open files with the following command:
```bash
~]# lsof -N
```

### Write Speed Test
Using the dd command you can write a file to the local file system and then to the NFS mount point to then compare the speed results. The write speeds over NFS should always be slower

#### Local File System
```bash
~]# dd if=/dev/zero of=/root/testfile bs=1G count=1 oflag=direct
1073741824 bytes (1.1 GB) copied, 1.12829 s, 952 MB/s
~]# rm -f /root/testfile
```

#### NFS Mount Point
This write speed test creates the file /nfsshare/testfile with NFS being mounted to /nfsshare/

```bash
~]# dd if=/dev/zero of=/nfsshare/testfile bs=1G count=1 oflag=direct
1073741824 bytes (1.1 GB) copied, 1.82611 s, 588 MB/s
~]# rm -f /nfsshare/testfile
```

```eval_rst
  .. meta::
     :title: Magento2 NFS | UKFast Documentation
     :description: A guide to using NFS on our Magento2 optimised stack
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, Magento, Magento2, NFS, eCommerce

