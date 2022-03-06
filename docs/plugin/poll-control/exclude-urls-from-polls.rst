=======================
Exclude URLs From Polls
=======================

Plugin Key
   ``au_exclude_urls_from_polls_pattern``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

   The strings are ``printf`` format strings, accepting expressions made of plugin configuration parameter keys.

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
