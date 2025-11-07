==================
Installing Turtles
==================

.. include:: subst.rst

---------------------
Turtles Prerequisites
---------------------

|TURTLES| requires Python 3.9 or greater [#fn-python-version]_.

:ref:`Turtles Installation` is typically done with |PIPX|, which you may need to install [#fn-pipx-version]_:

.. include:: ../pipx-installation.rst

.. _Maven Plugin Set Builder Prerequisites:

.. rubric:: Maven Plugin Set Builder Prerequisites

The Maven Plugin Set Builder is the most common plugin set builder type, likely needed by any |TURTLES| application.

The Maven Plugin Set Builder has these additional prerequisites:

*  `Java <https://www.oracle.com/java/>`_ Development Kit (JDK) 17

*  `Apache Maven <https://maven.apache.org/>`_

.. _Other Turtles Prerequisites:

.. rubric:: Other Turtles Prerequisites

.. dropdown:: Legacy Ant Plugin Set Builder Prerequisites

   The Legacy Ant Plugin Set Builder (now **deprecated**), if in use, has these additional prerequisites:

   *  `Java <https://www.oracle.com/java/>`_ Development Kit (JDK) 8

   *  `Apache Ant <https://ant.apache.org/>`_

   *  The ``JAVA_HOME`` environment variable must be set.

.. dropdown:: RCS Plugin Registry Layout Prerequisites

   The RCS Plugin Registry Layout, if in use, has these additional prerequisites:

   *  `GNU RCS <https://www.gnu.org/software/rcs/>`_

--------------------
Turtles Installation
--------------------

|TURTLES| is available from the `Python Package Index <https://pypi.org/>`_ (PyPI) as ``lockss-turtles`` (https://pypi.org/project/lockss-turtles).

To install |TURTLES|, we recommend using |PIPX| version 1.5.0 or greater [#fn-pipx-version]_. Run this command as ``root``:

.. code-block:: shell

   pipx install --global lockss-turtles

.. tip::

   If you are running an older version of |PIPX| [#fn-pipx-version]_, each user needing to run |TURTLES| will have to install it individually by running this non-``root`` command:

   .. code-block:: shell

      pipx install lockss-turtles

The installation process adds a :command:`turtles` :doc:`command line tool <using>` and a ``lockss.turtles`` :doc:`Python library <api>`. You can check at the command line that the installation is functional by running ``turtles version`` or ``turtles --help``.

----

.. rubric:: Footnotes

.. [#fn-python-version]

   Type ``python --version`` (or ``python -V``) to see if Python is installed, and if so, which version.

.. [#fn-pipx-version]

   Type ``pipx --version`` to see if |PIPX| is installed, and if so, which version.
