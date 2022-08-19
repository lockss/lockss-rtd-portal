===========
Hash Filter
===========

Plugin Key
   :samp:`{mediatype}_filter_factory`, where :samp:`{mediatype}` is a media type like :mimetype:`text/html`

Value Type
   :ref:`string-value`

Plugin Value Type
   The string is the fully-qualified name of a Java class implementing the ``org.lockss.plugin.FilterFactory`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>text/html_filter_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXHtmlHashFilterFactory</string>
        </entry>

Description
   To canonicalize content before comparison between nodes in the LOCKSS audit and repair protocol, a plugin can define a hash filter for each affected media type. The goal is to pre-process content so that it is fit for a **logical comparison** between nodes, even if different nodes do not have byte-identical versions. This occurs frequently in HTML content that has personalizations ("You are logged in as..."), advertising, and other variable content ("You may also be interested in...", "Top 10 viewed articles this week...", "Recently added articles...") other than the main content. It can be needed for other media types like PDF and RIS because of timestamping, watermarking, and other dynamic server behaviors.

   The ``org.lockss.plugin.FilterFactory`` interface defines a ``createFilteredInputStream`` method that accepts an ``org.lockss.plugin.ArchivalUnit`` object, an ``InputStream`` of the URL's raw content, and a string representing the encoding, and returns an ``InputStream` of the canonicalized byte stream, which does not need to be a valid object of that media type (it is only used to compute a checksum).

   As part of its general content filtering framework, the LOCKSS plugin framework offers a variety of utility classes specifically for :doc:`html-filters` and :doc:`pdf-filters`.
