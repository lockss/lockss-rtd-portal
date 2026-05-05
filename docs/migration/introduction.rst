.. include:: subst.rst

=============================
Introduction to the Migration
=============================

-------------------------
Supported Migration Paths
-------------------------

As of the last update of this migration guide (|LASTUPDATED|), the only supported migration path is from LOCKSS |UPGRADE_FROM_PATCH| (the latest version of LOCKSS |UPGRADE_FROM_MINOR|) to LOCKSS |UPGRADE_TO_PATCH| (the latest version of LOCKSS |UPGRADE_TO_MINOR|). In particular, as of the twin release of LOCKSS |UPGRADE_FROM_MINOR| and LOCKSS |UPGRADE_TO_MINOR|, upgrades from earlier versions of LOCKSS 1.x and/or to earlier versions of LOCKSS 2.x are no longer supported.

------------------
Migration Overview
------------------

Conceptually, migration from LOCKSS 1.x to LOCKSS 2.x follows this outline:

1. A pre-existing LOCKSS 1.x instance is preserving content in one or more content storage areas (legend [#fn-legend]_):

   .. image:: laaws-migration-basic-before.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. This illustrates that all AUs are handled by the LOCKSS 1.x instance.

2. An empty LOCKSS 2.x instance is configured with one or more content storage areas of its own (legend [#fn-legend]_):

   .. image:: laaws-migration-basic-start.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. Nothing appears on the red disks. This illustrates that all AUs are handled by the LOCKSS 1.x instance and that the LOCKSS 2.x instance is empty.

3. The LOCKSS migrator sets up and executes the migration, and the LOCKSS 2.x instance is gradually populated with the data from the LOCKSS 1.x instance. Each archival unit (AU) [#fn-au]_ becomes deactivated in the LOCKSS 1.x instance; then its contents are copied to the LOCKSS 2.x instance; finally the AU is reactivated in the LOCKSS 2.x instance (legend [#fn-legend]_):

   .. image:: laaws-migration-basic-middle.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. A box with a non-bold label "AU #1" appears on the first blue disk, and a corresponding box with a bold label "AU #1" appears on the first red disk. A box with a non-bold label "AU #2" appears on the first blue disk, and a corresponding box with a bold label "AU #2" appears on the second red disk. A box with a non-bold label "AU #3" appears on the first blue disk, and a corresponding box with a bold label "AU #3" appears on the first red disk. A box with a non-bold label "AU #4" appears on the second blue disk, and another corresponding box with a non-bold label "AU #4" appears on the second red disk; additionally, an arrow with the text "AU #4 migration in progress" goes from the LOCKSS 1.x box to the LOCKSS 2.x box. Boxes with bold labels "AU #5" and "AU #6" appear on the second blue disk, with no corresponding boxes appearing on the red disks. AU #1, AU #2 and AU #3 illustrate AUs that have been migrated; they are no longer handled by the LOCKSS 1.x instance but still occupy disk space, and they are handled by the the LOCKSS 2.x instance. AU #4 illustrates a migration in progress; it is not handled by either instance. AU #5 and AU #6 illustrate AUs that have not yet been migrated; they are handled by the LOCKSS 1.x instance, and do not yet occupy any disk space associated with the LOCKSS 2.x instance. The diagram also illustrates that corresponding AUs may not be distributed the same way on the blue disks and the red disks.

4. At the end of the migration process, the LOCKSS 2.x instance is handling all AUs, and the LOCKSS 1.x instance is no longer handling any AUs (legend [#fn-legend]_):

   .. image:: laaws-migration-basic-end.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with non-bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with non-bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. Boxes with bold labels "AU #1", "AU #3" and "AU #5" appear on the first red disk, and boxes with bold labels "AU #2", "AU #4" and "AU #6" appear on the second red disk. This illustrates that all AUs are handled by the LOCKSS 2.x instance and that the LOCKSS 2.x instance is no longer handling any AUs, although the disk space used by the AUs formerly is still occupied.

5. Finally, the LOCKSS 1.x instance is decommissioned (legend [#fn-legend]_):

   .. image:: laaws-migration-basic-after.png
      :align: center
      :alt: Diagram showing a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #3" and "AU #5" appear on the first red disk, and boxes with bold labels "AU #2", "AU #4" and "AU #6" appear on the second red disk. This illustrates that all AUs are handled by the LOCKSS 2.x instance.

The different :ref:`Migration Scenarios <Migration Scenario>` differ only in two key ways: where the LOCKSS 2.x instance is located compared to the LOCKSS 1.x instance, and when the storage space occupied by deactivated AUs from the LOCKSS 1.x instance is reclaimed.

------------------
Migration Scenario
------------------

.. |NEWHOSTMIGRATION| replace:: In this migration scenario, a newly-commissioned host with its own storage is used for the LOCKSS 2.x instance. After migration, the LOCKSS 1.x instance, its storage, and its host are decommissioned.

.. |SAMEHOSTMIGRATION| replace:: In this migration scenario, the LOCKSS 2.x instance is run on the existing host of the LOCKSS 1.x instance. After migration, the LOCKSS 1.x instance is decommissioned.

.. |SAMEHOSTMIGRATIONQUALIFICATION| replace:: if a new-host migration is not feasible

.. |SAMEHOSTMIGRATIONFUTURE| replace:: In this :ref:`Same-Host Migration` scenario, the LOCKSS 2.x instance is configured to use different storage areas than the LOCKSS 1.x instance. After migration, the LOCKSS 1.x instance's storage areas are reclaimed all at once, and can then be devoted to the LOCKSS 2.x instance.

.. |SAMEHOSTMIGRATIONFUTUREQUALIFICATION| replace:: if a same-host migration is needed, and there is sufficient storage space to hold an entire LOCKSS 1.x and LOCKSS 2.x copy of the content simultaneously

.. |SAMEHOSTMIGRATIONINCREMENTAL| replace:: In this :ref:`Same-Host Migration` scenario, the LOCKSS 2.x instance is configured to use the same storage areas as the LOCKSS 1.x instance. The LOCKSS Migrator is operated in a mode in which the storage used by each AU in the LOCKSS 1.x instance is reclaimed after the AU is done migrating to the LOCKSS 2.x instance.

.. |SAMEHOSTMIGRATIONINCREMENTALQUALIFICATION| replace:: only if a same-host migration is needed, but there is insufficient storage space to hold an entire LOCKSS 1.x and LOCKSS 2.x copy of the content simultaneously

You may choose one of two migration scenarios:

*  :ref:`New-Host Migration` (**recommended**). |NEWHOSTMIGRATION|

*  :ref:`Same-Host Migration` (|SAMEHOSTMIGRATIONQUALIFICATION|). |SAMEHOSTMIGRATION|

   If chosen, this scenario has two subtypes:

   *  :ref:`Same-Host Migration With Future Reclamation` (|SAMEHOSTMIGRATIONFUTUREQUALIFICATION|). |SAMEHOSTMIGRATIONFUTURE|

   *  :ref:`Same-Host Migration With Incremental Reclamation` (|SAMEHOSTMIGRATIONINCREMENTALQUALIFICATION|). |SAMEHOSTMIGRATIONINCREMENTAL|

New-Host Migration
==================

.. tip::

   This :ref:`Migration Scenario` is **recommended**.

|NEWHOSTMIGRATION|

.. image:: laaws-migration-new-host-overview.png
   :align: center

.. _migration-new-host-recommended:

.. admonition:: Why is a new host recommended?

   *  LOCKSS 2.x has higher system requirements.

   *  Unlike LOCKSS 1.x, LOCKSS 2.x can be installed on a greater variety of :external+lockss-manual:ref:`Compatible Operating Systems`. This is an opportunity to move to a new host better fitting your institution's IT infrastructure preferences.

   *  If your LOCKSS 1.x host is running an outdated operating system in the RHEL family such as CentOS Linux 7, you must first upgrade the OS to another operating system in the RHEL family before proceeding with a same-host migration.

   *  Running LOCKSS 1.x and LOCKSS 2.x together on the same host will degrade performance, and may cause the migration process to take longer.

Same-Host Migration
===================

|SAMEHOSTMIGRATION|

This migration scenario is used |SAMEHOSTMIGRATIONQUALIFICATION|. It has two subtypes:

*  :ref:`Same-Host Migration With Future Reclamation`

*  :ref:`Same-Host Migration With Incremental Reclamation`


Same-Host Migration With Future Reclamation
-------------------------------------------

|SAMEHOSTMIGRATIONFUTURE|

This migration scenario is used |SAMEHOSTMIGRATIONFUTUREQUALIFICATION|.

.. image:: laaws-migration-same-host-future-overview.png
   :align: center

Same-Host Migration With Incremental Reclamation
------------------------------------------------

|SAMEHOSTMIGRATIONINCREMENTAL|

This migration scenario is used |SAMEHOSTMIGRATIONINCREMENTALQUALIFICATION|.

The process is largely the same as that for a :ref:`Same-Host Migration With Future Reclamation`, except for a step in :numref:`Configuring LOCKSS 1.x for Migration` (:ref:`Configuring LOCKSS 1.x for Migration`).

.. image:: laaws-migration-same-host-incremental-overview.png
   :align: center

-----------------
Dry Run Migration
-----------------

It is possible to try out a :ref:`New-Host Migration` or a :ref:`Same-Host Migration With Future Reclamation` in **dry run mode**, meaning only for testing purposes without permanent changes to your LOCKSS 1.x system. (This is not possible for a :ref:`Same-Host Migration With Incremental Reclamation`.)

The process is largely the same as that for a corresponding :ref:`New-Host Migration` or :ref:`Same-Host Migration With Future Reclamation`, with a few differences highlighted as such in this guide:

*  A step in :numref:`Running configure-lockss --migrate` (:ref:`Running configure-lockss --migrate`) is slightly different for dry run migrations.

*  A step in :numref:`Configuring LOCKSS 1.x for Migration` (:ref:`Configuring LOCKSS 1.x for Migration`) is specific to dry run migrations.

*  At the end of experimentation, you will need to reset your LOCKSS 2.x instance to its initial state before performing a genuine migration.

   .. COMMENT FIXME How: reference to manual

---------------------
How To Use This Guide
---------------------

Chapters
========

This guide is organized in consecutive chapters (:numref:`Chapter %s <Upgrading LOCKSS 1.x>` through :numref:`Chapter %s <Decommissioning LOCKSS 1.x>`) representing the steps of the migration:

.. image:: laaws-migration-steps-start.png
   :align: center
   :alt: A diagram of eight consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The eight boxes are successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", "Running the Migrator", "Reconfiguring LOCKSS 2.x for Normal Operation", and "Decommissioning LOCKSS 1.x".

followed by some appendices.

LOCKSS 2.x System Manual References
===================================

Many parts of this guide accompany you as you apply sections of the |MANUAL|. To help identify cross-references to this complementary source of instructions, the symbol |TAB| is used to denote such references, for example:

    See |TAB| Section 1.2.3 in the |MANUAL|.

Parallel Sections
=================

In a number of places, the instructions differ somewhat between a :ref:`New-Host Migration` and a :ref:`Same-Host Migration`, and you will find parallel sections for each, like in this example:

    .. tab-set::

       .. tab-item:: New-Host Migration
          :sync: newhost

          Example of instructions specific to a :ref:`New-Host Migration`.

       .. tab-item:: Same-Host Migration
          :sync: samehost

          Example of instructions specific to a :ref:`Same-Host Migration`.

Scenario-Specific Instruction
=============================

If a single instruction step applies only to one :ref:`Migration Scenario` or to a :ref:`Dry Run Migration`, the following visuals will augment the text to that effect:

    *  |NEWHOSTONLY| This step applies only to a :ref:`New-Host Migration`.

    *  |SAMEHOSTONLY| This step applies only to a :ref:`Same-Host Migration` (either a :ref:`Same-Host Migration With Future Reclamation` or a :ref:`Same-Host Migration With Incremental Reclamation`).

    *  |SAMEHOSTFUTUREONLY| This step applies only to a :ref:`Same-Host Migration With Future Reclamation`.

    *  |SAMEHOSTINCREMENTALONLY| This step applies only to a :ref:`Same-Host Migration With Incremental Reclamation`.

    *  |DRYRUNONLY| This step applies only to a :ref:`Dry Run Migration`.

    *  |ALLOTHERSCENARIOS| If a step applies to only one :ref:`Migration Scenario`, this counterpart applies to all other scenarios.

Console Hint
============

The commands to be typed at the console at various points in the migration process will occur in several environments, in terms of host, user, and directory, and the following visuals will augment the text to that effect:

    *  |LOCKSS1ROOT| This command occurs on your LOCKSS 1.x host, as the ``root`` user.

    *  |LOCKSS2LOCKSS| This command occurs on your LOCKSS 2.x host, as the ``lockss`` user, in the :ref:`LOCKSS Installer Directory`.

    *  |LOCKSS2ROOT| This command occurs on your LOCKSS 2.x host, as the ``root`` user, in the :ref:`LOCKSS Installer Directory`.

.. rubric:: LOCKSS Installer Directory
   :name: LOCKSS Installer Directory
   :heading-level: 4

The **LOCKSS Installer Directory** is an important concept in LOCKSS 2.x. It is the directory from which many LOCKSS 2.x installation, configuration and operation commands are run -- usually as the ``lockss`` user, but in the case of installing LOCKSS 2.x for the first time, sometimes as the ``root`` user. The **default LOCKSS Installer Directory** is :file:`{$HOME}/lockss-installer` relative to the ``lockss`` user, meaning :file:`/home/lockss/lockss-installer` on most Linux systems. For complete details, see |TAB| :external+lockss-manual:ref:`LOCKSS Installer Directory` and |TAB| :external+lockss-manual:ref:`Default LOCKSS Installer Directory` in the |MANUAL|.

------------------------
Important Considerations
------------------------

Adopting the LOCKSS 1.x IP Address and Hostname
===============================================

|NEWHOSTONLY|

In a :ref:`New-Host Migration`, **it is strongly recommended that at the end, you allow your LOCKSS 2.x host to adopt the IP address, and ideally the hostname, previously associated with your LOCKSS 1.x host**. This is an important consideration for planning purposes, because coordinated action with your system administrator or IT department to effect the change of IP addresses and/or hostnames may be required and may cause an interruption of service.

Changing the IP address and hostname of the LOCKSS 2.x host occurs after the principal part of the migration is finished, at a designated step in :numref:`Chapter %s <Reconfiguring LOCKSS 2.x for Normal Operation>` (:ref:`Reconfiguring LOCKSS 2.x for Normal Operation`). At a high level, it consists of shutting down your LOCKSS 1.x host (or at least reconfiguring it to yet another IP address and hostname), reconfiguring your LOCKSS 2.x host so it uses the IP address (and ideally hostname) previously associated with your LOCKSS 1.x host, and restarting |K3S| to adjust to the newly configured IP address.

.. rubric:: Implications if adopting the LOCKSS 1.x IP address is not possible
   :name: Implications if adopting the LOCKSS 1.x IP address is not possible

If adopting the IP address of your LOCKSS 1.x host is not possible, there are implications for your LOCKSS network and its participants to a permanent change of IP address for your node:

   *  The administrator of your LOCKSS network will need to include the permanent change of IP address of your node in the LOCKSS network's configuration file, and make other  adjustments to the props server (firewall rules, Web server access rules, etc.) and more.

   *  Other nodes in your LOCKSS network may have to adjust firewall rules and other access control lists (for example in the Content Access Options section of the Web user interface).

.. rubric:: Implications if adopting the LOCKSS 1.x hostname is not possible
   :name: Implications if adopting the LOCKSS 1.x hostname is not possible

Adopting the hostname of your LOCKSS 1.x host is not strictly required for the node to function, but a change of hostname may also have downstream implications. If you keep the new hostname permanently, it will need to be used when accessing the Web user interface, and browser bookmarks, monitoring tools and dashboards, link resolvers (e.g. OpenURL resolvers), proxy configuration, etc. will need to be updated.

Firewall Rules
==============

FIXME

----

.. rubric:: Footnotes

.. [#fn-legend]

   Legend for the diagrams in :numref:`Migration Overview` (:ref:`Migration Overview`):

   .. image:: laaws-migration-basic-legend.png
      :alt: A legend for the diagrams in the Migration Overview section. A box with a thick border labeled AU9 for "archival unit #9" is described as "Storage space occupied by an AU actively handled by the corresponding LOCKSS instance". A box with a regular border labeled AU9 for "archival unit #9" is described as "Storage space occupied by an AU not actively handled by the corresponding LOCKSS instance". A box with a dashed border labeled AU9 for "archival unit #9" is described as "Storage space reclaimed from an AU formerly hanlded by the corresponding LOCKSS instance".

.. [#fn-au]

   An **archival unit**, or **AU**, is a unit of preserved content in LOCKSS. Consisting of any number of versioned objects, an AU might be a volume of a journal, a single book and its assets, a given digitized collection, etc.
