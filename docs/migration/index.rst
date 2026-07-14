.. include:: subst.rst

=================================
LOCKSS 1.x to 2.x Migration Guide
=================================

:Last updated: |LASTUPDATED|

**Welcome, LOCKSS 1.x users!**

This document will guide you through the migration from LOCKSS 1.x to LOCKSS 2.x. Different audiences will be interested in different portions of this document:

*  If you are a **system administrator of a LOCKSS node**, :numref:`Chapter %s <Introduction to the Migration>` (:ref:`Introduction to the Migration`) through :numref:`Chapter %s <Decommissioning LOCKSS 1.x>` (:ref:`Decommissioning LOCKSS 1.x`) will walk you through the steps to populate an initially empty LOCKSS |MIGRATE_TO_MINOR| instance with the data preserved in a LOCKSS |MIGRATE_FROM_MINOR| instance.

*  If you are a **user of a LOCKSS node**, see :numref:`Chapter %s <Appendix: Instructions for Users of LOCKSS Nodes>` (:ref:`Appendix: Instructions for Users of LOCKSS Nodes`) for important information about using the LOCKSS node during and after the migration. 

*  If you are an **administrator of a LOCKSS network**, see :numref:`Chapter %s <Appendix: Instructions for Administrators of LOCKSS Networks>` (:ref:`Appendix: Instructions for Administrators of LOCKSS Networks`) for important information about the transitional period while the nodes in your network are migrating from LOCKSS 1.x to 2.x. Additionally, if you are providing technical support to system administrators or users of individual LOCKSS nodes, you will also want to review the information provided to them (see above).

*  If you are **installing LOCKSS for the first time**, there is no migration involved; see the |MANUAL| to install LOCKSS 2.x directly.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 1
   :numbered:

   introduction
   upgrading1
   preparing2
   installing2
   configuring2
   configuring1
   running
   reconfiguring2
   decommissioning1
   user
   network
   faq
   differences
