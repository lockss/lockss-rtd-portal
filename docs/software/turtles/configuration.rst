===============================
Turtles Configuration Reference
===============================

.. include:: subst.rst

-------------------------------
Plugin Set Definition Reference
-------------------------------

A :term:`plugin set definition` looks like the following:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: <<plugin set identifier>>
   name: <<plugin set display name>>
   builder:
     type: <<buildertype>>
     <<...type-specific plugin set builder configuration...>>

The object is defined as follows:

``kind``
   :Type: string
   :Required: yes

   The constant ``PluginSet``, indicating a :term:`plugin set definition`.

``id``
   :Type: string
   :Required: yes

   An identifier for the plugin set [#fn-turtles-identifier]_. Example: ``our-plugin-set``.

``name``
   :Type: string
   :Required: yes

   A display name for the plugin set. Example: ``Our Plugin Set``.

``builder``
   :Type: :ref:`plugin set builder specification` object
   :Required: yes

   A :ref:`plugin set builder specification` for the plugin set (see below).

Plugin Set Builder Specification
================================

Because there are two types of :term:`plugin set builder`\s, the **Maven plugin set builder** and the deprecated **legacy Ant plugin set builder**, there are two types of plugin set builder specifications, identified by their ``type`` property:

.. list-table::
   :header-rows: 1

   *  *  ``type``
      *  Name
   *  *  ``maven``
      *  :ref:`Maven Plugin Set Builder Specification`
   *  *  ``ant``
      *  :ref:`Legacy Ant Plugin Set Builder Specification` (deprecated)

Maven Plugin Set Builder Specification
--------------------------------------

.. admonition:: Prerequisites

   This plugin set builder requires:

   *  `Java <https://www.oracle.com/java/>`_ Development Kit (JDK) 17

   *  `Apache Maven <https://maven.apache.org/>`_

A Maven plugin set builder specification looks like the following:

.. code-block:: yaml

   type: maven
   main: src/main/java  # optional
   test: src/test/java  # optional

The object is defined as follows:

``type``
   :Type: string
   :Required: yes

   The constant ``maven``, indicating a Maven plugin set builder specification. Designates a plugin set that is built using `Maven <https://maven.apache.org/>`_ with the parent POM `org.lockss:lockss-plugins-parent-pom <https://central.sonatype.com/artifact/org.lockss/lockss-plugins-parent-pom>`_.

``main``
   :Type: string
   :Required: no
   :Default: ``src/main/java``

   The path to the plugins' source code, relative to the root of the project (``src/main/java`` by default).

``test``
   :Type: string
   :Required: no
   :Default: ``src/test/java``

   The path to the plugins' unit tests, relative to the root of the project (``src/test/java`` by default).

Legacy Ant Plugin Set Builder Specification
-------------------------------------------

.. warning::

   This plugin set builder is deprecated.

.. admonition:: Prerequisites

   This plugin set builder requires:

   *  `Java <https://www.oracle.com/java/>`_ Development Kit (JDK) 8

   *  `Apache Ant <https://ant.apache.org/>`_

A legacy Ant plugin set builder specification looks like the following:

.. code-block:: yaml

   type: ant
   main: plugins/src       # optional
   test: plugins/test/src  # optional

The object is defined as follows:

``type``
   :Type: string
   :Required: yes

   The constant ``ant``, indicating a legacy Ant plugin set builder specification. Designates a plugin set that is built using `Ant <https://ant.apache.org/>`_ with the LOCKSS Program's legacy Ant build (from the LOCKSS 1.x system).

``main``
   :Type: string
   :Required: no
   :Default: ``plugins/src``

   The path to the plugins' source code, relative to the root of the project (``plugins/src`` by default).

``test``
   :Type: string
   :Required: no
   :Default: ``plugins/test/src``

   The path to the plugins' unit tests, relative to the root of the project (``plugins/test/src`` by default).

---------------------------------------
Plugin Set Catalog Definition Reference
---------------------------------------

A :term:`plugin set catalog definition` looks like the following:

.. code-block:: yaml

   ---
   kind: PluginSetCatalog
   plugin-set-files:
     - <<plugin set file path 1>>
     - <<plugin set file path 2>>
     - ...

The object is defined as follows:

``kind``
   :Type: string
   :Required: yes

   The constant ``PluginSetCatalog``, indicating a :term:`plugin set catalog definition`.

``plugin-set-files``
   :Type: list of strings
   :Required: yes

   A non-empty list of :term:`plugin set definition` file paths.

------------------------------------
Plugin Registry Definition Reference
------------------------------------

A :term:`plugin registry definition` looks like the following:

.. code-block:: yaml

   ---
   kind: PluginRegistry
   id: <<plugin registry identifier>>
   name: <<plugin registry display name>>
   layout:
     type: <<plugin registry layout type>>
     <<...type-specific plugin registry layout configuration...>>
   layers:
     - id: <<plugin registry layer identifier>>
       name: <<plugin registry layer display name>>
       path: <<plugin registry layer directory path>>
     -  <<...other plugin registry layers...>>
   plugin-identifiers:
     - org.ourproject.plugin.plugin1.Plugin1
     - org.ourproject.plugin.plugin2.Plugin2
     - <<...other plugin identifiers...>>
   suppressed-plugin-identifiers:
     - org.ourproject.plugin.plugin8.Plugin8
     - org.ourproject.plugin.plugin9.Plugin9
     - <<...other plugin identifiers...>>

The object is defined as follows:

``kind``
   :Type: string
   :Required: yes

   The constant ``PluginRegistry``, indicating a :term:`plugin registry definition`.

``id``
   :Type: string
   :Required: yes

   An identifier for the plugin registry [#fn-turtles-identifier]_. Example: ``our-plugin-registry``.

``name``
   :Type: string
   :Required: yes

   A display name for the plugin registry. Example: ``Our Plugin Registry``.

``layout``
   :Type: :ref:`Plugin Registry Layout Specification` object
   :Required: yes

   A :ref:`Plugin Registry Layout Specification` for this plugin registry.

``layers``
   :Type: list of :ref:`Plugin Registry Layer Specification` objects
   :Required: yes

   A non-empty list of :ref:`Plugin Registry Layer Specification`\s.

``plugin-identifiers``
   :Type: list of strings
   :Required: yes

   A non-empty list of plugin identifiers in this plugin registry.

``suppressed-plugin-identifiers``
   :Type: list of strings
   :Required: no

   A list of plugin identifiers that have been retired from this plugin registry. |TURTLES| does not currently do anything actionable with this information, but it can be useful for plugin registry maintainers to document.

Plugin Registry Layout Specification
====================================

|TURTLES| supports two kinds of plugin registry layouts, identified by their ``type`` property:

.. list-table::
   :header-rows: 1

   *  *  ``type``
      *  Name
   *  *  ``directory``
      *  :ref:`Directory Plugin Registry Layout Specification`
   *  *  ``rcs``
      *  :ref:`RCS Plugin Registry Layout Specification`

Directory Plugin Registry Layout Specification
----------------------------------------------

In a **directory plugin registry layout**, the plugin JAR files of each :term:`layer <plugin registry layer>` simply go together in a flat directory structure, for instance:

.. code-block:: text

   /var/www/props.ourproject.org/plugins/
   +-- testing/
   |   +-- org.ourproject.plugin.plugin1.Plugin1.jar
   |   +-- org.ourproject.plugin.plugin2.Plugin2.jar
   |   +-- ...
   +-- production/
       +-- org.ourproject.plugin.plugin1.Plugin1.jar
       +-- org.ourproject.plugin.plugin2.Plugin2.jar
       +-- ...

A directory plugin registry layout specification looks like this:

.. code-block:: yaml

   type: directory
   file-naming-convention: identifier  # optional

The object is defined as follows:

``type``
   :Type: string
   :Required: yes

   The constant ``directory``, indicating a directory plugin registry layout.

``file-naming-convention``
   :Type: string
   :Required: no

   A file naming convention for the JAR files. The three available file naming conventions and their effect on the example plugin identifier ``org.ourproject.plugin.plugin1.Plugin1`` are:

   .. list-table::
      :header-rows: 1

      *  *  ``file-naming-convention``
         *  Effect
      *  *  ``abbreviated``
         *  ``Plugin1.jar``
      *  *  ``identifier`` (default)
         *  ``org.ourproject.plugin.plugin1.Plugin1.jar``
      *  *  ``underscore``
         *  ``org_ourproject_plugin_plugin1_Plugin1.jar``

RCS Plugin Registry Layout Specification
----------------------------------------

.. admonition:: Prerequisites

   This plugin registry layout requires:

   *  `GNU RCS <https://www.gnu.org/software/rcs/>`_

In an RCS plugin registry layout specification, the plugin JAR files of each :term:`layer <plugin registry layer>` go together in a flat directory structure, just like in a :ref:`directory plugin registry layout <Directory Plugin Registry Layout Specification>`, but additionally, each layer has an :file:`RCS` subdirectory and `RCS <https://www.gnu.org/software/rcs/>`_ is used to save a record of successive plugin versions. The resulting file structure would look like the following:

.. code-block:: text

   /var/www/props.ourproject.org/plugins/
   +-- testing/
   |   +-- RCS/
   |   |   +-- org.ourproject.plugin.plugin1.Plugin1.jar,v
   |   |   +-- org.ourproject.plugin.plugin2.Plugin2.jar,v
   |   |   +-- ...
   |   +-- org.ourproject.plugin.plugin1.Plugin1.jar
   |   +-- org.ourproject.plugin.plugin2.Plugin2.jar
   |   +-- ...
   +-- production/
       +-- RCS/
       |   +-- org.ourproject.plugin.plugin1.Plugin1.jar,v
       |   +-- org.ourproject.plugin.plugin2.Plugin2.jar,v
       |   +-- ...
       +-- org.ourproject.plugin.plugin1.Plugin1.jar
       +-- org.ourproject.plugin.plugin2.Plugin2.jar
       +-- ...

An RCS plugin registry layout specification looks like this:

.. code-block:: yaml

   type: rcs
   file-naming-convention: identifier  # optional

The object is defined as follows:

``type``
   :Type: string
   :Required: yes

   The constant ``rcs``, indicating an RCS plugin registry layout.

``file-naming-convention``
   :Type: string
   :Required: no

   A file naming convention for the JAR files. The three available file naming conventions and their effect on the example plugin identifier ``org.ourproject.plugin.plugin1.Plugin1`` are:

   .. list-table::
      :header-rows: 1

      *  *  ``file-naming-convention``
         *  Effect
      *  *  ``abbreviated``
         *  ``Plugin1.jar``
      *  *  ``identifier`` (default)
         *  ``org.ourproject.plugin.plugin1.Plugin1.jar``
      *  *  ``underscore``
         *  ``org_ourproject_plugin_plugin1_Plugin1.jar``

Plugin Registry Layer Specification
===================================

A :term:`plugin registry layer` specification requires an identifier, display name, and directory path, and looks like this:

.. code-block:: yaml

   id: <<identifier>>
   name: <<display name>>
   path: <<directory path>>

The object is defined as follows:

``id``
   :Type: string
   :Required: yes

   An identifier for the layer [#fn-turtles-identifier]_. Examples: ``production``, ``testing``.

``name``
   :Type: string
   :Required: yes

   A display name for the layer. Example: ``Our Project Plugin Registry (Production)``.

``path``
   :Type: string
   :Required: yes

   The layer's directory path. If the path is relative, it is understood to be relative to the :term:`plugin registry definition` file that contains it. Example: ``/var/www/props/props.ourproject.org/plugins/production`` (absolute), ``production`` (relative).

--------------------------------------------
Plugin Registry Catalog Definition Reference
--------------------------------------------



-----------------------------------------------
Plugin Signing Credentials Definition Reference
-----------------------------------------------

A :term:`plugin signing credentials definition` looks like the following:

.. code-block:: yaml

   ---
   kind: PluginSigningCredentials
   plugin-signing-keystore: <<plugin signing keystore path>>
   plugin-signing-alias: <<plugin signing keystore alias>>

The object is defined as follows:

``kind``
   :Type: string
   :Required: yes

   The constant ``PluginSigningCredentials``, indicating :term:`plugin signing credentials`.

``plugin-signing-keystore``
   :Type: string
   :Required: yes

   File path for a plugin signing keystore. If the path is relative, it is understood to be relative to the :term:`plugin signing credentials definition` file that contains it. Example: ``/home/user123/secrets/user123.keystore`` (absolute), ``secrets/user123.keystore`` (relative).

``plugin-signing-alias``
   :Type: string
   :Required: yes

   User alias within the plugin signing keystore. Example: ``user123``.

----

.. rubric:: Footnotes

.. [#fn-turtles-identifier]

   Although |TURTLES| does not enforce a particular syntax, the intended shape of these identifiers is that they are made of lowercase letters and digits, optionally separated by hyphens or underscores, excluding spaces and other characters/punctuation. |TURTLES| may specify the exact syntax of identifiers in a future version.
