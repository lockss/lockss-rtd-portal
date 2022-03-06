=======================
Required Daemon Version
=======================

Plugin Key
   ``required_daemon_version``

Plugin Value Type
   :ref:`string-value`

Sample

   .. code-block:: xml

        <entry>
          <string>required_daemon_version</string>
          <string>1.74.7</string>
        </entry>

Description
   The release number of the earliest version of the LOCKSS software that supports all the features required by the plugin.

   In the classic LOCKSS system (1.x), this is a string like `1.75.9` (version 1.75.9 or higher) or `1.75.0` (version 1.75.x or higher). In the rearchitected LOCKSS system (2.x), this is currently only `2.0-alpha1` through `2.0-alpha5`.
