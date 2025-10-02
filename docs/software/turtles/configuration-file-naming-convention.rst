:Type: string
:Required: no
:Default: ``identifier``

A file naming convention for the JAR files. Optional (``identifier`` by default). The three available file naming conventions and their effect on the plugin identifier ``org.ourproject.plugin.plugin1.Plugin1`` are:

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
