================
Using Debugpanel
================

.. include:: subst.rst

|DEBUGPANEL| is invoked at the command line as:

.. code-block:: shell

   debugpanel

or as a Python module:

.. code-block:: shell

   python -m lockss.debugpanel

Help messages and this document use ``debugpanel`` throughout, but the two invocation styles are interchangeable.

-------------------
Debugpanel Commands
-------------------

.. note::

   As of version 0.8.0, bare arguments are no longer allowed and treated as nodes; all nodes must be listed via the :ref:`Debugpanel Node Options` |NODE| and |NODES|.

.. note::

   As of version 0.8.0, the ``debugpanel usage`` command no longer exists.

|DEBUGPANEL| commands are in the subcommand style of programs like :command:`git`, :command:`dnf`/:command:`yum`, :command:`apt`/:command:`apt-get`, and the like.

The available commands are:

.. list-table::
   :header-rows: 1

   *  *  Command
      *  Abbreviation
      *  Purpose
   *  *  :ref:`debugpanel check-substance`
      *  ``debugpanel cs``
      *  cause nodes to check the substance of AUs
   *  *  :ref:`debugpanel copyright`
      *  n/a
      *  print the copyright and exit
   *  *  :ref:`debugpanel crawl`
      *  ``debugpanel cr``
      *  cause nodes to crawl AUs
   *  *  :ref:`debugpanel crawl-plugins`
      *  ``debugpanel cp``
      *  cause nodes to crawl plugins
   *  *  :ref:`debugpanel deep-crawl`
      *  ``debugpanel dc``
      *  cause nodes to deeply crawl AUs
   *  *  :ref:`debugpanel disable-indexing`
      *  ``debugpanel di``
      *  cause nodes to disable metadata indexing for AUs
   *  *  :ref:`debugpanel license`
      *  n/a
      *  print the software license and exit
   *  *  :ref:`debugpanel poll`
      *  ``debugpanel po``
      *  cause nodes to poll AUs
   *  *  :ref:`debugpanel reindex-metadata`
      *  ``debugpanel ri``
      *  cause nodes to reindex the metadata of AUs
   *  *  :ref:`debugpanel reload-config`
      *  ``debugpanel rc``
      *  cause nodes to reload their configuration
   *  *  :ref:`debugpanel validate-files`
      *  ``debugpanel vf``
      *  cause nodes to validate the files of AUs
   *  *  :ref:`debugpanel version`
      *  n/a
      *  print the version number and exit

You can see the this synopsis by invoking ``debugpanel --help``:

..  code-block:: text

    Usage: debugpanel [-h]
                      {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf} ...

    Tool to interact with the LOCKSS 1.x DebugPanel servlet

    Commands:
      {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf}
        check-substance     cause nodes to check the substance of AUs
        copyright           print the copyright and exit
        cp                  synonym for: crawl-plugins
        cr                  synonym for: crawl
        crawl               cause nodes to crawl AUs
        crawl-plugins       cause nodes to crawl plugins
        cs                  synonym for: check-substance
        dc                  synonym for: deep-crawl
        deep-crawl          cause nodes to deeply crawl AUs
        di                  synonym for: disable-indexing
        disable-indexing    cause nodes to disable metadata indexing for AUs
        license             print the software license and exit
        po                  synonym for: poll
        poll                cause nodes to poll AUs
        rc                  synonym for: reload-config
        reindex-metadata    cause nodes to reindex the metadata of AUs
        reload-config       cause nodes to reload their configuration
        ri                  synonym for: reindex-metadata
        validate-files      cause nodes to validate the files of AUs
        version             print the version number and exit
        vf                  synonym for: validate-files

    Help:
      -h, --help            show this help message and exit

.. _debugpanel command:

``debugpanel`` Command
======================

The top-level executable alone does not perform any action or default to a given command:

..  code-block:: text

    Usage: debugpanel [-h]
                      {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf} ...
    debugpanel: error: the following arguments are required: {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf}

.. _debugpanel check-substance:

.. _debugpanel cs:

``debugpanel check-substance``
==============================

The ``check-substance`` (or alternatively ``cs``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to check the substance of AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel check-substance [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME]
                                      [-a AUID [AUID ...]] [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool]
                                      [--thread-pool] [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel copyright:

``debugpanel copyright``
========================

The ``copyright`` command displays the copyright notice for |DEBUGPANEL| and exits.

.. _debugpanel crawl:

.. _debugpanel cr:

``debugpanel crawl``
====================

The ``crawl`` (or alternatively ``cr``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to crawl AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel crawl [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME] [-a AUID [AUID ...]]
                            [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool] [--thread-pool]
                            [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel crawl-plugins:

.. _debugpanel cp:

``debugpanel crawl-plugins``
============================

The ``crawl-plugins`` (or alternatively ``cp``) command is one of the :ref:`Debugpanel Node Operations`, used to cause nodes to crawl their plugins. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel crawl-plugins [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME]
                                    [--pool-size POOL_SIZE] [--process-pool] [--thread-pool] [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel deep-crawl:

.. _debugpanel dc:

``debugpanel deep-crawl``
=========================

The ``deep-crawl`` (or alternatively ``dc``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to crawl AUs with depth. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel deep-crawl [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME] [-a AUID [AUID ...]]
                                 [-A AUIDS [AUIDS ...]] [-d DEPTH] [--pool-size POOL_SIZE] [--process-pool] [--thread-pool]
                                 [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      -d, --depth DEPTH     (deep crawl) set crawl depth (default: 123)
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It has a unique option, ``--depth/-d``, which is an strictly positive integer specifying the desired crawl depth.

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel disable-indexing:

.. _debugpanel di:

``debugpanel disable-indexing``
===============================

The ``disable-indexing`` (or alternatively ``di``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to disable metadata indexing of AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel disable-indexing [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME]
                                       [-a AUID [AUID ...]] [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool]
                                       [--thread-pool] [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel license:

``debugpanel license``
======================

The ``license`` command displays the license terms for |DEBUGPANEL| and exits.

.. _debugpanel poll:

.. _debugpanel po:

``debugpanel poll``
===================

The ``poll`` (or alternatively ``po``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to poll AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel poll [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME] [-a AUID [AUID ...]]
                           [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool] [--thread-pool]
                           [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel reindex-metadata:

.. _debugpanel ri:

``debugpanel reindex-metadata``
===============================

The ``reindex-metadata`` command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to reindex the metadata of AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel reindex-metadata [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME]
                                       [-a AUID [AUID ...]] [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool]
                                       [--thread-pool] [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel reload-config:

.. _debugpanel rc:

``debugpanel reload-config``
============================

The ``reload-config`` (or alternatively ``rc``) command is one of the :ref:`Debugpanel Node Operations`, used to cause nodes to reload their configuration. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel reload-config [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME]
                                    [--pool-size POOL_SIZE] [--process-pool] [--thread-pool] [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel validate-files:

.. _debugpanel vf:

``debugpanel validate-files``
=============================

The ``validate-files`` (or alternatively ``vf``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to reindex the metadata of AUs. It has its own |HELP| option:

..  code-block:: text

    Usage: debugpanel validate-files [-h] [-n NODE [NODE ...]] [-N NODES [NODES ...]] [-p PASSWORD] [-u USERNAME] [-a AUID [AUID ...]]
                                     [-A AUIDS [AUIDS ...]] [--pool-size POOL_SIZE] [--process-pool] [--thread-pool]
                                     [--output-format OUTPUT_FORMAT]

    Optional Arguments:
      -n, --node NODE [NODE ...]
                            (nodes) add one or more nodes to the set of nodes to process (default: [])
      -N, --nodes NODES [NODES ...]
                            (nodes) add the nodes listed in one or more files to the set of nodes to process (default: [])
      -p, --password PASSWORD
                            (nodes) UI password; interactive prompt if not specified (default: None)
      -u, --username USERNAME
                            (nodes) UI username; interactive prompt if not unspecified (default: None)
      -a, --auid AUID [AUID ...]
                            (AUIDs) add one or more AUIDs to the set of AUIDs to process (default: [])
      -A, --auids AUIDS [AUIDS ...]
                            (AUIDs) add the AUIDs listed in one or more files to the set of AUIDs to process (default: [])
      --pool-size POOL_SIZE
                            (job pool) set the job pool size (default: None)
      --process-pool        (job pool) use a process pool (default: False)
      --thread-pool         (job pool) use a thread pool (default: False)
      --output-format OUTPUT_FORMAT
                            set the output format; choices: asciidoc, double_grid, double_outline, fancy_grid, fancy_outline, github,
                            grid, heavy_grid, heavy_outline, html, jira, latex, latex_booktabs, latex_longtable, latex_raw, mediawiki,
                            mixed_grid, mixed_outline, moinmoin, orgtbl, outline, pipe, plain, presto, pretty, psql, rounded_grid,
                            rounded_outline, rst, simple, simple_grid, simple_outline, textile, tsv, unsafehtml, youtrack (default:
                            simple)

    Help:
      -h, --help            show this help message and exit

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _debugpanel version:

``debugpanel version``
======================

The ``version`` command displays the version number of |DEBUGPANEL| and exits.

-----------------------
Debugpanel Node Options
-----------------------

.. note::

   As of version 0.8.0, bare arguments are no longer allowed and treated as nodes; all nodes must be listed via the :ref:`Debugpanel Node Options` |NODE| and |NODES|.

Commands for :ref:`Debugpanel Node Operations` expect one or more node references in ``HOST:PORT`` format, for instance ``lockss.myuniversity.edu:8081``. The set of nodes to process is derived from:

*  The nodes listed as |NODE| options. Each |NODE| option accepts one or more node references.

*  The nodes found in the files listed as |NODES| options. Each |NODES| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --node with one argument
   debugpanel reload-config --node node1:8081 --node node2:8081 --node node3:8081 ... --thread-pool ...

   # Same, with --node abbreviated to -n
   debugpanel reload-config -n node1:8081 -n node2:8081 -n node3:8081 ... --thread-pool ...

   # Each --node can have more than one argument
   debugpanel reload-config --node node1:8081 node2:8081 node3:8081 ... --thread-pool ...

   # Same, with --node abbreviated to -n
   debugpanel reload-config -n node1:8081 node2:8081 node3:8081 ... --thread-pool ...

   # --node with a single argument can also use an equals sign
   debugpanel reload-config --node=node1:8081 ... --thread-pool ...

   # Each --nodes with one argument
   debugpanel reload-config --nodes list1.txt --nodes list2.txt --nodes list3.txt ... --thread-pool ...

   # Same, with --nodes abbreviated to -N
   debugpanel reload-config -N list1.txt -N list2.txt -N list3.txt ... --thread-pool ...

   # Each --nodes can have more than one argument
   debugpanel reload-config --nodes list1.txt list2.txt list3.txt ... --thread-pool ...

   # Same, with --nodes abbreviated to -N
   debugpanel reload-config -N list1.txt list2.txt list3.txt ... --thread-pool ...

   # --nodes with a single argument can also use an equals sign
   debugpanel reload-config --nodes=list1.txt... --thread-pool ...

-----------------------
Debugpanel AUID Options
-----------------------

In addition to :ref:`Debugpanel Node Options`, commands for :ref:`Debugpanel AU Operations` expect one or more AUIDs. The set of AUIDs to process is derived from:

*  The AUIDs listed as |AUID| options. Each |AUID| option accepts one or more AUID.

*  The AUIDs found in the files listed as |AUIDS| options. Each |AUIDS| option accepts one or more file paths.

Examples:

.. code-block:: shell

   # Each --auid with one argument
   debugpanel poll ... --auid auid1 --auids auid2 --auid auid3 ... --thread-pool ...

   # Same, with --auid abbreviated to -a
   debugpanel poll ... -a auid1 -a auid2 -a auid3 ... --thread-pool ...

   # Each --auid can have more than one argument
   debugpanel poll ... --auid auid1 auid2 auid3 ... --thread-pool ...

   # Same, with --auid abbreviated to -a
   debugpanel poll ... -a auid1 auid2 auid3 ... --thread-pool ...

   # --auid with a single argument can also use an equals sign
   debugpanel poll ... --auid=auid1 ... --thread-pool ...

   # Each --auids with one argument
   debugpanel poll ... --auids list1.txt --auids list2.txt --auid list3.txt ... --thread-pool ...

   # Same, with --auids abbreviated to -A
   debugpanel poll ... -A list1.txt -A list2.txt -A list3.txt ... --thread-pool ...

   # Each --auids can have more than one argument
   debugpanel poll ... --auids list1.txt list2.txt list3.txt ... --thread-pool ...

   # Same, with --auids abbreviated to -A
   debugpanel poll ... -A list1.txt list2.txt list3.txt ... --thread-pool ...

   # --auids with a single argument can also use an equals sign
   debugpanel poll ... --auids=list1.txt ... --thread-pool ...

--------------------------------
Debugpanel Output Format Options
--------------------------------

|DEBUGPANEL|'s tabular output is performed by the `tabulate <https://pypi.org/project/tabulate>`_ library through the ``--output-format`` option. See `its README file <https://github.com/astanin/python-tabulate#table-format>`_ or the |HELP| message of any |DEBUGPANEL| node or AU command for a list of the various output formats available. The **default** is ``simple``. The option accepts a single argument, with or without an equals sign:

.. code-block:: shell

   # With an equals sign
   debugpanel ... --output-format=outline

   # Without an equals sign
   debugpanel ... --output-format outline

.. tip::

   The output format ``tsv`` produces tab-separated output, which can be more easily processed by other command line tools or imported into a spreadsheet.

---------------------------
Debugpanel Job Pool Options
---------------------------

|DEBUGPANEL| performs multiple operations in parallel, contacting multiple nodes and/or working on multiple AU requests per node, using a thread pool (``--thread-pool``) or a process pool (``--process-pool``). If neither is specified, by default a thread pool is used. You can change the size of the job pool with the ``--pool-size`` option, which accepts a nonzero integer. Note that the underlying implementation may limit the number of threads or processes despite a larger number requested at the command line. The default value depends on the system's CPU characteristics (represented in this document as "N"). Using ``--thread-pool --pool-size=1`` approximates no parallel processing.
