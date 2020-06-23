# Missing Inbox

If you have a missing Inbox in outlook (or another missing folder), this could be that it is set to hidden.

There is no official way to change this, it's a known bug with Exchange 2003/2007.

Firstly, try opening outlook via `Start` > `Run` with the following command:

```powershell
  outlook.exe /resetfolders
```


If this does not work,you will need the following:
<http://mfcmapi.codeplex.com/>

* Open Outlook (has to be 32bit as there is no 64bit version of this software)
* Open MFCMAPI
* Select the account
* Select the store that the folder is in
* Navigate to the folder that has vanished
* On the right hand pane, you should see an option for 'PR_ATTR_HIDDEN'
* Right click this and choose 'Edit Property'
* Untick the checkbox
* Close MFCMAPI
* Restart Outlook and you should see the folder

```eval_rst
  .. title:: Missing inbox in Microsoft Exchange | UKFast Documentation
  .. meta::
     :title: Missing inbox in Microsoft Exchange | UKFast Documentation
     :description: Guidance on resolving a missing inbox or other folders in Microsoft Exchange
     :keywords: ukfast, exchange, missing, inbox, outlook, cloud, account, server
