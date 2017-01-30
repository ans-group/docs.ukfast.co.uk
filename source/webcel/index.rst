======================
Webcelerator
======================

The Webcelerator (or "WebCel") is a caching appliance which sits in-front of your server solution and acts as a reverse proxy for your site.

Static content, such as CSS, JavaScript, and images are cached and served directly from the Webcelerator instead of loading from your backend server - freeing up resources on the backend to perform more important tasks like database queries or processing PHP.

We also perform optimisation of the content stored in the Webcelerator cache to serve it more quickly than it may have been served from the backend directly.

With a Webcelerator in place, we can also implement custom configuration to perform some more advanced routing of traffic, including load balancing over more than one backend; routing traffic to different backends based on domain; and presenting a maintenance page in the event that your backends are offline.

-------------------
Solution Diagram
-------------------

.. image:: images/WebCel-solution-diagram.png

-------------------
Documentation
-------------------

.. toctree::

  gettingstarted
  ssl
  purge
