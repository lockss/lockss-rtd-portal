-----------------------------
Using Debugpanel as a Library
-----------------------------

.. include:: subst.rst

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
