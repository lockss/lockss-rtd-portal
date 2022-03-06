=============
Parent Plugin
=============

Plugin Key
   ``plugin_parent``

Plugin Value Type
   :ref:`string-value`

   The value is the :doc:`../identification/plugin-identifier` of this plugin's parent.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_parent</string>
          <string>edu.example.plugin.platformx.PlatformXPlugin</string>
        </entry>

Description
   Declares that this plugin uses the specified plugin as its parent. This plugin inherits the key-value pairs from the parent plugin, and additionally adds values for keys not found in the parent or redefines the value for a key found in the parent.

   If the parent plugin maps a key to a specific value and this plugin wishes to undo the effect and simply use whatever the default is for the key in the system, this plugin can map the key to the special value ``<org.lockss.util.Default />``.
