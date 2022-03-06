===============
Permission URLs
===============

Plugin Key
   ``au_permission_url``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

   The strings are ``printf`` format strings, accepting expressions made of plugin configuration parameter keys and a small language of functions modifying them (e.g. ``url_host(...)`` applied to a plugin configuration parameter of type URL, resulting in the host portion of the URL).

Sample
   .. code-block:: xml

        <entry>
          <string>au_permission_url</string>
          <string>"%slockss.txt", base_url</string>
        </entry>

Description
   One or more URLs giving the LOCKSS software permission to crawl an AU, if permission is not given on the start URLs.
