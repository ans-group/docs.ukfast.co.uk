# Mcafee Anti-Virus Supplied by UKFast

If you choose an to include an Anti-Virus as part of your server package with UKFast, Mcafee Anti-Virus is the Software which we will provide, This is a Managed, Enterprise Grade Anti-Virus package, which is deployed on to your solution and is configured using best practice policies. An overview of the configuration can be found below.


## Scanning Configuration

* The Virus Scanning Engine is configured to scan files when they are written to disk during real time scanning. We disable continous read scannning to prevent IO Saturation which would result in performance degradation.

* A Weekly scan is scheduled to scan all disks apart from any exclusions which have been specified, if  you wish to add, remove or modify exclusions on your anti-virus scan, please contact support via a ticket, making sure that you include your requirements within the ticket, and we will be able to action those changes for you.

* Scanning of remote directories is disabled by default, however NFS mounts will be scanned and viewed as a local disk.

* Scanning Schedules can be customised to your requirements, or they can be managed by yourself, If you would like to have a custom schedule or if you would like to manage your own scanning schedule, please contact support via a ticket, making sure that you include your requirements within the ticket, and we will be able to action those changes for you.


## Schedules

Details on the default scanning and update policies which are applied can be found below

### Default Managed Update Policy (Windows & Linux);
Start Time – 5:00AM
Frequency – Daily
Type - .DAT update (Any pending software updates/security fixes will also be applied)

### Default Managed Weekly Scan Policy (Windows VSE 8.8 Patch 8)
Start Time – 11:00PM
Frequency – Weekly (Sunday)
Scan type – All Files, Detect unwanted programs, Scan inside .zip/archive files, find unknown program/macro threats
Threat action – Clean First / Continue Scanning

### Default Managed Weekly Scan Policy (Linux VSE 1.9 / 2.0)
Start Time – 11PM
Frequency – Weekly (Sunday)
Scan type – All Files, Detect unwanted programs, Scan inside .zip/archive files, find unknown program/macro threats
Threat action – Clean First / Continue Scanning

