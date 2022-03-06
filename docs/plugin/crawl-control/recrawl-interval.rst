================
Recrawl Interval
================

Plugin Key
   ``au_def_new_content_crawl``

Plugin Value Type
   :ref:`long-value`

Sample
   .. code-block:: xml

        <entry>
          <string>au_def_new_content_crawl</string>
          <long>1209600000</long>
        </entry>

Description
   The amount of time (in milliseconds) before an AU that has previously been crawled successfully is eligible to attempt crawling again.

   Sample values:

   *  ``31449600000`` for 52 weeks (364 days).

   *  ``1209600000`` for 2 weeks (the most typical value in the Global LOCKSS Network).

   *  ``604800000`` for 1 week.

   *  ``86400000`` for 24 hours.
