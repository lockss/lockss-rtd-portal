======================
Permitted Host Pattern
======================

.. note::

   This page is under construction.

Plugin Key
   ``au_permitted_host_pattern``

Plugin Value Type
   One of:

   *  :ref:`string-value`

   *  :ref:`List` of :ref:`string-value`

Plugin Value Format
   The strings are ``printf`` format strings, that expand to regular expressions used to match against host names. The ``printf`` format strings accept expressions made of plugin configuration parameter keys and a small language of functions modifying them (e.g. ``url_host(...)`` applied to a plugin configuration parameter of type URL, resulting in the host portion of the URL).

Example
   .. code-block:: xml

        <entry>
          <string>au_permitted_host_pattern</string>
          <string>"cdnjs\.cloudflare\.com|fast\.fonts\.net"</string>
        </entry>

Description
   Pattern rules to allow collection from hosts that cannot explicitly grant permission, such as content distribution network hosts used to distribute standard components used by Web sites like Javascript libraries and Web fonts.
