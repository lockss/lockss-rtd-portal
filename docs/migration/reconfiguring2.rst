.. include:: subst.rst

=============================================
Reconfiguring LOCKSS 2.x for Normal Operation
=============================================

.. image:: laaws-migration-steps-reconfiguring2.png
   :align: center
   :alt: A diagram of eight consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first six boxes, successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", and "Running the Migrator", are colored in light blue, indicating completed steps. The seventh box labeled "Reconfiguring LOCKSS 2.x for Normal Operation" is highlighted in yellow, indicating the step in progress. The last box, labeled "Decommissioning LOCKSS 1.x", is not colored, indicating a future step.

The next task, once all the content has been successfully migrated from LOCKSS 1.x to LOCKSS 2.x, is to reconfigure LOCKSS 2.x for normal operation.

.. important::

   This chapter marks the end of the |PRINCIPAL| and the cutover from LOCKSS 1.x to LOCKSS 2.x. It induces an interruption of service as the LOCKSS 1.x instance is taken out of service and the LOCKSS 2.x instance takes over as the sole system. Plan the steps of this chapter carefully to minimize downtime and disruption. Some steps may require coordination with a central IT department or communication with users of the system.

Follow these steps:

1. |LOCKSS1ROOT| Stop and disable your LOCKSS 1.x system. This occurs on your LOCKSS 1.x host, as ``root``:

   .. code-block:: shell

      systemctl disable --now lockss

2. |LOCKSS2LOCKSS| Stop your LOCKSS 2.x system (currently configured for migration). This occurs on your LOCKSS 2.x host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/stop-lockss

3. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a :ref:`New-Host Migration`, follow these steps to reconfigure your LOCKSS 2.x instance for normal operation:

         a. Undo the new-host migration firewall rules established in the :ref:`New-Host Migration` portion of :numref:`Chapter %s <Preparing the LOCKSS 2.x Host>` (:ref:`Preparing the LOCKSS 2.x Host`).

         b. **Allow your LOCKSS 2.x host to adopt the IP address, and ideally hostname, previously associated with your LOCKSS 1.x host.** This step is **strongly recommended**; see :numref:`Adopting the LOCKSS 1.x IP Address` (:ref:`Adopting the LOCKSS 1.x IP Address`) and :numref:`Adopting the LOCKSS 1.x Hostname` (:ref:`Adopting the LOCKSS 1.x Hostname`). This action requires you (or your system administrator) to take the following steps:

            (i) |LOCKSS1ROOT| Shut down your LOCKSS 1.x host, or at least reconfigure it to yet another IP address.

            (ii) |LOCKSS2ROOT| Reconfigure your LOCKSS 2.x host so it uses the IP address, and ideally hostname, previously associated with your LOCKSS 1.x host.

            (iii) |LOCKSS2ROOT| On the LOCKSS 2.x host, run these two commands as ``root``:

               .. code-block:: shell

                  /usr/local/bin/k3s-killall.sh

                  systemctl restart k3s

               This is necessary for |K3s| to adjust to the newly configured IP address.

            .. admonition:: Coordinating with Administrators of LOCKSS Networks

               Whether or not you adopt the IP address of your LOCKSS 1.x node, the administrator of your LOCKSS network has to adjust the firewall rules and Web server access control on the network configuration server. See :ref:`Access control after migration` in :numref:`Chapter %s <Appendix: Instructions for Administrators of LOCKSS Networks>` (:ref:`Appendix: Instructions for Administrators of LOCKSS Networks`).

         c. |LOCKSS2LOCKSS| Run this command, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`:

            .. code-block:: shell

               scripts/configure-lockss

         d. The LOCKSS 2.x configuration process will repeat. For the most part, you are only confirming existing values by simply hitting :kbd:`Enter`, but you will receive additional prompts and there are a few prompts to pay attention to:

            (i) (*additional prompt*) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`Fully qualified hostname (FQDN) of this machine`: If you are adopting the LOCKSS 1.x hostname (which is recommended), enter it here. See :numref:`Adopting the LOCKSS 1.x Hostname` (:ref:`Adopting the LOCKSS 1.x Hostname`).

               .. admonition:: Coordinating with Administrators of LOCKSS Networks

                  If your node does not adopt your LOCKSS 1.x hostname, the administrator of your LOCKSS network may have to take action to account for the change. See :ref:`Change of Hostname` in :numref:`Chapter %s <Appendix: Instructions for Administrators of LOCKSS Networks>` (:ref:`Appendix: Instructions for Administrators of LOCKSS Networks`).

               .. important::

                  Additionally, if your node does not adopt your LOCKSS 1.x hostname, users of the system and various other systems now have to switch to the new hostname. See :numref:`Adopting the LOCKSS 1.x Hostname` (:ref:`Adopting the LOCKSS 1.x Hostname`). 

            (iii) :guilabel:`IP address of this machine`: Likewise, if you are adopting the LOCKSS 1.x IP address (which is strongly recommended), enter it here. See :numref:`Adopting the LOCKSS 1.x IP Address` (:ref:`Adopting the LOCKSS 1.x IP Address`).

               .. admonition:: Coordinating with Administrators of LOCKSS Networks

                  If your node does not adopt your LOCKSS 1.x IP address and/or LCAP port, the administrator of your LOCKSS network has to take action to account for the change in |LCAP| identity induced. See :ref:`Change of LCAP identity` in :numref:`Chapter %s <Appendix: Instructions for Administrators of LOCKSS Networks>` (:ref:`Appendix: Instructions for Administrators of LOCKSS Networks`).

            (iv) :guilabel:`LCAP port`: It is strongly recommended that you adopt the LCAP port previously associated with your LOCKSS 1.x instance. See :numref:`Adopting the LOCKSS 1.x LCAP Port` (:ref:`Adopting the LOCKSS 1.x LCAP Port`).

            (v) :guilabel:`OK to proceed?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a :ref:`Same-Host Migration`, follow these steps:

         a. |LOCKSS2LOCKSS| On the LOCKSS host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`, run this command:

            .. code-block:: shell

               scripts/configure-lockss

         b. The LOCKSS 2.x configuration process will repeat. For the most part, you are only confirming existing values by simply hitting :kbd:`Enter`, but you will receive additional prompts and there are a few prompts to pay attention to:

            (i) (*additional prompt*) :guilabel:`Do you want to reconfigure LOCKSS 2.x to no longer be in migration mode?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

            (ii) :guilabel:`LCAP port`: It is strongly recommended that you adopt the LCAP port previously associated with your LOCKSS 1.x instance. See :numref:`Adopting the LOCKSS 1.x LCAP Port` (:ref:`Adopting the LOCKSS 1.x LCAP Port`).

               .. admonition:: Coordinating with Administrators of LOCKSS Networks

                  If your node does not adopt its LOCKSS 1.x LCAP port, the administrator of your LOCKSS network has to take action to account for the change in |LCAP| identity induced. See :ref:`Change of LCAP identity` in :numref:`Chapter %s <Appendix: Instructions for Administrators of LOCKSS Networks>` (:ref:`Appendix: Instructions for Administrators of LOCKSS Networks`).

            (iii) :guilabel:`OK to proceed?`: Enter :kbd:`Y` for "yes", or simply hit :kbd:`Enter`.

4. |LOCKSS2LOCKSS| Finally, on the LOCKSS 2.x host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`, run this command:

   .. code-block:: shell

      scripts/start-lockss --wait

   This will start the LOCKSS 2.x stack (now configured for normal operation).

5. .. COMMENT FIXME This should probably be in the manual's Ports appendix.

   Ports used in LOCKSS 2.x are largely different than in LOCKSS 1.x, so you need to update institutional and local firewall rules (and direct users of the system to the new ports). The full list of ports used in LOCKSS 2.x can be found in :external+lockss-manual:ref:`Network Ports` in the |MANUAL|, but here are the highlights:

   .. list-table::
      :header-rows: 1

      *  *  
         *  LOCKSS 1.x
         *  LOCKSS 2.x
      *  *  Web user interface
         *  8081
         *  -  24602: LOCKSS Configuration Service
            -  24603: LOCKSS Poller Service
            -  24604: LOCKSS Crawler Service
            -  24605: LOCKSS Metadata Service
      *  *  Content proxy
         *  Often in the 8082-8086 range; default: 9090
         *  24630
      *  *  Audit proxy
         *  Often in the 8082-8086 range
         *  24631
      *  *  ServeContent
         *  Often 8080 or in the 8082-8086 range; default: 8080
         *  24640
      *  *  SOAP API
         *  Also 8081
         *  24616
