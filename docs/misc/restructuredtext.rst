================================
reStructuredText Quick Reference
================================

A quick reference to reStructuredText syntax (and Sphynx extensions).

.. contents:: :local:

--------
Headings
--------

.. code-block:: rst

   =====
   Title
   =====

   -------------------
   First Level Heading
   -------------------

   Second Level Heading
   ====================

   Third Level Heading
   -------------------

   Fourth Level Heading
   ^^^^^^^^^^^^^^^^^^^^

   Fifth Level Heading
   ~~~~~~~~~~~~~~~~~~~

   Sixth Level Heading
   ___________________

-------------
Inline Markup
-------------

.. code-block:: rst

   *Italic (short)*

   :emphasis:`Italic (long)`

   **Bold (short)**

   :strong:`Bold (long)`

   ``Literal (short)``

   :literal:`Literal (long)`

   Superscript (short): E = m c :sup:`2`

   Superscript (long): E = m c :superscript:`2`

   Subscript (short): H :sub:`2` O

   Subscript (long): H :subscript:`2` O

-----
Links
-----

.. code-block:: rst

   Bare URL:

      Go to https://www.example.com/ for details.

   Link text and URL together:

      Click `here <https://www.example.com/>_ for details.

   Link text inline and URL elsewhere:

      Click `the link text`_ for details.

   and then elsewhere (e.g. bottom of the file):

      .. _the link text: https://www.example.com/

   Tagging a heading:

      .. _myreferencetag:

      Some Heading
      ------------

   and referencing it elsewhere:

      See :ref:`myreferencetag` for details. (Expands to the heading text, here "Some Heading")

-----
Lists
-----

With proper indentation (3 spaces), lists can be nested, and list items can have multiple paragraphs (separated by a blank line)..

.. code-block:: rst

   *  Bullet list

   *  Bullet markers can be:

      *  ``*``

      *  ``-``

      *  ``+``

   1. Numbered list

   2. Enumerators can be:

      1.  ``1, 2, 3...``

      2.  ``A, B, C...``

      3.  ``a, b, c...``

      4.  ``I, II, III...``

      5.  ``i, ii, iii...``

   3. Markers can be:

      1. Followed by a dot (``1.``)

      2. Followed by a parenthesis (``1)``)

      3. Surrounded by parentheses (``(1)``)

   definition list term 1
      Definition 1.

   definition list term 2
      Definition 2, paragraph 1.

      Definition 2, paragraph 2.

------
Asides
------

The following directives can have arbitrary bodies (indented with 3 spaces).

.. code-block:: rst

   Creates a box with an icon, colored background, and the implied heading (e.g. `Warning` for `.. warning::`):

   .. attention::
   .. caution::
   .. danger::
   .. error::
   .. hint::
   .. important::
   .. note::
   .. tip::
   .. warning::

   Two special versions:

   .. admonition:: My Custom Heading (on same line as directive)

   .. sidebar:: My Sidebar Title (box rendered off to the right in HTML)

---------------
Semantic Markup
---------------

.. note::

   The following roles are defined by Sphinx.

.. code-block:: rst

   File or directory: Edit :file:`/etc/passwd`

      Curly braces for placeholders: Found in :file:`/usr/lib/jvm/java-{n}-openjdk`

   GUI element (button, field name...): Click :guilabel:`OK`

      Ampersand before accelerator key: Click :guilabel:`&Cancel`

      Literal ampersand escaped by another ampersand

   Keystrokes: Hit :kbd:`Ctrl + C`

   Menu selection: Select :menuselection:`Edit --> Copy`

      Supports ampersands for accelerator keys like `guilabel`

   OS command: Use :command:`grep`

   Executable program: Run :program:`config.sh`

   Sample user entry: Enter your name, for example :samp:`Darth Vader`

      Curly braces for placeholders: Add :samp:`allow {port} from {ipaddress}`

      Literal curly brace escaped by a backslash

   HTTP header: The :mailheader:`User-Agent` header

   Content type: File of type :mimetype:`application/pdf`

   Regular expression: By default :regexp:`^ab*c$`

   Abbreviation and expansion: :abbr:`FTP (File Transfer Protocol)`

   Defining occurrence of a term: We call this a :dfn:`plugin`

--------
Verbatim
--------

ReStructuredText defines ``.. code::`` but **Sphinx** offers the much more featureful ``.. code-block::`` and ``.. literalinclude::``. The body is indented by 3 spaces. The language keywords are those understood by `Pygments <https://pygments.org/docs/lexers/>`_. There are options for adding a title and line numbers, highlighting certain lines, de-indenting the body, and more (see `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_). The ``literalinclude::`` directive's same-line argument is an external file instead (the language code goes in a ``:language:`` option instead), and it also has options for only transcluding lines before or after certain criteria, for doing a :command:`diff` with a second file, and more (see `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_).

Basic example:

.. code-block:: rst

   .. code-block:: java

      public static void main(String[] args) {
        System.out.println("Hello world!");
      }

------
Images
------

.. code-block:: rst

   .. image:: /images/test-image.png
      :alt: HTML alt text
      :width: 100px

   .. figure:: /images/test-image.png
      :alt: HTML alt text

      This is the caption.

      This is the legend, paragraph 1.

      This is the legend, paragraph 2.
