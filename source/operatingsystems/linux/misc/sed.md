# The sed command

The sed command is used to edit text files and generally its most common use is to replace all occurrences of a word in a file. This is extremely helpful in situations where a configuration file has a lot of instances of the same word that needs replacing throughout the file.

For example if you were to copy a configuration to use for a new site and wanted to replace all instances of the original domain with the new domain then you could use this command. The example below replaces all instances of ukfast.co.uk with ukfast.net and

```bash
  sed 's/ukfast.co.uk/ukfast.net/g' ukfast.co.uk.conf > ukfast.net.conf
```

```eval_rst
  .. title:: Using the SED command in Linux | UKFast Documentation
  .. meta::
     :title: Using the SED command in Linux | UKFast Documentation
     :description: Information and guidance on using the SED command to edit text files in Linux
     :keywords: ukfast, server, linux, sed, command, files, edit, text, editor, cloud
