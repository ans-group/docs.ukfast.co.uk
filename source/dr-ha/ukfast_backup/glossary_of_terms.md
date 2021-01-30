# Glossary of Terms

* **Backup Exclusions** - A list of locations or files that will NOT be backed up upon the schedule execution.
* **Backup Job** – An instance of a schedule that is backing up files.
* **Backup Quota** – A storage space that is used to store backups on the server.
* **Backup Schedule** – A set of instructions that are executed in a specific order to produce a set of backed up files.
* **Backup Source (Includes)** – A list of locations or files that will be backed up upon the schedule execution.
* **Backup Type: Full** - A backup that has been performed and backed up the whole source location.
* **Backup Type: Incremental** – A backup that has been performed and only backed up files that were changed from the previous backup. A backup server will always do a Full Backup first, and any sub-sequential backups performed will be incremental ones.
* **Directory** – a file which consists solely of a set of other files (which may themselves be directories).
* **Files Processed** – The number of files backup server processed during the backup.
* **Files Transferred** – The number of files backup server actually transferred to itself during backup. The reason why files processed and files transferred will often differ is because backup server won't transfer excluded files, or files it already has backed up (duplicates).
* **Force Stop Job** – forces the running job (backup or Restore) to be aborted immediately.
* **Full Restore** - A restore process where all files of the backup are being restored.
* **Partial Restore** - A restore process where only selected files of the backup are being restored.
* **Recurrence** – The amount of time backup server waits between executing the schedule. Recurrence is usually a value of days, while start / end time is more granular period of time.
* **Restore Job** – A set of backed up files that are being restored.
* **Retention Period** – A number of iterations the backup server will keep backups. An iteration period of 7 will maintain only 7 backups, meaning that upon 8th backup being completed, the oldest backup will be deleted.
* **Start Time / End Time** – A time window when the backup server is actively trying to execute any enabled schedules to produce backups.
* **Wildcard** – an asterisk * symbol that denotes 'any' value.

```eval_rst
  .. title:: UKFast Backup Glossary
  .. meta::
     :title: UKFast Backup Glossary  | UKFast Documentation
     :description: General glossary of terms for backup
     :keywords: ukfast, backup, files, folders, recovery
