=================================
Appendix: LCAP Over SSL Migration
=================================

If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes (ask your LOCKSS network admin to know if this situation applies to you), you will need to perform a few additional steps related to your LCAP SSL keystore. The instructions in this manual will refer you to this section in several appropriate places.

Take these steps into consideration, depending on your :ref:`Migration Scenario`:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      1. In the :ref:`Importing Configuration From LOCKSS 1.x` section of the :doc:`configuring2` chapter, after you make the LOCKSS 1.x configuration file available to LOCKSS 2.x, you will need to perform the following actions.

         a. On the LOCKSS 2.x host, in the :ref:`lockss-manual:LOCKSS Installer Directory`, create a new subdirectory for LOCKSS 1.x keys by running this command as the ``lockss`` user:

            .. code-block:: shell

               mkdir -p config/keys/v1keys

         b. Copy the three files from the :file:`/etc/lockss/keys` directory of your LOCKSS 1.x host into this new :file:`config/keys/v1keys` directory on your LOCKSS 2.x host.

      2. In the :ref:`Running LOCKSS 2.0-beta1` section of the :doc:`configuring2` chapter, after you edit the :guilabel:`Admin Access Control` screen with the IP address or subnet of your LOCKSS 1.x host (:numref:`Running LOCKSS 2.0-beta1` steps *(2)(b)* and *(2)(c)*), you will need to perform the following actions.

         a. Follow the instructions in the :ref:`lockss-manual:Interactive Tool` section in the :doc:`lockss-manual:appendix/lcap-ssl` section of the :doc:`lockss-manual:index` to generate a keystore for your LOCKSS 2.x host and add it to your network's public keystore.

         b. Follow the instructions in the :ref:`lockss-manual:Installing the Keystores` section in the :doc:`lockss-manual:appendix/lcap-ssl` section of the :doc:`lockss-manual:index` to install the newly generated keystore to your LOCKSS 2.x host.

         c. Additionally, the newly generated network public keystore must replace the one present on your LOCKSS 1.x host. Copy the newly generated network public keystore to the :file:`/etc/lockss/keys` directory on your LOCKSS 1.x host, such that it replaces the original one.

      3. At the end of the :doc:`reconfiguring2` chapter, after you successfully re-run the :program:`configure-lockss` script, you will need to perform the following action.

         Relative to the :ref:`lockss-manual:LOCKSS Installer Directory` on your LOCKSS 2.0 host, copy the three files from the :file:`config/keys/v1keys` directory into the :file:`config/keys` directory, replacing the corresponding files there.

         .. note::

            If renaming your LOCKSS 2.x host name to that previously used by your LOCKSS 1.x host is not possible, do not perform this step; instead, your LOCKSS network admin will need to distribute a new network public keystore to all nodes in the network, for which you will have to coordinate with them.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      1. In the :ref:`Importing Configuration From LOCKSS 1.x` section of the :doc:`configuring2` chapter, after you make the LOCKSS 1.x configuration file available to LOCKSS 2.x, you will need to perform the following action.

         Copy the three files from the :file:`/etc/lockss/keys` directory into the :file:`config/keys` directory relative to the :ref:`lockss-manual:LOCKSS Installer Directory` (usually :file:`/home/lockss/lockss-installer/config/keys`), following the instructions from :ref:`lockss-manual:Installing the Keystores` in the :doc:`lockss-manual:appendix/lcap-ssl` section of the :doc:`lockss-manual:index`.
