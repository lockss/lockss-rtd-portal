==================
Substance Patterns
==================

.. note::

   This page is under construction.

Plugin Key
   ``au_substance_url_pattern`` and ``au_non_substance_url_pattern``

Plugin Value Type
   :ref:`string-value`

   The strings are ``printf`` format strings, accepting expressions made of plugin configuration parameter keys.

Sample
   .. code-block:: xml

        <entry>
          <string>au_substance_url_pattern</string>
          <string>"^%s/%s/(fulltext|pdf)/", base_url, journal_id</string>
        </entry>

Description
   It can be useful to test whether at least one URL in an AU is "of substance", meaning that it is one of the objects of preservation interest and not simply navigation pages and ancillary files (icons, CSS stylesheets, Javascript code). The substance pattern can be used to characterize the URLs of an AU that are of substance. Conversely, the non-substance pattern can be used to characterize the URLs of an AU that are not of substance.
