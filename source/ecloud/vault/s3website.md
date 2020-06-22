```eval_rst
.. meta::
   :title: UKFast Documentation | eCloud Vault | Basic s3website API usage
   :description: Information on how you can host a static website on eCloud vault using the S3website interface
```
# Basic s3website API usage

```eval_rst
.. warning::
  As with most of our Vault  guides, we're going to assume that you already have a working s3cmd environment

  If you're not using this method of authentication, you may need to specify additional flags/options in the commands used in this article.
```

You can host a static website on eCloud vault using the S3website interface.

## Hosting a Static Website on eCloud Vault

Start by creating a bucket using the domain name you wish to use such as:

```bash
  s3cmd mb s3://www.example.com
```

Nowe we can mark the bucket as a website bucket:

```bash
  s3cmd ws-create --ws-index=index.html s3://www.example.com
```

Now you can upload your website including the index page:

```bash
  s3cmd put --acl-public index.html s3://www.example.com/
```

You can test the WebPage is working by viewing the website

```bash
  browser> http://www.example.com.vault-website-man-5.ecloud.co.uk
```
## Hosting a Static Website on eCloud Vault with a Custom domain name

In this section we discuss the DNS settings required to point your domain to the static website bucket created above.

Using your favourite DNS provider add a CNAME to the bucket name, in our example We added the below:

```bash
  www.example.com.         300     IN      CNAME   www.example.com.vault-website-man-5.ecloud.co.uk
```
