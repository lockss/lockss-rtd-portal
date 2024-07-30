===================================================
Reconfiguring LOCKSS 2.0-beta1 for Normal Operation
===================================================

The next task, once all the content has been migrated from LOCKSS 1.78 to LOCKSS 2.0-beta1, is to reconfigure LOCKSS 2.0-beta1 for normal operation.

Follow these steps:

1. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/stop-lockss

   This will stop the LOCKSS 2.0-beta1 system (currently configured for migration).

2. On the LOCKSS 1.x host, run this command as ``root``:

   .. code-block:: shell

      systemctl stop lockss

   This will stop the LOCKSS 1.78 system.

3. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a new-host migration, it is strongly recommended that you allow your LOCKSS 2.x host to assume the host name and IP address previously associated with your LOCKSS 1.x host.

         .. note::

            If this is not possible, follow the instructions for this step in the "same-host migration" scenario instead, then contact your LOCKSS network administrator so the LOCKSS network configuration can be updated with your new LOCKSS 2.x IP address.

         To allow your LOCKSS 2.x host to reclaim the host name and IP address of your LOCKSS 1.x host, follow these steps:

         1. Power off your LOCKSS 1.x host.

         2. Reconfigure your LOCKSS 2.x host so it uses the host name and IP address previously associated with your LOCKSS 1.x host. Contact your systems administrator for specifics.

         3. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss

         4. The configuration process for LOCKSS 2.x will repeat; for most questions, you will simply hit :kbd:`Enter` to re-accept the previously entered value, except in the following cases:

            1. For the prompt:

               :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`

               enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            2. For the prompt:

               :guilabel:`Fully qualified hostname (FQDN) of this machine`

               enter the host name previously associated with your LOCKSS 1.x host.

            3. For the prompt:

               :guilabel:`IP address of this machine`

               enter the IP address previously associated with your LOCKSS 1.x host.

            4. *Optional.* There may be other configuration values you need to change at this stage, but in most cases, everything else will be the same.

            5. You will eventually receive the prompt:

               :guilabel:`OK to store this configuration?`

               Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a same-host migration, follow these steps:

         1. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss --replay

         2. You will receive the following prompt:

            :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`

            Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

         3. You will then receive the following prompt:

            :guilabel:`OK to store this configuration?`

            Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

4. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/start-lockss --wait

   to start the LOCKSS 2.0-beta1 system (now configured for normal operation).
