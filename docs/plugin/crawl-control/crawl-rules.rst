===========
Crawl Rules
===========

Plugin Key
   ``au_crawlrules``

Plugin Value Type
   :ref:`List` of :ref:`string-value`

Plugin Value Format
   The strings consist of:

   *  An integer crawl rule code,

   *  A comma,

   *  A ``printf`` format string that expands into a regular expression used to match against URLs. The ``printf`` format string accepts expressions made of plugin configuration parameter keys and a small language of functions modifying them (e.g. ``url_host(...)`` applied to a plugin configuration parameter of type :ref:`URL`, resulting in the host portion of the URL).

Sample
   .. code-block:: xml

        <entry>
          <string>au_crawlrules</string>
          <list>
            <string>4, "^%s", base_url</string>
            <string>1, "^%s.*\.(css|js|gif|jpg|png)$", base_url</string>
            <string>2, "^%s%s/vol%s/iss[^/]+/art[^/]+/citedby", base_url, journal_id, volume_name</string>
            <string>1, "^%s%s/vol%s/", base_url, journal_id, volume_name</string>
            <string>1, "^%spdf/.*\.pdf$", base_url</string>
          </list>
        </entry>

Description
   Sequential rules determining if a URL discovered during the crawl of an AU should in turn be fetched as part of the AU or not.

   Given a URL, the crawler tries each crawl rule in the order of the list, until one of them produces an outcome for the URL. If none of the crawl rules result in an outcome for the URL, the default outcome is :ref:`Exclude` (the URL is excluded from the AU).

----------------
Crawl Rule Types
----------------

The crawl rule codes are:

=============== ===============
Crawl Rule Code Crawl Rule Type
=============== ===============
``1``           :ref:`Include`
``2``           :ref:`Exclude`
``3``           :ref:`Include No Match`
``4``           :ref:`Exclude No Match`
``5``           :ref:`Include Match Else Exclude`
``6``           :ref:`Exclude Match Else Include`
=============== ===============

Include
-------

Crawl Rule Code
   ``1``

Description
   If the URL matches the regular expression, include the URL in the AU; otherwise, this rule produces no outcome for the URL.

Exclude
-------

Crawl Rule Code
   ``2``

Description
   If the URL matches the regular expression, exclude the URL from the AU; otherwise, this rule produces no outcome for the URL.

Include No Match
----------------

Crawl Rule Code
   ``3``

Description
   If the URL does not match the regular expression, include the URL in the AU; otherwise, this rule produces no outcome for the URL.

Exclude No Match
----------------

Crawl Rule Code
   ``4``

Description
   If the URL does not match the regular expression, exclude the URL from the AU; otherwise, this rule produces no outcome for the URL.

Include Match Else Exclude
--------------------------

Crawl Rule Code
   ``5``

Description
   If the URL matches the regular expression, include the URL in the AU; otherwise, exclude the URL from the AU.

Exclude Match Else Include
--------------------------

Crawl Rule Code
   ``6``

Description
   If the URL matches the regular expression, exclude the URL from the AU; otherwise, include the URL in the AU.
