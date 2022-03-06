============
Crawl Window
============
.. note::

   This page is under construction.

Plugin Key
   ``au_crawlwindow``, ``au_crawlwindow_ser``

Plugin Value Type
  ``au_crawlwindow`` value type: :ref:`string-value` representing the fully-qualified name of a Java class implementing the ``org.lockss.plugin.definable.DefinableArchivalUnit.ConfigurableCrawlWindow`` interface, which is a factory for the ``org.lockss.daemon.CrawlWindow`` interface.

   ``au_crawlwindow_ser`` value type: a serialized ``org.lockss.daemon.CrawlWindow`` object.

Description
   A crawl window controls what times of day or days of the week crawls against the preservation target are allowed; by default an AU is eligible to crawl at any time.
