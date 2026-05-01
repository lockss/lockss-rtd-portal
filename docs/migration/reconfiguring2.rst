.. include:: subst.rst

=============================================
Reconfiguring LOCKSS 2.x for Normal Operation
=============================================

.. image:: laaws-migration-steps-reconfiguring2.png
   :align: center
   :alt: A diagram of seven consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first six boxes, successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration" and "Running the Migrator", are colored in light blue, indicating completed steps. The seventh box labeled "Reconfiguring LOCKSS 2.x for Normal Operation" is highlighted in yellow, indicating the step in progress.

The next task, once all the content has been successfully migrated from LOCKSS 1.x to LOCKSS 2.x, is to reconfigure LOCKSS 2.x for normal operation.

Follow these steps:

1. |LOCKSS1ROOT| Stop your LOCKSS 1.x system. This occurs on your LOCKSS 1.x host [#fn-same-host]_, as ``root``:

   .. code-block:: shell

      systemctl stop lockss

2. |LOCKSS2LOCKSS| Stop your LOCKSS 2.x system (currently configured for migration). This occurs on your LOCKSS 2.x host [#fn-same-host]_, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/stop-lockss

3. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a :ref:`New-Host Migration`, follow these steps to reconfigure your LOCKSS 2.x instance for normal operation:

         a. .. rubric:: Adopting the LOCKSS 1.x IP Address and Hostname
               :name: Adopting the LOCKSS 1.x IP Address and Hostname

            First, in a :ref:`New-Host Migration`, **it is strongly recommended that you now allow your LOCKSS 2.x host to adopt the IP address, and ideally the host name, previously associated with your LOCKSS 1.x host**, and you should perform this action at this stage.

            .. tip::

               .. dropdown:: What if adopting the LOCKSS 1.x IP address is not possible
                  :name: reconfiguring-implications-ip
                  :icon: light-bulb
                  :animate: fade-in-slide-down

                  If adopting the IP address of your LOCKSS 1.x host is not possible, there are implications to a change of IP address for your LOCKSS network and its participants:

                  *  The administrator of your LOCKSS network will need to include the change of IP address of your node in the LOCKSS network's configuration file, and make other  adjustments to the props server (firewall rules, Web server access rules, etc.) and more.

                  *  Other nodes in your LOCKSS network may have to adjust firewall rules and other access control lists (for example in the Content Access Options section of the Web user interface).

               .. dropdown:: What if adopting the LOCKSS 1.x hostname is not possible
                  :name: reconfiguring-implications-hostname
                  :icon: light-bulb
                  :animate: fade-in-slide-down

                  Adopting the host name of your LOCKSS 1.x host is not strictly required for the node to function, but a change of host name may also have downstream implications. For example, users of the Web user interface, browser bookmarks, monitoring tools and dashboards, link resolvers (e.g. OpenURL resolvers), proxy configuration, and more, will need to be updated to use the new host name.

            To allow your LOCKSS 2.x host to adopt the IP address, and ideally host name, of your LOCKSS 1.x host, follow these steps:

            (i) Shut down your LOCKSS 1.x host (or at least reconfigure it to a different IP address and host name). Contact your system administrator for specifics.

            (ii) Reconfigure your LOCKSS 2.x host so it uses the IP address, and ideally host name, previously associated with your LOCKSS 1.x host. Contact your system administrator for specifics.

         b. |LOCKSS2ROOT| On the LOCKSS 2.x host, run these two commands, as ``root``:

            (i) First: ``/usr/local/bin/k3s-killall.sh``

            (ii) Then: ``systemctl restart k3s``

            This will restart :external+lockss-manual:term:`K3s`.

         c. |LOCKSS2LOCKSS| Then run this command, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss

         d. The LOCKSS 2.x configuration process will repeat; for most questions, you will simply hit :kbd:`Enter` to re-accept the previously entered value, **except for the following prompts**:

            (i) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`Fully qualified hostname (FQDN) of this machine`: If you are adopting the LOCKSS 1.x hostname, enter it here (see :ref:`Adopting the LOCKSS 1.x IP Address and Hostname`).

            (iii) :guilabel:`IP address of this machine`: Likewise, if you are adopting the LOCKSS 1.x IP address, enter it here (see :ref:`Adopting the LOCKSS 1.x IP Address and Hostname`).

            (iv) *Optional.* There may be other configuration values you need to change at this stage, but in most cases, everything else will be the same.

            (v) :guilabel:`OK to store this configuration?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

         e. If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes, see the :doc:`lcap-ssl` chapter.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a :ref:`Same-Host Migration`, follow these steps:

         a. |LOCKSS2LOCKSS| On the LOCKSS host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`, run this command:

            .. code-block:: shell

               scripts/configure-lockss --replay

         b. The LOCKSS 2.x configuration process will auto-repeat, but you will receive a few prompts:

            (i) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`OK to store this configuration?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

4. |LOCKSS2LOCKSS| Finally, on the LOCKSS 2.x host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`, run this command:

   .. code-block:: shell

      scripts/start-lockss --wait

   This will start the LOCKSS 2.x stack (now configured for normal operation).

----

.. rubric:: Footnotes

.. [#fn-same-host]

   |FN_SAME_HOST|
