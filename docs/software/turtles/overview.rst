================
Turtles Overview
================

----------------
Turtles Concepts
----------------

Plugin set
   A code repository containing the source code and unit tests of one or more LOCKSS plugins.

Plugin set definition file
   A configuration file identifying a plugin set and its characteristics.

Plugin set catalog
   A configuration file identifying one or more plugin set definition files.

Plugin registry
   An on-disk directory tree served by a Web server to make LOCKSS plugins available to the nodes of a LOCKSS network configured to use it.

Plugin registry layer
   A subdivision of a plugin registry that might be used by different subsets of LOCKSS nodes configured to use it. Some LOCKSS plugin registries have a single layer (traditionally named ``production``), and many have two (traditionally named ``testing`` and ``production``, with the former serving for plugin development or content processing quality assurance purposes before the corresponding plugins or content are made available to the latter), but there can be more and layers can have arbitrary names.

Plugin registry definition file
   A configuration file identifying a plugin registry and its characteristics (including its layers).

Plugin registry catalog
   A configuration file identifying one or more plugin registry definition files.

Plugin signing credentials definition file
   A configuration file identifying a user's credentials for cryptographically signing LOCKSS plugins.

Building a plugin
   Producing a JAR file out of the source code of a LOCKSS plugin from a plugin set and cryptographically signing it.

Deploying a plugin
   Putting the JAR file of a built plugin in one or more plugin registry layers, making it available to LOCKSS nodes configured to use the corresponding plugin registries.

Releasing a plugin
   Building and deploying a plugin.

------------------
Turtles Operations
------------------

Turtles has three main operations:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Build plugins
      *  :ref:`turtles build-plugin`
      *  :py:meth:`lockss.turtles.app.TurtlesApp.build_plugin`

------------------------
Other Turtles Operations
------------------------

Other operations include:

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
