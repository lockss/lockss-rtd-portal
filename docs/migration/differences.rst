=======================================================
Appendix: Differences Between LOCKSS 1.x and LOCKSS 2.x
=======================================================

.. note::

   This document is under construction.

This document is aimed at LOCKSS 1.x users and summarizes some of the main differences between LOCKSS 1.x and LOCKSS 2.x.

-----------------
Technical Aspects
-----------------

.. list-table::
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10 45 45

   *  *  .. COMMENT Intentionally left blank
      *  LOCKSS 1.x
      *  LOCKSS 2.x
   *  *  Operating system
      *  **RHEL-compatible Linux flavors only.** The operating system to run LOCKSS 1.x can only be a RHEL-compatible flavor of Linux (RHEL, CentOS, Rocky Linux, Alma Linux OS, Oracle Linux...).
      *  **Most Linux flavors.** The operating system to run LOCKSS 2.x can be most flavors of Linux, including RHEL-compatible (RHEL, CentOS, Rocky Linux, Alma Linux OS, Oracle Linux...), Debian-compatible (Debian, Ubuntu, Linux Mint...), SUSE-compatible (SLES, OpenSUSE...), Fedora Linux, and more.
   *  *  Database
      *  **No embedded high-performance database.** LOCKSS 1.x can be configured to either run an embedded Apache Derby database, which is not high-performance, or use an external PostgreSQL database, which requires installing, configuring and administering PostgreSQL independently (on the same host as LOCKSS 1.x or elsewhere in your IT infrastructure).
      *  **Embedded high-performance database by default.** LOCKSS 2.x runs an embedded PostgreSQL database by default (or can alternatively be configured to use an external PostgreSQL database as in LOCKSS 1.x).

--------------
Node Operation
--------------

.. list-table::
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10 45 45

   *  *  .. COMMENT Intentionally left blank
      *  LOCKSS 1.x
      *  LOCKSS 2.x
   *  *  Installation
      *  **OS-specific installation process.** LOCKSS 1.x installation consists of installing software packages from default and custom RPM repositories, which is OS-specific. Integration scripts may exist to partially facilitate the process on some compatible operating systems.
      *  **Multi-OS installer.** LOCKSS 2.x comes with a single installer that can be downloaded and run on all compatible operating systems.
   *  *  Configuration
      *  **Configuration script.** LOCKSS 1.x is configured by answering questions from a script called :program:`hostconfig`.
      *  **Configuration script.** LOCKSS 2.x is configured by answering questions from a script called :program:`configure-lockss`.
   *  *  Modularity
      *  **Monolithic.** LOCKSS 1.x is a standalone application, including all available functionality of the system regardless of need.
      *  **Modular.** LOCKSS 2.x is a modular application, offering the user a configurable set of components to tailor different areas of available functionality to their need.

--------
Features
--------

.. list-table::
   :align: center
   :header-rows: 1
   :stub-columns: 1
   :widths: 10 45 45

   *  *  .. COMMENT Intentionally left blank
      *  LOCKSS 1.x
      *  LOCKSS 2.x
   *  *  APIs
      *  **Some SOAP APIs.** LOCKSS 1.x offers SOAP APIs to query some state information programmatically.
      *  **Full REST APIs.** LOCKSS 2.x components offer REST APIs to drive functionality and query state information programmatically. These REST APIs are available as OpenAPI specifications, which can be used to generate clients in a variety of programming languages and application frameworks.
   *  *  Web crawlers
      *  **LOCKSS Web crawler.** LOCKSS 1.x includes the built-in LOCKSS Web Crawler.
      *  **LOCKSS Web crawler and pluggable Web crawlers.** LOCKSS 2.x includes the LOCKSS Crawler Service, a component that manages Web crawls. The LOCKSS Crawler Service includes the built-in LOCKSS Web Crawler, and a system to add pluggable Web crawlers via an API.
   *  *  Web replay engines
      *  **LOCKSS ServeContent.** LOCKSS 1.x includes the built-in LOCKSS ServeContent Web replay engine.
      *  **LOCKSS ServeContent, Pywb, and OpenWayback.** LOCKSS 2.x includes the built-in LOCKSS ServeContent Web replay engine, the Pywb Web replay engine, and the OpenWayback Web replay engine.
