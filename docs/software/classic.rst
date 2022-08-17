==========================
Classic LOCKSS Development
==========================

.. note::

   This page is under construction.

The code base of the Classic LOCKSS system (version 1.x) is contained in a single Git repository, https://github.com/lockss/lockss-daemon.

-------------
Prerequisites
-------------

To do development work with the Classic LOCKSS system (version 1.x), you will need:

*  `Git <https://git-scm.com/>`_

*  Java 8 Development Kit (JDK 8), for example `OpenJDK <https://openjdk.org/>`_ 8

*  `Apache Ant <https://ant.apache.org/>`_

*  `Python <https://www.python.org/>`_ 3

   .. note::

      A few scripts in the repository use Python 2.7, invoked as :command:`python2`.

Installing Git
==============

.. include:: git.rst

.. _installing-openjdk:

Installing the Java Development Kit
===================================

.. include:: openjdk.rst

Installing Apache Ant
=====================

.. include:: ant.rst

Additional Prerequisites
========================

*  `JUnit 3.8.1 <http://junit.sourceforge.net/junit3.8.1/>`_ is included is included in the LOCKSS source distribution to run unit tests, but the Ant targets that invoke JUnit (``test-xxx``) require the JUnit JAR to be on Ant's :envvar:`CLASSPATH`. The easiest way to do this is to copy :file:`lib/junit.jar` (relative to the root of the ``lockss-daemon`` Git tree) into Ant's :file:`lib` directory (relative to its installation directory on the system).

*  For some tools and Ant targets, the :envvar:`JAVA_HOME` environment variable must be set to the directory in which the JDK is installed, i.e. it is expected that :file:`tools.jar` can be found in :file:`${JAVA_HOME}/lib`.

*  For runtime contexts that process split Zip files and some unit tests, the command-line :program:`zip` program must be installed.

   .. tip::

      Most Linux systems have :program:`zip` and :program:`unzip` installed by default.
