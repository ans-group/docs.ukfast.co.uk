======================
WebCelerator
======================

The WebCelerator (or "WebCel") is a caching appliance which sits in-front of your server solution and acts as a reverse proxy for your site.

Statis content, such as CSS, JavaScript, and images are cached and served directly from the WebCelerator instead of loading from your backend server, freeing up resources on the backend to perform more important tasks like database queries or processing PHP.

We also perform optimisation of the content stored in the WebCelerator cache to serve it more quickly than it may have been served from the backend directly.

With a WebCelerator in place, we can also implement custom configuration to perform some more advanced routing of traffic, including load balancing over more than one backend; sending some traffic to certain backends, and other traffic to other backends; and presenting a maintenance page in the event that your backends are offline.

-------------------
Solution Diagram
-------------------

.. image:: images/WebCel-solution-diagram.png

-------------------
Documentation
-------------------

.. toctree::

  ssl
