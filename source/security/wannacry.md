# Wana Decryptor / Wana Decrypt0r 2.0 / WannaCry

## How is this malware distributed?

Wana Decrypt0r 2.0 ransomware is spreading via an exploit named 'EternalBlue' allegedly discovered by the NSA which was then leaked online by a group of hackers known as 'The Shadow Brokers'. Since its initial detection this malware has caused serious issues for the UK National Health Service, Telefonica, Chinese Universities and the Russian Interior Ministry.

The exploit works by gaining access to a remote system via the SMBv1 (Server Message Block) protocol which
can be exploited via the following ports.

* TCP 445 (SMB)
* TCP 139 (Direct SMB)
* UDP 137 (NetBIOS API)
* UDP 138 (NetBIOS API)
* UDP 139 (NetBIOS API)

UKFast close the above TCP/UDP ports with our default Firewall configuration, these ports may be open if requested manually or manually changed via the MyUKFast Firewall Portal.

Microsoft have recently patched this exploit via the following security bulletin which covers all Microsoft operating systems later than Windows Vista. Older operating systems such as Windows 2003 and Windows XP are not covered via the SMB patch automatically. Older operating systems will require the SMB v1 protocol be patched manually (see [2003/XP section](https://technet.microsoft.com/en-us/library/security/ms17-010.aspx) for more details.

Affected Microsoft Operating Systems:
* Windows Server 2003 x86/x64
* Windows XP x86/x64
* Windows Server 2008 x86/x64
* Windows Vista x86/x64
* Windows Server 2008 R2 x86/x64
* Windows 7 x86/x64
* Windows Server 2012 x64
* Windows Server 2012 R2 x64
* Windows 8/8.1 x86/x64
* Windows 10 x86/x64
* Windows 2016 x64

UKFast recommend this security patch be applied with immediate effect if not already installed on your Windows platform. Upon installation of the security patch will require a server restart, we advise taking note of any highly available (HA) services and/or clusters when performing restarts. If you are unfamiliar with this process or require some assistance please contact our support team either via [MyUKFast](https://portal.ans.co.uk/pss/add.php), by emailing [support@ukfast.co.uk](mailto:support@ukfast.co.uk) or by calling 0800 230 0032.

Our support engineers are have been working around the clock since information became available to reduce any impact to our customer base and keep your systems secure and protected.

## How does this malware function?

Wana Decrypt0r utilises an embedded installer which extracts a password protected `.zip` archive. This archive has a number of randomly named executable files within which are run to execute the Wana Decrypt0r functionality. Once the executable files are present on the Windows file system, execution of the start-up tasks utilising the newly extracted `.exe`'s. The ransomware will then utilise the TOR client and TOR network to allow communication between the malware and its command and control to be performed via an encrypted near untraceable network. More information regarding TOR can be found on Wikipedia [here](https://en.wikipedia.org/wiki/Tor_(anonymity_network))

Once the ransomware is present on the operating system, the malware will perform remote connectivity to the following `.onion` addresses within the TOR network

- `gx7ekbenv2riucmf.onion`
- `57g7spgrzlojinas.onion`
- `xxlvbrloxvriy2c5.onion`
- `76jdd2ir2embyv47.onion`
- `cwwnhwhlz52maqm7.onion`

Once connected, the malware will execute a command to attempt to modify permissions on all available file system folders the malware resides within to provide 'Everyone' full access;

```text
icacls . /grant Everyone:F /T /C /Q*
```

Once complete the malware then performs a `taskkill` of all database applications to allow for running database content to also be encrypted;

- `taskkill.exe /f /im mysqld.exe`
- `taskkill.exe /f /im sqlwriter.exe`
- `taskkill.exe /f /im sqlserver.exe`
- `taskkill.exe /f /im MSExchange`
- `taskkill.exe /f /im Microsoft.Exchange`

Upon confirmation of the `taskkill.exe` being run, the ransomware will start to perform encryption of all files that access rights permit. The files encrypted would be of the following extension types, these are the current known types:

`*.der`, `.pfx`, `.key`, `.crt`, `.csr`, `.pem`, `.odt`, `.ott`, `.sxw`, `.stw`, `.uot`, `.max`, `.ods`, `.ots`, `.sxc`, `.stc`, `.dif`, `.slk`, `.odp`, `.otp`, `.sxd`, `.std`,
`.uop`, `.odg`, `.otg`, `.sxm`, `.mml`, `.lay`, `.lay6`, `.asc`, `.sqlite3`, `.sqlitedb`, `.sql`, `.accdb`, `.mdb`, `.dbf`, `.odb`, `.frm`, `.myd`, `.myi`, `.ibd`,
`.mdf`, `.ldf`, `.sln`, `.suo`, `.cpp`, `.pas`, `.asm`, `.cmd`, `.bat`, `.vbs`, `.dip`, `.dch`, `.sch`, `.brd`, `.jsp`, `.php`, `.asp`, `.java`, `.jar`, `.class`, `.wav`,
`.swf`, `.fla`, `.wmv`, `.mpg`, `.vob`, `.mpeg`, `.asf`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wma`, `.mid`, `.djvu`, `.svg`, `.psd`, `.nef`, `.tiff`, `.tif`, `.cgm`, `.raw`,
`.gif`, `.png`, `.bmp`, `.jpg`, `.jpeg`, `.vcd`, `.iso`, `.backup`, `.zip`, `.rar`, `.tgz`, `.tar`, `.bak`, `.tbk`, `.PAQ`, `.ARC`, `.aes`, `.gpg`, `.vmx`, `.vmdk`,
`.vdi`, `.sldm`, `.sldx`, `.sti`, `.sxi`, `.hwp`, `.snt`, `.onetoc2`, `.dwg`, `.pdf`, `.wks`, `.rtf`, `.csv`, `.txt`, `.vsdx`, `.vsd`, `.edb`, `.eml`, `.msg`, `.ost`,
`.pst`, `.potm`, `.potx`, `.ppam`, `.ppsx`, `.ppsm`, `.pps`, `.pot`, `.pptm`, `.pptx`, `.ppt`, `.xltm`, `.xltx`, `.xlc`, `.xlm`, `.xlt`, `.xlw`, `.xlsb`, `.xlsm`,
`.xlsx`, `.xls`, `.dotx`, `.dotm`, `.dot`, `.docm`, `.docb`, `.docx`, `.doc`, `*`

Once encryption has taken place on all the above file extension types, a command is performed to remove all available shadow copies, Windows Backup files and to prevent any access to the Windows Recovery feature on start-up:

Command performed;

```test
C:\Windows\SysWOW64\cmd.exe /c vssadmin delete shadow /all /quiet & wmic shadowcopy delete & bcdedit /set {default} boostatuspolicy ignoreallfailures & bcdedit /set {default} recoveryenabled no & wbadmin delete catalog –quiet
```

The above command significantly reduces the available backup set, however if you are protected by alternate UKFast backup systems, please contact our support team regarding a restore request.

## What steps can be taken to mitigate this malware and prevent re-infection?

### Server Mitigation

* We recommend installing the Microsoft patch MS17-010 with immediate effect, if you require assistance with installation of this patch please contact our support team.
* Anti-Virus/Malware Protection
* UKFast have taken steps to include Wana Decrypt0r mitigation within our McAfee Access Protection ruleset as per [McAfee's recent KB article](https://kc.mcafee.com/corporate/index?page=content&id=KB89335). If you are not currently using McAfee and require UKFast to install/manage McAfee within your Windows infrastructure, please contact our UKFast support team to arrange installation.
* Enabling software firewall(s) between servers within the same subnet. Windows Firewall can be configured to prevent communication on SMB protocol ports between servers, this can be utilised to reduce risk of malware spread to multiple servers behind a firewall.
* Disabling the SMB protocol - If you have no requirement for the SMB protocol to be utilised, this can be disabled via registry changes. Disabling SMB requires a server restart, SMB is required for certain server functionality, please contact our support team before proceeding with any changes to live systems.
* AppLocker implementation (available within Windows Server 2008 R2 and above) - AppLocker can be implemented to allow system administrators to impose restrictions on user access of executables, prevention of user run scripts, denial of user performed software installation/updates and prevention of changes to system `.dll` and `.ocx` files.  Click [here for details](https://technet.microsoft.com/en-us/library/dd759117(v=ws.11).aspx)
* Hosts file DNS redirection - <nospell>Wana DeCrypt0r</nospell> 2.0 is known to retrieve a TOR client via the following address; https://dist.torproject.org/torbrowser/6.5.1/tor-win32-0.2.9.10.zip
The TOR `.onion` network is also utilised
Adding a new HOSTS entry to redirect DNS lookups to this site and onion network;

```test
0.0.0.0 dist.torproject.org
0.0.0.0 gx7ekbenv2riucmf.onion
0.0.0.0 57g7spgrzlojinas.onion
0.0.0.0 xxlvbrloxvriy2c5.onion
0.0.0.0 76jdd2ir2embyv47.onion
0.0.0.0 cwwnhwhlz52maqm7.onion
```

The Windows HOSTS file can be found in the following location;

```text
C:\Windows\System32\Drivers\etc\HOSTS
```

Open with an administrative notepad to add any additional changes

Addition of this HOSTS entry will prevent the TOR aspect removing some command and control aspect of the ransomware. Preventing external connectivity to the malware by forcing the DNS request to a null address.

* UKFast's default firewall configuration excludes access on the above TCP and UDP ports for public access, however these ports can be modified by your team(s) to be open for public access. To clarify if your firewall has these ports open or not please login to the [MyUKFast firewall section](https://portal.ans.co.uk/server/firewalls.php) to verify the firewall port configuration.  UKFast recommends the SMB protocol TCP and UDP ports be closed for public access if open, we do not recommend allowing public access to the SMB protocol as standard practice. If you are unfamiliar with firewall ports or require additional assistance, please contact our support team on any of the following;
   * [Priority Support Request](https://portal.ans.co.uk/pss/add.php)

   * Email [support@ukfast.co.uk](mailto:support@ukfast.co.uk)

   * Telephone 0800 230 0032

* UKFast recommends a review of domain and local administrative accounts. Allowing end users to have administrative access is quite common when faced with permission related problems. We do not recommend allowing user accounts to have domain or local administrative access.
* Disable or removal of unnecessary domain or local user accounts. Commonly missed is the removal of accounts which are no longer in use, ex-employees or accounts for previously installed service(s) and/or software packages. We recommend these be removed if confirmed as no longer required.
* Force password complexity rules with regular password expiry to improve account security and prevent easy access to accounts.
* Require email attachments to have administrative review prior to reaching the recipient target. Although this process can require a large amount of time dedicated to management, this will reduce the impact of email based attack vectors by allowing administrative users to review all attachments safely.
* Education of end users to reduce the potential attack surface. End users may not always be tech savvy and may not easily spot an unsolicited email attachment. Education of end users is paramount and should be taken very seriously by IT administrators to improve the security of their infrastructure with education of their end user base.

### Windows 2003 & XP

Microsoft have released patching for Windows XP which is available via the Microsoft Update Catalog. Although these operating systems are no longer within Microsoft's supported operating systems, they have provided patching availability which needs to be applied manually.

Patches for older operating systems are available [here](http://www.catalog.update.microsoft.com/Search.aspx?q=KB4012598&ranMID=24542&ranEAID=TnL5HPStwNw&ranSiteID=TnL5HPStwNw-veALAaECnpbc3sX3qwgd3Q&tduid=(f359256c2e7587423e1da93cc0f03bff)(256380)(2459594)(TnL5HPStwNw-veALAaECnpbc3sX3qwgd3Q)())

### Windows 2003 & XP – KB4012598
UKFast recommends upgrading the operating system at your earliest convenience. Windows 2003 and XP are no longer within support scope for standard patching and will be subjected to a number of zero-day exploits which will leave your server at risk.

### Paying for decryption?
UKFast cannot endorse the payment of ransomware to third parties. This decision will require serious deliberation within your company to choose the desired option for your business.

## Contacting UKFast Support
Please don't hesitate to contact our support professionals who can provide assistance and information surrounding this malware
* [Priority Support Request](https://portal.ans.co.uk/pss/add.php)

* Email [support@ukfast.co.uk](mailto:support@ukfast.co.uk)
* Telephone 0800 230 0032

```eval_rst
   .. title:: Patching the WannaCry vulnerability
   .. meta::
      :title: Patching the WannaCry vulnerability | UKFast Documentation
      :description: Information on patching the WannaCry vulnerability
      :keywords: ukfast, security, pci, dss, vulnerability, cryptolock, wannacry
```
