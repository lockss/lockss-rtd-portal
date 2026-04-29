.. include:: subst.rst

====================
Upgrading LOCKSS 1.x
====================

.. image:: laaws-migration-steps-upgrading1.png
   :align: center
   :alt: A diagram of seven consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first box labeled "Upgrading LOCKSS 1.x" is highlighted in yellow, indicating the step in progress. The last six boxes, successively labeled "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", "Running the Migrator" and "Reconfiguring LOCKSS 2.x for Normal Operation", are not colored, indicating future steps.

The first task in the migration process is to upgrade your LOCKSS 1.x instance to LOCKSS |UPGRADE_FROM_PATCH|, the latest version of LOCKSS |UPGRADE_FROM_MINOR|.

To upgrade your LOCKSS 1.x instance to LOCKSS |UPGRADE_FROM_PATCH|, follow these steps on your LOCKSS 1.x host [#fn-same-host]_, as ``root``:

1. :bdg-success:`new-host migration only`

   If you are doing a :ref:`New-Host Migration`, double-check that you are in a shell console for your LOCKSS 1.x host, for example by typing:

   .. code-block:: shell

      hostname

   and verifying that the output is the expected name of your LOCKSS 1.x host.

2. Double-check that you are acting as ``root`` in the shell console for your LOCKSS 1.x host [#fn-same-host]_ by typing:

   .. code-block:: shell

      whoami

   and verifying that the output is ``root``.

3. Run this :program:`systemctl` command (as ``root``):

   .. code-block:: shell

      systemctl stop lockss

   This will stop the LOCKSS 1.x instance.

4. Upgrade the ``lockss-daemon`` RPM package with a Dnf or Yum command, depending on your operating system:

   .. COMMENT OSTABS

   .. tab-set::

      .. tab-item:: AlmaLinux OS
         :sync: almalinux-os

         .. include:: upgrading1-dnf.rst

      .. tab-item:: CentOS Linux
         :sync: centos-linux

         .. tab-set::

            .. tab-item:: CentOS Linux 8
               :sync: centos8

               .. include:: upgrading1-dnf.rst

            .. tab-item:: CentOS Linux 6-7
               :sync: centos7

               .. include:: upgrading1-yum.rst

      .. tab-item:: EuroLinux
         :sync: eurolinux

         .. tab-set::

            .. tab-item:: EuroLinux 8-9
               :sync: eurolinux8

               .. include:: upgrading1-dnf.rst

            .. tab-item:: EuroLinux 7
               :sync: eurolinux7

               .. include:: upgrading1-yum.rst

      .. tab-item:: Oracle Linux
         :sync: oracle-linux

         .. tab-set::

            .. tab-item:: Oracle Linux 8-10
               :sync: oracle8

               .. include:: upgrading1-dnf.rst

            .. tab-item:: Oracle Linux 7
               :sync: oracle7

               .. include:: upgrading1-yum.rst

      .. tab-item:: Red Hat Enterprise Linux (RHEL)
         :sync: rhel

         .. tab-set::

            .. tab-item:: RHEL 8-10
               :sync: rhel8

               .. include:: upgrading1-dnf.rst

            .. tab-item:: RHEL 7
               :sync: rhel7

               .. include:: upgrading1-yum.rst

      .. tab-item:: Rocky Linux
         :sync: rocky-linux

         .. include:: upgrading1-dnf.rst

      .. tab-item:: Scientific Linux
         :sync: scientific-linux

         .. include:: upgrading1-yum.rst

5. Run this :program:`systemctl` command:

   .. code-block:: shell

      systemctl start lockss

   This will start the LOCKSS 1.x instance.

----

.. rubric:: Footnotes

.. [#fn-same-host]

   |FN_SAME_HOST|
