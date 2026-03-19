=============
Using Turtles
=============

.. include:: subst.rst

|TURTLES| is invoked at the command line as:

.. code-block:: shell

   turtles

or as a Python module:

.. code-block:: shell

   python -m lockss.turtles

Help messages and this document use ``turtles`` throughout, but the two invocation styles are interchangeable.

----------------
Turtles Commands
----------------

|TURTLES| commands are in the subcommand style of programs like :command:`git`, :command:`dnf`/:command:`yum`, :command:`apt`/:command:`apt-get`, and the like.

The available commands mirror the various :ref:`Turtles Operations`:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command
      *  Abbreviation
   *  *  Build plugins
      *  :ref:`turtles build-plugin`
      *  :ref:`turtles bp <turtles build-plugin>`
   *  *  Copyright statement
      *  :ref:`turtles copyright`
      *  
   *  *  Deploy plugins
      *  :ref:`turtles deploy-plugin`
      *  :ref:`turtles dp <turtles deploy-plugin>`
   *  *  Software license
      *  :ref:`turtles license`
      *  
   *  *  Release plugins
      *  :ref:`turtles release-plugin`
      *  :ref:`turtles rp <turtles release-plugin>`
   *  *  Subcommand tree
      *  :ref:`turtles tree`
      *  
   *  *  Version number
      *  :ref:`turtles version`
      *  

You can see the synopsis by invoking ``turtles --help``:

.. click:run::

   invoke(_turtles, args=['--help'])

.. _turtles command:

``turtles`` command
===================

The top-level ``turtles`` command, alone, defaults to ``turtles --help``.

.. note::

   The |COLOR| and |SHOW_PARAMS| options attach to the top-level ``turtles`` command only, not to a subcommand that may also be specified. For example, this is not valid:

   .. click:run::

      invoke(_turtles, args=['build-plugin', '--help', '--no-color'])

   Instead, you should invoke ``turtles --no-color build-plugin --help``.

.. _turtles build-plugin:

.. _turtles bp:

``turtles build-plugin``
========================

The ``turtles build-plugin`` (or alternatively ``turtles bp``) command is used for :term:`building plugins`, turning the source code found in |plugin sets| into signed JAR files ready to be deployed to |plugin registries|. It has its own |HELP| option:

.. click:run::

   invoke(_turtles, args=['build-plugin', '--help'])

The command requires:

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER|, |PLUGIN_IDENTIFIERS|).

*  One or more plugin sets, from the :ref:`Turtles Plugin Set Options` (|PLUGIN_SET|, |PLUGIN_SET_CATALOG|) or from a :ref:`Default Plugin Set Catalog File`.

*  Plugin signing credentials, from the :ref:`Turtles Plugin Signing Credentials Options` (|PLUGIN_SIGNING_CREDENTIALS|, |PLUGIN_SIGNING_PASSWORD|) or from a :ref:`Default Plugin Signing Credentials File`.

It also accepts :ref:`Turtles Interactivity Options` (|INTERACTIVE|) and :ref:`Turtles Output Format Options` (|TABLE_FORMAT|, |HEADINGS|).

.. _turtles copyright:

``turtles copyright``
=====================

The ``turtles copyright`` command outputs the copyright for |TURTLES|:

.. click:run::

   invoke(_turtles, args=['copyright'])

.. _turtles deploy-plugin:

.. _turtles dp:

``turtles deploy-plugin``
=========================

The ``turtles deploy-plugin`` (or alternatively ``turtles dp``) command is used for :term:`deploying plugins`, moving signed plugin JARs into appropriate plugin registry layers. It has its own |HELP| option:

.. click:run::

   invoke(_turtles, args=['deploy-plugin', '--help'])

The command requires:

*  One or more plugin JAR files, from the :ref:`Turtles Plugin JAR Options` (|PLUGIN_JAR|, |PLUGIN_JARS|).

*  One or more plugin registries, from the :ref:`Turtles Plugin Registry Options` (|PLUGIN_REGISTRY|, |PLUGIN_REGISTRY_CATALOG|) or from a :ref:`Default Plugin Registry Catalog File`.

*  One or more plugin registry layers, from the :ref:`Turtles Plugin Registry Layer Options` (|PLUGIN_REGISTRY_LAYER|, |PLUGIN_REGISTRY_LAYERS|, |TESTING|, |PRODUCTION|).

It also accepts :ref:`Turtles Interactivity Options` (|INTERACTIVE|) and :ref:`Turtles Output Format Options` (|TABLE_FORMAT|, |HEADINGS|).

.. _turtles license:

``turtles license``
===================

The ``turtles license`` command outputs the software license for |TURTLES|:

.. click:run::

   invoke(_turtles, args=['license'])

.. _turtles release-plugin:

.. _turtles rp:

``turtles release-plugin``
==========================

The ``turtles release-plugin`` (or alternatively ``turtles rp``) command is used for :term:`releasing plugins` (:term:`building <building plugins>` then :term:`deploying <deploying plugins>` plugins), that is, turning the source code found in |plugin sets| into signed JAR files, and then moving them into appropriate plugin registry layers. It has its own |HELP| option:

.. click:run::

   invoke(_turtles, args=['release-plugin', '--help'])

As a command that combines plugin building and plugin deployment operations, this command requires:

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER|, |PLUGIN_IDENTIFIERS|).

*  One or more plugin sets, from the :ref:`Turtles Plugin Set Options` (|PLUGIN_SET|, |PLUGIN_SET_CATALOG|) or from a :ref:`Default Plugin Set Catalog File`.

*  Plugin signing credentials, from the :ref:`Turtles Plugin Signing Credentials Options` (|PLUGIN_SIGNING_CREDENTIALS|, |PLUGIN_SIGNING_PASSWORD|) or from a :ref:`Default Plugin Signing Credentials File`.

*  One or more plugin registries, from the :ref:`Turtles Plugin Registry Options` (|PLUGIN_REGISTRY|, |PLUGIN_REGISTRY_CATALOG|) or from a :ref:`Default Plugin Registry Catalog File`.

*  One or more plugin registry layers, from the :ref:`Turtles Plugin Registry Layer Options` (|PLUGIN_REGISTRY_LAYER|, |PLUGIN_REGISTRY_LAYERS|, |TESTING|, |PRODUCTION|).

It also accepts :ref:`Turtles Interactivity Options` (|INTERACTIVE|) and :ref:`Turtles Output Format Options` (|TABLE_FORMAT|, |HEADINGS|).

.. _turtles tree:

``turtles tree``
===================

The ``turtles tree`` command displays the |TURTLES| subcommand tree:

.. click:run::

   invoke(_turtles, args=['tree'])

.. _turtles version:

``turtles version``
===================

The ``turtles version`` command outputs the |TURTLES| version number:

.. click:run::

   invoke(_turtles, args=['version'])

---------------
Turtles Options
---------------

Turtles Interactivity Options
=============================

Some |TURTLES| commands may prompt for input interactively:

*  :ref:`Turtles Plugin Building Operations` will prompt for a plugin signing password unless the |PLUGIN_SIGNING_PASSWORD| option was specified.

*  :ref:`Turtles Plugin Deployment Operations` will prompt for confirmation before deploying a plugin to a |plugin registry layer| for the very first time.

The ``--non-interactive`` option prevents these interactive prompts.

Turtles Output Format Options
=============================

.. note::

   As of version 0.7.0, ``--output-format`` has been renamed to |TABLE_FORMAT|.

|TURTLES|'s tabular output is performed by the `Click Extra <https://kdeldycke.github.io/click-extra/index.html>`_ library, via the |TABLE_FORMAT| and |HEADINGS| options. See `its documentation <https://kdeldycke.github.io/click-extra/table.html#table-formats>`_ or the |HELP| message of any |TURTLES| plugin building or plugin deployment command for a list of the various output formats available in the |TABLE_FORMAT| option. The default value is ``simple``. This option accepts a single argument, with or without an equals sign:

.. code-block:: shell

   # Without an equals sign
   turtles ... --table-format outline

   # With an equals sign
   turtles ... --table-format=outline

The |HEADINGS| options control whether or not column headings are displayed, respectively. The default is ``--headings``.

Turtles Plugin Identifier Options
=================================

.. note::

   As of version 0.7.0, |PLUGIN_IDENTIFIER| and |PLUGIN_IDENTIFIERS| options only accept one argument at a time each, rather than one or more each.

Commands for :ref:`Turtles Plugin Building Operations` expect one or more plugin identifiers, for instance ``edu.myuniversity.plugin.MyFirstPlugin``. The set of plugin identifiers to process is derived from:

*  The plugin identifiers specified in |PLUGIN_IDENTIFIER| options. Each |PLUGIN_IDENTIFIER| option accepts one plugin identifier. The long option ``--plugin-identifier`` and its argument can optionally be joined by an equals sign.

*  The plugin identifiers listed in the files specified as |PLUGIN_IDENTIFIERS| options. Each |PLUGIN_IDENTIFIERS| option accepts one file path. The long option ``--plugin-identifiers`` and its argument can optionally be joined by an equals sign.

Examples:

.. code-block:: shell

   # --plugin-identifier without an equals sign
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin \
                        --plugin-identifier edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # Same, but with --plugin-identifier abbreviated to -i
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin \
                        -i edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # --plugin-identifier with an equals sign
   turtles build-plugin --plugin-identifier=edu.myuniversity.plugin.MyFirstPlugin \
                        --plugin-identifier=edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # --plugin-identifiers without an equals sign
   turtles build-plugin --plugin-identifiers list1.txt \
                        --plugin-identifiers list2.txt \
                        ...

   # Same, but with --plugin-identifiers abbreviated to -I
   turtles build-plugin -I list1.txt -I list2.txt ...

   # --plugin-identifiers with an equals sign
   turtles build-plugin --plugin-identifiers=list1.txt \
                        --plugin-identifiers=list2.txt \
                        ...

Turtles Plugin JAR Options
==========================

.. note::

   As of version 0.7.0, |PLUGIN_JAR| and |PLUGIN_JARS| options only accept one argument at a time each, rather than one or more each.

Commands for :ref:`Turtles Plugin Deployment Operations` expect one or more plugin JAR file paths. The set of plugin JARs to process is derived from:

*  The plugin JAR file paths specified in |PLUGIN_JAR| options. Each |PLUGIN_JAR| option accepts one plugin JAR file path. The long option ``--plugin-jar`` and its argument can optionally be joined by an equals sign.

*  The plugin JAR files paths listed in the files specified as |PLUGIN_JARS| options. Each |PLUGIN_JARs| option accepts one file paths. The long option ``--plugin-jars`` and its argument can optionally be joined by an equals sign.

Examples:

.. code-block:: shell

   # --plugin-jar without an equals sign
   turtles deploy-plugin --plugin-jar edu.myuniversity.plugin.MyFirstPlugin.jar \
                         --plugin-jar edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # Same, but with --plugin-jar abbreviated to -j
   turtles deploy-plugin -j edu.myuniversity.plugin.MyFirstPlugin.jar \
                         -j edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # --plugin-jar with an equals sign
   turtles deploy-plugin --plugin-jar=edu.myuniversity.plugin.MyFirstPlugin.jar \
                         --plugin-jar=edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # --plugin-jars without an equals sign
   turtles deploy-plugin --plugin-jars list1.txt --plugin-jars list2.txt ...

   # Same, but with --plugin-jars abbreviated to -J
   turtles deploy-plugin -J list1.txt -J list2.txt ...

   # --plugin-jars with an equals sign
   turtles deploy-plugin --plugin-jars=list1.txt \
                         --plugin-jars=list2.txt \
                         ...

Turtles Plugin Registry Options
===============================

.. note::

   As of version 0.7.0, |PLUGIN_REGISTRY| and |PLUGIN_REGISTRY_CATALOG| options only accept one argument at a time each, rather than one or more each.

Commands for :ref:`Turtles Plugin Deployment Operations` need one or more |plugin registries|. The loaded plugin registries are derived from:

*  The |plugin registry definitions| found in files specified in |PLUGIN_REGISTRY| options. Each |PLUGIN_REGISTRY| option accepts one file path. The long option ``--plugin-registry`` and its argument can optionally be joined by an equals sign.

*  The plugin registries listed in the |plugin registry catalog definitions| found in files specified in |PLUGIN_REGISTRY_CATALOG| options. Each |PLUGIN_REGISTRY_CATALOG| option accepts one file path. The long option ``--plugin-registry-catalog`` and its argument can optionally be joined by an equals sign.

If no plugin registry nor plugin registry catalog is specified with |PLUGIN_REGISTRY| or |PLUGIN_REGISTRY_CATALOG| options (respectively), |TURTLES| loads a :ref:`Default Plugin Registry Catalog File`.

Turtles Plugin Registry Layer Options
=====================================

.. note::

   As of version 0.7.0, |PLUGIN_REGISTRY_LAYER| and |PLUGIN_REGISTRY_LAYERS| options only accept one argument at a time each, rather than one or more each.

Commands for :ref:`Turtles Plugin Deployment Operations` expect one or more plugin registry layers, for instance ``testing`` or ``production``. The set of plugin registry layers to process is derived from:

*  The plugin registry layer identifiers specified in |PLUGIN_REGISTRY_LAYER| options. Each |PLUGIN_REGISTRY_LAYER| option accepts one plugin registry layer identifier. The long option ``--plugin-registry-layer`` and its argument can optionally be joined by an equals sign.

*  The plugin registry layer identifiers listed in the files specified as |PLUGIN_REGISTRY_LAYERS| options. Each |PLUGIN_REGISTRY_LAYERS| option accepts one file path. The long option ``--plugin-registry-layers`` and its argument can optionally be joined by an equals sign.

*  The |TESTING| options, which add ``testing`` to the set of plugin registry layers to process.

*  The |PRODUCTION| options, which add ``production`` to the set of plugin registry layers to process.

Examples:

.. code-block:: shell

   # --plugin-registry-layer without an equals sign
   turtles deploy-plugin ... --plugin-registry-layer testing \
                             --plugin-registry-layer production \
                             ...

   # Same, but with --plugin-registry-layer abbreviated to -l
   turtles deploy-plugin ... -l testing -l production ...

   # --plugin-registry-layer with an equals sign
   turtles deploy-plugin ... --plugin-registry-layer=testing \
                             --plugin-registry-layer=production \
                             ...

   # Using --testing as a synonym for --plugin-registry-layer=testing
   # and --production as a synonym for --plugin-registry-layer=production
   turtles deploy-plugin ... --testing --production ...

   # Same, but with --testing abbreviated to -t
   # and --production abbreviated to -p
   turtles deploy-plugin ... -t -p ...

   # Same, but combining -t and -p into one
   turtles deploy-plugin ... -tp ...

   # --plugin-registry-layers without an equals sign
   turtles deploy-plugin ... --plugin-registry-layers list1.txt \
                             --plugin-registry-layers list2.txt \
                             ...

   # Same, but with --plugin-registry-layers abbreviated to -L
   turtles deploy-plugin ... -L list1.txt -L list2.txt ...

   # --plugin-registry-layers with an equals sign
   turtles deploy-plugin ... --plugin-registry-layers=list1.txt \
                             --plugin-registry-layers=list2.txt \
                             ...

Turtles Plugin Set Options
==========================

Commands for :ref:`Turtles Plugin Building Operations` need one or more |plugin sets|. The loaded plugin sets are derived from:

*  The |plugin set definitions| found in files specified in |PLUGIN_SET| options. Each |PLUGIN_SET| option accepts one file path. The long option ``--plugin-set`` and its argument can optionally be joined by an equals sign.

*  The plugin sets listed in the |plugin set catalog definitions| found in files specified in |PLUGIN_SET_CATALOG| options. Each |PLUGIN_SET_CATALOG| option accepts one file path. The long option ``--plugin-set-catalog`` and its argument can optionally be joined by an equals sign.

If no plugin set nor plugin set catalog is specified with |PLUGIN_SET| or |PLUGIN_SET_CATALOG| options (respectively), |TURTLES| loads a :ref:`Default Plugin Registry Catalog File`.

Turtles Plugin Signing Credentials Options
==========================================

Commands for :ref:`Turtles Plugin Building Operations` need plugin signing credentials and a plugin signing password.

The plugin signing credentials are derived from the |PLUGIN_SIGNING_CREDENTIALS| option or, if not specified, from a :ref:`Default Plugin Signing Credentials File`. The long option ``--plugin-signing-credentials`` and its argument can optionally be joined by an equals sign.

The plugin signing password can be given interactively (unless the ``--non-interactive`` option is specified; see :ref:`Turtles Interactivity Options`), or passed at the command line with the |PLUGIN_SIGNING_PASSWORD| option. The long option ``--plugin-signing-password`` and its argument can optionally be joined by an equals sign.
