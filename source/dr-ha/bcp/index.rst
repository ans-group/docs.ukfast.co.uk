=================================
Business Continuity Platform
=================================

The Business Continuity Platform (or "BCP" / "cluster") is a highly-available configuration of `Linux </operatingsystems/linux/index.html>`_ servers, allowing for failover in the event of a node going offline and for balancing workload across more than one server when all members are operational.

More information about the BCP platform is available on `our website <https://www.ukfast.co.uk/business-continuity-platform.html>`_.

.. seealso::
   BCP solutions vary depending on client requirements, so the information provided here may be inaccurate for your individual deployment; however for most standard BCP solutions the principles will remain the same.

There are a number of differences between managing a standalone Linux server, and managing a clustered Linux server, so it would be advisable to read over this documentation before using your cluster for the first time.

.. warning::
   **Do not** use the ``service`` or ``systemctl`` commands to start or stop `clustered services <management.html>`_. Doing so will likely cause your cluster to `fence <fencing.html>`_.

----------
Contents
----------

.. toctree::
  :maxdepth: 2

  generalinformation
  management
  drbd
  unison
  fencing
  software
  splitbrain
  faq
