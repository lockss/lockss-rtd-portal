=============================
Redirect to Login URL Pattern
=============================

Plugin Key
   ``au_redirect_to_login_url_pattern``

Plugin Value Type
   :ref:`string-value`

Plugin Value Format
   The string is a ``printf`` format string that expands to a regular expression used to match against URLs. The ``printf`` format string accepting expressions made of plugin configuration parameter keys.

Sample
   .. code-block:: xml

        <entry>
          <string>au_redirect_to_login_url_pattern</string>
          <string>"^%ssignup-login.*", base_url</string>
        </entry>

Description
   Determines whether an HTTP redirect returned by the crawled site is actually a redirect to a login page.

   During the crawl of an AU, a redirect from a URL that is accepted by the crawl rules to a URL that is not is a non-fatal crawl error, meaning it gets reported at the end of the crawl rather than immediately stopping it.

   If a Web site issues an HTTP redirect to a login page URL when an IP address accesses a URL it is not authorized to view, it is often desirable to recognize this situation differently than other redirects to URLs outside the crawl rules. This key is used to identify such redirects and treat them as fatal crawl errors instead of non-fatal crawl errors.
