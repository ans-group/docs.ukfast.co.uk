# Failover costs
There are two different types of DRaaS solutions, Public and Private. This will give you a rough summary of how the DRaaS costs are calculated.

## DRaaS Public Solutions
DRaaS Public solutions replicate in to an eCloud Public environment in the given DRaaS Region. This means that when you failover your VMs will run on shared hypervisors.

In this scenario, there are two parts of the failover costings.

### Recurring costs
You will pay static monthly costs for:
- Per VM
- Per GB storage, at the 600 IOPs tier

### Failover Costs
When you failover, you will pay based on our eCloud Public billing model, pro rata'd hourly.

#### Compute costs
|                 | Monthly Cost | Hourly Cost |
|-----------------|--------------|-------------|
| Per vCPU        | £5.07        | £0.0069     |
| Per 1GB RAM     | £8.62        | £0.012      |
| Windows License | £12          | ~£0.0164    |

#### Storage Costs
All customers pay 20p per GB as a static monthly charge for the storage they require in DRaaS, which is the cost for the 600 IOPs tier.

If a client decides to increase the IOPs tier to 1200 or 2500 on a VM, they will pay the difference in cost pro rata hourly when they failover.

|           | Monthly Additional Cost per GB| Hourly Cost (100GB) |
|-----------|-------------------------|---------------------|
| 1200 IOPs | £0.10                   | £0.014              |
| 2500 IOPS | £0.35                   | 0.048               |


## DRaaS Private Solutions

DRaaS Private Solutions have a dedicated eCloud solution in the DRaaS region, which will be paid for by the client. Due to this, in most cases failover will not cost anything.

Every DRaaS private solution is different, so this should be confirmed with your Account Manager or Service Manager.



```eval_rst
   .. title:: Veeam Failover Costs
   .. meta::
      :title: Veeam Failover Costs | UKFast Documentation
      :description: Summary of DRaaS failover costs
      :keywords: ukfast,cloud,ecloud,public,hosting,infrastructure,vmware,draas,veeam,connect,dr,replication,backup,failover
```
