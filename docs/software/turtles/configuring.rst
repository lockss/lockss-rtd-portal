===================
Configuring Turtles
===================

.. include:: subst.rst

|TURTLES| is configured via |YAML| files containing |YAML configuration objects|. This chapter introduces each of these |YAML configuration objects|, and the chapter :doc:`configuration` offers a complete reference of their syntax.

*  :ref:`Turtles Plugin Building Operations` need to know about:

   *  One or more |plugin sets|, specified by |plugin set definitions| (see :ref:`Configuring a Plugin Set`) and/or |plugin set catalog definitions| (see  and :ref:`Configuring a Plugin Set Catalog`), or, if neither are specified, by a :ref:`Default Plugin Set Catalog File`.

   *  |plugin signing credentials|, specified by a |plugin signing credentials definition| (see :ref:`Configuring Plugin Signing Credentials`), or, if not specified, by a :ref:`Default Plugin Signing Credentials File`.

*  :ref:`Turtles Plugin Deployment Operations` need to know about one or more |plugin registries|, specified by |plugin registry definitions| (see :ref:`Configuring a Plugin Registry`) and/or |plugin registry catalogs| (see :ref:`Configuring a Plugin Registry Catalog`), or, if neither are specified, by a :ref:`Default Plugin Registry Catalog File`.

------------------------
Configuring a Plugin Set
------------------------

.. tip::

   For detailed information about plugin set definitions, see :ref:`Plugin Set Definition Reference`.

Most |plugin set| code projects are `Maven <https://maven.apache.org/>`_ projects that use the parent POM `org.lockss:lockss-plugins-parent-pom <https://central.sonatype.com/artifact/org.lockss/lockss-plugins-parent-pom>`_. In this typical scenario, the |plugin set definition| looks like this:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: maven

This requires a display name (``name``), and an identifier [#fn-turtles-identifier]_ (``id``).

Conventionally, this definition is stored in a file named :file:`turtles.yaml` (or :file:`turtles.yml`, or alternatively a ``.yaml`` or ``.yml`` file named after the plugin set's ``id``) in the project's top-level directory, that is, in the directory containing the project's :file:`pom.xml` file:

.. code-block:: text

   |
   +-- src/
   |   +-- main/
   |   |   +-- java/
   |   |       +-- ...
   |   +-- test/
   |   |   +-- java/
   |   |       +-- ...
   +-- pom.xml
   +-- turtles.yaml

.. dropdown:: Legacy Ant projects (deprecated)

   .. warning::

      This plugin set type is deprecated.

   Some LOCKSS plugin code project are `Ant <https://ant.apache.org/>`_ projects that use the LOCKSS Program's legacy Ant build (from the LOCKSS 1.x system). In this legacy situation, the |plugin set definition| looks like this:

   .. code-block:: yaml

      ---
      kind: PluginSet
      id: my-plugin-set
      name: My Plugin Set
      builder:
        type: ant

   This requires a display name (``name``), and an identifier [#fn-turtles-identifier]_ (``id``).

   This definition is stored in a file named :file:`turtles.yaml` in the project's top-level directory, that is, in the directory containing the project's :file:`build.xml` file:

   .. code-block:: text

      |
      +-- plugins/
      |   +-- src/
      |   |   +-- ...
      |   +-- test/
      |   |   +-- src/
      |   |       +-- ...
      +-- build.xml
      +-- turtles.yaml

--------------------------------
Configuring a Plugin Set Catalog
--------------------------------

.. tip::

   For detailed information about plugin set catalog definitions, see :ref:`Plugin Set Catalog Definition Reference`.

If you are working with multiple |plugin sets|, and even if you are working with just one, it is convenient to list one or more plugin sets in a |plugin set catalog|. Furthermore, to avoid specifying a plugin set catalog each time you invoke one of the :ref:`Turtles Plugin Building Operations`, you can save this |plugin set catalog definition| in a :ref:`Default Plugin Set Catalog File` which is loaded by default when no plugin sets and/or plugin set catalogs are specified.

A |plugin set catalog definition| looks like this:

.. code-block:: yaml

   ---
   kind: PluginSetCatalog
   plugin-set-files:
     - /opt/plugins/our-plugin-project/turtles.yaml
     - /opt/plugins/secondary-plugin-project/turtles.yaml
     - ...

Relative plugin set file paths are understood to be relative to the |plugin set catalog definition| file.

-----------------------------
Configuring a Plugin Registry
-----------------------------

.. tip::

   For detailed information about plugin registry definitions, see :ref:`Plugin Registry Definition Reference`.

The simplest kind of |plugin registry| has a single :term:`layer <plugin registry layer>`, conventionally named ``production``, and is a directory of plugin JAR files, each a ``.jar`` file named after the plugin's identifier (``plugin_identifier`` in the plugin definition XML). The |plugin registry definition| in this scenario would look like this:

.. code-block:: yaml

   ---
   kind: PluginRegistry
   id: our-project-plugin-registry
   name: Our Project Plugin Registry
   layout:
     type: directory
   layers:
     - id: production
       name: Our Project Plugin Registry Plugin Registry (Production)
       path: /var/www/props.ourproject.org/plugins/production
   plugin-identifiers:
     - org.ourproject.plugin.plugin1.Plugin1
     - org.ourproject.plugin.plugin2.Plugin2
     - ...

Plugin registries with two :term:`layers <plugin registry layer>` are also common, conventionally one called ``testing`` and the second ``production``:

.. code-block:: yaml

   ---
   kind: PluginRegistry
   id: our-project-plugin-registry
   name: Our Project Plugin Registry
   layout:
     type: directory
   layers:
     - id: testing
       name: Our Project Plugin Registry Plugin Registry (Testing)
       path: /var/www/props.ourproject.org/plugins/testing
     - id: production
       name: Our Project Plugin Registry Plugin Registry (Production)
       path: /var/www/props.ourproject.org/plugins/production
   plugin-identifiers:
     - org.ourproject.plugin.plugin1.Plugin1
     - org.ourproject.plugin.plugin2.Plugin2
     - ...

Relative plugin registry layer directory paths are understood to be relative to the |plugin registry definition| file. Using the two-layer example above, this means that another way to express the same plugin registry definition would be to store it in the file :file:`/var/www/props.ourproject.org/plugins/turtles.yaml` and write its ``layers`` section as:

.. code-block:: yaml

   layers:
     - id: testing
       name: Our Project Plugin Registry Plugin Registry (Testing)
       path: testing
     - id: production
       name: Our Project Plugin Registry Plugin Registry (Production)
       path: production

-------------------------------------
Configuring a Plugin Registry Catalog
-------------------------------------

.. tip::

   For detailed information about plugin registry catalog definitions, see :ref:`Plugin Registry Catalog Definition Reference`.

If you are working with multiple |plugin registries|, and even if you are working with just one, it is convenient to list one or more plugin registries in a |plugin registry catalog|. Furthermore, to avoid specifying a plugin registry catalog each time you invoke one of the :ref:`Turtles Plugin Deployment Operations`, you can save this |plugin registry catalog definition| in a :ref:`Default Plugin Registry Catalog File` which is loaded by default when no plugin registries and/or plugin registry catalogs are specified.

A |plugin registry catalog definition| looks like this:

.. code-block:: yaml

   ---
   kind: PluginRegistryCatalog
   plugin-registry-files:
     - /var/www/props.ourproject.org/plugins/turtles.yaml
     - /var/www/props.otherproject.net/plugins/turtles.yaml
     - ...

Relative plugin registry file paths are understood to be relative to the |plugin registry catalog definition| file.

.. FIXME where to store the definition

--------------------------------------
Configuring Plugin Signing Credentials
--------------------------------------

.. tip::

   For detailed information about plugin signing credential definitions, see :ref:`Plugin Signing Credentials Definition Reference`.

Each user who might sign plugins requires |plugin signing credentials|. A |plugin signing credentials definition| looks like this:

.. code-block:: yaml

   ---
   kind: PluginSigningCredentials
   plugin-signing-keystore: /home/user123/secrets/user123.keystore
   plugin-signing-alias: user123

This requires a path to a plugin signing keystore (``plugin-signing-keystore``) and the alias of the user within the keystore (``plugin-signing-alias``). A relative plugin signing keystore path is understood to be relative to the |plugin signing credentials definition| file.

----

.. rubric:: Footnotes

.. [#fn-turtles-identifier]

   Although |TURTLES| does not enforce a particular syntax, the intended shape of these identifiers is that they are made of lowercase letters and digits, optionally separated by hyphens or underscores, excluding spaces and other characters/punctuation. |TURTLES| may specify the exact syntax of identifiers in a future version.
