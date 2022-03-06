================
Response Handler
================

.. note::

   This page is under construction.

Plugin Key
   ``plugin_cache_result_list``

Plugin Value Type
   :ref:`List` of :ref:`string-value`

   The list represents a mapping; each string is of the form :samp:`{x}={y}`, mapping from the left-hand side :samp:`{x}` which can be:

   * An HTTP response code (integer).

   * One of a finite set of Java exceptions (string).

   to the right-hand side :samp:`{y}` which can be:

   * The fully-qualified name of a Java class extending the ``org.lockss.util.urlconn.CacheException`` class.

   * The fully-qualified name of a Java class implementing the ``org.lockss.util.urlconn.CacheResultHandler`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_cache_result_list</string>
          <list>
            <string>500=edu.example.plugin.publisherx.PublisherXHttpResponseHandler</string>
            <string>java.io.IOException=org.lockss.util.urlconn.CacheException$RetryableNetworkException_3_30S</string>
          </list>
        </entry>
