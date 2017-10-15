```eval_rst
.. title:: UKFast Documentation | eCloud Vault | Connecting to eCloud Vault
.. meta::
   :title: UKFast Documentation | eCloud Vault | Connecting to eCloud Vault
   :description: Detailed information on ways to connect to UKFast's eCloud Vault
```

# Connecting to eCloud Vault

There are 2 primary means of interacting with eCloud Vault.

One is by accessing the drag and drop interface in your MyUKFast area:

<https://my.ukfast.co.uk/ecloud-vault/index.php>

The second way is the most powerful way of accessing vault and the one that most people will probably need. This is the API level access and can be achieved using the access and secret key pair found in your MyUKFast client area on the following page:

<https://my.ukfast.co.uk/ecloud-vault/integration.php>

These keys will allow you to access the API endpoint found here:

<http://vault.ecloud.co.uk/>

If you aren't familiar with the S3 API specification, information can be found here:

<http://docs.ceph.com/docs/master/radosgw/s3/>

Your keypair will also allow you to access your buckets through various s3 enabled third party applications. Though UKFast can't offer any support on these applications (see below), a few are mentioned below:

* [Cyberduck]     - Windows, Mac
* [s3cmd]        - Windows, Linux and Mac CLI tool (see below)
* [Duplicati]    - Windows backup utility
* [Expandrive]    - Windows s3 drive utility
* [S3Anywhere]    - Android s3 client

Configuration and use of these aren't supported by UKFast, but they can typically all be configured by setting the s3 host/address as ``vault.ecloud.co.uk`` and inputting your access and secret keys.

UKFast will take all necessary steps to ensure that your data on our systems remains accessible, that data integrity is maintained and the API remains accessible. Beyond this, UKFast take no responsibility for your use of this system. We are not able to offer support for any 3rd-party product, nor the use of the Ceph API in your own applications.

# s3cmd

While UKFast does not offer support for any 3rd-party clients, interally our go-to client to test functionality and debug issues with Vault is `s3cmd`. As such, if you encounter an issue you may be asked to replicate the problem with `s3cmd`. If you're not used to using command-line applications we appreciate it can be frustrating to use, but it's a useful comparison against other clients.

You must configure s3cmd before you use it. To do this, on Linux and MacOS, create a file in your home directory called `.s3cfg` with the following content. On Windows this should be in `C:\Users\[username]\AppData\Roaming\s3cmd.ini`.

```
[default]
access_key = YOUR_ACCESS_KEY
secret_key = YOUR_SECRET_KEY
host_base = vault.ecloud.co.uk
host_bucket = %(bucket)s.vault.ecloud.co.uk
human_readable_sizes = True
use_https = True

# If your s3cmd version is 1.6.1 or greater, you should add the following line
signature_v2 = True
```

As noted in the configuration for version 1.6.1 or above, you will need to add `signature_v2 = True` to your configuration file or you may encounter `SignatureDoesNotMatch` errors when uploading files with spaces in the filename.

Once you have the configuration in place, you can start to use `s3cmd` to view and change your buckets and files. Some example usage:

* List your buckets: `s3cmd ls`
* Create a new bucket: `s3cmd mb s3://bucketname` 
* List the contents of a bucket: `s3cmd ls s3://bucketname/`
* List the contents of a 'directory' (known as 'prefix'): `s3cmd ls s3://bucketname/path/` (note trailing slash)
* Upload a file to a bucket: `s3cmd put myfile.txt s3://bucketname/path/myfile.txt`
* Make a file public: `s3cmd setacl --acl-public s3://bucketname/path/myfile.txt` (you can also specify the `--acl-public` option during upload)
* Make a file private: `s3cmd setacl --acl-private s3://bucketname/path/myfile.txt`
* Remove a file: `s3cmd del s3://bucketname/path/myfile.txt`
* Remove a bucket and all files in it (danger!): `s3cmd rb --recursive s3://bucketname`

[Cyberduck]: https://cyberduck.io/
[s3cmd]: http://s3tools.org/s3cmd
[Duplicati]: http://www.duplicati.com/
[Expandrive]: http://www.expandrive.com/
[S3Anywhere]: https://play.google.com/store/apps/details?id=lysesoft.s3anywhere&hl=en
