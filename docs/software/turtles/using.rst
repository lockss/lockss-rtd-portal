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

.. note::

   As of version 0.6.0, bare arguments are no longer allowed and treated as plugin identifiers or plugin JARs; all plugin identifiers must be listed via the :ref:`Turtles Plugin Identifier Options` |PLUGIN_IDENTIFIER| and |PLUGIN_IDENTIFIERS|, and all plugin JARs must be listed via the :ref:`Turtles Plugin JAR Options` |PLUGIN_JAR| and |PLUGIN_JARS|.

.. note::

   As of version 0.6.0, the ``turtles usage`` command no longer exists.

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
   *  *  Version number
      *  :ref:`turtles version`
      *  

You can see the synopsis by invoking ``turtles --help``:

..  code-block:: text

    Usage: turtles [-h]
                   {bp,build-plugin,copyright,deploy-plugin,dp,license,release-plugin,rp,version} ...
    
    Tool for managing LOCKSS plugin sets and LOCKSS plugin registries
    
    Commands:
      {bp,build-plugin,copyright,deploy-plugin,dp,license,release-plugin,rp,version}
        bp                  synonym for: build-plugin
        build-plugin        build plugins
        copyright           print the copyright and exit
        deploy-plugin       deploy plugins
        dp                  synonym for: deploy-plugin
        license             print the software license and exit
        release-plugin      release (build and deploy) plugins
        rp                  synonym for: release-plugin
        version             print the version number and exit
    
    Help:
      -h, --help            show this help message and exit

The top-level ``turtles`` command, alone, does not perform any action or default to an implied subcommand.

.. _turtles build-plugin:

.. _turtles bp:

``turtles build-plugin``
========================

The ``turtles build-plugin`` (or alternatively ``turtles bp``) command is used for :term:`building plugins`, turning the source code found in |plugin sets| to signed JAR files ready to be deployed to |plugin registries|. It has its own |HELP| option:

..  code-block:: text

    Usage: turtles build-plugin [-h]
                                [-i PLUGIN_IDENTIFIER [PLUGIN_IDENTIFIER ...]]
                                [-I PLUGIN_IDENTIFIERS [PLUGIN_IDENTIFIERS ...]]
                                [-s PLUGIN_SET [PLUGIN_SET ...]]
                                [-S PLUGIN_SET_CATALOG [PLUGIN_SET_CATALOG ...]]
                                [-c PLUGIN_SIGNING_CREDENTIALS]
                                [--plugin-signing-password PLUGIN_SIGNING_PASSWORD]
                                [--non-interactive]
                                [--output-format OUTPUT_FORMAT]
    
    Optional Arguments:
      -i, --plugin-identifier PLUGIN_IDENTIFIER [PLUGIN_IDENTIFIER ...]
                            (plugin identifiers) add one or more plugin
                            identifiers to the set of plugin identifiers to
                            process (default: None)
      -I, --plugin-identifiers PLUGIN_IDENTIFIERS [PLUGIN_IDENTIFIERS ...]
                            (plugin identifiers) add the plugin identifiers listed
                            in one or more files to the set of plugin identifiers
                            to process (default: None)
      -s, --plugin-set PLUGIN_SET [PLUGIN_SET ...]
                            (plugin sets) add one or more plugin set definition
                            files to the loaded plugin sets (default: None)
      -S, --plugin-set-catalog PLUGIN_SET_CATALOG [PLUGIN_SET_CATALOG ...]
                            (plugin sets) add one or more plugin set catalogs to
                            the loaded plugin set catalogs; if no plugin set
                            catalogs or plugin sets are specified, load
                            /home/$USER/.config/lockss-turtles/plugin-set-catalog.y
                            aml or
                            /usr/local/share/lockss-turtles/plugin-set-catalog.yam
                            l or /etc/lockss-turtles/plugin-set-catalog.yaml
                            (default: None)
      -c, --plugin-signing-credentials PLUGIN_SIGNING_CREDENTIALS
                            (plugin signing credentials) load the plugin signing
                            credentials from the given file, or if none, from
                            /home/myuser/.config/lockss-turtles/plugin-signing-crede
                            ntials.yaml or
                            /usr/local/share/lockss-turtles/plugin-signing-credent
                            ials.yaml or
                            /etc/lockss-turtles/plugin-signing-credentials.yaml
                            (default: None)
      --plugin-signing-password PLUGIN_SIGNING_PASSWORD
                            (plugin signing credentials) set the plugin signing
                            password, or if none, prompt interactively (default:
                            None)
      --non-interactive     (plugin signing credentials) disallow interactive
                            prompts (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid,
                            double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex,
                            latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                            pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid,
                            simple_outline, textile, tsv, unsafehtml, youtrack
                            (default: simple)
    
    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER|, |PLUGIN_IDENTIFIERS|).

*  One or more plugin sets, from the :ref:`Turtles Plugin Set Options` (|PLUGIN_SET|, |PLUGIN_SET_CATALOG|) or from a :ref:`Default Plugin Set Catalog File`.

*  Plugin signing credentials, from the :ref:`Turtles Plugin Signing Credentials Options` (|PLUGIN_SIGNING_CREDENTIALS|, |PLUGIN_SIGNING_PASSWORD|) or from a :ref:`Default Plugin Signing Credentials File`.

It also accepts :ref:`Turtles Interactivity Options` (|NON_INTERACTIVE|) and :ref:`Turtles Output Format Options` (|OUTPUT_FORMAT|).

.. _turtles copyright:

``turtles copyright``
=====================

The ``turtles copyright`` command outputs the copyright for |TURTLES|.

.. _turtles deploy-plugin:

.. _turtles dp:

``turtles deploy-plugin``
=========================

The ``turtles deploy-plugin`` (or alternatively ``turtles dp``) command is used for :term:`deploying plugins`, moving signed plugin JARs into appropriate plugin registry layers. It has its own |HELP| option:

..  code-block:: text

    Usage: turtles deploy-plugin [-h] [-j PLUGIN_JAR [PLUGIN_JAR ...]]
                                 [-J PLUGIN_JARS [PLUGIN_JARS ...]]
                                 [-r PLUGIN_REGISTRY [PLUGIN_REGISTRY ...]]
                                 [-R PLUGIN_REGISTRY_CATALOG [PLUGIN_REGISTRY_CATALOG ...]]
                                 [-l PLUGIN_REGISTRY_LAYER [PLUGIN_REGISTRY_LAYER ...]]
                                 [-L PLUGIN_REGISTRY_LAYERS [PLUGIN_REGISTRY_LAYERS ...]]
                                 [-t] [-p] [--non-interactive]
                                 [--output-format OUTPUT_FORMAT]
    
    Optional Arguments:
      -j, --plugin-jar PLUGIN_JAR [PLUGIN_JAR ...]
                            (plugin JARs) add one or more plugin JARs to the set
                            of plugin JARs to process (default: None)
      -J, --plugin-jars PLUGIN_JARS [PLUGIN_JARS ...]
                            (plugin JARs) add the plugin JARs listed in one or
                            more files to the set of plugin JARs to process
                            (default: None)
      -r, --plugin-registry PLUGIN_REGISTRY [PLUGIN_REGISTRY ...]
                            (plugin registry) add one or more plugin registries to
                            the loaded plugin registries (default: None)
      -R, --plugin-registry-catalog PLUGIN_REGISTRY_CATALOG [PLUGIN_REGISTRY_CATALOG ...]
                            (plugin registry) add one or more plugin registry
                            catalogs to the loaded plugin registry catalogs; if no
                            plugin registry catalogs or plugin registries are
                            specified, load
                            /home/$USER/.config/lockss-turtles/plugin-registry-cata
                            log.yaml or
                            /etc/lockss-turtles/plugin-registry-catalog.yaml or
                            /usr/local/share/lockss-turtles/plugin-registry-catalo
                            g.yaml (default: None)
      -l, --plugin-registry-layer PLUGIN_REGISTRY_LAYER [PLUGIN_REGISTRY_LAYER ...]
                            (plugin registry layers) add one or more plugin
                            registry layers to the set of plugin registry layers
                            to process (default: None)
      -L, --plugin-registry-layers PLUGIN_REGISTRY_LAYERS [PLUGIN_REGISTRY_LAYERS ...]
                            (plugin registry layers) add the plugin registry
                            layers listed in one or more files to the set of
                            plugin registry layers to process (default: None)
      -t, --testing         (plugin registry layers) synonym for
                            --plugin-registry-layer testing (i.e. add "testing" to
                            the list of plugin registry layers to process)
                            (default: False)
      -p, --production      (plugin registry layers) synonym for
                            --plugin-registry-layer production (i.e. add
                            "production" to the list of plugin registry layers to
                            process) (default: False)
      --non-interactive     (plugin signing credentials) disallow interactive
                            prompts (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid,
                            double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex,
                            latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                            pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid,
                            simple_outline, textile, tsv, unsafehtml, youtrack
                            (default: simple)
    
    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more plugin JAR files, from the :ref:`Turtles Plugin JAR Options` (|PLUGIN_JAR|, |PLUGIN_JARS|).

*  One or more plugin registries, from the :ref:`Turtles Plugin Registry Options` (|PLUGIN_REGISTRY|, |PLUGIN_REGISTRY_CATALOG|) or from a :ref:`Default Plugin Registry Catalog File`.

*  One or more plugin registry layers, from the :ref:`Turtles Plugin Registry Layer Options` (|PLUGIN_REGISTRY_LAYER|, |PLUGIN_REGISTRY_LAYERS|, |TESTING|, |PRODUCTION|).

It also accepts :ref:`Turtles Interactivity Options` (|NON_INTERACTIVE|) and :ref:`Turtles Output Format Options` (|OUTPUT_FORMAT|).

.. _turtles license:

``turtles license``
===================

The ``turtles license`` command outputs the software license for |TURTLES|.

.. _turtles release-plugin:

.. _turtles rp:

``turtles release-plugin``
==========================

The ``turtles release-plugin`` (or alternatively ``turtles rp``) command is used for :term:`releasing plugins` (:term:`building <building plugins>` then :term:`deploying <deploying plugins>` plugins), that is, turning the source code found in |plugin sets| to signed JAR files, and then moving them into appropriate plugin registry layers. It has its own |HELP| option:

..  code-block:: text

    Usage: turtles release-plugin [-h]
                                  [-i PLUGIN_IDENTIFIER [PLUGIN_IDENTIFIER ...]]
                                  [-I PLUGIN_IDENTIFIERS [PLUGIN_IDENTIFIERS ...]]
                                  [-s PLUGIN_SET [PLUGIN_SET ...]]
                                  [-S PLUGIN_SET_CATALOG [PLUGIN_SET_CATALOG ...]]
                                  [-c PLUGIN_SIGNING_CREDENTIALS]
                                  [--plugin-signing-password PLUGIN_SIGNING_PASSWORD]
                                  [-r PLUGIN_REGISTRY [PLUGIN_REGISTRY ...]]
                                  [-R PLUGIN_REGISTRY_CATALOG [PLUGIN_REGISTRY_CATALOG ...]]
                                  [-l PLUGIN_REGISTRY_LAYER [PLUGIN_REGISTRY_LAYER ...]]
                                  [-L PLUGIN_REGISTRY_LAYERS [PLUGIN_REGISTRY_LAYERS ...]]
                                  [-t] [-p] [--non-interactive]
                                  [--output-format OUTPUT_FORMAT]
    
    Optional Arguments:
      -i, --plugin-identifier PLUGIN_IDENTIFIER [PLUGIN_IDENTIFIER ...]
                            (plugin identifiers) add one or more plugin
                            identifiers to the set of plugin identifiers to
                            process (default: None)
      -I, --plugin-identifiers PLUGIN_IDENTIFIERS [PLUGIN_IDENTIFIERS ...]
                            (plugin identifiers) add the plugin identifiers listed
                            in one or more files to the set of plugin identifiers
                            to process (default: None)
      -s, --plugin-set PLUGIN_SET [PLUGIN_SET ...]
                            (plugin sets) add one or more plugin set definition
                            files to the loaded plugin sets (default: None)
      -S, --plugin-set-catalog PLUGIN_SET_CATALOG [PLUGIN_SET_CATALOG ...]
                            (plugin sets) add one or more plugin set catalogs to
                            the loaded plugin set catalogs; if no plugin set
                            catalogs or plugin sets are specified, load
                            /home/$USER/.config/lockss-turtles/plugin-set-catalog.y
                            aml or /etc/lockss-turtles/plugin-set-catalog.yaml or
                            /usr/local/share/lockss-turtles/plugin-set-catalog.yam
                            l (default: None)
      -c, --plugin-signing-credentials PLUGIN_SIGNING_CREDENTIALS
                            (plugin signing credentials) load the plugin signing
                            credentials from the given file, or if none, from
                            /home/$USER/.config/lockss-turtles/plugin-signing-crede
                            ntials.yaml or
                            /etc/lockss-turtles/plugin-signing-credentials.yaml or
                            /usr/local/share/lockss-turtles/plugin-signing-credent
                            ials.yaml (default: None)
      --plugin-signing-password PLUGIN_SIGNING_PASSWORD
                            (plugin signing credentials) set the plugin signing
                            password, or if none, prompt interactively (default:
                            None)
      -r, --plugin-registry PLUGIN_REGISTRY [PLUGIN_REGISTRY ...]
                            (plugin registry) add one or more plugin registries to
                            the loaded plugin registries (default: None)
      -R, --plugin-registry-catalog PLUGIN_REGISTRY_CATALOG [PLUGIN_REGISTRY_CATALOG ...]
                            (plugin registry) add one or more plugin registry
                            catalogs to the loaded plugin registry catalogs; if no
                            plugin registry catalogs or plugin registries are
                            specified, load
                            /home/$USER/.config/lockss-turtles/plugin-registry-cata
                            log.yaml or
                            /etc/lockss-turtles/plugin-registry-catalog.yaml or
                            /usr/local/share/lockss-turtles/plugin-registry-catalo
                            g.yaml (default: None)
      -l, --plugin-registry-layer PLUGIN_REGISTRY_LAYER [PLUGIN_REGISTRY_LAYER ...]
                            (plugin registry layers) add one or more plugin
                            registry layers to the set of plugin registry layers
                            to process (default: None)
      -L, --plugin-registry-layers PLUGIN_REGISTRY_LAYERS [PLUGIN_REGISTRY_LAYERS ...]
                            (plugin registry layers) add the plugin registry
                            layers listed in one or more files to the set of
                            plugin registry layers to process (default: None)
      -t, --testing         (plugin registry layers) synonym for
                            --plugin-registry-layer testing (i.e. add "testing" to
                            the list of plugin registry layers to process)
                            (default: False)
      -p, --production      (plugin registry layers) synonym for
                            --plugin-registry-layer production (i.e. add
                            "production" to the list of plugin registry layers to
                            process) (default: False)
      --non-interactive     (plugin signing credentials) disallow interactive
                            prompts (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid,
                            double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex,
                            latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline,
                            pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid,
                            simple_outline, textile, tsv, unsafehtml, youtrack
                            (default: simple)
    
    Help:
      -h, --help            show this help message and exit

As a command that combines plugin building and plugin deployment operations, this command requires:

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER|, |PLUGIN_IDENTIFIERS|).

*  One or more plugin sets, from the :ref:`Turtles Plugin Set Options` (|PLUGIN_SET|, |PLUGIN_SET_CATALOG|) or from a :ref:`Default Plugin Set Catalog File`.

*  Plugin signing credentials, from the :ref:`Turtles Plugin Signing Credentials Options` (|PLUGIN_SIGNING_CREDENTIALS|, |PLUGIN_SIGNING_PASSWORD|) or from a :ref:`Default Plugin Signing Credentials File`.

*  One or more plugin registries, from the :ref:`Turtles Plugin Registry Options` (|PLUGIN_REGISTRY|, |PLUGIN_REGISTRY_CATALOG|) or from a :ref:`Default Plugin Registry Catalog File`.

*  One or more plugin registry layers, from the :ref:`Turtles Plugin Registry Layer Options` (|PLUGIN_REGISTRY_LAYER|, |PLUGIN_REGISTRY_LAYERS|, |TESTING|, |PRODUCTION|).

It also accepts :ref:`Turtles Interactivity Options` (|NON_INTERACTIVE|) and :ref:`Turtles Output Format Options` (|OUTPUT_FORMAT|).

.. _turtles version:

``turtles version``
===================

The ``turtles version`` command outputs the |TURTLES| version number.

---------------
Turtles Options
---------------

Turtles Interactivity Options
=============================

Some |TURTLES| commands may prompt for input interactively:

*  :ref:`Turtles Plugin Building Operations` will prompt for a plugin signing password unless the |PLUGIN_SIGNING_PASSWORD| option was specified.

*  :ref:`Turtles Plugin Deployment Operations` will prompt for confirmation before deploying a plugin to a |plugin registry layer| for the very first time.

The |NON_INTERACTIVE| option prevents these interactive prompts.

Turtles Output Format Options
=============================

|TURTLES|'s tabular output is performed by the `tabulate <https://pypi.org/project/tabulate>`_ library through the |OUTPUT_FORMAT| option. See `its README file <https://github.com/astanin/python-tabulate#table-format>`_ or the |HELP| message of any |TURTLES| plugin building or plugin deployment command for a list of the various output formats available. The **default** is ``simple``. The option accepts a single argument, with or without an equal sign:

.. code-block:: shell

   # Without an equal sign
   turtles ... --output-format outline

   # With an equal sign
   turtles ... --output-format=outline

.. tip::

   The output format ``tsv`` produces tab-separated output, which can be more easily processed by other command line tools or imported into a spreadsheet.

Turtles Plugin Identifier Options
=================================

.. note::

   As of version 0.6.0, bare arguments are no longer allowed and treated as plugin identifiers; all plugin identifiers must be listed via the |PLUGIN_IDENTIFIER| and |PLUGIN_IDENTIFIERS| options.

Commands for :ref:`Turtles Plugin Building Operations` expect one or more plugin identifiers, for instance ``edu.myuniversity.plugin.MyFirstPlugin``. The set of plugin identifiers to process is derived from:

*  The plugin identifiers specified in |PLUGIN_IDENTIFIER| options. Each |PLUGIN_IDENTIFIER| option accepts one or more plugin identifiers.

*  The plugin identifiers listed in the files specified as |PLUGIN_IDENTIFIERS| options. Each |PLUGIN_IDENTIFIERS| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --plugin-identifier with one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin \
                        --plugin-identifier edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # Same, but with an equal sign
   turtles build-plugin --plugin-identifier=edu.myuniversity.plugin.MyFirstPlugin \
                        --plugin-identifier=edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # Same, but with --plugin-identifier abbreviated to -i
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin \
                        -i edu.myuniversity.plugin.MySecondPlugin \
                        ...

   # Each --plugin-identifier can have more than one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin \
                                            edu.myuniversity.plugin.MySecondPlugin \
                                            ...

   # Same, but with --plugin-identifier abbreviated to -i [recommended]
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin \
                           edu.myuniversity.plugin.MySecondPlugin \
                           ...

   # Each --plugin-identifiers with one argument
   turtles build-plugin --plugin-identifiers list1.txt \
                        --plugin-identifiers list2.txt \
                        ...

   # Same, but with an equal sign
   turtles build-plugin --plugin-identifiers=list1.txt \
                        --plugin-identifiers=list2.txt \
                        ...

   # Same, but with --plugin-identifiers abbreviated to -I
   turtles build-plugin -I list1.txt -I list2.txt ...

   # Each --plugin-identifiers can have more than one argument
   turtles build-plugin --plugin-identifiers list1.txt list2.txt ...

   # Same, but with --plugin-identifiers abbreviated to -I [recommended]
   turtles build-plugin -I list1.txt list2.txt ...

Turtles Plugin JAR Options
==========================

.. note::

   As of version 0.6.0, bare arguments are no longer allowed and treated as plugin JARs; all plugin identifiers must be listed via the |PLUGIN_JAR| and |PLUGIN_JARS| options.

Commands for :ref:`Turtles Plugin Deployment Operations` expect one or more plugin JAR file paths. The set of plugin JARs to process is derived from:

*  The plugin JAR file paths specified in |PLUGIN_JAR| options. Each |PLUGIN_JAR| option accepts one or more plugin JAR file paths.

*  The plugin JAR files paths listed in the files specified as |PLUGIN_JARS| options. Each |PLUGIN_JARs| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --plugin-jar with one argument
   turtles deploy-plugin --plugin-jar edu.myuniversity.plugin.MyFirstPlugin.jar \
                         --plugin-jar edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # Same, but with an equal sign
   turtles deploy-plugin --plugin-jar=edu.myuniversity.plugin.MyFirstPlugin.jar \
                         --plugin-jar=edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # Same, but with --plugin-jar abbreviated to -j
   turtles deploy-plugin -j edu.myuniversity.plugin.MyFirstPlugin.jar \
                         -j edu.myuniversity.plugin.MySecondPlugin.jar \
                         ...

   # Each --plugin-jar can have more than one argument
   turtles deploy-plugin --plugin-jar edu.myuniversity.plugin.MyFirstPlugin.jar \
                                      edu.myuniversity.plugin.MySecondPlugin.jar \
                                      ...

   # Same, but with --plugin-jar abbreviated to -j [recommended]
   turtles deploy-plugin -j edu.myuniversity.plugin.MyFirstPlugin.jar \
                            edu.myuniversity.plugin.MySecondPlugin.jar \
                            ...

   # Each --plugin-jars with one argument
   turtles deploy-plugin --plugin-jars list1.txt --plugin-jars list2.txt ...

   # Same, but with an equal sign
   turtles deploy-plugin --plugin-jars=list1.txt \
                         --plugin-jars=list2.txt \
                         ...

   # Same, but with --plugin-jars abbreviated to -J
   turtles deploy-plugin -J list1.txt -J list2.txt ...

   # Each --plugin-jars can have more than one argument
   turtles deploy-plugin --plugin-jars list1.txt list2.txt ...

   # Same, but with --plugin-jars abbreviated to -J [recommended]
   turtles deploy-plugin -J list1.txt list2.txt ...

Turtles Plugin Registry Options
===============================

Commands for :ref:`Turtles Plugin Deployment Operations` need one or more plugin registries. The loaded plugin registries are derived from:

*  The plugin registry definitions found in files specified in |PLUGIN_REGISTRY| options. Each |PLUGIN_REGISTRY| option accepts one or more file paths.

*  The plugin registries listed in the plugin registry catalog definitions found in files specified in |PLUGIN_REGISTRY_CATALOG| options. Each |PLUGIN_REGISTRY_CATALOG| option accepts one or more file paths.

If no plugin registry nor plugin registry catalog is specified with |PLUGIN_REGISTRY| or |PLUGIN_REGISTRY_CATALOG| options (respectively), |TURTLES| loads a :ref:`Default Plugin Registry Catalog File`.

Turtles Plugin Registry Layer Options
=====================================

Commands for :ref:`Turtles Plugin Deployment Operations` expect one or more plugin registry layers, for instance ``testing`` or ``production``. The set of plugin registry layers to process is derived from:

*  The plugin registry layer identifiers specified in |PLUGIN_REGISTRY_LAYER| options. Each |PLUGIN_REGISTRY_LAYER| option accepts one or more plugin registry layer identifiers.

*  The plugin registry layer identifiers listed in the files specified as |PLUGIN_REGISTRY_LAYERS| options. Each |PLUGIN_REGISTRY_LAYERS| option accepts one or more file paths.

*  The |TESTING| options, which add ``testing`` to the set of plugin registry layers to process.

*  The |PRODUCTION| options, which add ``production`` to the set of plugin registry layers to process.

Examples:

.. code-block:: shell

   # Each --plugin-registry-layer with one argument
   turtles deploy-plugin ... --plugin-registry-layer testing \
                             --plugin-registry-layer production \
                             ...

   # Same, but with an equal sign
   turtles deploy-plugin ... --plugin-registry-layer=testing \
                             --plugin-registry-layer=production \
                             ...

   # Same, but with --plugin-registry-layer abbreviated to -l
   turtles deploy-plugin ... -l testing -l production ...

   # Each --plugin-registry-layer can have more than one argument
   turtles deploy-plugin ... --plugin-registry-layer testing production ...

   # Same, but with --plugin-registry-layer abbreviated to -l [recommended]
   turtles deploy-plugin ... -l testing production ...

   # Using --testing as a synonym for --plugin-registry-layer=testing
   # and --production as a synonym for --plugin-registry-layer=production
   turtles deploy-plugin ... --testing --production ...

   # Same, but with --testing abbreviated to -t
   # and --production abbreviated to -p
   turtles deploy-plugin ... -t -p ...

   # Same, but combining -t and -p into one
   turtles deploy-plugin ... -tp ...

   # Each --plugin-registry-layers with one argument
   turtles deploy-plugin ... --plugin-registry-layers list1.txt \
                             --plugin-registry-layers list2.txt \
                             ...

   # Same, but with an equal sign
   turtles deploy-plugin ... --plugin-registry-layers=list1.txt \
                             --plugin-registry-layers=list2.txt \
                             ...

   # Same, but with --plugin-registry-layers abbreviated to -L
   turtles deploy-plugin ... -L list1.txt -L list2.txt ...

   # Each --plugin-registry-layers can have more than one argument
   turtles deploy-plugin ... --plugin-registry-layers list1.txt \
                                                      list2.txt \
                                                      ...

   # Same, but with --plugin-registry-layers abbreviated to -L [recommended]
   turtles deploy-plugin ... -L list1.txt list2.txt ...

Turtles Plugin Set Options
==========================

Commands for :ref:`Turtles Plugin Building Operations` need one or more plugin sets. The loaded plugin sets are derived from:

*  The plugin set definitions found in files specified in |PLUGIN_SET| options. Each |PLUGIN_SET| option accepts one or more file paths.

*  The plugin sets listed in the plugin set catalog definitions found in files specified in |PLUGIN_SET_CATALOG| options. Each |PLUGIN_SET_CATALOG| option accepts one or more file paths.

If no plugin set nor plugin set catalog is specified with |PLUGIN_SET| or |PLUGIN_SET_CATALOG| options (respectively), |TURTLES| loads a :ref:`Default Plugin Registry Catalog File`.

Turtles Plugin Signing Credentials Options
==========================================

Commands for :ref:`Turtles Plugin Building Operations` need plugin signing credentials and a plugin signing password.

The plugin signing credentials are derived from the |PLUGIN_SIGNING_CREDENTIALS| option or, if not specified, from a :ref:`Default Plugin Signing Credentials File`.

The plugin signing password can be given interactively (unless the |NON_INTERACTIVE| option is specified; see :ref:`Turtles Interactivity Options`), or passed at the command line with the |PLUGIN_SIGNING_PASSWORD| option.
