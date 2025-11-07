=====================
Installing Debugpanel
=====================

.. include:: subst.rst

------------------------
Debugpanel Prerequisites
------------------------

|DEBUGPANEL| requires Python 3.9 or greater [#fn-python-version]_.

:ref:`Debugpanel Installation` is typically done with |PIPX|, which you may need to install [#fn-pipx-version]_:

.. include:: ../pipx-installation.rst

-----------------------
Debugpanel Installation
-----------------------

|DEBUGPANEL| is available from the `Python Package Index <https://pypi.org/>`_ (PyPI) as ``lockss-debugpanel`` (https://pypi.org/project/lockss-debugpanel).

To install |DEBUGPANEL|, we recommend using |PIPX| version 1.5.0 or greater [#fn-pipx-version]_. Run this command as ``root``:

.. code-block:: shell

   pipx install --global lockss-debugpanel

.. tip::

   If you are running an older version of |PIPX| [#fn-pipx-version]_, each user needing to run |DEBUGPANEL| will have to install it individually by running this non-``root`` command:

   .. code-block:: shell

      pipx install lockss-debugpanel

The installation process adds a :command:`debugpanel` :doc:`command line tool <using>` and a ``lockss.debugpanel`` :doc:`Python library <api>`. You can check at the command line that the installation is functional by running ``debugpanel version`` or ``debugpanel --help``.

----

.. rubric:: Footnotes

.. [#fn-python-version]

   Type ``python --version`` (or ``python -V``) to see if Python is installed, and if so, which version.

.. [#fn-pipx-version]

   Type ``pipx --version`` to see if |PIPX| is installed, and if so, which version.
