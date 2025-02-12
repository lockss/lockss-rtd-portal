========================================
Upgrading to LOCKSS |UPGRADE_FROM_PATCH|
========================================

The first task in the migration process is to upgrade your LOCKSS 1.x instance to LOCKSS |UPGRADE_FROM_PATCH|, the latest version of LOCKSS |UPGRADE_TO_MINOR|.

To do so, run the command appropriate for your operating system:

.. COMMENT OSTABS

.. tab-set::

   .. tab-item:: AlmaLinux OS
      :sync: alma

      .. include:: upgrading1-dnf.rst

   .. tab-item:: CentOS
      :sync: centos

      .. tab-set::

         .. tab-item:: CentOS Stream
            :sync: centosstream

            .. include:: upgrading1-dnf.rst

         .. tab-item:: CentOS 7
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
      :sync: oracle

      .. tab-set::

         .. tab-item:: Oracle Linux 8-9
            :sync: oracle8

            .. include:: upgrading1-dnf.rst

         .. tab-item:: Oracle Linux 7
            :sync: oracle7

            .. include:: upgrading1-yum.rst

   .. tab-item:: RHEL
      :sync: rhel

      .. tab-set::

         .. tab-item:: RHEL 8-9
            :sync: rhel8

            .. include:: upgrading1-dnf.rst

         .. tab-item:: RHEL 7
            :sync: rhel7

            .. include:: upgrading1-yum.rst

   .. tab-item:: Rocky Linux
      :sync: rocky

      .. include:: upgrading1-dnf.rst

   .. tab-item:: Scientific Linux
      :sync: scientific

      .. include:: upgrading1-yum.rst
