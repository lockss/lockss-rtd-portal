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

*  `Python <https://www.python.org/>`_ 3, invoked as :command:`python3`

*  Some scripts require `Python <https://www.python.org/>`_ 2.7, invoked as :command:`python2`

*  Some runtime contexts that process split Zip files and some unit tests require the :program:`zip` program (:program:`zip` and :program:`unzip` are installed by default on most Linux systems).

Installing Git
==============

.. include:: git.rst

.. _installing-openjdk:

Installing the Java Development Kit
===================================

1. .. include:: openjdk.rst

2. Set the :envvar:`JAVA_HOME` environment variable to the directory in which the JDK is installed, for example :file:`/usr/lib/jvm/java-8-openjdk`. It is expected that the file :file:`${JAVA_HOME}/lib/tools.jar` exists.

Installing Apache Ant
=====================

.. include:: ant.rst

Cloning the Git Repository
==========================

To clone the ``lockss-daemon`` repository from Git, use one of these commands:

.. code-block:: shell

   # GitHub account with SSH key
   git clone git@github.com:lockss/lockss-daemon

   # Anonymous access
   git clone https://github.com/lockss/lockss-daemon

This will create a :file:`lockss-daemon` directory.

JUnit Prerequisites
===================

`JUnit 3.8.1 <http://junit.sourceforge.net/junit3.8.1/>`_ is included is included in the LOCKSS source distribution to run unit tests, but the Ant targets that invoke JUnit (``test-xxx``) require the JUnit JAR to be on Ant's :envvar:`CLASSPATH`. The easiest way to do this is to copy :file:`lib/junit.jar` (relative to the root of the ``lockss-daemon`` Git tree) into Ant's :file:`lib` directory (relative to its installation directory on the system).

-------------------------
Tour of ``lockss-daemon``
-------------------------

The main components of the ``lockss-daemon`` repository are as follows:

*  :file:`build.xml` is the Ant build file. Type ``ant -projecthelp`` (or ``ant -p``) will output a list of available build targets. The :file:`lib` directory contains Java (JAR) dependencies for the project at large.

*  The :file:`src` tree contains the source code of the LOCKSS system proper, and :file:`test/src` its unit tests. The :file:`ant/src` tree contains the source code for an ancillary prerequisite.

*  The :file:`plugins/src` tree contains the source code of plugins written by the LOCKSS Program to support the preservation activities of LOCKSS networks such as the Global LOCKSS Network (GLN) and the CLOCKSS Archive, and :file:`plugins/test/src` the unit tests.

*  The :file:`tools/src` tree contains the source code of ancillary tools sometimes used in the context of LOCKSS development, and :file:`tools/test/src` the unit tests.

*  The :file:`tdb` directory contains the archival unit (AU) inventory of content managed by the LOCKSS Program on behalf of various LOCKSS networks such as the GLN and CLOCKSS.

*  The :file:`scripts` and :file:`test/scripts` directories contains scripts and tools used for TDB file processing, SOAP Web services, and more.

*  The :file:`test/frameworks` tree contains multiple testing frameworks, to bring up one or more instance of the (classic) LOCKSS system on the local machine for testing or development purposes.











