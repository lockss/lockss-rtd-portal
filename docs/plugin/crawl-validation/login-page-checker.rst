==================
Login Page Checker
==================

.. note::

   This page is under construction.

Plugin Key
   ``au_login_page_checker``

Plugin Value Type
   :ref:`string-value`

   The value is the fully qualified name of a Java class implementing the ``org.lockss.daemon.LoginPageChecker`` interface.

Sample
   .. code-block:: xml

        <entry>
          <string>au_login_page_checker</string>
          <string>edu.example.plugin.publisherx.PublisherXLoginPageChecker</string>
        </entry>

Description
   When fetching a URL that the requesting IP address is not authorized to retrieve, some Web sites respond with HTTP success code accompanied by an HTML page that is really a login page or error page, rather than with an HTTP error code. A login page checker is a general interface for checking the contents of a URL and determine if it is a login page rather than the intended content.
