# Connecting to eCloud Vault

There are two primary ways of interacting with eCloud Vault.

One is through "drag and drop" in [MyUKFast](https://my.ukfast.co.uk/ecloud-vault/index.php).

The second is the most powerful way of accessing eCloud Vault, and the one that most people will probably need. This is via API, using the access and secret key pair found in [the eCloud Vault section in MyUKFast](https://my.ukfast.co.uk/ecloud-vault/integration.php).

These keys will allow you to access the API endpoint found here: <http://vault.ecloud.co.uk/>

If you aren't familiar with the S3 API specification, [information can be found here](http://docs.ceph.com/docs/master/radosgw/s3/).

Your key pair will also allow you to access your eCloud Vault buckets through various S3-enabled third party applications. Though UKFast can't offer support on your configuration or use of these applications (see below), a few options are:

- **[Cyberduck](https://cyberduck.io/)** - Windows, Mac
- **[s3cmd](http://s3tools.org/s3cmd)** - Windows, Linux and Mac CLI tool (further details below)
- **[Duplicati](http://www.duplicati.com/)** - Windows backup utility
- **[Expandrive](http://www.expandrive.com/)** - Windows backup utility
- **[S3Anywhere](https://play.google.com/store/apps/details?id=lysesoft.s3anywhere&hl=en)** - Android s3 client

These applications can typically all be configured by setting the S3 host/address as ``vault.ecloud.co.uk`` and inputting your access and secret keys.

# s3cmd

While UKFast does not offer support for 3rd-party clients, interally we use `s3cmd` to test functionality and debug issues with eCloud Vault. As such, if you contact UKFast Support with an eCloud Vault issue you may be asked to replicate the problem with `s3cmd`. If you're not used to using command-line applications we appreciate it can be frustrating to use, but it's a useful comparison against other clients.

You must configure `s3cmd` before you use it. To do this, on Linux and MacOS, create a file in your home directory called `.s3cfg` with the following content. On Windows this should be in `C:\Users\[username]\AppData\Roaming\s3cmd.ini`.

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

```eval_rst
.. title: Connecting to eCloud Vault
.. meta::
   :title: Connecting to eCloud Vault | UKFast Documentation
   :description: Detailed information on connecting to eCloud Vault object storage from UKFast
   :keywords: eCloud, Vault, eCloud Vault, object storage, cloud storage, s3cmd
```

