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

The available commands are:

.. list-table::
   :header-rows: 1

   *  *  Command
      *  Abbreviation
      *  Purpose
   *  *  :ref:`turtles build-plugin`
      *  ``turtles bp``
      *  build plugins
   *  *  :ref:`turtles copyright`
      *  n/a
      *  print the copyright and exit
   *  *  :ref:`turtles deploy-plugins`
      *  ``turtles dp``
      *  deploy plugins
   *  *  :ref:`turtles copyright`
      *  n/a
      *  print the software license and exit
   *  *  :ref:`turtles release-plugins`
      *  ``turtles rp``
      *  release (build and deploy) plugins
   *  *  :ref:`turtles copyright`
      *  n/a
      *  print the version number and exit

You can see the this synopsis by invoking ``turtles --help``:

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

.. _turtles command:

``turtles`` Command
===================

The top-level executable alone does not perform any action or default to a given command:

..  code-block:: text

    Usage: turtles [-h]
                   {bp,build-plugin,copyright,deploy-plugin,dp,license,release-plugin,rp,version} ...
    turtles: error: the following arguments are required: {bp,build-plugin,copyright,deploy-plugin,dp,license,release-plugin,rp,version}

.. _turtles build-plugin:

.. _turtles bp:

``turtles build-plugin``
========================

The ``build-plugin`` (or alternatively ``bp``) command is used produce JAR files out of the source code of LOCKSS plugins from a plugin set, and cryptographically signing them. It has its own |HELP| option:

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
                            /home/myuser/.config/lockss-turtles/plugin-set-catalog.y
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

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER| options, |PLUGIN_IDENTIFIERS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

---------------------------------
Turtles Plugin Identifier Options
---------------------------------

.. note::

   As of version 0.6.0, bare arguments are no longer allowed and treated as plugin identifiers; all plugin identifiers must be listed via the :ref:`Turtles Plugin Identifier Options` |PLUGIN_IDENTIFIER| and |PLUGIN_IDENTIFIERS|.

The :ref:`turtles build-plugin` and :ref:`turtles release-plugin` commands expect one or more plugin identifiers, for instance ``edu.myuniversity.plugin.MyFirstPlugin``. The set of plugin identifiers to process is derived from:

*  The plugin identifiers listed in |PLUGIN_IDENTIFIER| options. Each |PLUGIN_IDENTIFIER| option accepts one or more plugin identifiers.

*  The plugin identifiers found in the files listed as |PLUGIN_IDENTIFIERS| options. Each |PLUGIN_IDENTIFIERS| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --plugin-identifier with one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin --plugin-identifier edu.myuniversity.plugin.MySecondPlugin ... --output-format simple ...

   # Same, with --plugin-identifier abbreviated to -i
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin -i edu.myuniversity.plugin.MySecondPlugin ... --output-format simple ...

   # Each --plugin-identifier can have more than one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin edu.myuniversity.plugin.MySecondPlugin ... --output-format simple ...

   # Same, with --plugin-identifier abbreviated to -i
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin edu.myuniversity.plugin.MySecondPlugin ... --output-format simple ...

   # --plugin-identifier with a single argument can also use an equals sign
   turtles build-plugin --plugin-identifier=edu.myuniversity.plugin.MyFirstPlugin ... --output-format simple ...

   # Each --plugin-identifiers with one argument
   turtles build-plugin --plugin-identifiers list1.txt --plugin-identifiers list2.txt ... --output-format simple ...

   # Same, with --plugin-identifiers abbreviated to -I
   turtles build-plugin -I list1.txt -I list2.txt ... --output-format simple ...

   # Each --plugin-identifiers can have more than one argument
   turtles build-plugin --plugin-identifiers list1.txt list2.txt ... --output-format simple ...

   # Same, with --plugin-identifiers abbreviated to -I
   turtles build-plugin -I list1.txt list2.txt ... --output-format simple ...

   # --plugin-identifiers with a single argument can also use an equals sign
   turtles build-plugin --plugin-identifiers=list1.txt ... --output-format simple ...
