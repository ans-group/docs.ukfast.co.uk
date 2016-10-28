# System State

To change the system state backups, edit the following file on the protected server:

```console
  C:\Program Files\Microsoft Data Protection Manager\DPM\Datasources\PSDatasourceConfig.xml
```


Change the `<FilesToProtect>` value from `%systemdrive%` to the desired location


Save the File
