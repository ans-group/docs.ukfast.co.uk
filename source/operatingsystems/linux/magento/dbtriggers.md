# Magento Database Triggers

When performing actions in the admin area (Saving products for example) and you get a similar error message to:

```bash
SQLSTATE[HY000]: General error: 1449 The user specified as a definer ('username'@'localhost') does not exist, query was: UPDATE `catelog_product_entity` SET `attrivute_set_id` =?, `sku` =?, has_options` =?, `required_options` =?, `created_at` =?, `updated_at` =? WHERE(entity_id = '4062)
```

## Export Database Triggers

```bash
~]$ mysqldump -uroot --triggers --add-op-trigger --no-create-info --no-data --no-create-db --skip-opt DBNAME > /tmp/DBNAME_triggers_export.sql
```

## Search and Replace Username In Triggers

```bash
~]$ sed -i 's/172.25.124.38/172.25.124.\%/g'  /tmp/DBNAME_triggers_export.sql
```

## Drop Database Triggers

## Import Triggers

```bash
~]$ mysql DBNAME <  /tmp/DBNAME_triggers_export.sql
```

```

```eval_rst
  .. meta::
     :title: Magento Database Triggers | UKFast Documentation
     :description: A guide to export, edit and then import database triggers
     :keywords: ukfast, linux, database, triggers, install, centos, cloud, server, virtual, Magento

