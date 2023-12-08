# Technical Information

FASTcloudbackup is based on Commvault technology and software, and consists of 4 primary components:
* Web console – consists of the web front end, which links into the CommCell
* CommCell – handles configuration and management
* `CVStorage` – data storage
* FASTcloudbackup agents – FASTcloudbackup currently supports x64 Windows machines and the CentOS Linux distribution

All the UKFast infrastructure used to host FASTcloudbackup is designed to N+1 standards, including:
* Cisco ASA Firewalls and Cisco 3K switches
* UKFast Load Balancers
* VMware vSAN

UKFast data centres are ISO 27001 certified, PCI-compliant and secured up to UK government IL4 standards.  Your solution is protected by exceptional levels of both physical and virtual security at all times.

## Web console

The web console is the front end management interface for FASTcloudbackup. The components include:-
* UKFast Load Balancers – used to load balance traffic to the web front ends
* Bespoke Commvault web server service to deliver the web management console
* Commvault Communications Service – to handle changes to scheduling/backup sets
The web servers are installed outside of the DMZ, and traffic is passed through to the CommCell on secure ports.

__Encryption__

To protect customer data and changes made, the web console servers support TLS 1.2 with up to 256 bit AES encryption and no less than 128 bit encryption, with the negotiation to TLS/AES-256 dependent on whether the end user's device or proxy supports TLS/AES-256.

__Access/Security__

FASTcloudbackup is a secure, self-managed platform.  Each end user will be provided with their own login credentials, supplied via MyUKFast. End user accounts can login to the web console and manage all aspects of backups and restores

## CommCell

The CommCell is used to manage jobs, communicate with web console servers, storage and FASTcloudbackup agents.

The following process describes a backup job:
1. Client logs into web console and manually initiates a backup, or a backup runs automatically as previously scheduled
2. The request is relayed to the CommCell
3. The CommCell then communicates with both the FASTcloudbackup agent on the device to be backed up, and the storage via media agent servers, to ensure that it has a connection to both, and that the customer account has sufficient storage quota to run the job
4. The media agent will connect to the FASTcloudbackup agent and begin the transfer of data. This transfer uses AES encryption (<nospell>RijnDael</nospell>), making use of Commvault's propriety encryption library - Commvault Cryptographic Library Version – 1.0 (FIPS 140-2 Certified)
5. The media agent also updates the CommCell with progress information, which is passed back to the web console server and displayed in the console.

## `CVStorage`

The storage consists of multiple Dell R730 servers with RAID10 raid sets, providing redundancy at the hardware level. On the software layer, integrity checks are performed at the block-level by the media agent, which is checked with CRC32.

All backup data is encrypted with AES encryption (<nospell>RijnDael</nospell>) and is encrypted both in transit and at rest. The only time data is decrypted is when a restore request is carried out, and this is performed locally by the agent.

The storage is accessed via media agent servers - the server which actively writes the backup data to the storage, and also connects through to the clients.

## FASTcloudbackup agents

FASTcloudbackup agents can be downloaded via the web console, and provide the functionality and connectivity required for backups to be performed.  The agent provides file-level backups and performs deduplication and compression of data before this is transferred to the storage servers.

```eval_rst
   .. title:: Technical information on FASTcloudbackup
   .. meta::
      :description: Technical information on FASTcloudbackup | ANS Documentation
      :keywords: ukfast, FASTcloudbackup
```
