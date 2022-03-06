===========================
Repair From Peer If Missing
===========================

.. note::

   This page is under construction.

Plugin Key
   ``au_repair_from_peer_if_missing_url_pattern``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

   The strings are ``printf`` format strings, accepting expressions made of plugin configuration parameter keys.

Sample
   .. code-block:: xml

        <entry>
          <string>au_repair_from_peer_if_missing_url_pattern</string>
          <list>
            <string>"^%s.*\.(css|js|png|jpe?g|png|gif|tiff)\?ver=.*$", base_url</string>
            <string>"^https://code\.jquery\.org/"</string>
          </list>
        </entry>

Description
   When this feature is set, if during a poll the poller determines it is missing a URL that matches one of the patterns, it will seek a repair from a peer. This can be useful when a family of URLs keeps getting new variants (with unique names) rapidly, to allow the variants to spread among the network of peers.
