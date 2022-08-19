===============================
Exclude URLs From Polls Pattern
===============================

Plugin Key
   ``au_exclude_urls_from_polls_pattern``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

Plugin Value Type
   The strings are ``printf`` format strings that expand to regular expressions used to match against URLs. The ``printf`` format strings accept expressions made of plugin configuration parameter keys.

Sample
   .. code-block:: xml

        <entry>
          <string>au_exclude_urls_from_polls_pattern</string>
          <list>
            <string>"^%scss/.*\.css\?version=", base_url</string>
            <string>"^%sfiles/[0-9]+/.*\.js", base_url</string>
          </list>
        </entry>

Description
   URLs characterized by the regular expressions expanded from the ``printf`` strings are excluded (ignored) during polls of the AU.
