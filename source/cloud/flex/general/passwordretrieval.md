# Retrieving passwords for eCloud Flex instances

The public-key-encrypted instance password can be retrieved and decrypted (when available) using the corresponding private-key, useful for decrypting the `Administrator` password within Windows instances. The methods for doing so are outlined here. To access your Linux server, please follow the steps on [accessing Linux eCloud Flex Instances Using SSH](accesslinuxinstances.html).

## Nova

The Nova CLI can be used to retrieve the password as below:

```console
[root@workstation ~]# nova get-password ba7a6424-3674-4f43-aca0-97dae8c23ef5 ~/private.key
Enter pass phrase for /root/private.key:
GDrtWKpcKHTQFUux3gpv
```

## eCloud Flex Dashboard

The [eCloud Flex dashboard](https://api.openstack.ecloud.co.uk/project) can be used to retrieve passwords.  Head to the Instances area, then click on the instance in question.  In the drop down menu at the top right of the screen you'll find the option to Retrieve Password. You'll then need to input your private key, and the password will appear in the popup window.

```eval_rst
.. meta::
    :title: Password Retrieval on eCloud Flex | UKFast Documentation
    :description: Detailed guidance on retrieving your password on eCloud Flex instances
    :keywords: ecloud, flex, instance, password, retrieve, key pair, openstack, windows
```
