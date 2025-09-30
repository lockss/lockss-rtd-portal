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
      *  :ref:`turtles bp <turtles build-plugin>`
      *  build plugins
   *  *  :ref:`turtles copyright`
      *  n/a
      *  print the copyright and exit
   *  *  :ref:`turtles deploy-plugins`
      *  :ref:`turtles dp <turtles deploy-plugins>`
      *  deploy plugins
   *  *  :ref:`turtles license`
      *  n/a
      *  print the software license and exit
   *  *  :ref:`turtles release-plugins`
      *  :ref:`turtles rp <turtles release-plugins>`
      *  release (build and deploy) plugins
   *  *  :ref:`turtles version`
      *  n/a
      *  print the version number and exit

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

The ``turtles build-plugin`` (or alternatively ``turtles bp``) command is one of the :ref:`Turtles Plugin Building Operations`. It has its own |HELP| option:

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

*  One or more plugin identifiers, from the :ref:`Turtles Plugin Identifier Options` (|PLUGIN_IDENTIFIER|, |PLUGIN_IDENTIFIERS|).

*  One or more plugin sets, from the :ref:`Turtles Plugin Set Options` (|PLUGIN_SET|, |PLUGIN_SET_CATALOG|) or from a :ref:`Default Plugin Set Catalog File`.

*  Plugin signing credentials, from the :ref:`Turtles Plugin Signing Credentials Options` (|PLUGIN_SIGNING_CREDENTIALS|, |PLUGIN_SIGNING_PASSWORD|) or from a :ref:`Default Plugin Signing Credentials File`.

It also accepts :ref:`Turtles Interactivity Options` (|NON_INTERACTIVE|) and :ref:`Turtles Output Format Options` (|OUTPUT_FORMAT|).

---------------
Turtles Options
---------------

Turtles Plugin Identifier Options
=================================

.. note::

   As of version 0.6.0, bare arguments are no longer allowed and treated as plugin identifiers; all plugin identifiers must be listed via the :ref:`Turtles Plugin Identifier Options` |PLUGIN_IDENTIFIER| and |PLUGIN_IDENTIFIERS|.

Commands for :ref:`Turtles Plugin Building Operations` expect one or more plugin identifiers, for instance ``edu.myuniversity.plugin.MyFirstPlugin``. The set of plugin identifiers to process is derived from:

*  The plugin identifiers specified in |PLUGIN_IDENTIFIER| options. Each |PLUGIN_IDENTIFIER| option accepts one or more plugin identifiers.

*  The plugin identifiers listed in the files specified as |PLUGIN_IDENTIFIERS| options. Each |PLUGIN_IDENTIFIERS| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --plugin-identifier with one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin --plugin-identifier edu.myuniversity.plugin.MySecondPlugin ...

   # Same, with --plugin-identifier abbreviated to -i
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin -i edu.myuniversity.plugin.MySecondPlugin ...

   # Each --plugin-identifier can have more than one argument
   turtles build-plugin --plugin-identifier edu.myuniversity.plugin.MyFirstPlugin edu.myuniversity.plugin.MySecondPlugin ...

   # Same, with --plugin-identifier abbreviated to -i [recommended]
   turtles build-plugin -i edu.myuniversity.plugin.MyFirstPlugin edu.myuniversity.plugin.MySecondPlugin ...

   # --plugin-identifier with a single argument can also use an equals sign
   turtles build-plugin --plugin-identifier=edu.myuniversity.plugin.MyFirstPlugin ...

   # Each --plugin-identifiers with one argument
   turtles build-plugin --plugin-identifiers list1.txt --plugin-identifiers list2.txt ...

   # Same, with --plugin-identifiers abbreviated to -I
   turtles build-plugin -I list1.txt -I list2.txt ...

   # Each --plugin-identifiers can have more than one argument
   turtles build-plugin --plugin-identifiers list1.txt list2.txt ...

   # Same, with --plugin-identifiers abbreviated to -I [recommended]
   turtles build-plugin -I list1.txt list2.txt ...

   # --plugin-identifiers with a single argument can also use an equals sign
   turtles build-plugin --plugin-identifiers=list1.txt ...

Turtles Plugin Set Options
==========================

Commands for :ref:`Turtles Plugin Building Operations` need one or more plugin sets. The loaded plugin sets are derived from:

*  The plugin set definitions found in files specified in |PLUGIN_SET| options. Each |PLUGIN_SET| option accepts one or more file paths.

*  The plugin sets listed in the plugin set catalog definitions found in files specified in |PLUGIN_SET_CATALOG| options. Each |PLUGIN_SET_CATALOG| option accepts one or more file paths.

Default Plugin Set Catalog File
-------------------------------

If no plugin set nor plugin set catalog is specified with |PLUGIN_SET| or |PLUGIN_SET_CATALOG| options (respectively), |TURTLES| loads a **default plugin set catalog file**, trying each of the following until one is found:

1. :file:`{$HOME}/.config/lockss-turtles/plugin-set-catalog.yaml`, which is typically :file:`/home/{$USER}/.config/lockss-turtles/plugin-set-catalog.yaml` for the given user on the machine

2. :file:`/etc/lockss-turtles/plugin-set-catalog.yaml`

3. :file:`/usr/local/share/lockss-turtles/plugin-set-catalog.yaml`

Turtles Plugin Signing Credentials Options
==========================================

Commands for :ref:`Turtles Plugin Building Operations` need plugin signing credentials and a plugin signing password.

The plugin signing credentials are derived from the |PLUGIN_SIGNING_CREDENTIALS| option or from a :ref:`default plugin signing credentials file`.

The plugin signing password can be given interactively (unless the |NON_INTERACTIVE| option is specified; see :ref:`Turtles Interactivity Options`), or passed at the command line with the |PLUGIN_SIGNING_PASSWORD| option.

Default Plugin Signing Credentials File
---------------------------------------

If no plugin signing credentials are specified with |PLUGIN_SIGNING_CREDENTIALS| option, |TURTLES| loads a **default plugin signing credentials file**, trying each of the following until one is found:

1. :file:`{$HOME}/.config/lockss-turtles/plugin-signing-credentials.yaml`, which is typically :file:`/home/{$USER}/.config/lockss-turtles/plugin-signing-credentials.yaml` for the given user on the machine

2. :file:`/etc/lockss-turtles/plugin-signing-credentials.yaml`

3. :file:`/usr/local/share/lockss-turtles/plugin-signing-credentials.yaml`
