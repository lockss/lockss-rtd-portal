=====================
Rewrite Meta Tag URLs
=====================

.. note::

   This page is under construction.

Plugin Key
   ``plugin_rewrite_html_meta_urls``

Plugin Value Type
   :ref:`List` of :ref:`string-value`

   Each string in the list is a value of the ``name`` attribute of HTML ``<meta>`` tags.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_rewrite_html_meta_urls</string>
          <list>
            <string>citation_abstract_url</string>
            <string>citation_pdf_url</string>
          </list>
        </entry>

Description
   This plugin feature enables a canned HTML :doc:`link-rewriter` that seeks out ``<meta name="..." content="...">`` tags where the value of the ``name`` attribute matches one of the specified names, and rewrites the URL that is the value of their ``content`` attribute.
