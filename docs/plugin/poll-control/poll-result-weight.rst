==================
Poll Result Weight
==================

Plugin Key
   ``au_url_poll_result_weight``

Plugin Value Type
   *  :ref:`List` of :ref:`string-value`

Plugin Value Format
   Each string in the list consists of:

   *  A regular expression,
   *  A comma,
   *  A weight between 0.0 and 1.0.

Sample
   .. code-block:: xml

        <entry>
          <string>au_url_poll_result_weight</string>
          <list>
            <string>\.(css|js|png|jpe?g|png|gif|tiff)\?ver=.*$, 0</string>
          </list>
        </entry>

Description
   This mechanism is a generalization of :doc:`exclude-urls-from-polls`, which can only exclude URLs from a poll (equivalent of assigning the corresponding URLs a weight of 0.0). Here, URLs can be assigned a partial weight, to reduce the importance of certain families of URLs in polls.
