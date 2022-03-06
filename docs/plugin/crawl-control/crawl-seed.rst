==========
Crawl Seed
==========

.. note::

   This page is under construction.

Plugin Key
   ``plugin_craw_seed_factory``

Plugin Value Type
   :ref:`string-value`

   The string is the fully-qualified name of a Java class implementing the ``org.lockss.crawler.CrawlSeedFactory`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_craw_seed_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXCrawlSeedFactory</string>
        </entry>

Description
   In lieu of a list of start URLs, code called a crawl seed can compute the starting points of the crawl of an AU, for instance by interacting with an API.
