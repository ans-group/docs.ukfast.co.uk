# Magento Database Triggers

When performing actions in the Magento admin area (Saving products for example) and you get a similar error message to:

```bash
SQLSTATE[HY000]: General error: 1449 The user specified as a definer ('username'@'localhost') does not exist, query was: UPDATE `catelog_product_entity` SET `attrivute_set_id` =?, `sku` =?, has_options` =?, `required_options` =?, `created_at` =?, `updated_at` =? WHERE(entity_id = '4062)
```

The database triggers may have been impotred with the wrong username defined in the triggers. You can correct this with the following process:

## Export Database Triggers

Replace DBNAME with the database name in question:
```bash
~]$ mysqldump --triggers --no-create-info --no-data --no-create-db --skip-opt DBNAME > /tmp/DBNAME_triggers_export.sql
```

## Replace The Incorrect Useranme/Hostname

Review the file above and look for the DEFINER, exmaple:

```bash 
/*!50003 CREATE*/ /*!50017 DEFINER=`username`@`localhost`*/
```

We need to replace the username and hostname in the file /tmp/DBNAME_triggers_export.sql with the username and host defined in the Magento local.xml/env.php:
```bash
~]$ sed -i 's/username/newusername/g' /tmp/DBNAME_triggers_export.sql
~]$ sed -i 's/localhost/22.93.135.106/g' /tmp/DBNAME_triggers_export.sql
```

## Drop Database Triggers

Before you import the triggers that now have the correct username in, we need to drop the triggers with the wrong usernames. Replace DBNAME with the database name in question and run the following:

```bash
~]$ mysql -ANe "SELECT CONCAT('DROP TRIGGER ',trigger_name,';') FROM information_schema.triggers WHERE trigger_schema = 'DBNAME';" | sed s'/\|//g' > /tmp/DBNAME_drop_statement.sql
~]$ mysql DBNAME < /tmp/DBNAME_drop_statement.sql
```

## Import Triggers

No we have removed the triggers in the database we need to import the triggers again with the correct username:

```bash
~]$ mysql DBNAME < /tmp/DBNAME_triggers_export.sql
```

```eval_rst
  .. meta::
     :title: Magento Database Triggers | UKFast Documentation
     :description: A guide to export, edit and then import database triggers
     :keywords: ukfast, linux, database, triggers, install, centos, cloud, server, virtual, Magento

