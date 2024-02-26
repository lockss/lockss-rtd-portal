==================================
Starter Network Configuration File
==================================

Below is a suitable starter network configuration file for many typical LOCKSS networks, starting with LOCKSS 1.78 for LOCKSS 1x and and LOCKSS 2.0-beta1 for LOCKSS 2.x. The absolute must-haves are to define plugin registries and AU inventories, to set the polling quorum, and to list the LCAPv3 identities of the nodes in the network.

.. literalinclude:: starter.xml
   :language: xml
   :linenos:
