==============
URL Normalizer
==============

.. note::

   This page is under construction.

Plugin Key
   ``au_url_normalizer``

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The value is the fully-qualified name of a Java class that implements the ``org.lockss.plugin.UrlNormalizer`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>au_url_normalizer</string>
          <string>edu.example.plugin.publisherx.PublisherXUrlNormalizer</string>
        </entry>

Description
   A URL normalizer maps URL variants to a canonical representation, for example by re-arranging equivalent URL query strings into a canonical order, removing extraneous URL substrings (for instance session IDs), canonicalizing the case (for instance to lowercase), etc. so that equivalent variants are stored only once under the canonical name.
