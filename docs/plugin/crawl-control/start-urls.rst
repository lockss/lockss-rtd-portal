==========
Start URLs
==========

Plugin Key
   ``au_start_url``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

   The strings are ``printf`` format strings, accepting expressions made of plugin configuration parameter keys and a small language of functions modifying them (e.g. ``url_host(...)`` applied to a plugin configuration parameter of type URL, resulting in the host portion of the URL).

Sample
   .. code-block:: xml

        <entry>
          <string>au_start_url</string>
          <string>"%s%s/vol%s/index.html", base_url, journal_id, volume_name</string>
        </entry>

Description
   One or more URLs from which the crawl of an AU begins.
