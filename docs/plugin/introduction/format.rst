====================
LOCKSS Plugin Format
====================

A LOCKSS plugin is expressed as a mapping from keys to values. Except for rare exceptions that are built into the LOCKSS software, LOCKSS plugins consist of an **XML file** containing these key-value pairs, accompanied by optional **Java class files** (compiled Java code), bundled together in a **JAR file** (a Zip file of Java class files and associated metadata).

The XML format of the plugin is a single ``<map>`` element, containing any number of **map entries** expressed as ``<entry>`` elements. Each map entry is a key-value pair, namely a **plugin key** which must be the first child of the ``<entry>`` element and must be of type :ref:`string-value`, and a **plugin value** which must be the second child of the ``<entry>`` element. See the :numref:`Plugin Value Types` section for more about possible plugin values.

The order of the key-value pairs does not matter, but the effect of specifying the same key in more than one map entry is undefined.

Example:

.. code-block:: xml

   <map>

     <!-- plugin key with string value -->
     <entry>
       <string>key_one</string>
       <string>Lots Of Copies Keep Stuff Safe</string>
     </entry>

     <!-- plugin key with integer value -->
     <entry>
       <string>key_two</string>
       <int>3000</int>
     </entry>

     <!-- plugin key with long integer value (e.g. number of milliseconds) -->
     <entry>
       <string>key_three</string>
       <long>1209600000</long>
     </entry>

     <!-- plugin key with list value (e.g. list of strings) -->
     <entry>
       <string>key_four</string>
       <list>
         <string>List item one</string>
         <string>List item two</string>
         <string>List item three</string>
       </list>
     </entry>

     <!-- plugin key with map value (e.g. mapping from string to string) -->
     <entry>
       <string>key_five</string>
       <map>
         <entry>
           <string>subkey1</string>
           <string>subvalue1</string>
         </entry>
         <entry>
           <string>subkey2</string>
           <string>subvalue2</string>
         </entry>
         <entry>
           <string>subkey3</string>
           <string>subvalue3</string>
         </entry>
       </map>
     </entry>

   </map>

------------------
Plugin Value Types
------------------

Plugin values can be of the following types:

============= =================
XML Element   Plugin Value Type
============= =================
``<string>``  :ref:`string-value`
``<int>``     :ref:`integer-value`
``<long>``    :ref:`long-value`
``<list>``    :ref:`List`
``<map>``     :ref:`Map`
============= =================

.. _string-value:

String
======

XML Element
   ``<string>``

Description
   An arbitrary string of characters.

   Because the plugin is expressed as XML, some characters in the string must be properly encoded:

   *  ``&`` is encoded as ``&amp;``.

   *  ``<`` is encoded as ``&lt;``.

   *  ``>`` is encoded as ``&gt;``.

   *  Non-printable characters and characters outside the 7-bit ASCII set are encoded with numeric character references [#fnxmlncr]_, either decimal character references (for example ``é`` encoded as ``&#0233;`` or ``&#233;``) or hexadecimal character references (for example ``é`` encoded as ``&#x00e9;`` or ``&#x00E9;`` or ``&#xe9;`` or ``&#xE9;``).

Examples
   .. code-block:: xml

          <string>This is a string value</string>

          <string>Taylor &amp; Francis</string>

          <string>Vive la diff&#x00e9;rence !</string>

.. _integer-value:

Integer
=======

XML Element
   ``<int>``

Description
   An integer value. Represented internally as a 32-bit integer.

Example
   .. code-block:: xml

          <int>1234</int>

.. _long-value:

Long Integer
============

XML Element
   ``<long>``

Description
   A long integer value. Represented internally as a 64-bit integer.

Example
   .. code-block:: xml

          <long>5000000000</long>

List
====

XML Element
   ``<list>``

Description
   A ``<list>`` elements containing an ordered sequence of values (typically all of the same type).

Example
   .. code-block:: xml

          <!-- list of strings -->
          <list>
            <string>Item one</string>
            <string>Item two</string>
            <string>Item three</string>
          </list>

Map
===

XML Element
   ``<map>``

Description
   A ``<map>`` element containing an unordered sequence of map entries expressed as ``<entry>`` elements. Each map entry is a key-value pair; the key must be the first child of the ``<entry>`` element and must be a :ref:`string-value`, and the value must be the second child of the ``<entry>`` element.

   The effect of specifying the same key in more than one map entry is undefined.

Example
   .. code-block:: xml

          <!-- mapping from string to string -->
          <map>
            <entry>
              <string>key1</string>
              <string>value1</string>
            </entry>
            <entry>
              <string>key2</string>
              <string>value2</string>
            </entry>
            <entry>
              <string>key3</string>
              <string>value3</string>
            </entry>
          </map>
        </entry>

----

.. rubric:: Footnotes

.. [#fnxmlncr]

   See also:

   *  https://www.w3.org/TR/2006/REC-xml11-20060816/#dt-charref

   *  https://www.w3.org/TR/2008/REC-xml-20081126/#dt-charref

   *  https://en.wikipedia.org/wiki/Numeric_character_reference
