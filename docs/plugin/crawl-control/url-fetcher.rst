===========
URL Fetcher
===========

.. note::

   This page is under construction.

Plugin Key
   ``plugin_url_fetcher_factory``

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.UrlFetcherFactory`` interface, which is a factory for the ``org.lockss.plugin.UrlFetcher`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_url_fetcher_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXUrlFetcherFactory</string>
        </entry>

Description
   *Under construction*
