==================
Installing Turtles
==================

.. include:: subst.rst

|TURTLES| is available from the `Python Package Index <https://pypi.org/>`_ (PyPI) as ``lockss-turtles`` (https://pypi.org/project/lockss-turtles).

*  To install |TURTLES| in your own non-virtual environment, we recommend using |PIPX|:

   .. code-block:: shell

      pipx install lockss-turtles

*  To install |TURTLES| globally for every user, you can use |PIPX| as ``root`` with the ``--global`` flag (provided you are running a recent enough |PIPX|):

   .. code-block:: shell

      pipx install --global lockss-turtles

*  To install |TURTLES| in a Python virtual environment, simply use :program:`pip`:

   .. code-block:: shell

      pip install lockss-turtles

   or create a dependency on the ``lockss-turtles`` package.

The installation process adds a :command:`turtles` :doc:`command line tool <using>` and a ``lockss.turtles`` :doc:`Python library <api>`. You can check at the command line that the installation is functional by running ``turtles version`` or ``turtles --help``.
