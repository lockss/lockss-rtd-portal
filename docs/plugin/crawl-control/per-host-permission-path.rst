========================
Per-Host Permission Path
========================

Plugin Key
   ``plugin_per_host_permission_path``

Plugin Value Type
   :ref:`string-value`

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_per_host_permission_path</string>
          <string>/lockss.txt</string>
        </entry>

Description
   Relative path where a permission statement may be found on hosts not listed in start URLs or permission URLs. Useful for sites that have banks of similar hosts with unpredictable names, but with a predictable path to the permission URL on each.
