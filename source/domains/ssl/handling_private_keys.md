# How to find your private key

```eval_rst
   .. title:: SSL | Handling Private Keys
   .. meta::
      :title: SSL | Handling Private Keys | ANS Documentation
      :description: Information on handling SSL Private Keys

```

Private keys are generated after purchasing, renewing, reissuing or managing domains on an SSL certificate. During these processes,
the private key is only shown once and you will need to copy it at this stage and store it securely, ideally on the device(s) it will be installed on.

If the key isn't copied or securely stored the SSL Certificate will need to be completed and reissued (at no extra cost).
We recommend only keeping the private key until the installation is completed on all servers where it is required.

## Windows servers

If you have a Windows server you will still need to copy the private key and store it securely as above,
as this is needed to download the PFX required for installation on Windows servers.

## FAQ:

### How do I reissue my certificate if I no longer have the private key

Please go to: **Glass > Services > SSL Certificates > Domain Certificate > "Reissue Certificate"**

### Where should I keep my private key after copying it?

We recommend storing your private key onto the server(s) that you will be installing the SSL on.
