=====================
Installing Debugpanel
=====================

.. include:: subst.rst

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
