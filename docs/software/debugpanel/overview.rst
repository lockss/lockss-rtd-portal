===================
Debugpanel Overview
===================

.. include:: subst.rst

--------------------------
Debugpanel Node Operations
--------------------------

Some operations operate on one or more nodes.

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Crawl plugins
      *  :ref:`debugpanel crawl-plugins`
      *  :py:func:`lockss.debugpanel.crawl_plugins`
   *  *  Reload node configuration
      *  :ref:`debugpanel reload-config`
      *  :py:func:`lockss.debugpanel.reload_config`

------------------------
Debugpanel AU Operations
------------------------

Some operations operate on one or more AUs on one or more nodes.

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Check substance of AUs
      *  :ref:`debugpanel check-substance`
      *  :py:func:`lockss.debugpanel.check_substance`
   *  *  Crawl AUs
      *  :ref:`debugpanel crawl`
      *  :py:func:`lockss.debugpanel.crawl`
   *  *  Crawl AUs with depth
      *  :ref:`debugpanel deep-crawl`
      *  :py:func:`lockss.debugpanel.deep_crawl`
   *  *  Disable metadata indexing of AUs
      *  :ref:`debugpanel disable-indexing`
      *  :py:func:`lockss.debugpanel.disable_indexing`
   *  *  Poll
      *  :ref:`debugpanel poll`
      *  :py:func:`lockss.debugpanel.poll`
   *  *  Reindex AU metadata
      *  :ref:`debugpanel reindex-metadata`
      *  :py:func:`lockss.debugpanel.reindex_metadata`
   *  *  Validate AU files
      *  :ref:`debugpanel validate-files`
      *  :py:func:`lockss.debugpanel.validate_files`

---------------------------
Other Debugpanel Operations
---------------------------

Other operations include:

.. list-table::
   :header-rows: 1

   *  *  Operation
      *  Command Line
      *  API
   *  *  Copyright statement
      *  :ref:`debugpanel copyright`
      *  :py:const:`lockss.debugpanel.__copyright__`
   *  *  Software license
      *  :ref:`debugpanel license`
      *  :py:const:`lockss.debugpanel.__license__`
   *  *  Version number
      *  :ref:`debugpanel version`
      *  :py:const:`lockss.debugpanel.__version__`
