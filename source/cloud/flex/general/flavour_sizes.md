# eCloud Flex Flavours

Each instance on eCloud Flex comes in a variety of configurations called Flavours. The resources available for each of these flavours are shown in the table below:

|     Flavour    	| Disk Size (GB) 	| VCPUs 	| Memory (GB) 	| IOPS 	| Network (Mbps) 	|
|:--------------:	|:--------------:	|:-----:	|:-----------:	|:----:	|:--------------:	|
|  UKF2-cpu-2x12 	|       60       	|   2*  	|      12     	| 3000 	|     10,000     	|
|  UKF2-cpu-4x24 	|       60       	|   4*  	|      24     	| 3000 	|     10,000     	|
|  UKF2-cpu-6x36 	|       60       	|   6*  	|      36     	| 3000 	|     10,000     	|
|  UKF2-cpu-8x48 	|       60       	|   8*  	|      48     	| 3000 	|     10,000     	|
|   UKF2-io-1x2  	|       60       	|   1   	|      2      	| 5000 	|     10,000     	|
|   UKF2-io-2x4  	|       60       	|   2   	|      4      	| 5000 	|     10,000     	|
|   UKF2-io-4x8  	|       60       	|   4   	|      8      	| 5000 	|     10,000     	|
|  UKF2-io-8x16  	|       60       	|   8   	|      16     	| 5000 	|     10,000     	|
|  UKF2-mem-1x8  	|       60       	|   1   	|      8      	| 2500 	|     10,000     	|
|  UKF2-mem-2x16 	|       60       	|   2   	|      16     	| 2500 	|     10,000     	|
|  UKF2-mem-4x32 	|       60       	|   4   	|      32     	| 2500 	|     10,000     	|
|  UKF2-mem-8x64 	|       60       	|   8   	|      64     	| 2500 	|     10,000     	|
| UKF2-small-1x0 	|       60       	|   1   	|     0.5     	|  500 	|     10,000     	|
| UKF2-small-1x1 	|       60       	|   1   	|      1      	| 1000 	|     10,000     	|
|  UKF2-std-2x2  	|       60       	|   2   	|      2      	| 1000 	|     10,000     	|
|  UKF2-std-4x4  	|       60       	|   4   	|      4      	| 1000 	|     10,000     	|
|  UKF2-std-8x8  	|       60       	|   8   	|      8      	| 1000 	|     10,000     	|

\* = *UKF2-CPU-*\* *range has an increased clock speed offering superior performance over other flavours with identical quantities of CPUs.*

Additional storage is also available through attachable volumes, with each tier offering increasing IOPS and decreased access latency:

* **SATA** storage offers up to 500 IOPS and is ideal for storage of large files which are infrequently accessed and log files
* **SSD** volumes will perform in excess of 5,000 IOPS and are ideal for frequently accessed files, databases and web files
* **PCIE** drives brings performance of over 50,000 IOPS and are ideal for high performance databases and applications

  You can quickly calculate your cloud costs using our [eCloud Flex Calculator](https://www.ukfast.co.uk/calculate-ecloud-flex.html), and get started with a [free trial account](https://www.ukfast.co.uk/ecloud-flex-trial.html) to see if Flex is the right solution for your business.

```eval_rst
.. meta::
    :title: eCloud Flex Flavours | UKFast Documentation
    :description: Detailed guidance on the resources for each eCloud Flex Flavour
    :keywords: ecloud, flex, volume, instance, flavour, flavor, RAM, memory, CPU, clock speed, IOPS, network
```
