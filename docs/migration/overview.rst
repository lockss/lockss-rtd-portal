==================
Migration Overview
==================

-------------------------
Overview of the Migration
-------------------------

The migration process has six phases:

1. **Preparing your LOCKSS 2.x host.**

   If you are installing LOCKSS 2.x on a new host (recommended), you will need to commission a new Linux host.

   If you are installing LOCKSS 2.x on a LOCKSS 1.x host, you will need to ensure that the host meets the requirements for LOCKSS 2.x, and to upgrade the operating system before starting if necessary.

2. **Installing LOCKSS 2.0-beta1.**

3. **Configuring LOCKSS 2.0-beta1 specifically for migration.**

4. **Configuring LOCKSS 1.x for migration.**

5. **Running the migration process in LOCKSS 1.x.**

6. **Reconfiguring LOCKSS 2.0-beta1 for normal operation.**

.. COMMENT explain the general flow of the migration, polling, content access etc. not in the FAQ

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

.. _new-machine-recommended:

.. admonition:: Why is a new host recommended?

   *  Running LOCKSS 1.x and LOCKSS 2.x together on the same host will significantly degrade performance and cause the migration process to take much longer.

   *  Unlike LOCKSS 1.x, LOCKSS 2.x can be installed on a great variety of operating systems. This is an opportunity to move to a new host better fitting your institution's IT infrastructure preferences.

.. COMMENT commissioning a new host means not having to upgrade the existing host

.. COMMENT upgrading to RHEL 9 compatible is a pain

----------------------------------------------
Frequently Asked Questions about the Migration
----------------------------------------------

.. dropdown:: How long will the migration take?
   :name: migration-faq-duration
   :icon: question
   :animate: fade-in-slide-down

   The duration of the migration process is proportional to the amount of content preserved in the LOCKSS 1.x system. A LOCKSS 1.x system the size of a Global LOCKSS Network node is expected to take many weeks to migrate to LOCKSS 2.x.

.. dropdown:: If I am installing LOCKSS 2.x on my LOCKSS 1.x machine, do I need to have at least as much free space as the LOCKSS 1.x system occupies?
   :name: migration-faq-reclaim
   :icon: question
   :animate: fade-in-slide-down

   No, there is a documented mode for running the migration tool that progressively reclaims disk space as AUs are migrated from LOCKSS 1.x to LOCKSS 2.x. That being said, installing LOCKSS 2.x on a brand-new machine is recommended, and if you must install LOCKSS 2.x on the same machine as LOCKSS 1.x, having at least as much free space as the LOCKSS 1.x system occupies is preferred.

.. dropdown:: Can I use the LOCKSS system while the migration is in progress?
   :name: migration-faq-progress
   :icon: question
   :animate: fade-in-slide-down

   Largely, yes.

   *  **Each previously existing archival unit becomes temporarily unavailable at some point during the migration.**

      The migration tool processes existing AUs in the LOCKSS 1.x system sequentially. Each AU in turn becomes unavailable in the LOCKSS 1.x system, then its contents are copied to the LOCKSS 2.x system, then the AU becomes available in the LOCKSS 2.x system.

   *  **During the migration process, a previously existing archival unit is active in either the LOCKSS 1.x system or the LOCKSS 2.x system** (except during its content copy, where it is unavailable in both).

      Between the time the migration process starts and the time a given AU becomes unavailable in the LOCKSS 1.x system, you can see the AU in the Web user interface of the LOCKSS 1.x system (port 8081), but you should limit your dealings to "read-only" interactions.

      Once a given AU's contents have been migrated to the LOCKSS 2.x system, the AU is fully operational; you can interact with it in any way you like in the LOCKSS 2.x system, including in the LOCKSS 2.x Web user interface (ports 24600-24699).

   *  **During the migration process, the LOCKSS 1.x system forwards certain operations to the LOCKSS 2.x system.**

      The LOCKSS 1.x system knows how to respond to certain operations related to AUs that have already been fully migrated to the LOCKSS 2.x system. Poll requests from other nodes in your LOCKSS network are forwaded by the LOCKSS 1.x system to the LOCKSS 2.x polling service, and the responses are relayed back to the poller, for applicable AUs. Likewise, proxy requests, ServeContent Web replay requests and OpenURL queries are forwarded by the LOCKSS 1.x system to the corresponding LOCKSS 2.x service for applicable AUs.

      What this means is that other nodes in your LOCKSS network and clients of your LOCKSS node continue to interact with your existing LOCKSS 1.x node throughout the migration. Only at the end of the migration process will your LOCKSS 2.x system become your sole LOCKSS node while your LOCKSS 1.x system is taken out of the equation.

   *  **While the migration process is underway, new archival units should be created in the LOCKSS 2.x system.**

      After the migration process begins, you should add any new AUs to your LOCKSS 2.x system. These new AUs are then immediately operational in your LOCKSS 2.x system.

.. dropdown:: What might not work properly during the migration process?
   :name: migration-faq-hiccups
   :icon: question
   :animate: fade-in-slide-down

   FIXME

   *  OpenURL
   *  Subscription manager
