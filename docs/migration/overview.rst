==================
Migration Overview
==================

------------------
Migration Scenario
------------------

There are two migration scenarios:

.. tab-set::

   .. tab-item:: New-Host Migration (Recommended)
      :sync: newhost

      **In this migration scenario, you will install LOCKSS 2.x on a brand-new physical host or virtual machine.**

   .. tab-item:: Same-Host Migration
      :sync: samehost

      **In this migration scenario, you will install LOCKSS 2.x on the same host as LOCKSS 1.x.**

.. _new-host-recommended:

.. admonition:: Why is a new host recommended?

   *  LOCKSS 2.x has higher system requirements.

   *  Unlike LOCKSS 1.x, LOCKSS 2.x can be installed on a great variety of operating systems. This is an opportunity to move to a new host better fitting your institution's IT infrastructure preferences.

   *  Running LOCKSS 1.x and LOCKSS 2.x together on the same host will degrade performance and cause the migration process to take longer.

   *  If your LOCKSS 1.x host is running an outdated operating system such as CentOS 7, you would have to upgrade the OS before proceeding with a same-host migration.

---------------------------------
Overview of the Migration Process
---------------------------------

.. admonition:: TL;DR

   *  During migration, continue to access content (ServeContent, proxy) using the 1.x host and port.

   *  During migration, additional AUs to be preserved and subscriptions should be added using the 2.x Web UI.

   *  During migration, changes to configuration, such as IP access lists and proxy settings, should be made to both the 1.x and 2.x systems.

The LOCKSS migration process provides a way to copy content and configuration from LOCKSS 1.x to LOCKSS 2.x. It requires that both the 1.x and the 2.x systems be running simultaneously, either on the same or on different hosts. The migrator is a 1.x component which talks to the 2.x REST services to store content, configuration, state information (such as agreement histories), and the metadata database (if applicable). It is operated from the LOCKSS 1.x Web UI.

The set of archival units to copy is determined by selecting either all AUs or just those belonging to a single plugin. Migrating content takes significant time, and is highly dependent on content characteristics and environment (file size distribution, network vs. local storage, etc.). In some cases (e.g. GLN nodes), we expect it will take months to migrate all the content.

The migrator facilitate running both the 1.x and the 2.x systems in tandem, so that content collection, polling, and access are not interrupted significantly while migration proceeds. If performing a same-host migration, content may be incrementally deleted as it is moved, if necessary to reclaim disk space.

The migrator copies, and optionally verifies, content and state data for each AU. By default, the verification step does not compare copied content byte-for-byte, though this additional step can be switched on (but it will approximately double the time required to complete the migration).

The migrator migrates several AUs at a time. When an AU is being migrated, first it becomes "frozen" in 1.x so it will not crawl or poll; then its content is copied from 1.x to 2.x; then it is configured in 2.x; then it is deactivated (or deleted) from 1.x, at which point it again becomes eligible to crawl and poll in 2.x. During the migration process, the 1.x node continues to communicate with other nodes in the network; the 1.x nodes handles all the polling and voting traffic for AUs that have been migrated to 2.x, so as to give the impression of a single LOCKSS node to the rest of the network. Similarly, all content access (ServeContent, proxy) during the migration should be to the 1.x system, and requests corresponding to AUs that have been migrated to 2.x will be forwarded to 2.x as necessary, so as to give users the experience of a single LOCKSS node. (Note that this is experimental in LOCKSS 2.0-beta1.)

If you wish to add additional AUs to preserve, they should be added in the 2.x system. Similarly, new subscription should be added to the subscription manager on 2.x, but they will not take effect until migration is complete. Configuration data such as IP access lists and proxy settings are copied at the beginning of the migration process; if you need to make changes to them in the 1.x system during the migration, the same changes should be made in the 2.x system.

If you have set any configuration parameters in the Expert Config screen, this file is also copied at the beginning of migration, but each line is commented out to allow you to review which custom settings you wish to be in effect in the 2.x system.
