 # File Changes

File Integrity Monitoring alerts can be found in the 'Alerts' section of your MyUKFast area. Critical File Changes are also sent as an email alert to the selected contacts. Both of these alert types will contain important information regarding the event.

By default, File Integrity Monitoring scans run every 12 hours and will alert when the MD5/SHA1/SHA256 sum of monitored files change, prompting for further investigation. This is useful however it can sometimes be difficult to investigate these alerts as little information is captured.

 To combat this, realtime monitoring can be configured, utilising 'Aduitd' on Linux systems and Windows Auditing. When realtime FIM is configured, changes to these files are reported within 30 seconds. Additionally, extra data such as what user changed the file, what the effective user was (for example root if sudo was used), the process name that changed the file, and what exactly what changed is provided in the alert.

 With this additional information, a File Change Alert can easily be recognised as suspicious or as a false positive. The needed action can then be taken quickly by either yourself or by the Threat Response Team when coupled with our Threat Response service for active alert investigation. 

 Information on the important aspects of a File Integrity Monitoring alert are detailed below:

 **File Path and metadata**

 Towards the top of an email alert, the absolute path to the file or directory that changed will be shown. This is followed by meta-information on the file, including the size in bytes, the MD5/SHA1/SHA256 sums of the file before and after the file changes and modification times.

 ```
 Log: File '/etc/passwd' checksum changed.
 Size changed from '1437' to '1513'
 Old md5sum was: '48b88dc532f53a02d17e4ed75f10256a'
 New md5sum is : 'f5ce4f64c5e5cd0a9d17e4ed75f109e8'
 Old sha1sum was: 'b7fd06319a04dbccfd17e4ed75f10831c702db5e'
 New sha1sum is : 'b40031f9706719662b84fb9d17e4ed75f1063634'
 Old sha256sum was: '84b87d17e4ed75f10ae77cc1d4cb49876abebf7d7adb7c658ac0d254eea6168554'
 New sha256sum is : 'e96d17e4ed75f10baca3818fbebd0112abe5fb9d0dc4c1c894baf5b3595f12b7'
 Old modification time was: 'Mon Oct 7 12:00:06 2019', now it is 'Mon Oct 7 12:04:25 2019'
 Old inode was: '17199916', now it is '17339211'
 ```

 **User Data**

 If real-time monitoring is configured, information on the user that changed the file will also be passed. For example, here we can see the user 'john.doe' with the group 'john.doe' changed this file. His must-have been using 'sudo' as the effective user was 'root'. user and group IDs are also passed for convenience.

 ```
 (Audit) User: 'john.doe (1010)'
 (Audit) Effective user: 'root (0)'
 (Audit) Group: 'john.doe (1010)'
 ```

 **Process Data**

 If real-time monitoring is configured, process information is also passed. This will detail the process ID and the name of the process that changed the file. This is useful when diagnosing why a file was changed.

 ```
 (Audit) Process id: '616'
 (Audit) Process name: '/usr/bin/passwd
 ```

 **Change Data**

 Finally, when real-time monitoring is configured, information on what exactly has changed in the file is also passed. Please note that although this does have a generous character limit, if an entire code block is added to a file, for example, this information may not be passed due to the size limitations. 

 This section follows the common output format of the 'diff' command. As a result '<' will indicate what has been removed and '>' will indicate what has been added.

 In the example below, we can see that information for the user john.doe was changed. Please note that the below has been obfuscated.

 ```
 What changed:
 97g52
 < john.doe:$6$bf/M33a397b7b69cG$RJK04FsbqxgMzu3oDF40415bmVU33a397b7b69cvwAZUxjxJYjv0mQ94Isz3ajfmm6kSEDGu/dQEdsdsCxOOHVj/:17325:0:93429:1:::
 ---
 > john.doe:!!$6$bf/M8HsySGWIiT33a397b7b69cxgMzu3oDF40415bmV33a397b7b69covwAZUxjxJYjv0mQ94Isz3ajfmm6kSEDGu/dQEMjCxOOHVj/:15576::99739:1:::
 ```
 
```eval_rst
   .. title:: File Monitoring
   .. meta::
      :title: File Monitoring | UKFast Documentation
      :description: Our Threat Monitoring ruleset explained
      :keywords: threat monitoring, alerts, security, compliance, rules, rulesets, ukfast, hosting, file integrity monitoring, rootkit, detection, vulnerability scan, scans, hids, intrusion detection, set up
```