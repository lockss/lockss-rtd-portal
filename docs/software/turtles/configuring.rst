===================
Configuring Turtles
===================

.. include:: subst.rst

|TURTLES| is configured via :term:`YAML configuration object`\s.

Operations that are :term:`building a plugin` (:ref:`turtles build-plugin` and :ref:`turtles release-plugin`) need to know about:

*  One or more :term:`plugin set`\s, specified by :term:`plugin set catalog definition`\s and/or :term:`plugin set definition`\s. See :ref:`Configuring a Plugin Set`.

*  :term:`Plugin signing credentials`, specified by a :term:`plugin signing credentials definition`. See :ref:`Configuring Plugin Signing Credentials`.

Operations that are :term:`deploying a plugin` (:ref:`turtles deploy-plugin` and :ref:`turtles release-plugin`) need to know about one or more :term:`plugin registries <plugin registry>`, specified by a :term:`plugin signing credentials definition`.

------------------------
Configuring a Plugin Set
------------------------

|TURTLES| recognizes two :term:`plugin set builder`\s:

*  The **Maven plugin set builder**, where the plugin set is built with `Maven <https://maven.apache.org/>`_ using the parent POM `org.lockss:lockss-plugins-parent-pom <https://central.sonatype.com/artifact/org.lockss/lockss-plugins-parent-pom>`_).

*  The **legacy Ant plugin set builder**, where  the plugin set is built with `Ant <https://ant.apache.org/>`_ using the LOCKSS Program's legacy build process from the LOCKSS 1.x system).

   .. note::

      The legacy Ant plugin set builder is deprecated; new plugin sets should use the Maven plugin set builder.

A :term:`plugin set definition` is usually found at the root of the plugin set code tree (the directory that contains :file:`pom.xml` in a Maven plugin set, or :file:`build.xml` in a legacy Ant plugin set) in a file called :file:`turtles.yaml`. Most plugin sets use the Maven plugin set builder and the corresponding code project follows normal Maven conventions; in this most typical case, the plugin set definition would look like this:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: maven

More generally, a plugin set definition looks like the following:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: <buildertype>
     <...additional builder configuration...>

The object is defined as follows:

``kind``
   :Type: string
   :Required: yes

   The constant ``PluginSet``, indicating a :term:`plugin set definition`.

``id``
   :Type: string
   :Required: yes
   :Example: ``my-plugin-set``

   An identifier for the plugin set (meant for machine consumption). Typically a short abbreviation featuring lowercase letters and digits, possibly separated by hyphens and underscores, but no spaces or other punctuation.

``name``
   :Type: string
   :Required: yes
   :Example: ``My Plugin Set``

   A display name for the plugin set (meant for human consumption).

``builder``
   :Type: :ref:`plugin set builder specification`
   :Required: yes

   A :ref:`plugin set builder specification` for the plugin set (see below).

Plugin Set Builder Specification
================================

Because there are two types of plugin set builders, there are two types of plugin set builder specifications, the :ref:`Maven plugin set builder specification` and the :ref:`legacy Ant plugin set builder specification`. Both look similar:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: <buildertype>  # 'maven' or 'ant'
     main: <mainpath>     # optional
     test: <testpath>     # optional

The object is defined as follows:

``type``
   :Type: string
   :Required: yes

   The type a plugin set builder used for the plugin set. Must be one of:

   * ``maven`` for a :ref:`Maven Plugin Set Builder Specification`

   *  ``ant`` for a :ref:`Legacy Ant Plugin Set Builder Specification`

``main``
   :Type: string
   :Required: no

   The path to the plugins' source code, relative to the root of the project. This property is optional; each plugin set builder has a sensible default.

``test``
   :Type: string
   :Required: no

   The path to the plugins' unit tests, relative to the root of the project. This property is optional; each plugin set builder has a sensible default.

Maven Plugin Set Builder Specification
======================================

In a :ref:`plugin set builder specification` for the Maven plugin set builder:

*  ``type`` must be ``maven``

*  ``main`` defaults to ``src/main/java``, which is typical for a well-structured Maven project.

*  ``test`` defaults to ``src/test/java``, which is typical for a well-structured Maven project.

A plugin set with a Maven plugin set builder specification would look like this:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: maven
     main: src/main/custom  # if not the default src/main/java
     test: src/test/weird   # if not the default src/test/java

Legacy Ant Plugin Set Builder Specification
===========================================

In a :ref:`plugin set builder specification` for the legacy Ant plugin set builder:

*  ``type`` must be ``ant``

*  ``main`` defaults to ``plugins/src``, which is typical for this legacy build process.

*  ``test`` defaults to ``plugins/test/src``, which is typical for this legacy build process.

A plugin set with a legacy Ant plugin set builder specification would look like this:


.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: ant
     main: custom/src  # if not the default plugins/src
     test: weird/src   # if not the default plugins/test/src

--------------------------------
Configuring a Plugin Set Catalog
--------------------------------

