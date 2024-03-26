==================================
Starter Network Configuration File
==================================

The following is a suitable starter network configuration file for a typical LOCKSS network, namely, a closed network where all the nodes are running LOCKSS 1.x version 1.78 or later and/or LOCKSS 2.x version 2.0-beta1 or later:

.. literalinclude:: starter.xml
   :language: xml
   :linenos:

The key configuration properties are:

*  **Plugin registries** (``org.lockss.plugin.registries``): One or more URLs of plugin registries used by this network.

*  **Archival unit catalogs** (``org.lockss.titleDbs``): *Optional.* One or more URLs of archival unit catalog files for this network. Omit if all nodes are running LOCKSS 2.0-beta1 or later, and there are no pre-defined AUs (all AUs are created and populated dynamically through API calls to each node's repository).

*  **Polling quorum** (``org.lockss.poll.v3.quorum``): The quorum for the polling and repair protocol in this network. The absolute minimum is 3.

*  **Node list** (``org.lockss.id.initialV3PeerList``): The list of LCAPv3 identities of the nodes in the network.

Optional settings to consider include:

*  **Network logo** (``org.lockss.ui.logo.img``): *Optional.* The URL of an image file representing the network's logo. Recommended height: 80 pixels.

*  **Network Web site link** (``org.lockss.ui.logo.link``): *Optional.* The URL of the network's Web site, to make the network logo (see above) clickable.

*  **Help link** (``org.lockss.ui.helpUrl``): *Optional.* The URL of a help Web page, to appear in the LOCKSS Web user interface in the top-right menu.

*  **Initial access subnets** (``org.lockss.ui.access.ip.include``): *Optional.* One or more IP subnets that should be able to access the Web UI of a node in the network, until the node sets its own access list. Useful only if there is a meaningful network-wide value for this.

The default values for a number of useful configuration properties were changed in LOCKSS 1.x version 1.78 and LOCKSS 2.x version 2.0-beta1 so they better reflect typical LOCKSS networks rather than very large networks like the GLN or CLOCKSS. If your network includes some nodes running LOCKSS 1.x version 1.77.6 or earlier and/or LOCKSS 2.x version 2.0-alpha7 or earlier, you will need to add the highlighted section below to your network configuration file:

.. literalinclude:: starter-hybrid.xml
   :language: xml
   :linenos:
   :emphasize-lines: 92-139

You can then remove that section when all nodes in the network are running LOCKSS 1.x version 1.78 or later and/or LOCKSS 2.x version 2.0-beta1 or later.
