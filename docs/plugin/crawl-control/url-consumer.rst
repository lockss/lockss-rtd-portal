============
URL Consumer
============

.. note::

   This page is under construction.

Plugin Key
   ``plugin_url_consumer_factory``

Plugin Value Type
   :ref:`string-value`

   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.UrlConsumerFactory`` interface, which is a factory for the ``org.lockss.plugin.UrlConsumer`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_url_consumer_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXUrlConsumerFactory</string>
        </entry>

Description
   *Under construction*
