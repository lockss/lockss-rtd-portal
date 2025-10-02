================
Turtles Overview
================

.. include:: subst.rst

----------------
Turtles Concepts
----------------

.. glossary::

   YAML
      A structured data format, like XML or JSON.

   YAML configuration object
      A :term:`YAML` object that describes the an entity and its configuration, using a specified vocabulary. A YAML file contains one or more YAML configuration objects.

   Plugin set
      A code repository containing the source code and unit tests of one or more LOCKSS plugins.

   Plugin set builder
      A code build process that is used to compile and package the plugins in a :term:`plugin set`.

   Plugin set definition
      A :term:`YAML configuration object` describing a :term:`plugin set` and its characteristics, including characteristics needed by its :term:`builder <plugin set builder>`. See :ref:`Configuring a Plugin Set`, :ref:`Plugin Set Definition Reference`.

   Plugin set catalog
      A collection of one or more :term:`plugin set`\s.

   Plugin set catalog definition
      A :term:`YAML configuration object` describing a :term:`plugin set catalog`. See :ref:`Configuring a Plugin Set Catalog`, :ref:`Plugin Set Catalog Definition Reference`.

   Plugin registry
      An on-disk directory tree served by a Web server, to make LOCKSS plugins available to the nodes of a LOCKSS network.

   Plugin registry layer
      A subdivision of a :term:`plugin registry`. Some LOCKSS plugin registries have a single layer (traditionally named ``production``), and many have two (traditionally named ``testing`` and ``production``, with the former serving for plugin development and/or content processing purposes before the corresponding plugins and/or content are made available to the latter). There can be more layers and they can have arbitrary names.

   Plugin registry definition
      A :term:`YAML configuration object` describing a :term:`plugin registry` and its characteristics, including its :term:`layers <plugin registry layer>`. See :ref:`Configuring a Plugin Registry`, :ref:`Plugin Registry Definition Reference`.

   Plugin registry catalog
      A collection of one or more :term:`plugin registry definition`\s.

   Plugin registry catalog definition
      A :term:`YAML configuration object` describing a :term:`plugin registry catalog`.

   Plugin signing credentials
      Elements needed to cryptographically sign plugins. Currently, this includes a signing keystore and a signer identifier from the keystore.

   Plugin signing credentials definition
      A :term:`YAML configuration object` describing a user's :term:`plugin signing credentials`.

   Building plugins
      Producing JAR files out of the source code of LOCKSS plugins from a :term:`plugin set`, and cryptographically signing them with given :term:`plugin signing credentials`.

   Deploying plugins
      Putting the JAR files of built LOCKSS plugins in one or more :term:`plugin registry layer`\s, making them available to LOCKSS nodes configured to use the corresponding :term:`plugin registries <plugin registry>`.

   Releasing plugins
      :term:`Building <building plugins>` then :term:`deploying <deploying plugins>` plugins.

------------------
Turtles Operations
------------------

|TURTLES| operations fall into three categories:

*  :ref:`Turtles Plugin Building Operations`

*  :ref:`Turtles Plugin Deployment Operations`

*  :ref:`Other Turtles Operations`

Turtles Plugin Building Operations
==================================

|TURTLES| has two operations that are concerned with :term:`building plugins`:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Build plugins
      *  :ref:`turtles build-plugin`
      *  :py:meth:`lockss.turtles.app.TurtlesApp.build_plugin`
   *  *  Release plugins [#fn-release-plugin]_
      *  :ref:`turtles release-plugin`
      *  :py:meth:`lockss.turtles.app.TurtlesApp.release_plugin`

Turtles Plugin Deployment Operations
====================================

|TURTLES| has two operations that are concerned with :term:`deploying plugins`:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Deploy plugins
      *  :ref:`turtles deploy-plugin`
      *  :py:meth:`lockss.turtles.app.TurtlesApp.deploy_plugin`
   *  *  Release plugins [#fn-release-plugin]_
      *  :ref:`turtles release-plugin`
      *  :py:meth:`lockss.turtles.app.TurtlesApp.release_plugin`

Other Turtles Operations
========================

Other |TURTLES| operations include:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Copyright statement
      *  :ref:`turtles copyright`
      *  :py:const:`lockss.turtles.__copyright__`
   *  *  Software license
      *  :ref:`turtles license`
      *  :py:const:`lockss.turtles.__license__`
   *  *  Version number
      *  :ref:`turtles version`
      *  :py:const:`lockss.turtles.__version__`

----

.. rubric:: Footnotes

.. [#fn-release-plugin]

   Because :term:`releasing plugins` means :term:`building <building plugins>` then :term:`deploying <deploying plugins>` plugins, :ref:`turtles release-plugin` is listed among both :ref:`Turtles Plugin Building Operations` and :ref:`Turtles Plugin Deployment Operations`.
