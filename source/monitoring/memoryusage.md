# Memory usage

The following command can be used to show your current memory usage:

```bash
  free -m
```

This will return output similar to the following:

```console
  # free -m
  total       used       free     shared    buffers     cached
  Mem:          7872       2238       5634          0        183       1702
  -/+ buffers/cache:        351       7520
  Swap:            0          0          0
```

At first glance, it may seem that the server only has `5.3G` available, but the value we're interested in is the one just below it, in the `-/+ buffers/cache` section. This takes Linux's native disk caching into account, which can otherwise makes it look as though most of your RAM is being used up.

For further explanation, see <http://www.linuxatemyram.com/>

```eval_rst
  .. meta::
     :title: Memory Usage | UKFast Documentation
     :description: Information on memory usage
     :keywords: ukfast, monitoring, memory, ram, usage, check, cloud, hosting

