=============================================
Reconfiguring LOCKSS 2.x for Normal Operation
=============================================

The next task, once all the content has been migrated from LOCKSS 1.x to LOCKSS 2.x, is to reconfigure LOCKSS 2.x for normal operation.

Follow these steps:

1. Stop your LOCKSS 2.x system (currently configured for migration) by running this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory` on your LOCKSS 2.x host [#fnsamehost]_:

   .. code-block:: shell

      scripts/stop-lockss

2. Stop your LOCKSS 1.x system by running this :program:`systemctl` command as ``root`` on your LOCKSS 1.x host [#fnsamehost]_:

   .. code-block:: shell

      systemctl stop lockss

3. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a **new-host migration**, it is strongly recommended that you allow your LOCKSS 2.x host to adopt the host name and IP address previously associated with your LOCKSS 1.x host.

         .. note::

            If adopting the IP address is not possible, contact the admin of your LOCKSS network to take into account the fact that your LOCKSS 2.x host now has an IP address not previously known to the other nodes in the network (e.g. firewall rules).

            Adopting the host name is not required, but if the host name is not changed, clients -- including users of the Web user interface, monitoring tools and dashboards, link resolvers (e.g. OpenURL resolvers), proxies, and more -- will need to be updated to use this new host name.

         To allow your LOCKSS 2.x host to adopt the host name and IP address of your LOCKSS 1.x host, follow these steps:

         a. Shut down your LOCKSS 1.x host.

         b. Reconfigure your LOCKSS 2.x host so it uses the host name and IP address previously associated with your LOCKSS 1.x host. Contact your system administrator for specifics.

         c. If applicable, firewall rules on the LOCKSS 2.x host and elsewhere at your institution need to be updated, because LOCKSS 1.x and LOCKSS 2.x use different ports: **firewall rules to TCP ports 8081-8085 are no longer needed and need to be replaced with rules to TCP ports 24600-24699 instead**. Note that **firewall rules to TCP ports 22, 8080, and 9729 remain the same**.

         d. Restart K3s on the LOCKSS 2.x node by running these two commands as ``root``:

            (i) First: ``/usr/local/bin/k3s-killall.sh``

            (ii) Then: ``systemctl restart k3s``

         e. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss

         f. The LOCKSS 2.x configuration process will repeat; for most questions, you will simply hit :kbd:`Enter` to re-accept the previously entered value, **except for the following prompts**:

            (i) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`Fully qualified hostname (FQDN) of this machine`: Enter the host name previously associated with your LOCKSS 1.x host.

            (iii) :guilabel:`IP address of this machine`: Enter the IP address previously associated with your LOCKSS 1.x host.

            (iv) *Optional.* There may be other configuration values you need to change at this stage, but in most cases, everything else will be the same.

            (v) :guilabel:`OK to store this configuration?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

         g. If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes, see the :doc:`lcap-ssl` chapter.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a **same-host migration**, follow these steps:

         a. On the LOCKSS 2.x host [#fnsamehost]_, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss -r

            which is short for:

            .. code-block:: shell

               scripts/configure-lockss --replay

         b. The LOCKSS 2.x configuration process will auto-repeat, but you will receive a few prompts:

            (i) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`OK to store this configuration?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

4. On the LOCKSS 2.x host, run this command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/start-lockss -w

   which is short for:

   .. code-block:: shell

      scripts/start-lockss --wait

   to start the LOCKSS 2.0-beta1 system (now configured for normal operation).

----

.. only:: html

   .. rubric:: Footnotes

.. [#fnsamehost]

   If your :ref:`Migration Scenario` is a **same-host migration**, your LOCKSS 1.x host and your LOCKSS 2.x host are the same host.
