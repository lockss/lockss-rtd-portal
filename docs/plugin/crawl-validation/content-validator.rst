=================
Content Validator
=================

.. note::

   This page is under construction.

Plugin Key
   :samp:`{mediatype}_content_validator_factory`, where :samp:`{mediatype}` is a media type like :mimetype:`application/pdf`

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.ContentValidatorFactory`` interface, which is a factory for the ``org.lockss.plugin.ContentValidator`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>application/pdf_content_validator_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXPdfValidatorFactory</string>
        </entry>

Description
   A content validator can be used to reject files of a given media type, by examining the headers and/or the content of a crawled URL.
