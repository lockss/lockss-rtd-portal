.. include:: subst.rst

============================================================
Appendix: Instructions for Administrators of LOCKSS Networks
============================================================

This guide is primarily aimed at operators of individual LOCKSS nodes; this appendix describes **actions that must be performed by administrators of LOCKSS networks through the transitional period of migration of the nodes from LOCKSS 1.x to 2.x**:

*  There are network-wide tasks to perform :ref:`Before the First Migration` and :ref:`After the Last Migration`.

*  Additionally, there are node-specific tasks to perform :ref:`Before Each Migration` and :ref:`After Each Migration`.

--------------------------
Before the First Migration
--------------------------

.. rubric:: LOCKSS 2.x poll compatibility mode before migration
   :name: LOCKSS 2.x poll compatibility mode before migration

Before any LOCKSS 1.x node in your network migrates to LOCKSS 2.x, you will need to set ``org.lockss.poll.2.0Compatible`` to ``true`` in LOCKSS 1.79.1 or later in the network configuration file [#fn-props-file]_. For example in a typical XML network configuration file where the prefix ``org.lockss`` is enclosed in a file-wide ``<property name="org.lockss">`` block, this would look like this:

.. code-block:: xml

   <if daemonVersionMin="1.79.1">
     <then>
       <property name="poll.2.0Compatible" value="true" />
     </then>
   </if>

---------------------
Before Each Migration
---------------------

1. .. rubric:: Access control before migration
      :name: Access control before migration

   |NEWHOSTONLY| When a node in the network is slated to begin a :ref:`New-Host Migration`, add the new IP address of the LOCKSS 2.x host to your network configuration server [#fn-props-server]_ firewall rules and Web server access control, so it can access resources like the network configuration file [#fn-props-file]_ and plugin registries. See the :ref:`New-Host Migration` portion of :numref:`Chapter %s <Preparing the LOCKSS 2.x Host>` (:ref:`Preparing the LOCKSS 2.x Host`).

2. .. rubric:: Initial peer list before migration
      :name: Initial peer list before migration

   When a node in the network is slated to begin migration (in any :ref:`Migration Scenario`), **do not add** an |LCAP| identity to the initial peer list (``org.lockss.id.initialV3PeerList``); simply leave the existing LCAP identity of the migrating node alone during its migration.

--------------------
After Each Migration
--------------------

1. .. rubric:: Access control after migration
      :name: Access control after migration

   |NEWHOSTONLY| When a node in the network finishes a :ref:`New-Host Migration`, you need to adjust your network configuration server [#fn-props-server]_ firewall rules and Web server access control accordingly:

   *  If the LOCKSS 2.x host adopts the IP address previously associated with the corresponding LOCKSS 1.x host, which is recommended, you can remove the new IP address of the LOCKSS 2.x host which had been added in :ref:`Access control before migration` in :numref:`Before Each Migration` (:ref:`Before Each Migration`).

   *  If adopting the IP address previously associated with the corresponding LOCKSS 1.x host is not possible, instead you will need to remove the old IP address of the LOCKSS 1.x host which had been present prior to the migration.

   See the :ref:`New-Host Migration` portion of :numref:`Chapter %s <Reconfiguring LOCKSS 2.x for Normal Operation>` (:ref:`Reconfiguring LOCKSS 2.x for Normal Operation`) for context.

2. .. rubric:: Change of Hostname
      :name: Change of Hostname

   |NEWHOSTONLY| If the node finishing a :ref:`New-Host Migration` does not retain the hostname previously used by its LOCKSS 1.x instance, you may need to update the hostname in monitoring tools you utilize in the network. See the :ref:`New-Host Migration` portion of :numref:`Chapter %s <Reconfiguring LOCKSS 2.x for Normal Operation>` (:ref:`Reconfiguring LOCKSS 2.x for Normal Operation`) for context.

3. .. rubric:: Change of LCAP identity
      :name: Change of LCAP identity

   If the node finishing a migration does not retain both the IP address and |LCAP| port previously used by its LOCKSS 1.x instance, its |LCAP| (LOCKSS audit and repair) identity in the network has changed and action is needed. See :numref:`Chapter %s <Reconfiguring LOCKSS 2.x for Normal Operation>` (:ref:`Reconfiguring LOCKSS 2.x for Normal Operation`) for context. Follow these steps:

   a. .. rubric:: Initial peer list after migration
         :name: Initial peer list after migration

      You will need to update from the old LCAP identity to the new LCAP identity in the initial peer list (``org.lockss.id.initialV3PeerList``) in the network configuration file [#fn-props-file]_.

   b. .. rubric:: Poll transfer map
         :name: Poll transfer map

      You will need to add the new LCAP identity to the poll transfer map (``org.lockss.poll.v3.reputationTransferMap``) in the network configuration file [#fn-props-file]_:

      *  If the node already has a chain in the poll transfer map, append the new LCAP identity to the end of the node's chain (after a comma), which currently ends with the LCAP identity that just changed as a result of the migration, symbolically:

         :samp:`<value>{list_of_prior_identities},{most_recent_identity},{brand_new_identity}</value>`

      *  If this is the node's first change of LCAP identity, add a chain for it, consisting of the old identity, a comma, and the new identity, symbolically:

         :samp:`<value>{old_identity},{new_identity}</value>`

         This might be the first change of LCAP identity in the network, in which case you will be adding the poll transfer map to the  network configuration file [#fn-props-file]_ for the poll transfer map for the first time. For example in a typical XML network configuration file where the prefix ``org.lockss`` is enclosed in a file-wide ``<property name="org.lockss">`` block, this would look like this:

         .. code-block:: xml

            <property name="poll.v3.reputationTransferMap">
              <list>
                <value>...</value>
              </list>
            </property>

------------------------
After the Last Migration
------------------------

.. rubric:: LOCKSS 2.x poll compatibility mode after migration
   :name: LOCKSS 2.x poll compatibility mode after migration

After all nodes in your network are running LOCKSS 2.x, unset the ``org.lockss.poll.2.0Compatible`` parameter in the network configuration file [#fn-props-file]_.

----

.. rubric:: Footnotes

.. [#fn-props-server]

   The network configuration server is also often referred to as the *props server*.

.. [#fn-props-file]

   The network configuration file is also often referred to as the *props file*.
