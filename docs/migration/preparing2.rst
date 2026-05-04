.. include:: subst.rst

==============================
Preparing Your LOCKSS 2.x Host
==============================

.. image:: laaws-migration-steps-preparing2.png
   :align: center
   :alt: A diagram of eight consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first box labeled "Upgrading LOCKSS 1.x" is colored in light blue, indicating a completed step. The second box labeled "Preparing the LOCKSS 2.x Host" is highlighted in yellow, indicating the step in progress. The last six boxes, successively labeled "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", "Running the Migrator", "Reconfiguring LOCKSS 2.x for Normal Operation", and "Decommissioning LOCKSS 1.x", are not colored, indicating future steps.

The next task in the migration process is to prepare your LOCKSS 2.x host [#fn-same-host]_ for LOCKSS |UPGRADE_TO_PATCH|, the latest version of LOCKSS |UPGRADE_TO_MINOR|.

The necessary work depends on your :ref:`Migration Scenario`:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a :ref:`New-Host Migration`, you will need to **commission a new host for your LOCKSS 2.x instance**, for example setting up a new physical machine and installing Linux, or spinning up a new Linux virtual machine. See the |TAB| :external+lockss-manual:doc:`introduction/prerequisites` section and |TAB| :external+lockss-manual:ref:`Operating Systems` appendix of the |MANUAL| for details.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a :ref:`Same-Host Migration` on a **discontinued** operating system in the RHEL family:

      *  `CentOS Linux <https://www.centos.org/centos-linux/>`_ (not to be confused with `CentOS Stream <https://centos.org/>`_)

      *  `CentOS Stream <https://www.centos.org/centos-stream/>`_ 8 (not to be confused with CentOS Linux)

      *  `EuroLinux <https://euro-linux.com/>`_

      *  `Red Hat Enterprise Linux <https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`_ (RHEL) 7 or earlier

      *  `Oracle Linux <https://www.oracle.com/linux/>`_ 7 or earlier

      *  `Scientific Linux <https://scientificlinux.org/>`_

      then you must **upgrade your LOCKSS host** to a **supported** operating system in the RHEL family [#fn-same-host]_:

      *  `AlmaLinux OS <https://almalinux.org/>`_ 8 or later

      *  `CentOS Stream <https://www.centos.org/centos-stream/>`_ 9 or later

      *  `Red Hat Enterprise Linux <https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`_ (RHEL) 8 or later

      *  `Oracle Linux <https://www.oracle.com/linux/>`_ 8 or later

      *  `Rocky Linux <https://rockylinux.org/>`_ 8 or later

      before you can co-install LOCKSS 2.x with LOCKSS 1.x. In particular, CentOS Linux (not to be confused with CentOS Stream) was once common in the LOCKSS 1.x user community, and requires an upgrade before installing LOCKSS 2.x.

      The LOCKSS Community Wiki offers a page on `OS Upgrades <https://github.com/lockss/community/wiki/OS-Upgrades>`_, providing guidance on various upgrade paths.

----

.. rubric:: Footnotes

.. [#fn-same-host]

   If your :ref:`Migration Scenario` is a :ref:`Same-Host Migration`, your LOCKSS 1.x host and your LOCKSS 2.x host are the same host.
