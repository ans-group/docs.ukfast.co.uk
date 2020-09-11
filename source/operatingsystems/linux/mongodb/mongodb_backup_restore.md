# How to Backup & Restore a MongoDB Database

## File Formats

`MongoDB` uses the `mongodump` tool to export databases. This can export to the following formats;

- **BSON** (Default for data)
- **JSON** (Default for collection metadata)
- **CSV** (specify with --type csv)
- **TSV** (specify with --type tsv)

**BSON** is the recommended database export format.

## Exporting all databases

To export all databases, `cd` to a directory path of your choosing, and run the following command

```bash
mongodump
```

This will automatically create a `/dump` folder in that location. Alternatively, specify a folder path with the following command.
```bash
mongodump --out /your/file/path
``` 

## Exporting a single database

To export a single database, `cd` to a directory path of your choosing, and run the following command

```bash
mongodump --db=yourdb
```

``` note:: Commvault does not currently offer plugin/agent for MongoDB specifically, so this would only be backed up in a File Level backup.
```

## Restoring a MongoDB Database

``` warning:: If requesting a database restore from UKFast Support, please provide the directory for your database dumps. Without this, only /var/lib/mongodb would be restored.
```

To restore from a database backup you will need to use the `mongorestore` command. To import a dump, you just need to specify the location of the restore folder, eg.

```bash
mongorestore dump/
```
This will create the *database* and *collections* specified within the dump data.

To import a *specific collection* from this dump, you would use the following syntax

```bash
mongorestore --nsInclude=testdb.orders /dump
```

## Restoring from JSON

Though not recommended, if your dump is in `JSON v2.0` format you can use the `mongoimport` command to import your database.

```bash
mongoimport --db yourdb --file /path/to/database/dump.json
```
If using `JSON v1.0`, you should use the above with the addition of the `--legacy` flag.



```eval_rst
  .. title:: MongoDB | How to Backup & Restore a MongoDB Database
  .. meta::
     :title: How to Backup & Restore a MongoDB Database | UKFast Documentation
     :description: How to Backup & Restore a MongoDB Database
     :keywords: mongodb, backup, restore, howto, guide, tutorial
```
