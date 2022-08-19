===================
Substance Predicate
===================

.. note::

   This page is under construction.

Plugin Key
   ``plugin_substance_predicate_factory``

Plugin Value Type
   :ref:`string-value`

Plugin Value Type
   The value is the fully qualified name of a Java class implementing the ``org.lockss.plugin.SubstancePredicateFactory`` interface, which is a factory for the ``org.lockss.plugin.SubstancePredicate`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_substance_predicate_factory</string>
          <string>edu.example.plugin.publisherx.PublisherXSubstancePredicateFactory</string>
        </entry>

Description
   An alternative to the regular expressions in the :doc:`substance-patterns` is a substance predicate, which is implemented as Java code.
