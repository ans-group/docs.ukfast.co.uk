# Configuring a Replication job

Before configuring your replication job please ensure you have read through this document: [Veeam Replication Jobs](veeam_replication_jobs.md)

## Creating the Job
1. Open **Veeam Backup & Replication Console** and connect to your Veeam server
2. Navigate to **Home**
3. On the top bar, select **Replication Job** > **Virtual Machine**

![Create Replication Job](files/createreplicationjob/createreplicationjob.png)

### Name
1. Enter a name for the replication job and a description if needed (something that makes it easy to reference which VMs are in the job)
    1. **Replica seeding** - Used if there has been a copy of your backups shipped to us and uploaded on to our Veeam environment.
    2. **Network remapping** - <span style="color:green">**(enable)**</span> Used to map the internal networks on your current VMs to the internal networks UKFast has provided to you.
    3. **Replica re-IP** - <span style="color:red">**(do not enable)**</span> - Used when your DR sites use different internal networks to your production. This is not required when replicating to UKFast, as you will keep your current internal IPs.

![Replication Job - Name](files/createreplicationjob/createreplicationjob_name.png)

### Virtual Machines
1. **Add** - Select the VMs that you would like to replicate in this job<br />
    1. **Exclusions** - You have the option to exclude specific disks on VMs from being replicated. You may want to do this if you want to save your Cloud Connect storage and there is a non-critical data disk that won't be needed in the event of a DR situation.
    2. **Source** - You can choose to obtain the replication data from a Veeam backup rather than taking it directly from a snapshot on the VM. This is useful if you want to limit the snapshots on a VM and there aren't strict RPO requirements. <span style="color:red">**This will only replicate data from the latest backup, so enable with caution.**</span>

![Replication Job - Virtual Machine](files/createreplicationjob/createreplicationjob_virtualmachine.png)


### Destination
1. Under "Host or cluster" select **Choose** > **Cloud host** > select the UKFast Service Provider (UKFast’s external DNS name with your login name after in brackets) > Click "OK"
2. Under "Datastore" ensure that your datastore is select. If you have multiple, select the relevant one.

![Replication Job - Destination](files/createreplicationjob/createreplicationjob_destination.png)

### Network

Here you’ll create your network mappings. When you create a mapping all VMs on the "source network" at your site will be connected to the "target network" at UKFast. You should have a dedicated target network for each of the source networks which you are replicating VMs from.


1. Select "Add" to create a network mapping > select the "source network" and "target network"

![Replication Job - Network](files/createreplicationjob/createreplicationjob_network.png)

### Job Settings
1. **Repository for replica metadata** - Select a local repository for replica metadata. You will need on average 128MB of storage for every 1TB replicated, but this could vary.
2. **Replica name suffix** - This shows up within UKFast’s VMware environment, so we recommend that it is left as the default "_replica"
3. **Restore points to keep** - This specifies the amount of restore points that will be available when performing a failover; the maximum number possible is 28. The time difference between each restore point is defined by the schedule that is chosen in a later step (i.e. if you choose an hourly replication with seven restore points, you will have seven hours’ worth of restore points, each an hour apart. Depending on the amount of data change between each restore point these have the potential to take up a considerable amount of space, due to them being stored in a VMware snapshot.

4. **Advanced**
    1. **Storage optimisation** - This setting needs changing to "WAN Target" to ensure the replication jobs get the best performance when replicating over the internet to UKFast
    2. **Guess quiescence** - on the "vSphere" page there is an option "Enable VMware Tools quiescence", which is disabled by default. It is recommended to leave this disabled due to the potential impact caused when the VM is stunned, unless you definitely need it enabled.

![Replication Job - Job Settings](files/createreplicationjob/createreplicationjob_jobsettings.png)

### Data Transfer

Section to configure WAN accelerators, these are only beneficial to use when you have a network upload speed of lower than 60Mb/s. If you have not purchased a WAN accelerator from UKFast, you only need to complete step 1 ("Source Proxy"). You cannot configure one at your side if it hasn't been enabled on the service provider’s end.

Sizing information for WAN accelerators can be found on Veeam’s website  - [WAN accelerator sizing](https://helpcenter.veeam.com/docs/backup/vsphere/wan_accelerator_sizing.html?ver=100). We generally recommend a starting point of the following:  
* Hard disk size - 10% of total data that requires replicating
* 4 CPUs
* 16GB RAM


1. **Source proxy** - we would generally recommend this is left as the default "Automatic Selection" unless you have any specific requirements.
2. **Through built-in WAN accelerators** - if you have purchased a WAN accelerator from UKFast, select this option. 
    1. **Source WAN accelerator** - select the WAN accelerator at your site to be used for this replication job. It's recommended the WAN accelerator is set up as a separate virtual machine and not installed on the Veeam Backup and Replication Server.
    2. **Target WAN accelerator** - select the WAN accelerator at UKFast’s site to be used for this replication job.

    ![Replication Job - Data Transfer](files/createreplicationjob/createreplicationjob_datatransfer.png)


### Guest processing
1. **Enable application-aware processing** - you should consider enabling this option on certain VMs to assist in creating consistent backups for the likes for Exchange, database VMs or AD. You will need to provide Guest OS administrator credentials in order for this to work successfully.

![Replication Job - Guest Processing](files/createreplicationjob/createreplicationjob_guestprocessing.png)

### Schedule
**If you are running the replication as a one-time job you can skip past this page.**

1. **Run the job automatically** - Schedule the job to run daily, monthly or periodically specifying minutes or hours. You also have the option to select the job only to run on certain days, months or at certain times if using the periodically option.
2. **Automatic retry** - We find the default settings here usually suffice, but you have the option to change this if you have a specific need.
3. **Terminate job if it exceeds allowed backup window** - Caution should be applied before enabling this option, as it could result in a backup that wasn't necessarily going to fail being cancelled early

![Replication Job - Schedule](files/createreplicationjob/createreplicationjob_schedule.png)


```eval_rst
   .. meta::
      :title: Configuring a replication job | UKFast Documentation
      :description: How to configure a replication job to UKFast
      :keywords: ukfast, cloud, ecloud, public, hosting, infrastructure, vmware, draas, veeam, connect, dr, replication, backup

