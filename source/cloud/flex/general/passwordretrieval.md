# Retrieving passwords for eCloud Flex instances

The public-key-encrypted instance password can be retrieved and decrypted (when available) using the corresponding private-key, useful for decrypting the `Administrator` password within Windows instances. The methods for doing so are outlined here.

## Nova

The Nova CLI can be used to retrieve the password as below:

```console
[root@workstation ~]# nova get-password ba7a6424-3674-4f43-aca0-97dae8c23ef5 ~/private.key
Enter pass phrase for /root/private.key:
GDrtWKpcKHTQFUux3gpv
```

## eCloud Flex Dashboard

The [eCloud Flex dashboard](https://api.openstack.ecloud.co.uk/project) can be used to retrieve passwords.  Head to the Instances area, then click on the instance in question.  In the drop down menu at the top right of the screen you'll find the option to Retrieve Password.

![instances-retrievepassword](../files/instances-retrievepassword.PNG)

```eval_rst
  .. meta::
     :title: Retrieving passwords for eCloud Flex instances | UKFast Documentation
     :description: A guide to retrieving passwords for eCloud Flex instances
     :keywords: ukfast, password, retrieve, find, ecloud, flex, cloud, server
