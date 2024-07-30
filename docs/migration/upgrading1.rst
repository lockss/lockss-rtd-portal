========================
Upgrading to LOCKSS 1.78
========================

The first task in the migration process is to upgrade your LOCKSS 1.x instance to LOCKSS 1.78.

To do so, run the following command as ``root`` on your LOCKSS 1.x host, depending on your operating system:

.. code-block:: shell

   # RHEL 7-compatible
   # (CentOS 7, Oracle Linux 7, RHEL 7, etc.)
   yum update lockss-daemon

   # RHEL 8-compatible or RHEL 9-compatible
   # (CentOS 8, CentOS Stream 8 or 9, Rocky Linux 8 or 9, AlmaLinux OS
   # 8 or 9, Oracle Linux 8 or 9, RHEL 8 or 9, etc.)
   dnf update lockss-daemon
