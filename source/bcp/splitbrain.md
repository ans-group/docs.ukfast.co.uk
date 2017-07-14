# Split brain

Occasionally clusters can suffer what is known as a "split brain", which is where both sides of the cluster believe that they are the active node for an active / passive service.

This is usually indicative of a network failure, or a problem with replication.

```eval_rst
.. warning::
   **If you encounter a split brain, please contact support for further assistance.**
```

## Resolution

Resolving a split brain situation usually involves one of the following:

1. Fixing the underlying issue that caused the split brain, and then promote the side of the cluster which held the problem resource group to master, demote the other node, and confirm replication catches up.

    **or:**

2. After resolving the underlying issue, find which node held the resource before going split brain, and therefore holds the most up-to-date data. We then instruct DRBD to delete the data of the other node, and overwrite with the data we've picked as being most recent.

    **or:**

3. Blank the DRBD volumes and re-establish replication, then perform a restore from the most recent backup.

However, these situations tend to vary between incidents, so we may take a different course of action when presented with a different problem or split brain cause.
