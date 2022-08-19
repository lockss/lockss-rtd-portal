=============
Link Rewriter
=============

.. note::

   This page is under construction.

Plugin Key
   :samp:`{mediatype}_link_rewriter_factory`, where :samp:`{mediatype}` is a media type like ``text/html``

Plugin Value Type
   :ref:`string-value`

Plugin Value Type
   The value is the fully qualified name of a Java class implementing the ``org.lockss.extractor.LinkRewriterFactory`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>text/html_link_rewriter_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXHtmlLinkRewriterFactory</string>
        </entry>

Description
   When content is replayed through the LOCKSS system's ServeContent Web replay engine, links have to be rewritten so that they point to other ServeContent URLs where applicable. ServeContent contains logic to handle typical cases in HTML and CSS, but some specific use cases may require additional or custom link rewriting. To accomplish this, the plugin defines link rewriters for the affected media types.

   For example, a Web site could have image tags for journal article figures that look like this: ``<img src="fig1_small.jpg" data-target="fig1_large.jpg" />``, and Javascript code in the page such that when the small version of the image is clicked, an image viewer widget is displayed with the large version of the image instead. ServeContent has internal logic that knows to look for the ``src`` attribute of ``<img>`` tags, but would not know to also process this non-standard ``data-target`` attribute so the image viewer widget works with a preserved copy of the large version of the image. Depending on the situation, this might require a custom rewriter for just HTML, or for HTML plus Javascript.
