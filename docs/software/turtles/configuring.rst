===================
Configuring Turtles
===================

.. include:: subst.rst

|TURTLES| is configured via YAML files containing :term:`YAML configuration object`\s.

Operations that are :term:`building a plugin` (:ref:`turtles build-plugin` and :ref:`turtles release-plugin`) need to know about:

*  One or more :term:`plugin set`\s, specified by :term:`plugin set definition`\s (see :ref:`Configuring a Plugin Set`) and/or :term:`plugin set catalog definition`\s (see  and :ref:`Configuring a Plugin Set Catalog`).

*  :term:`Plugin signing credentials`, specified by a :term:`plugin signing credentials definition` (see :ref:`Configuring Plugin Signing Credentials`).

Operations that are :term:`deploying a plugin` (:ref:`turtles deploy-plugin` and :ref:`turtles release-plugin`) need to know about one or more :term:`plugin registries <plugin registry>`, specified by a :term:`plugin registry definition`\s (see :ref:`Configuring a Plugin Registry`) and/or :term:`plugin registry catalog`\s (see :ref:`Configuring a Plugin Registry Catalog`).

------------------------
Configuring a Plugin Set
------------------------

The majority of :term:`plugin set` code projects are arranged as `Maven <https://maven.apache.org/>`_ projects using the parent POM `org.lockss:lockss-plugins-parent-pom <https://central.sonatype.com/artifact/org.lockss/lockss-plugins-parent-pom>`_. In this typical scenario, the :term:`plugin set definition` is in a top-level file (meaning in the same directory as the project's :file:`pom.xml` file), conventionally named :file:`turtles.yaml` (or a ``.yaml`` file named after the plugin set's ``id``), which looks like this:

.. code-block:: yaml

   ---
   kind: PluginSet
   id: my-plugin-set
   name: My Plugin Set
   builder:
     type: maven

This requires a display name (``name``), and an identifier [#fn-turtles-identifier]_ (``id``).

.. dropdown:: Legacy Ant projects (deprecated)

   Another available type of LOCKSS plugin code project is one arranged as an `Ant <https://ant.apache.org/>`_ project using the LOCKSS Program's legacy Ant build (from the LOCKSS 1.x system). **The LOCKSS Program's legacy Ant build is deprecated.** If in use in legacy projects, similarly to Maven, the plugin set definition for it is in a top-level file (meaning in the same directory as the project's :file:`build.xml` file), conventionally named :file:`turtles.yaml`, which looks like this:

   .. code-block:: yaml

      ---
      kind: PluginSet
      id: my-plugin-set
      name: My Plugin Set
      builder:
        type: ant

   This, too, requires a display name (``name``), and an identifier [#fn-turtles-identifier]_ (``id``).

For detailed information about plugin set definitions, see :ref:`Plugin Set Definition Reference`.

--------------------------------
Configuring a Plugin Set Catalog
--------------------------------

If you are working with multiple :term:`plugin set`\s, and even if you are working with just one, it is convenient to list one or more plugin sets in a :term:`plugin set catalog`. A :ref:`plugin set catalog definition` looks like this:

.. code-block:: yaml

   ---
   kind: PluginSetCatalog
   plugin-set-files:
     - /opt/plugins/our-plugin-project/turtles.yaml
     - /opt/plugins/secondary-plugin-project/turtles.yaml
     - <<...other plugin set definition file paths...>>

For detailed information about plugin set catalog definitions, see :ref:`Plugin Set Catalog Definition Reference`.

-----------------------------
Configuring a Plugin Registry
-----------------------------

The simplest kind of :term:`plugin registry` has a single :term:`layer <plugin registry layer>`, conventionally named ``production``, and is a directory of plugin JAR files, each a ``.jar`` file named after the plugin's identifier (``plugin_identifier`` in the plugin definition), which is the default naming convention. The :term:`plugin registry definition` in this scenario would look like this:

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
     - <<...other plugin identifiers...>>

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
     - <<...other plugin identifiers...>>

For detailed information about plugin set catalog definitions, see :ref:`Plugin Registry Definition Reference`.

-------------------------------------
Configuring a Plugin Registry Catalog
-------------------------------------

If you are working with multiple :term:`plugin registries <plugin registry>`, and even if you are working with just one, it is convenient to list one or more plugin registries in a :term:`plugin registry catalog`. A :ref:`plugin registry catalog definition` looks like this:

.. code-block:: yaml

   ---
   kind: PluginRegistryCatalog
   plugin-registry-files:
     - /var/www/props.ourproject.org/plugins/turtles.yaml
     - /var/www/props.otherproject.net/plugins/turtles.yaml
     - <<...other plugin set definition file paths...>>

For detailed information about plugin registry catalog definitions, see :ref:`Plugin Registry Catalog Definition Reference`.



----

.. rubric:: Footnotes

.. [#fn-turtles-identifier]

   Although |TURTLES| does not enforce a particular syntax, the intended shape of these identifiers is that they are made of lowercase letters and digits, optionally separated by hyphens or underscores, excluding spaces and other characters/punctuation. |TURTLES| may specify the exact syntax of identifiers in a future version.
