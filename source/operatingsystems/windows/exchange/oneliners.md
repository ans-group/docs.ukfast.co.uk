# Exchange PowerShell Quick Commands

List all messages out from a specific domain within a specific time::

```ps1con
  Get-MessageTrackingLog -Server "servername" -EventID "SEND" -Start "27/07/2015 06:00:00" -End "27/07/2015 07:00:00" -ResultSize unlimited | where{$_.sender -like "*@contoso.com"}
```

Or you could output it to a text file::

```ps1con
  Get-MessageTrackingLog -Server "servername" -EventID "SEND" -Start "27/07/2015 06:00:00" -End "27/07/2015 07:00:00" -ResultSize unlimited | where{$_.sender -like "*@contoso.com"} | tee contoso.txt
```

List all of the distribution groups for a given domain::

```ps1con
  Get-DistributionGroup | where{$_.primarysmtpaddress -like "*@contoso.com"} | select name, primarysmtpaddress
```

List all members of that distribution group::

```ps1con
  Get-DistributionGroupMember -Identity "Name of Dist Group" | select -primarysmtpaddress
```


Set SCL rating of a domain and reject messages at the threshold::

```powershell
  Get-Mailbox -OrganisationalUnit contoso.com | Set-Mailbox -SCLRejectEnabled $true -SCLRejectThreshold 5
```


List the size of a mailbox and the number of messages::

```ps1con
  $array = @()
  get-mailbox -identity *@contoso.com -resultsize unlimited | foreach-object {
  $dname=$_.DisplayName
  $email = $_.primarysmtpaddress
  $size=(Get-MailboxStatistics -identity $_).totalitemsize
  $count=(Get-MailboxStatistics -identity $_).itemcount
  $email = $email.Local + "@" + $email.Domain
  $object = New-Object -TypeName PSObject
  $object | Add-Member -Name 'Email' -MemberType Noteproperty -Value $email
  $object | Add-Member -Name 'Count' -MemberType Noteproperty -Value $count
  $object | Add-Member -Name 'Size' -MemberType Noteproperty -Value $size
  $array += $object

  }
  $array | export-csv C:\contoso.com.csv -notypeinformation
```

```eval_rst
  .. title:: Microsoft Exchange PowerShell quick commands
  .. meta::
     :title: Microsoft Exchange PowerShell quick commands | UKFast Documentation
     :description: A list of quick PowerShell commands for Microsoft Exchange
     :keywords: ukfast, windows, exchange, powersell, quick, command, one, liner, output, cloud, server, virtual
