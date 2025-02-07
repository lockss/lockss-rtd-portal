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

         If you are doing a new-host migration, it is strongly recommended that you allow your LOCKSS 2.x host to adopt the host name and IP address previously associated with your LOCKSS 1.x host.

         .. note::

            If adopting the IP address is not possible, contact the admin of your LOCKSS network to take into account the fact that your LOCKSS 2.x host now has an IP address not previously known to the other nodes in the network (e.g. firewall rules).

            Adopting the host name is not required, but if the host name is not changed, clients -- including users of the Web user interface, monitoring tools and dashboards, link resolvers (e.g. OpenURL resolvers), proxies, and more -- will need to be updated to use this new host name.

         To allow your LOCKSS 2.x host to adopt the host name and IP address of your LOCKSS 1.x host, follow these steps:

         a. On your LOCKSS 1.x host, stop the LOCKSS 1.x daemon (``systemctl stop lockss`` as ``root``), and shut down your LOCKSS 1.x host.

         b. Reconfigure your LOCKSS 2.x host so it uses the host name and IP address previously associated with your LOCKSS 1.x host. Contact your systems administrator for specifics.

         c. If applicable, firewall rules on the LOCKSS 2.x host and at your institution need to be updated, because LOCKSS 1.x and LOCKSS 2.x use different ports: firewall rules for ports 8081-8085 are no longer needed and need to be replaced with rules for ports 24600 through 24699 instead; firewall rules for ports 22, 8080, and 9729 remain the same.

         d. Restart K3s on the LOCKSS 2.x node by running these two commands as ``root``:

            .. code-block:: shell

               /usr/local/bin/k3s-killall.sh

               systemctl restart k3s

         e. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss

         f. The configuration process for LOCKSS 2.x will repeat; for most questions, you will simply hit :kbd:`Enter` to re-accept the previously entered value, except in the following cases:

            (i) For the prompt:

               :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`

               enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) For the prompt:

                :guilabel:`Fully qualified hostname (FQDN) of this machine`

                enter the host name previously associated with your LOCKSS 1.x host.

            (iii) For the prompt:

                 :guilabel:`IP address of this machine`

                 enter the IP address previously associated with your LOCKSS 1.x host.

            (iv) *Optional.* There may be other configuration values you need to change at this stage, but in most cases, everything else will be the same.

            (v) You will eventually receive the prompt:

               :guilabel:`OK to store this configuration?`

               Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a same-host migration, follow these steps:

         a. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss --replay

         b. You will receive the following prompt:

            :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`

            Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

         c. You will then receive the following prompt:

            :guilabel:`OK to store this configuration?`

            Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

4. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/start-lockss --wait

   to start the LOCKSS 2.0-beta1 system (now configured for normal operation).
