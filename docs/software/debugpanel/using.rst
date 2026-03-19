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

|DEBUGPANEL| commands are in the subcommand style of programs like :command:`git`, :command:`dnf`/:command:`yum`, :command:`apt`/:command:`apt-get`, and the like.

The available commands are:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command
      *  Abbreviation
   *  *  Cause nodes to check the substance of AUs
      *  :ref:`debugpanel check-substance`
      *  :ref:`debugpanel cs <debugpanel check-substance>`
   *  *  Print the copyright and exit
      *  :ref:`debugpanel copyright`
      *  
   *  *  Cause nodes to crawl AUs
      *  :ref:`debugpanel crawl`
      *  :ref:`debugpanel cr <debugpanel crawl>`
   *  *  Cause nodes to crawl plugins
      *  :ref:`debugpanel crawl-plugins`
      *  :ref:`debugpanel cp <debugpanel crawl-plugins>`
   *  *  Cause nodes to deeply crawl AUs
      *  :ref:`debugpanel deep-crawl`
      *  :ref:`debugpanel dc <debugpanel deep-crawl>`
   *  *  Cause nodes to disable metadata indexing for AUs
      *  :ref:`debugpanel disable-indexing`
      *  :ref:`debugpanel di <debugpanel disable-indexing>`
   *  *  Print the software license and exit
      *  :ref:`debugpanel license`
      *  
   *  *  Cause nodes to poll AUs
      *  :ref:`debugpanel poll`
      *  :ref:`debugpanel po <debugpanel poll>`
   *  *  Cause nodes to reindex the metadata of AUs
      *  :ref:`debugpanel reindex-metadata`
      *  :ref:`debugpanel ri <debugpanel reindex-metadata>`
   *  *  cause nodes to reload their configuration
      *  :ref:`debugpanel reload-config`
      *  :ref:`debugpanel rc <debugpanel reload-config>`
   *  *  Display the subcommand tree and exit
      *  :ref:`debugpanel tree`
      *  
   *  *  cause nodes to validate the files of AUs
      *  :ref:`debugpanel validate-files`
      *  :ref:`debugpanel vf <debugpanel validate-files>`
   *  *  Print the version number and exit
      *  :ref:`debugpanel version`
      *  

You can see the synopsis by invoking ``debugpanel --help``:

.. click:run::

   invoke(_debugpanel, args=['--help'])

.. _debugpanel command:

``debugpanel`` Command
======================

The top-level `debugpanel``command, alone, defaults to ``debugpanel --help``.

.. note::

   The |COLOR| and |SHOW_PARAMS| options attach to the top-level ``debugpanel`` command only, not to a subcommand that may also be specified. For example, this is not valid:

   .. click:run::

      invoke(_debugpanel, args=['reload-config', '--help', '--no-color'])

   Instead, you should invoke ``debugpanel --no-color reload-config --help``.

.. _debugpanel check-substance:

.. _debugpanel cs:

``debugpanel check-substance``
==============================

The ``debugpanel check-substance`` (or alternatively ``debugpanel cs``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to check the substance of AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['check-substance', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel copyright:

``debugpanel copyright``
========================

The ``debugpanel copyright`` command displays the copyright notice for |DEBUGPANEL| and exits:

.. click:run::

   invoke(_debugpanel, args=['copyright'])

.. _debugpanel crawl:

.. _debugpanel cr:

``debugpanel crawl``
====================

The ``debugpanel crawl`` (or alternatively ``debugpanel cr``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to crawl AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['crawl', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel crawl-plugins:

.. _debugpanel cp:

``debugpanel crawl-plugins``
============================

The ``debugpanel crawl-plugins`` (or alternatively ``debugpanel cp``) command is one of the :ref:`Debugpanel Node Operations`, used to cause nodes to crawl their plugins. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['crawl-plugins', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel deep-crawl:

.. _debugpanel dc:

``debugpanel deep-crawl``
=========================

The ``debugpanel deep-crawl`` (or alternatively ``debugpanel dc``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to crawl AUs with depth. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['deep-crawl', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It has a unique option, ``--depth/-d``, which is an strictly positive integer specifying the desired crawl depth.

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel disable-indexing:

.. _debugpanel di:

``debugpanel disable-indexing``
===============================

The ``debugpanel disable-indexing`` (or alternatively ``debugpanel di``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to disable metadata indexing of AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['disable-indexing', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel license:

``debugpanel license``
======================

The ``debugpanel license`` command displays the license terms for |DEBUGPANEL| and exits:

.. click:run::

   invoke(_debugpanel, args=['license'])

.. _debugpanel poll:

.. _debugpanel po:

``debugpanel poll``
===================

The ``debugpanel poll`` (or alternatively ``debugpanel po``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to poll AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['poll', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel reindex-metadata:

.. _debugpanel ri:

``debugpanel reindex-metadata``
===============================

The ``debugpanel reindex-metadata`` (or alternatively ``debugpanel ri``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to reindex the metadata of AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['reindex-metadata', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel reload-config:

.. _debugpanel rc:

``debugpanel reload-config``
============================

The ``debugpanel reload-config`` (or alternatively ``debugpanel rc``) command is one of the :ref:`Debugpanel Node Operations`, used to cause nodes to reload their configuration. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['reload-config', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel tree:

``debugpanel tree``
===================

The ``debugpanel tree`` command displays the subcommand tree for |DEBUGPANEL|:

.. click:run::

   invoke(_debugpanel, args=['tree'])

.. _debugpanel validate-files:

.. _debugpanel vf:

``debugpanel validate-files``
=============================

The ``debugpanel validate-files`` (or alternatively ``debugpanel vf``) command is one of the :ref:`Debugpanel AU Operations`, used to cause nodes to reindex the metadata of AUs. It has its own |HELP| option:

.. click:run::

   invoke(_debugpanel, args=['validate-files', '--help'])

The command requires:

*  One or more nodes, from the :ref:`Debugpanel Node Options` (|NODE|, |NODES|).

*  One or more AUIDs, from the :ref:`Debugpanel AUID Options` (|AUID|, |AUIDS|).

It also accepts :ref:`Debugpanel Output Format Options` (|TABLE_FORMAT|, |HEADINGS|, |PROGRESS|) and :ref:`Debugpanel Job Pool Options` (|POOL_TYPE|, |POOL_SIZE|).

.. _debugpanel version:

``debugpanel version``
======================

The ``debugpanel version`` command displays the version number of |DEBUGPANEL| and exits:

.. click:run::

   invoke(_debugpanel, args=['version'])

-----------------------
Debugpanel Node Options
-----------------------

.. note::

   As of version 0.9.0, |NODE| and |NODES| options only accept one argument at a time each, rather than one or more each.

Commands for :ref:`Debugpanel Node Operations` expect one or more node references in ``HOST:PORT`` format, for instance ``lockss.myuniversity.edu:8081``. The set of nodes to process is derived from:

*  The nodes listed as |NODE| options. Each |NODE| option accepts one node reference. The long option ``--node`` and its argument can optionally be joined by an equals sign.

*  The node references found in the files listed as |NODES| options. Each |NODES| option accepts one file paths. The long option ``--nodes`` and its argument can optionally be joined by an equals sign.

Examples:

.. code-block:: shell

   # --node without an equals sign
   debugpanel reload-config --node node1:8081 --node node2:8081 --node node3:8081 ...

   # Same, with --node abbreviated to -n
   debugpanel reload-config -n node1:8081 -n node2:8081 -n node3:8081 ...

   # --node with an equals sign
   debugpanel reload-config --node=node1:8081 ...

   # --nodes without an equals sign
   debugpanel reload-config --nodes list1.txt --nodes list2.txt --nodes list3.txt ...

   # Same, with --nodes abbreviated to -N
   debugpanel reload-config -N list1.txt -N list2.txt -N list3.txt ...

   # --nodes with an equals sign
   debugpanel reload-config --nodes=list1.txt ...

-----------------------
Debugpanel AUID Options
-----------------------

In addition to :ref:`Debugpanel Node Options`, commands for :ref:`Debugpanel AU Operations` expect one or more AUIDs. The set of AUIDs to process is derived from:

*  The AUIDs listed as |AUID| options. Each |AUID| option accepts one. The long option ``--auid`` and its argument can optionally be joined by an equals sign.

*  The AUIDs found in the files listed as |AUIDS| options. Each |AUIDS| option accepts one file path. The long option ``--auids`` and its argument can optionally be joined by an equals sign.

Examples:

.. code-block:: shell

   # --auid without an equals sign
   debugpanel poll ... --auid auid1 --auids auid2 --auid auid3 ...

   # Same, with --auid abbreviated to -a
   debugpanel poll ... -a auid1 -a auid2 -a auid3 ...

   # --auid with an equals sign
   debugpanel poll ... --auid=auid1 ...

   # --auids without an equals sign
   debugpanel poll ... --auids list1.txt --auids list2.txt --auid list3.txt ...

   # Same, with --auids abbreviated to -A
   debugpanel poll ... -A list1.txt -A list2.txt -A list3.txt ...

   # --auids with an equals sign
   debugpanel poll ... --auids=list1.txt ...

--------------------------------
Debugpanel Output Format Options
--------------------------------

.. note::

   As of version 0.9.0, ``--output-format`` has been renamed to |TABLE_FORMAT|.

|DEBUGPANEL|'s tabular output is performed by the `Click Extra <https://kdeldycke.github.io/click-extra/index.html>`_ library, via the |TABLE_FORMAT| and |HEADINGS| options. See `its documentation <https://kdeldycke.github.io/click-extra/table.html#table-formats>`_ or the |HELP| message of any |DEBUGPANEL| node or AU command for a list of the various output formats available in the |TABLE_FORMAT| option. The default value is ``simple``. This option accepts a single argument, with or without an equals sign:

.. code-block:: shell

   # Without an equals sign
   debugpanel ... --table-format outline

   # With an equals sign
   debugpanel ... --table-format=outline

The |HEADINGS| options control whether or not column headings are displayed, respectively. The default is ``--headings``.

The |PROGRESS| options control whether or not a progress bar of individual tasks is displayed, respectively. The default is ``--progress``.

---------------------------
Debugpanel Job Pool Options
---------------------------

.. note::

   As of version 0.9.0, ``--process-pool`` and ``thread-pool`` are deprecated in favor of ``--pool-type=process-pool`` and ``--pool-type=thread-pool`` respectively.

|DEBUGPANEL| performs multiple operations in parallel, contacting multiple nodes and/or working on multiple AU requests per node, using a thread pool (``--pool-type=thread-pool``) or a process pool (``--pool-type=process-pool``). If neither is specified, by default a thread pool is used. You can change the size of the job pool with the ``--pool-size`` option, which accepts a nonzero integer. Note that the underlying implementation may limit the number of threads or processes despite a larger number requested at the command line. The default value depends on the system's CPU characteristics (represented in this document as "N"). Using ``--pool-type=thread-pool --pool-size=1`` approximates no parallel processing.
