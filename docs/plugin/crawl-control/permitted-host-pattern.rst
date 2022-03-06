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

Example
   .. code-block:: xml

        <entry>
          <string>au_permitted_host_pattern</string>
          <string>"cdnjs\.cloudflare\.com|fast\.fonts\.net"</string>
        </entry>

Description
   Pattern rules to allow collection from hosts that cannot explicitly grant permission, such as content distribution network hosts used to distribute standard components used by Web sites like Javascript libraries and Web fonts.
