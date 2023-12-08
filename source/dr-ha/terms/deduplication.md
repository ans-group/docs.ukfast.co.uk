# Deduplicated Backups
Some backup applications such as Commvault and DPM offer to deduplicate your data to greatly reduce the required amount of space to store your backed up data.

When your data is backed up it is divided into "blocks" of data. The size of blocks can vary, but usually they are close to 64KB in size.

Because of this, many blocks are actually identical and saving multiple copies of the same block of data takes up unnecessary space.

Deduplication means that only the unique blocks of data are kept and stored, and any duplicate blocks are referenced to the unique blocks that are already stored.

This is done by using clever algorithms that generate digital signatures from blocks. Any blocks that generate the same signature as a stored block is discarded and referenced to the original.

```eval_rst
   .. title:: Deduplicated Backups
   .. meta::
      :title: Deduplicated Backups | ANS Documentation
      :description: Information about deduplication offered by backups software
      :keywords: Backups, dedup, commvault, dpm
```
