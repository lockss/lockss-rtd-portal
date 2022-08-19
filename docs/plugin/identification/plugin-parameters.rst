===============================
Plugin Configuration Parameters
===============================

Plugin Key
   ``plugin_config_props``

Plugin Value Type
      :ref:`List` of ``<org.lockss.daemon.ConfigParamDescr>`` stanzas

Sample
   .. code-block:: xml

        <entry>
          <string>plugin_config_props</string>
          <list>
            <org.lockss.daemon.ConfigParamDescr>
              <key>base_url</key>
              <displayName>Base URL</displayName>
              <description>Usually of the form http://&lt;journal-name&gt;.com/</description>
              <type>3</type>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>
            <org.lockss.daemon.ConfigParamDescr>
              <key>journal_id</key>
              <displayName>Journal Identifier</displayName>
              <description>Identifier for journal (often used as part of file names)</description>
              <type>1</type>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>
            <org.lockss.daemon.ConfigParamDescr>
              <key>volume_name</key>
              <displayName>Volume Name</displayName>
              <type>1</type>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>
          </list>
        </entry>

Description
   A list of **configuration parameter descriptors**, defining the placeholders in use in the plugin's rules and code.

   A plugin's rules and code (start and permission URLs, crawl rules, substance patterns...) are made general by identifying placeholders for AU-specific values and substituting them later. These placeholders for variable values are called **plugin configuration parameters**.

   Defining the necessary configuration parameters for a given plugin comes mostly from studying the URL structure of the preservation target, finding patterns, and identifying the parts of those patterns that differ between Archival Units.

Structure
   Each plugin configuration parameter is represented by a ``<org.lockss.daemon.ConfigParamDescr>`` stanza that looks like this:

   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>...</key>
              <type>...</type>
              <displayName>...</displayName>
              <description>...</description>
              <size>...</size>
              <definitional>...</definitional>  <!-- default: true -->
              <defaultOnly>...</defaultOnly>    <!-- default: false -->
            </org.lockss.daemon.ConfigParamDescr>

   Only ``<key>`` and ``<type>`` are required.

   Each ``<org.lockss.daemon.ConfigParamDescr>`` stanza contains the following important elements:

   *  ``<key>``: the **parameter key**, an identifier for the configuration parameter, standing in as a placeholder for the AU-specific value in rules and code. Example: ``base_url`` for a base URL (URL prefix common to all or most URLs in an AU).

   *  ``<type>``: the **parameter type**, an integer describing the type of value the configuration parameter represents (string, integer, etc.). See :ref:`Parameter Types` below for details.

   *  ``<definitional>``: whether the parameter is a **definitional parameter** or **non-definitional parameter**, expressed as the booleans ``true`` or ``false``. Most parameters are definitional (``true``), meaning the parameter is part of the set of parameters that together form the unique identity of the AU.

   *  ``<defaultOnly>``: set to ``false`` in almost all cases.

   The other elements only play a role in the *Manual Add/Edit* screen in the LOCKSS Web user interface:

   *  ``<displayName>``: the **parameter display name**, a user-friendly name for the parameter in in the *Manual Add/Edit* screen.

   *  ``<description>``: the **parameter description**, a user-friendly text string describing the parameter and giving an example value in the *Manual Add/Edit* screen.

   *  ``<size>``: the parameter display size in characters in the *Manual Add/Edit* screen.

---------------
Parameter Types
---------------

The following plugin configuration parameter types are defined in the LOCKSS software:

=================== ==============
Parameter Type Code Parameter Type
=================== ==============
``1``               :ref:`string-type`
``2``               :ref:`integer-type`
``3``               :ref:`URL`
``4``               :ref:`year-type`
``5``               :ref:`Boolean`
``6``               :ref:`Non-Negative Integer`
``7``               :ref:`String Range`
``8``               :ref:`Numeric Range`
``9``               :ref:`Set`
``10``              :ref:`User Credentials`
``11``              :ref:`long-type`
``12``              :ref:`Time Interval`
=================== ==============

.. _string-type:

String
======

Parameter Type Code
   ``1``

Description
   A non-empty string.

Built-In Examples
   :ref:`Volume Name`, :ref:`Journal Directory`, :ref:`Journal Abbreviation`, :ref:`Journal Identifier`, :ref:`Journal ISSN`, :ref:`Publisher Name`, :ref:`OAI Spec`, :ref:`Crawl Proxy`, :ref:`Crawl Test Substance Threshold`

URL
===

Parameter Type Code
   ``3``

Description
   Used most frequently as a URL prefix. This must be a valid URL string according to Java's ``java.net.URL`` constructor (`<https://docs.oracle.com/javase/8/docs/api/java/net/URL.html#URL-java.lang.String->`_).

Built-In Examples
   :ref:`Base URL`, :ref:`Second Base URL`, :ref:`OAI Request URL`

See Also
   :ref:`Derivative URL Parameters`

User Credentials
================

Parameter Type Code
   ``10``

Description
   A colon-separated username and password, for instance ``myuser:mypass``.

Built-In Examples
   :ref:`Username and Password`

.. _integer-type:

Integer
=======

Parameter Type Code
   ``2``

Description
   The integer can be negative. Represented internally as a 32-bit integer.

Non-Negative Integer
====================

Parameter Type Code
   ``6``

Description
   The integer can be zero but cannot be negative. Represented internally as a 32-bit integer.

Built-In Examples
   :ref:`Volume Number`

.. _long-type:

Long Integer
============

Parameter Type Code
   ``11``

Description
   The value can be negative. Represented internally as a 64-bit integer.

.. _year-type:

Year
====

Parameter Type Code
   ``4``

Description
   A four-digit year, or the special value `0` to denote an unspecified year.

Built-In Examples
   :ref:`year-param`

See Also
   :ref:`Derivative Year Parameters`

Time Interval
=============

Parameter Type Code
   ``12``

Description
   Specified as a long integer followed by a suffix indicating a time unit: ``ms`` for milliseconds, ``s`` for seconds, ``m`` for minutes, ``h`` for hours, ``d`` for days, ``w`` for weeks (7 days), ``y`` for years (365 days). If there is no suffix, the default interpretation is milliseconds. The time unit suffixes are case-insensitive.

.. COMMENT TODO pointer to Javadoc

Built-In Examples
   :ref:`New Content Crawl Interval`

String Range
============

Parameter Type Code
   ``7``

Description
   The range is specified with two strings separated by a dash (``-``) and is inclusive. If there is a single string with no dash, the range is interpreted to contain only that string.

.. COMMENT TODO comment about how this might not be what people expect

Built-In Examples
   :ref:`Issue Range`

Numeric Range
=============

Parameter Type Code
   ``8``

Description
   The range is specified with two integers separated by a dash (``-``). If there is a single integer, the range is interpreted to contain only that integer.

Built-In Examples
   :ref:`Numeric Issue Range`

Set
===

Parameter Type Code
   ``9``

Description
   Specified as a comma-separated list of strings, with whitespace surrounding strings ignored, and empty strings discarded.

   The string :samp:`\{{n},{m}\}`, where :samp:`{n}` and :samp:`{m}` are integers, will be replaced by all the integers in the range from :samp:`{n}` to :samp:`{m}` inclusive.  For instance, the set ``{2002-2005}, 2003Supp, 2004Supp`` is equivalent to ``2002, 2003, 2003Supp, 2004, 2004Supp, 2005``.

Built-In Examples
   :ref:`Issue Set`

Boolean
=======

Parameter Type Code
   ``5``

Description
   The canonical values are ``true`` or ``false``, although ``yes``, ``on`` and ``1`` are recognized as ``true``, and ``no``, ``off`` and ``0`` are recognized as ``false``. All these value strings are case-insensitive.

Built-In Examples
   :ref:`AU Down`, :ref:`AU Off-Limits`, :ref:`AU Closed`

--------------------------------
Built-In Definitional Parameters
--------------------------------

The LOCKSS software defines a number of built-in definitional parameters.

Definitional parameters give an AU its identity -- change the value for a definitional parameter and you will be describing a different slice of content (different year, different directory, etc.).

Base URL
========

Parameter Key
   ``base_url``

Parameter Type
   :ref:`URL`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>base_url</key>
              <type>3</type>
              <displayName>Base URL</displayName>
              <description>Usually of the form http://&lt;journal-name&gt;.com/</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Second Base URL
===============

Parameter Key
   ``base_url2``

Parameter Type
   :ref:`URL`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>base_url2</key>
              <type>3</type>
              <displayName>Second Base URL</displayName>
              <description>Use if AU spans two hosts</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

.. _year-param:

Year
====

Parameter Key
   ``year``

Parameter Type
   :ref:`year-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>year</key>
              <type>4</type>
              <displayName>Year</displayName>
              <description>Four digit year (e.g., 2004)</description>
              <size>4</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Volume Number
=============

Parameter key
   ``volume``

Parameter Type
   :ref:`Non-Negative Integer`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>volume</key>
              <type>6</type>
              <displayName>Volume No.</displayName>
              <description>Numeric volume number, e.g. 7</description>
              <size>8</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Volume Name
===========

Parameter Key
   ``volume_name``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>volume_name</key>
              <type>1</type>
              <displayName>Volume Name</displayName>
              <description>Volume name, e.g. 23A</description>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Issue Range
===========

Parameter Key
   ``issue_range``

Parameter Type
   :ref:`String Range`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>issue_range</key>
              <type>7</type>
              <displayName>Issue Range</displayName>
              <description>A Range of issues in the form: aaa-zzz</description>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Numeric Issue Range
===================

Parameter Key:
   ``num_issue_range``

Parameter Type
   :ref:`Numeric Range`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>num_issue_range</key>
              <displayName>Numeric Issue Range</displayName>
              <description>A Range of issues in the form: min-max</description>
              <type>8</type>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Issue Set
=========

Parameter Key
   ``issue_set``

Parameter Type
   :ref:`Set`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>issue_set</key>
              <type>9</type>
              <displayName>Issue Set</displayName>
              <description>A comma delimited list of issues. (eg issue1, issue2)</description>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Journal Directory
=================

Parameter Key
   ``journal_dir``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>journal_dir</key>
              <type>1</type>
              <displayName>Journal Directory</displayName>
              <description>Directory name for journal content (i.e. 'american_imago').</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Journal Abbreviation
====================

Parameter Key
   ``journal_abbr``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>journal_abbr</key>
              <type>1</type>
              <displayName>Journal Abbreviation</displayName>
              <description>Abbreviation for journal (often used as part of file names).</description>
              <size>10</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Journal Identifier
==================

Parameter Key
   ``journal_id``

Parameter type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>journal_id</key>
              <type>1</type>
              <displayName>Journal Identifier</displayName>
              <description>Identifier for journal (often used as part of file names).</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Journal ISSN
============

Parameter Key
   ``journal_issn``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>journal_issn</key>
              <type>1</type>
              <displayName>Journal ISSN</displayName>
              <description>International Standard Serial Number.</description>
              <size>20</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Publisher Name
==============

.. note::

   Use of this parameter is not recommended. It is unlikely the publisher name will appear in URLs, as opposed to a publisher abbreviation or code.

Parameter Key
   ``publisher_name``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>publisher_name</key>
              <type>1</type>
              <displayName>Publisher Name</displayName>
              <description>Publisher Name for Archival Unit</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

OAI Request URL
===============

Parameter Key
   ``oai_request_url``

Parameter Type
   :ref:`URL`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>oai_request_url</key>
              <type>3</type>
              <displayName>OAI Request URL</displayName>
              <description>Usually of the form http://&lt;journal-name&gt;.com/</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

OAI Spec
========

Parameter Key
   ``oai_spec``

Parameter Type
   :ref:`string-type`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>oai_spec</key>
              <type>1</type>
              <displayName>OAI Spec</displayName>
              <description>Spec for journal in the OAI crawl</description>
              <size>40</size>
              <definitional>true</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

------------------------------------
Built-In Non-Definitional Parameters
------------------------------------

The LOCKSS software also defines a number of non-definitional parameters.

Non-definitional parameters are necessary as placeholders in plugin rules and code, but they do not contribute to the AU's identity -- you may need to change the value of a non-definitional parameter but it will not change which slice of content the AU corresponds to.

Some non-definitional parameters might be listed in the plugin itself, like the ``user_pass`` parameter for user credentials, if all AUs are expected to supply a value for the parameter, but most others are involved in the lifecycle of an AU and need not be listed in the plugin, like the ``pub_down`` parameter for AUs that are not currently allowed to crawl.

Username and Password
=====================

Parameter Key
   ``user_pass``

Parameter Type
   :ref:`User Credentials`

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>user_pass</key>
              <type>10</type>
              <displayName>Username:Password</displayName>
              <description>Colon-separated username and password string, e.g. myuser:mypass</description>
              <size>30</size>
              <definitional>false</definitional>
              <defaultOnly>false</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   Some harvesting processes may require user credentials (username and password). A non-definitional parameter is needed because the username and password might be different for different harvesting nodes, or may change over time, without changing the identity of the AU (for instance its year).

AU Down
=======

Parameter Key
   ``pub_down``

Parameter Type
   :ref:`Boolean`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>pub_down</key>
              <type>5</type>
              <displayName>Pub Down</displayName>
              <description>If true, AU is no longer available from the publisher</description>
              <size>4</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used routinely in the title database files of LOCKSS networks, but does not need to appear explicitly in plugins.

   When this parameter value is supplied as ``true`` for an AU, the AU is considered to be "down", meaning that it is currently unavailable from its source and should not attempt to crawl or recrawl.

   The name ``pub_down``, for "publisher down", reflects the idea that the entire publisher site (content provider) might be unavailable, but this parameter can be used to mark individual AUs as being down outside the context of an entire content provider being unavailable.

AU Off-Limits
=============

Parameter Key
   ``pub_never``

Parameter Type
   :ref:`Boolean`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>pub_never</key>
              <type>5</type>
              <displayName>Pub Never</displayName>
              <description>If true, don't try to access any content from publisher</description>
              <size>4</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used routinely in the title database files of LOCKSS networks, but does not need to appear explicitly in plugins.

   When this parameter value is supplied as ``true`` for an AU, the AU is considered to be "off-limits", meaning that the LOCKSS software will not satisfy a proxy request for a URL it determines to be in this AU by going to the original Web site.

.. COMMENT TODO but does this also have the effect of pub_down in terms of crawls?

AU Closed
=========

Parameter Key
   ``au_closed``

Parameter Type
   :ref:`Boolean`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>au_closed</key>
              <type>5</type>
              <displayName>AU Closed</displayName>
              <description>If true, AU is complete, no more content will be added</description>
              <size>4</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used routinely in the title database files of LOCKSS networks, but does not need to appear explicitly in plugins.

   When this parameter value is supplied as ``true`` for an AU, the AU is marked as "closed", meaning it is considered that no more content will be added to it in the future.

.. COMMENT TODO does this have a concrete effect?

Crawl Proxy
===========

Parameter Key
   ``crawl_proxy``

Parameter Type
   :ref:`string-type`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>crawl_proxy</key>
              <type>1</type>
              <displayName>Crawl Proxy</displayName>
              <description>If set to host:port, crawls of this AU will be proxied. If set to DIRECT, crawls will not be proxied, even if the LOCKSS node has been configured with a default crawl proxy.</description>
              <size>40</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used routinely in the title database files of LOCKSS networks, but does not need to appear explicitly in plugins.

   When this parameter value is supplied as a host:port pair (for example ``proxy.myuniversity.edu:8080``) for an AU, crawls of the AU will be proxied through the given proxy. When this parameter value is supplied as the special value ``DIRECT`` for an AU, crawls of the AU will not be proxied, even if the LOCKSS node is configured to always use a crawl proxy.

New Content Crawl Interval
==========================

Parameter Key
   ``nc_interval``

Parameter Type
   :ref:`Time Interval`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>nc_interval</key>
              <type>12</type>
              <displayName>Crawl Interval</displayName>
              <description>The interval at which the AU should crawl the publisher site.</description>
              <size>10</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used routinely in the title database files of LOCKSS networks, but does not need to appear explicitly in plugins.

   When this parameter value is supplied as a time interval for an AU, crawls of the AU will be attempted with the given requested interval rather than the LOCKSS node's default new content crawl interval.

Crawl Test Substance Threshold
==============================

Parameter Key
   ``crawl_test_substance_threshold``

Parameter Type
   :ref:`string-type`

.. COMMENT defaultOnly

Canonical Form
   .. code-block:: xml

            <org.lockss.daemon.ConfigParamDescr>
              <key>crawl_test_substance_threshold</key>
              <type>1</type>
              <displayName>Crawl Test Substance Threshold</displayName>
              <description>Minimum number of substance URLs necessary for successful abbreviated crawl test.</description>
              <size>20</size>
              <definitional>false</definitional>
              <defaultOnly>true</defaultOnly>
            </org.lockss.daemon.ConfigParamDescr>

Description
   This non-definitional parameter is used in special circumstances, for networks set up to perform abbreviated test crawls.

---------------------
Derivative Parameters
---------------------

For parameters of type :ref:`URL` and :ref:`year-type`, the system automatically brings into existence **derivative parameters** with special names, as if those parameters had also been defined by the plugin.

.. tip::

   Derivative parameters have fallen out of favor. The contemporary way to achieve the same effect is through **parameter functors**.

Derivative URL Parameters
=========================

For any parameter of type :ref:`URL` with key :samp:`{urlkey}`, the following derivative parameters are automatically defined:

*  :samp:`{urlkey}_host` of type :ref:`string-type`, whose value is just the host portion of the corresponding URL value. For example, if ``base_url`` has a value of ``https://www.publisher.com/jabc/``, ``base_url_host`` has a value of ``www.publisher.com``.

*  :samp:`{urlkey}_path` of type :ref:`string-type`, whose value is just the path portion of the corresponding URL value. For example, if ``base_url`` has a value of ``https://www.publisher.com/jabc/``, ``base_url_path`` has a value of ``/jabc/``.

Derivative Year Parameters
==========================

For any parameter of type :ref:`year-type` with key :samp:`{yearkey}`, the following derivative parameter is automatically defined:

*  :samp:`au_short_{yearkey}` of type :ref:`integer-type`, whose value is the corresponding year value modulo 100. For example, if ``year`` has a value of ``1998``, ``au_short_year`` has a value of ``98``; if ``year`` has a value of ``2002``, ``au_short_year`` has a value of ``2`` (the integer ``2``, not the string ``02``.

   .. tip::

      In many cases, what is useful is the zero-padded, two-character string from the derivative short year, not the potentially single-digit integer; use ``%02d`` in the ``printf`` format string.
