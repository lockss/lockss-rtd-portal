==============================
Preparing Your LOCKSS 2.x Host
==============================

.. warning::

   This page is under construction. LOCKSS 1.78 and LOCKSS 2.0-beta1 have not yet been released.

   .. image:: https://openmoji.org/php/download_asset.php?type=emoji&emoji_hexcode=1F6A7&emoji_variant=color
      :target: #
      :align: center
      :width: 256px
      :alt: Image of a road construction sign

The first task in the migration process is to prepare your LOCKSS 2.x host. The necessary work depends on your :ref:`Migration Scenario`:

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
