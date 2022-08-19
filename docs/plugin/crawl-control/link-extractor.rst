==============
Link Extractor
==============

.. note::

   This page is under construction.

Plugin Key
   :samp:`{mediatype}_link_extractor_factory`, where :samp:`{mediatype}` is a media type like :mimetype:`text/html`

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.LinkExtractorFactory`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>text/html_link_extractor_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXHtmlLinkExtractorFactory</string>
        </entry>

Description
   The LOCKSS software comes with built-in code to extract URLs from HTML and CSS files encountered during the crawl of an AU. A URL extracted in this manner is then subject to the :doc:`url-normalizer`, then the :doc:`crawl-rules` determine if it should in turn be included in the AU. If URLs need to be extracted from other file types, or if the extraction behavior for built-in types like HTML and CSS needs to be extended or customized, this plugin feature can be used to point the plugin at new link extraction code.
