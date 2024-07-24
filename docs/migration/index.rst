=================================
LOCKSS 1.x to 2.x Migration Guide
=================================

.. warning::

   This page is under construction. LOCKSS 1.78 and LOCKSS 2.0-beta1 have not yet been released.

   .. image:: https://openmoji.org/php/download_asset.php?type=emoji&emoji_hexcode=1F6A7&emoji_variant=color
      :target: #
      :align: center
      :width: 256px
      :alt: Image of a road construction sign

**Welcome, LOCKSS 1.x users!**

This document will guide you as you install LOCKSS 2.x and migrate the data you preserve in LOCKSS 1.x to LOCKSS 2.x.

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

.. _migration-faq:

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

------------------------------
Preparing Your LOCKSS 2.x Host
------------------------------

The first phase in the migration process is to prepare your LOCKSS 2.x host. The necessary work depends on your new-host vs. same-host migration scenario:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a new-host migration, you will need to commission the new host.

      See the :doc:`lockss-manual:introduction/prerequisites` chapter of the LOCKSS 2.0-beta1 System Manual for guidance about :ref:`lockss-manual:CPU`, :ref:`lockss-manual:Memory` and :ref:`lockss-manual:Storage` requirements.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a same-host migration, you may need to upgrade your operating system before you can co-install LOCKSS 2.x with LOCKSS 1.x.

      Many LOCKSS 1.x hosts are currently running RHEL 7 compatible operating systems (such as RHEL 7, CentOS 7, or Oracle Linux 7), or CentOS 8, or CentOS Stream 8, which have all reached end of life. If your host is running one of these operating systems, you must upgrade to a RHEL 9 compatible operating system. **We recommend Rocky Linux 9.**

      The following table shows upgrade paths for various operating systems:

      ======================== ======================= ===================== ================== ====================
      From ...                 ... to AlmaLinux OS 9   ... to Oracle Linux 9 ... to RHEL 9      ... to Rocky Linux 9
      ======================== ======================= ===================== ================== ====================
      From CentOS 7 ...        n/a                     :ref:`centos2ol`      n/a                n/a
      From CentOS 8 ...        :ref:`almalinux-deploy` :ref:`centos2ol`      n/a                n/a
      From CentOS Stream 8 ... :ref:`almalinux-deploy` n/a                   n/a                n/a
      From Oracle Linux 7 ...  n/a                     n/a                   n/a                n/a
      From RHEL 7 ...          n/a                     n/a                   :ref:`leapp-rhel`  n/a
      ======================== ======================= ===================== ================== ====================

      FIXME ignore the remainder

      *  Some LOCKSS 1.x hosts are running CentOS 8 or CentOS Stream 8, which have also reached end of life. If your host is running CentOS 8 or CentOS Stream 8, you must upgrade to a RHEL 9 compatible operating system. **We recommend Rocky Linux 9.**

         *  **Upgrade from CentOS 7 to Rocky Linux 9 (recommended)**: See `Alma ELevate <https://github.com/lockss/community/wiki/Alma-ELevate>`_ in the `LOCKSS Community Wiki <https://github.com/lockss/community/wiki>`_. This upgrade path uses the Alma ELevate tool.

         *  **Upgrade from**

FIXME ignore the remainder

Before co-installing LOCKSS 2.x with LOCKSS 1.x, you must **upgrade your RHEL 7 compatible system like CentOS 7 to a RHEL 9 compatible operating system like Rocky Linux 9**.

      *  CentOS 7 to Rocky Linux 9 (**recommended**): See `Alma ELevate <https://github.com/lockss/community/wiki/Alma-ELevate>`_ in the `LOCKSS Community Wiki <https://github.com/lockss/community/wiki>`_. This upgrade path uses the Alma ELevate tool.

      *  CentOS 8.5 or CentOS Stream to Rocky Linux 9: See `How to migrate to Rocky Linux from CentOS Stream, CentOS, AlmaLinux, RHEL, or Oracle Linux <https://docs.rockylinux.org/guides/migrate2rocky/>`_ in the `Rocky Linux Documentation <Rocky Linux Documentation>`_. This upgrade path uses the ``migrate2rocky`` tool.

      *  CentOS 8.4 to AlmaLinux OS 9: See `AlmaLinux Migration Guide <https://wiki.almalinux.org/documentation/migration-guide.html>`_ in the `AlmaLinux Wiki <https://wiki.almalinux.org/>`_. This upgrade path uses the ``almalinux-deploy`` tool.

      *  RHEL 7 to RHEL 9: See `Upgrading from RHEL 7 to RHEL 8 <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/upgrading_from_rhel_7_to_rhel_8/index>`_ and `Upgrading from RHEL 8 to RHEL 9 <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/index>`_ in the `Red Hat Customer Portal <https://access.redhat.com/>`_. This upgrade path uses the Leapp tool.

      *  CentOS 7 or CentOS 8 or CentOS Stream to Oracle Linux 9: See `Switch From CentOS Linux to Oracle Linux <https://docs.oracle.com/en/solutions/migrate-centos-ora-linux/switch-oracle-linux1.html>`_ in the `Oracle Help Center <https://docs.oracle.com/>`_. This upgrade path uses the ``centos2ol`` tool.

---------------------------
Installing LOCKSS 2.0-beta1
---------------------------

The second phase in the migration process is to install LOCKSS 2.0-beta1.

To do so, follow the instructions in chapter 3 (:doc:`lockss-manual:installing/index`) of the LOCKSS 2.0-beta1 System Manual.

----------------------------------------------------
Configuring LOCKSS 2.0-beta1 Specially for Migration
----------------------------------------------------

The third phase in the migration process is to configure LOCKSS 2.0-beta1 specifically for migration.

Importing the LOCKSS 1.x Configuration File
===========================================

The first part of this phase is to make the LOCKSS 1.x configuration file available to the LOCKSS 2.x configuration script. The steps depend on your new-host vs. same-host migration scenario:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a new-host migration, you need to copy the LOCKSS 1.x configuration file :file:`/etc/lockss/config.dat` from your LOCKSS 1.x host to somewhere on your LOCKSS 2.x host, for example using :program:`scp`. The LOCKSS 2.x configuration script will later prompt you for the path of this file on the LOCKSS 2.x host (by default, :file:`/tmp/v1config.dat`).

      If you are not able to copy the LOCKSS 1.x configuration file to the LOCKSS 2.x host, you can still configure LOCKSS 2.x for migration, but you will be prompted to supply more information.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a same-host migration, the LOCKSS 2.x configuration script will find the LOCKSS 1.x configuration file :file:`/etc/lockss/config.dat` directly, so you do not need to do anything here.

Running :program:`configure-lockss --migrate`
=============================================

The second part of this phase is to run the :program:`configure-lockss` tool with the special ``--migrate`` option. This will proceed largely as described in the :doc:`lockss-manual:configuring` chapter of the LOCKSS 2.0-beta1 System Manual, **but with a number of notable differences described here.** Follow these steps:

1. Per section 4.1 (:ref:`lockss-manual:before-invoking-configure-lockss`), gather information about the LOCKSS 2.x host (which might be the same host as the LOCKSS 1.x host if doing a same-host migration), .

2. Run the following command as the ``lockss`` user in the LOCKSS 2.x installation directory:

   .. code-block:: shell

      scripts/configure-lockss --migrate

   This is almost the ame as section 4.2 (:ref:`lockss-manual:invoking-configure-lockss`), but with the additional ``--migrate`` option.

3. The first prompt, :guilabel:`Command to use to execute kubectl commands`, is the same as that from section 4.3 (:ref:`lockss-manual:Kubernetes Settings`). If you are using the K3s Kubernetes environment that ships with LOCKSS 2.x, the proposed value is already correct; hit :kbd:`Enter` to accept it. (Otherwise, enter the command needed to invoke :program:`kubectl` in your environment.)

4. This step depends on your new-host vs. same-host migration scenario:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a new-host migration, follow these steps:

      1. You will receive the following prompt:

         :guilabel:`Did you copy a LOCKSS 1.x config.dat file to this host?`

         Enter :kbd:`Y` for "yes" (unless you were not able to copy the LOCKSS 1.x configuration file from the LOCKSS 1.x host, in which case you will need FIXME).

      2. You will then receive the following prompt:

         :guilabel:`Location of copied LOCKSS 1.x config.dat file`

         Enter the path of the copied LOCKSS 1.x configuration file, or hit :kbd:`Enter` to accept the default in square brackets if it matches the path you used.

      3. Data will be imported from the LOCKSS 1.x configuration file, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

         *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

         *  :guilabel:`IP address of this machine`

         *  :guilabel:`Initial subnet(s) for admin UI access`

         *  :guilabel:`LCAP protocol port`

         *  :guilabel:`Is this machine behind NAT?`

         *  :guilabel:`Mail relay for this machine`

         *  :guilabel:`Does the mail relay <mailhost> need a username and password?`

         *  :guilabel:`E-mail address for administrator`

         *  :guilabel:`Configuration URL`

         *  :guilabel:`Configuration proxy (host:port)`

         *  :guilabel:`Preservation group(s)`

         corresponding to sections 4.4 (:ref:`lockss-manual:Network Settings`) through 4.6 (:ref:`lockss-manual:Preservation Network Settings`).

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a same-host migration, follow these steps:

      1. Data will be imported from the LOCKSS 1.x configuration file, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

         *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

         *  :guilabel:`IP address of this machine`

         *  :guilabel:`Initial subnet(s) for admin UI access`

         *  :guilabel:`LCAP protocol port`

         corresponding to section 4.4 (:ref:`lockss-manual:Network Settings`).

      2. You will receive the following prompt:

         :guilabel:`Temporary LOCKSS 2.x LCAP port`

         Enter an LCAP port different from the one used by LOCKSS 1.x, for use during migration, or hit :kbd:`Enter` to accept the suggested value in square brackets.

      3. You will be asked to confirm more configuration values. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

         *  :guilabel:`Is this machine behind NAT?`

         *  :guilabel:`Mail relay for this machine`

         *  :guilabel:`Does the mail relay <mailhost> need a username and password?`

         *  :guilabel:`E-mail address for administrator`

         *  :guilabel:`Configuration URL`

         *  :guilabel:`Configuration proxy (host:port)`

         *  :guilabel:`Preservation group(s)`

         corresponding to sections 4.5 (:ref:`lockss-manual:Mail Settings`) through 4.6 (:ref:`lockss-manual:Preservation Network Settings`).














