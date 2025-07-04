==========
Debugpanel
==========

.. |RELEASE| replace:: 0.8.0
.. |RELEASE_DATE| replace:: 2025-07-01

.. |DEBUGPANEL| replace:: :program:`Debugpanel`
.. |PIPX| replace:: :program:`pipx`

.. |AUID| replace:: ``--auid/-a``
.. |AUIDS| replace:: ``--auids/-A``
.. |HELP| replace:: ``--help/-h``
.. |NODE| replace:: ``--node/-n``
.. |NODES| replace:: ``--nodes/-N``

.. image:: https://assets.lockss.org/images/logos/debugpanel/debugpanel_128x128.png
   :alt: Debugpanel logo
   :align: right

|DEBUGPANEL| is a command line tool and Python library to interact with the LOCKSS 1.x DebugPanel servlet.

:Latest release: |RELEASE| (|RELEASE_DATE|)
:Release notes: `CHANGELOG.rst <https://github.com/lockss/lockss-debugpanel/blob/main/CHANGELOG.rst>`_
:License: `LICENSE <https://github.com/lockss/lockss-debugpanel/blob/main/LICENSE>`_

----------------------
Debugpanel Quick Start
----------------------

.. code-block:: shell

   # Install with pipx
   pipx install lockss-debugpanel

   # Verify installation and discover all the commands
   debugpanel --help

   # Reload config on lockss1.example.edu:8081
   debugpanel reload-config -n lockss1.example.edu:8081

   # Crawl AUIDs from list.txt on lockss1.example.edu:8081 and lockss2.example.edu:8081
   # ...First alternative: each node gets a -n
   debugpanel crawl -A list.txt -n lockss1.example.edu:8081 -n lockss2.example.edu:8081

   # ...Second alternative: each -n can have more than argument
   debugpanel crawl -A list.txt -n lockss1.example.edu:8081 lockss2.example.edu:8081

---------------------
Installing Debugpanel
---------------------

|DEBUGPANEL| is available from the `Python Package Index <https://pypi.org/>`_ (PyPI) as ``lockss-debugpanel`` (https://pypi.org/project/lockss-debugpanel).

*  To install |DEBUGPANEL| in your own non-virtual environment, we recommend using |PIPX|:

   .. code-block:: shell

      pipx install lockss-debugpanel

*  To install |DEBUGPANEL| globally for every user, you can use |PIPX| as ``root`` with the ``--global`` flag (provided you are running a recent enough |PIPX|):

   .. code-block:: shell

      pipx install --global lockss-debugpanel

*  To install |DEBUGPANEL| in a Python virtual environment, simply use :program:`pip`:

   .. code-block:: shell

      pip install lockss-debugpanel

   or create a dependency on the ``lockss-debugpanel`` package.

The installation process adds a :command:`debugpanel` :ref:`command line tool <Using Debugpanel>` and a ``lockss.debugpanel`` :ref:`Python library <Using Debugpanel as a Library>`. You can check at the command line that the installation is functional by running ``debugpanel version`` or ``debugpanel --help``.

-------------------
Debugpanel Overview
-------------------

Debugpanel Node Operations
==========================

Some operations operate on one or more nodes.

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Crawl plugins
      *  `debugpanel crawl-plugins`_
      *  :py:func:`lockss.debugpanel.crawl_plugins`
   *  *  Reload node configuration
      *  `debugpanel reload-config`_
      *  :py:func:`lockss.debugpanel.reload_config`

Debugpanel AU Operations
========================

Some operations operate on one or more AUs on one or more nodes.

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Check substance of AUs
      *  `debugpanel check-substance`_
      *  :py:func:`lockss.debugpanel.check_substance`
   *  *  Crawl AUs
      *  `debugpanel crawl`_
      *  :py:func:`lockss.debugpanel.crawl`
   *  *  Crawl AUs with depth
      *  `debugpanel deep-crawl`_
      *  :py:func:`lockss.debugpanel.deep_crawl`
   *  *  Disable metadata indexing of AUs
      *  `debugpanel disable-indexing`_
      *  :py:func:`lockss.debugpanel.disable_indexing`
   *  *  Poll
      *  `debugpanel poll`_
      *  :py:func:`lockss.debugpanel.poll`
   *  *  Reindex AU metadata
      *  `debugpanel reindex-metadata`_
      *  :py:func:`lockss.debugpanel.reindex_metadata`
   *  *  Validate AU files
      *  `debugpanel validate-files`_
      *  :py:func:`lockss.debugpanel.validate_files`

Other Debugpanel Operations
===========================

Other operations include:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Copyright statement
      *  `debugpanel copyright`_
      *  :py:const:`lockss.debugpanel.__copyright__`
   *  *  Software license
      *  `debugpanel license`_
      *  :py:const:`lockss.debugpanel.__license__`
   *  *  Version number
      *  `debugpanel version`_
      *  :py:const:`lockss.debugpanel.__version__`

----------------
Using Debugpanel
----------------

|DEBUGPANEL| is invoked at the command line as:

.. code-block:: shell

   debugpanel

or as a Python module:

.. code-block:: shell

   python -m lockss.debugpanel

Help messages and this document use ``debugpanel`` throughout, but the two invocation styles are interchangeable.

Synopsis of Debugpanel
======================

.. note::

   As of version 0.8.0, bare arguments are no longer allowed and treated as nodes; all nodes must be listed via the :ref:`Debugpanel Node Options` |NODE| and |NODES|.

.. note::

   As of version 0.8.0, the ``debugpanel usage`` command no longer exists.

:ref:`Debugpanel Commands` are in the subcommand style of programs like :command:`git`, :command:`dnf`/:command:`yum`, :command:`apt`/:command:`apt-get`, and the like. You can see the list of available commands by invoking ``debugpanel --help``:

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

Debugpanel Node Options
=======================

.. note::

   As of version 0.8.0, bare arguments are no longer allowed and treated as nodes; all nodes must be listed via the :ref:`Debugpanel Node Options` |NODE| and |NODES|.

Commands for :ref:`Debugpanel Node Operations` expect one or more node references in ``HOST:PORT`` format, for instance ``lockss.myuniversity.edu:8081``. The set of nodes to process is derived from:

*  The nodes listed as |NODE| options.

*  The nodes found in the files listed as |NODES| options.

Examples:

.. code-block:: shell

   debugpanel reload-config --node node1:8081 --node node2:8081 --node node3:8081 ... --thread-pool ...

   debugpanel reload-config -n node1:8081 -n node2:8081 -n node3:8081 ... --thread-pool ...

   debugpanel reload-config --node node1:8081 node2:8081 node3:8081 ... --thread-pool ...

   debugpanel reload-config -n node1:8081 node2:8081 node3:8081 ... --thread-pool ...

   debugpanel reload-config --nodes list1.txt --nodes list2.txt --nodes list3.txt ... --thread-pool ...

   debugpanel reload-config -N list1.txt -N list2.txt -N list3.txt ... --thread-pool ...

   debugpanel reload-config --nodes list1.txt list2.txt list3.txt ... --thread-pool ...

   debugpanel reload-config -N list1.txt list2.txt list3.txt ... --thread-pool ...

Debugpanel AUID Options
=======================

In addition to :ref:`Debugpanel Node Options`, commands for :ref:`Debugpanel AU Operations` expect one or more AUIDs. The set of AUIDs to process is derived from:

*  The AUIDs listed as |AUID| options.

*  The AUIDs found in the files listed as |AUIDS| options.

Examples:

.. code-block:: shell

   debugpanel poll ... --auid auid1 --auids auid2 --auid auid3 ... --thread-pool ...

   debugpanel poll ... -a auid1 -a auid2 -a auid3 ... --thread-pool ...

   debugpanel poll ... --auid auid1 auid2 auid3 ... --thread-pool ...

   debugpanel poll ... -a auid1 auid2 auid3 ... --thread-pool ...

   debugpanel poll ... --auids list1.txt --auids list2.txt --auid list3.txt ... --thread-pool ...

   debugpanel poll ... -A list1.txt -A list2.txt -A list3.txt ... --thread-pool ...

   debugpanel poll ... --auids list1.txt list2.txt list3.txt ... --thread-pool ...

   debugpanel poll ... -A list1.txt list2.txt list3.txt ... --thread-pool ...

Debugpanel Commands
===================

The available commands are:

.. list-table::
   :header-rows: 1

   *  *  Command
      *  Abbreviation
      *  Purpose
   *  *  `debugpanel check-substance`_
      *  ``debugpanel cs``
      *  cause nodes to check the substance of AUs
   *  *  `debugpanel copyright`_
      *  n/a
      *  print the copyright and exit
   *  *  `debugpanel crawl`_
      *  ``debugpanel cr``
      *  cause nodes to crawl AUs
   *  *  `debugpanel crawl-plugins`_
      *  ``debugpanel cp``
      *  cause nodes to crawl plugins
   *  *  `debugpanel deep-crawl`_
      *  ``debugpanel dc``
      *  cause nodes to deeply crawl AUs
   *  *  `debugpanel disable-indexing`_
      *  ``debugpanel di``
      *  cause nodes to disable metadata indexing for AUs
   *  *  `debugpanel license`_
      *  n/a
      *  print the software license and exit
   *  *  `debugpanel poll`_
      *  ``debugpanel po``
      *  cause nodes to poll AUs
   *  *  `debugpanel reindex-metadata`_
      *  ``debugpanel ri``
      *  cause nodes to reindex the metadata of AUs
   *  *  `debugpanel reload-config`_
      *  ``debugpanel rc``
      *  cause nodes to reload their configuration
   *  *  `debugpanel validate-files`_
      *  ``debugpanel vf``
      *  cause nodes to validate the files of AUs
   *  *  `debugpanel version`_
      *  n/a
      *  print the version number and exit

``debugpanel`` Command
----------------------

The top-level executable alone does not perform any action or default to a given command:

..  code-block:: text

    Usage: debugpanel [-h]
                      {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf} ...
    debugpanel: error: the following arguments are required: {check-substance,copyright,cp,cr,crawl,crawl-plugins,cs,dc,deep-crawl,di,disable-indexing,license,po,poll,rc,reindex-metadata,reload-config,ri,validate-files,version,vf}

``debugpanel check-substance``
------------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel copyright``
------------------------

The ``copyright`` command displays the copyright notice for Debugpanel and exits.


``debugpanel crawl``
--------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel crawl-plugins``
----------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel deep-crawl``
-------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It has a unique option, ``--depth/-d``, which is an strictly positive integer specifying the desired crawl depth.

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel disable-indexing``
-------------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel license``
----------------------

The ``license`` command displays the license terms for Debugpanel and exits.

``debugpanel poll``
-------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel reindex-metadata``
-------------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel reload-config``
----------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

.. _validate-files:

``debugpanel validate-files``
-----------------------------

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

The command needs:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE| options, |NODES| options).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID| options, |AUIDS| options).

It also accepts :ref:`Debugpanel Output Format Options` and :ref:`Debugpanel Job Pool Options`.

``debugpanel version``
----------------------

The ``version`` command displays the version number of Debugpanel and exits.

Debugpanel Output Format Options
--------------------------------

|DEBUGPANEL|'s tabular output is performed by the `tabulate <https://pypi.org/project/tabulate>`_ library through the ``--output-format`` option. See its PyPI page for a visual reference of the various output formats available. The **default** is ``simple``.

Debugpanel Job Pool Options
---------------------------

|DEBUGPANEL| performs multiple operations in parallel, contacting multiple nodes and/or working on multiple AU requests per node, using a thread pool (``--thread-pool``) or a process pool (``--process-pool``). If neither is specified, by default a thread pool is used. You can change the size of the job pool with the ``--pool-size`` option, which accepts a nonzero integer. Note that the underlying implementation may limit the number of threads or processes despite a larger number requested at the command line. The default value depends on the system's CPU characteristics (represented in this document as "N"). Using ``--thread-pool --pool-size=1`` approximates no parallel processing.

-----------------------------
Using Debugpanel as a Library
-----------------------------

You can use |DEBUGPANEL| as a Python library. See the :ref:`Debugpanel API Reference` for details.

The :py:class:`lockss.debugpanel.Node` class can create a node object from a node reference (a string like ``host:8081``, ``http://host:8081``, ``http://host:8081/``, ``https://host:8081``, ``https://host:8081/``; no protocol defaults to ``http://``), a username, and a password.

.. note::

   The :py:func:`lockss.debugpanel.node` function is deprecated and will be removed in a future release.

This node object can be used as the argument to :py:func:`lockss.debugpanel.crawl_plugins` or :py:func:`lockss.debugpanel.reload_config`.

It can also be used as the first argument to :py:func:`lockss.debugpanel.check_substance`, :py:func:`lockss.debugpanel.crawl`, :py:func:`lockss.debugpanel.deep_crawl`, :py:func:`lockss.debugpanel.disable_indexing`, :py:func:`lockss.debugpanel.poll`, :py:func:`lockss.debugpanel.reindex_metadata`, or :py:func:`lockss.debugpanel.validate_files`, together with an AUID string as the second argument.

The :py:func:`lockss.debugpanel.deep_crawl` function has an optional third argument, ``depth``, for the crawl depth (which defaults to :py:const:`lockss.debugpanel.DEFAULT_DEPTH`).

All operations return the modified :py:class:`http.client.HTTPResponse` object from :py:func:`urllib.request.urlopen` (see https://docs.python.org/3.9/library/urllib.request.html#urllib.request.urlopen). A status code of 200 indicates that the request to the node was made successfully (but not much else; for example if there is no such AUID for an AUID operation, nothing happens).

Use of the module is illustrated in this example:

.. code-block:: python

   from getpass import getpass
   from lockss.debugpanel import Node, poll

   hostport: str = '...'
   username: str = input('Username: ')
   password: str = getpass('Password: ')
   node: Node = Node(hostport, username, password)
   auid: str = '...'

   try:
       resp = poll(node, auid)
       if resp.status == 200:
           print('Poll requested (200)')
       else:
           print(f'{resp.reason} ({resp.status})')
   except Exception as exc:
       print(f'Error: {exc!s}')

------------------------
Debugpanel API Reference
------------------------

``lockss.debugpanel``
=====================

.. automodule:: lockss.debugpanel


``lockss.debugpanel.cli``
=========================

.. automodule:: lockss.debugpanel.cli
