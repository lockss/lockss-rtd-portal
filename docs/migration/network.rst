.. include:: subst.rst

==============================================================
Appendix: Considerations for Administrators of LOCKSS Networks
==============================================================

This appendix describes a few actions that must be performed by administrators of LOCKSS networks :ref:`Before the First Migration`, :ref:`Before Each Migration`, :ref:`After Each Migration`, and :ref:`After the Last Migration` in a network.

--------------------------
Before the First Migration
--------------------------

Before any LOCKSS 1.x node in your network migrates to LOCKSS 2.x, you will need to set ``org.lockss.poll.2.0Compatible`` to ``true`` in the network configuration file [#fn-props-file]_. For example in a typical XML network configuration file where the prefix ``org.lockss`` is enclosed in a file-wide ``<property name="org.lockss">`` block, this would look like this:

.. code-block:: xml

   <property name="poll.2.0Compatible" value="true" />

---------------------
Before Each Migration
---------------------

When a migration is slated to occur, **do not add** an |LCAP| identity to the initial peer list (``org.lockss.id.initialV3PeerList``); simply leave the existing LCAP identity of the migrating box alone during its migration. Specifically:

*  |NEWHOSTONLY| For a :ref:`New-Host Migration`, **do not add** an |LCAP| identity constructed from the IP address of the LOCKSS 2.x host to the initial peer list. However, refer to :numref:`After Each Migration` (:ref:`After Each Migration`) in case the LOCKSS 2.x node does not adopt the LOCKSS 1.x node's IP address at the end of migration.

*  |SAMEHOSTONLY| For a :ref:`New-Host Migration`, **do not add** an |LCAP| identity constructed from the LOCKSS 2.x instance's temporary LCAP port to the initial peer list.

--------------------
After Each Migration
--------------------

FIXME (LCAP identity changes)

------------------------
After the Last Migration
------------------------

After all nodes in your network are running LOCKSS 2.x, unset the ``org.lockss.poll.2.0Compatible`` parameter in the network configuration file [#fn-props-file]_.

----

.. rubric:: Footnotes

.. [#fn-props-file]

   The network configuration file is also often referred to as the *props file*.
