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
* [s3cmd]        - Windows, Linux and Mac CLI tool (see note below)
* [Duplicati]    - Windows backup utility
* [Expandrive]    - Windows s3 drive utility
* [S3Anywhere]    - Android s3 client

Configuration and use of these aren't supported by UKFast, but they can typically all be configured by setting the s3 host/address as ``vault.ecloud.co.uk`` and inputting your access and secret keys.

Please note that for `s3cmd` version 1.6.1 or above, you will need to add `signature_v2 = True` to your `.s3cfg` configuration file or you may encounter `SignatureDoesNotMatch` errors when uploading files with spaces in the filename.

UKFast will take all necessary steps to ensure that your data on our systems remains accessible, that data integrity is maintained and the API remains accessible. Beyond this, UKFast take no responsibility for your use of this system. We are not able to offer support for any 3rd-party product, nor the use of the Ceph API in your own applications.


[Cyberduck]: https://cyberduck.io/
[s3cmd]: http://s3tools.org/s3cmd
[Duplicati]: http://www.duplicati.com/
[Expandrive]: http://www.expandrive.com/
[S3Anywhere]: https://play.google.com/store/apps/details?id=lysesoft.s3anywhere&hl=en
