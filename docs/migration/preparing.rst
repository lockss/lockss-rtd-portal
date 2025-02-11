==============================
Preparing Your LOCKSS 2.x Host
==============================

The next task in the migration process is to prepare your LOCKSS 2.x host. The necessary work depends on your :ref:`Migration Scenario`:

.. tab-set::
   :class: sd-bg-light

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a new-host migration, you will need to commission the new host.

      See the :doc:`lockss-manual:introduction/prerequisites` chapter of the :doc:`lockss-manual:index` for guidance about :ref:`lockss-manual:CPU`, :ref:`lockss-manual:Memory` and :ref:`lockss-manual:Storage` requirements.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a same-host migration, you may need to upgrade your operating system before you can co-install LOCKSS 2.x with LOCKSS 1.x.

      Many LOCKSS 1.x hosts are currently running RHEL 7-compatible operating systems (such as RHEL 7, CentOS 7, Oracle Linux 7), or CentOS 8-like operating systems (CentOS 8, CentOS Stream 8), which have all reached end of life. If your host is running one of these operating systems, you must upgrade to a RHEL 8-compatible or RHEL 9-compatible operating system (such as Rocky Linux 8 or 9, AlmaLinux OS 8 or 9, Oracle Linux 8 or 9, RHEL 8 or 9, etc.) first.

      The LOCKSS Community Wiki offers a page on `OS Upgrades <https://github.com/lockss/community/wiki/OS-Upgrades>`_, providing guidance on various upgrade paths.
