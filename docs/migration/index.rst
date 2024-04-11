=================================
LOCKSS 1.x to 2.x Migration Guide
=================================

.. warning::

   This page is under construction. LOCKSS 1.78 and LOCKSS 2.0-beta1 have not yet been released.

**Welcome, LOCKSS 1.x users!**

This document will guide you as you install LOCKSS 2.x and migrate the data you preserve in LOCKSS 1.x to LOCKSS 2.x.

You have the option to install LOCKSS 2.x on a brand-new physical or virtual machine (**recommended**), or to install it on the same machine as LOCKSS 1.x.

.. _new-machine-recommended:

.. tip::

   Why is a new machine recommended?

   *  Running LOCKSS 1.x and LOCKSS 2.x together on the same machine during the migration period will make very significant demands on the CPU, memory, and storage I/O.

   *  Unlike LOCKSS 1.x, LOCKSS 2.x can be installed on a great variety of operating systems. This will enable some LOCKSS users to move away from a physical machine to a virtual machine fitting their institution's IT infrastructure.

---------------------------------
Overview of the Migration Process
---------------------------------

The migration process has three major phases:

1. **Preparing your LOCKSS 2.x machine.**

   If you are installing LOCKSS 2.x on a new machine (recommended), you will need to commission a new Linux host.

   If you are installing LOCKSS 2.x on a LOCKSS 1.x machine, you will need to perform preparatory actions, which may include (where applicable) upgrading the operating system, or moving LOCKSS 1.x data around between disk volumes.

2. **Installing and configuring LOCKSS 2.0-beta1.**

3. **Configuring and running the migration process in the LOCKSS 1.x Web user interface.**

.. _migration-faq:

-----------------------------------------------------
Frequently Asked Questions about the Migration Process
-----------------------------------------------------

#. **Q: How long will the migration take?**

   A: The duration of the migration process is somewhat proportional to the amount of content preserved in the LOCKSS 1.x system. A LOCKSS 1.x system the size of a Global LOCKSS Network node is expected to take many weeks to migrate to LOCKSS 2.x.

#. **Q: If I am installing LOCKSS 2.x on my LOCKSS 1.x machine, do I need to have at least as much free space as the LOCKSS 1.x system occupies?**

   A: No, there is a documented mode for running the migration tool that progressively reclaims disk space as AUs are migrated from LOCKSS 1.x to LOCKSS 2.x. That being said, installing LOCKSS 2.x on a brand-new machine is recommended, and if you must install LOCKSS 2.x on the same machine as LOCKSS 1.x, having at least as much free space as the LOCKSS 1.x system occupies is recommended.

#. **Q: Can I use the LOCKSS system while the migration is in progress?**

   A: Largely, yes.

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

#. **Q: What might not work properly during the migration process?**

   A: FIXME

----

FIXME -- IGNORE ALL THIS BELOW:

1. **Prepare your LOCKSS 2.x machine.**

   Select the scenario that fits your situation:

   .. tab-set::

      .. tab-item:: LOCKSS 2.x on a new machine
         :sync: newmachine

         You will need to commission a new Linux host. See the `LOCKSS 2.0-beta1 System Prerequisites <https://docs.lockss.org/projects/manual/en/unstable/introduction/prerequisites.html>`_ page.

      .. tab-item:: LOCKSS 2.x on a LOCKSS 1.x machine
         :sync: samemachine

         For historical reasons, many LOCKSS 1.x machines are currently running RHEL 7 compatible operating systems like CentOS 7, which have reached end of life. Before co-installing LOCKSS 2.x with LOCKSS 1.x, you must **upgrade your RHEL 7 compatible system like CentOS 7 to a RHEL 9 compatible operating system like Rocky Linux 9**.

         *  CentOS 7 to Rocky Linux 9 (**recommended**): See `Alma ELevate <https://github.com/lockss/community/wiki/Alma-ELevate>`_ in the `LOCKSS Community Wiki <https://github.com/lockss/community/wiki>`_. This upgrade path uses the Alma ELevate tool.

         *  CentOS 8.5 or CentOS Stream to Rocky Linux 9: See `How to migrate to Rocky Linux from CentOS Stream, CentOS, AlmaLinux, RHEL, or Oracle Linux <https://docs.rockylinux.org/guides/migrate2rocky/>`_ in the `Rocky Linux Documentation <Rocky Linux Documentation>`_. This upgrade path uses the ``migrate2rocky`` tool.

         *  CentOS 8.4 to AlmaLinux OS 9: See `AlmaLinux Migration Guide <https://wiki.almalinux.org/documentation/migration-guide.html>`_ in the `AlmaLinux Wiki <https://wiki.almalinux.org/>`_. This upgrade path uses the ``almalinux-deploy`` tool.

         *  RHEL 7 to RHEL 9: See `Upgrading from RHEL 7 to RHEL 8 <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/upgrading_from_rhel_7_to_rhel_8/index>`_ and `Upgrading from RHEL 8 to RHEL 9 <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/index>`_ in the `Red Hat Customer Portal <https://access.redhat.com/>`_. This upgrade path uses the Leapp tool.

         *  CentOS 7 or CentOS 8 or CentOS Stream to Oracle Linux 9: See `Switch From CentOS Linux to Oracle Linux <https://docs.oracle.com/en/solutions/migrate-centos-ora-linux/switch-oracle-linux1.html>`_ in the `Oracle Help Center <https://docs.oracle.com/>`_. This upgrade path uses the ``centos2ol`` tool.
