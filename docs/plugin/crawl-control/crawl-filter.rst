============
Crawl Filter
============

.. note::

   This page is under construction.

Plugin Key
   :samp:`{mediatype}_crawl_filter_factory`, where :samp:`{mediatype}` is a media type like :mimetype:`text/html`

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.FilterFactory`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>text/html_crawl_filter_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXHtmlCrawlFilterFactory</string>
        </entry>

Description
   If files of a given media type need to be pre-processed (filtered) before URLs are extracted by the crawler using a :doc:`link-extractor`, this plugin feature can be used to point at custom filtering code.

   Crawl filters are somewhat related to :doc:`hash filters </plugin/hash-filtering/hash-filter>`.
