===========
Plugin Name
===========

Plugin Key
   ``plugin_name``

Plugin Value Type
   :ref:`string-value`

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_name</string>
          <string>Publisher X Journals Plugin</string>
        </entry>

Description
   A user-friendly name for the plugin.

   This name is only displayed in a few places in the LOCKSS Web user interface, for instance in the Plugins table.

Example
   In the Global LOCKSS Netowrk (GLN), the plugin to process volumes of journals by Oxford University Press (OUP) hosted on the Silverchair platform has the name ``Oxford University Press Journals Plugin``.

   .. code-block:: xml

        <entry>
          <string>plugin_name</string>
          <string>Oxford University Press Plugin</string>
        </entry>

   (You can find this plugin on GitHub at https://github.com/lockss/lockss-daemon/blob/master/plugins/src/org/lockss/plugin/silverchair/oup/OupSilverchairPlugin.xml.)
