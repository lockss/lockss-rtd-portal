=============
Refetch Depth
=============

.. note::

   This page is under construction.

Plugin Key
   ``au_refetch_depth``

Plugin Value Type
   :ref:`integer-value`

Sample
   .. code-block:: xml

        <entry>
          <string>au_refetch_depth</string>
          <int>2</int>
        </entry>

Description
   Number of links away from a start URL that will be fetched by normal crawls. Deep crawls may be used to cause all URLs in an AU to be refetched (subject to ``If-Modified-Since``).
