# Microsoft SQL Backups
With our UKFast Advanced backup options, we offer a range of backups for your SQL databases.

Most commonly used are a combination of Full and Transactional backups (typically one full backup a week and daily transactional backups).

## A Full Backup
A full backup takes a full backup of your SQL databases and updates the database and SQL to log the last time a database backup was completed.

## A Transactional Backup
If your databases are in Full Recovery Model, any changes made to the databases are written to a transactional log. A Transactional backup backs up only this log, to log what changes have been made since the last backup (full or transactional).

Running a transactional backup has a number of advantages. As we are only backing up changes made since the last backup, it is likely the backup completes in a much shorter time than a full backup would take, saving resources on the solution.

Also backing up transactional logs adds the ability to be able to do 'Point in time restores', so we can replay the transactional logs up to a point in time, effectively restoring your data as it was to the minute and second.

## A Differential Backup
As databases in Simple Recovery Model do not log changes to a transactional log, transactional logs are not possible to be ran against them. Instead, Differential backups can be ran, which backups up only the changes made from the last full backup.

These can be more resource intensive than a transactional backup and do not enable to 'Point in time restore' capability, but are still less intensive than running a Full backup every time.

## A Full Copy-Only Backup
From time to time you may want to perform your own backup of your databases, without interrupting the log chain of your transactional backups.

To do this, you can run a Full Copy-Only backup, which takes a full backup of your database without modifying the backup time and transactional logs.

```eval_rst
   .. title:: Microsoft SQL Backups
   .. meta::
      :title: Microsoft SQL Backups | UKFast Documentation
      :description: Guide for managing Microsoft SQL (MSSQL) backups
      :keywords: Backups, MSSQL, Microsoft SQL
```
