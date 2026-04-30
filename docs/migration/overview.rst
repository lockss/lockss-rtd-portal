.. include:: subst.rst

==================
Migration Overview
==================

------------------------
Basic Migration Overview
------------------------

Conceptually, migration from LOCKSS 1.x to LOCKSS 2.x follows this outline:

1. A pre-existing LOCKSS 1.x instance is preserving content in one or more content storage areas (key [#fn-key]_):

   .. image:: laaws-migration-basic-before.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. This illustrates that all AUs are handled by the LOCKSS 1.x instance.

2. An empty LOCKSS 2.x instance is configured with one or more content storage areas of its own (key [#fn-key]_):

   .. image:: laaws-migration-basic-start.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. Nothing appears on the red disks. This illustrates that all AUs are handled by the LOCKSS 1.x instance and that the LOCKSS 2.x instance is empty.

3. The LOCKSS migrator sets up and executes the migration, and the LOCKSS 2.x instance is gradually populated with the data from the LOCKSS 1.x instance. Each archival unit (AU) [#fn-au]_ becomes deactivated in the LOCKSS 1.x instance; then its contents are copied to the LOCKSS 2.x instance; finally the AU is reactivated in the LOCKSS 2.x instance (key [#fn-key]_):

   .. image:: laaws-migration-basic-middle.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. A box with a non-bold label "AU #1" appears on the first blue disk, and a corresponding box with a bold label "AU #1" appears on the first red disk. A box with a non-bold label "AU #2" appears on the first blue disk, and a corresponding box with a bold label "AU #2" appears on the second red disk. A box with a non-bold label "AU #3" appears on the first blue disk, and a corresponding box with a bold label "AU #3" appears on the first red disk. A box with a non-bold label "AU #4" appears on the second blue disk, and another corresponding box with a non-bold label "AU #4" appears on the second red disk; additionally, an arrow with the text "AU #4 migration in progress" goes from the LOCKSS 1.x box to the LOCKSS 2.x box. Boxes with bold labels "AU #5" and "AU #6" appear on the second blue disk, with no corresponding boxes appearing on the red disks. AU #1, AU #2 and AU #3 illustrate AUs that have been migrated; they are no longer handled by the LOCKSS 1.x instance but still occupy disk space, and they are handled by the the LOCKSS 2.x instance. AU #4 illustrates a migration in progress; it is not handled by either instance. AU #5 and AU #6 illustrate AUs that have not yet been migrated; they are handled by the LOCKSS 1.x instance, and do not yet occupy any disk space associated with the LOCKSS 2.x instance. The diagram also illustrates that corresponding AUs may not be distributed the same way on the blue disks and the red disks.

4. At the end of the migration process, the LOCKSS 2.x instance is handling all AUs, and the LOCKSS 1.x instance is no longer handling any AUs (key [#fn-key]_):

   .. image:: laaws-migration-basic-end.png
      :align: center
      :alt: Diagram showing a blue LOCKSS 1.x box with arrows pointing at two blue disks representing its content storage areas, side by side with a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with non-bold labels "AU #1", "AU #2" and "AU #3" appear on the first blue disk, and boxes with non-bold labels "AU #4", "AU #5" and "AU #6" appear on the second blue disk. Boxes with bold labels "AU #1", "AU #3" and "AU #5" appear on the first red disk, and boxes with bold labels "AU #2", "AU #4" and "AU #6" appear on the second red disk. This illustrates that all AUs are handled by the LOCKSS 2.x instance and that the LOCKSS 2.x instance is no longer handling any AUs, although the disk space used by the AUs formerly is still occupied.

5. Finally, the LOCKSS 1.x instance is decommissioned (key [#fn-key]_):

   .. image:: laaws-migration-basic-after.png
      :align: center
      :alt: Diagram showing a red LOCKSS 2.x box with arrows pointing at two red disks representing its content storage areas. Boxes with bold labels "AU #1", "AU #3" and "AU #5" appear on the first red disk, and boxes with bold labels "AU #2", "AU #4" and "AU #6" appear on the second red disk. This illustrates that all AUs are handled by the LOCKSS 2.x instance.

The different :ref:`Migration Scenarios <Migration Scenario>` differ only in two key ways: where the LOCKSS 2.x instance is located compared to the LOCKSS 1.x instance, and when the storage space occupied by deactivated AUs from the LOCKSS 1.x instance is reclaimed.

------------------
Migration Scenario
------------------

.. |NEWHOSTMIGRATION| replace:: In this migration scenario, a newly-commissioned host with its own storage is used for the LOCKSS 2.x instance. After migration, the LOCKSS 1.x instance, its storage, and its host are decommissioned.

.. |SAMEHOSTMIGRATION| replace:: In this migration scenario, the LOCKSS 2.x instance is run on the pre-existing host of the LOCKSS 1.x instance. After migration, the LOCKSS 1.x instance is decommissioned.

.. |SAMEHOSTMIGRATIONFUTURE| replace:: In this :ref:`Same-Host Migration` scenario, the LOCKSS 2.x instance is configured to use different storage areas than the LOCKSS 1.x instance. After migration, the LOCKSS 1.x instance's storage areas are reclaimed all at once, and can then be devoted to the LOCKSS 2.x instance.

.. |SAMEHOSTMIGRATIONINCREMENTAL| replace:: In this :ref:`Same-Host Migration` scenario, the LOCKSS 2.x instance is configured to use the same storage areas as the LOCKSS 1.x instance. The LOCKSS Migrator is operated in a special mode in which the storage used by each AU in the LOCKSS 1.x instance is reclaimed after the AU is done migrating to the LOCKSS 2.x instance.

There are two types of migrations:

*  :ref:`New-Host Migration` (**recommended**). |NEWHOSTMIGRATION|

*  :ref:`Same-Host Migration` (*if a new-host migration is not feasible*). |SAMEHOSTMIGRATION| This scenario has two subtypes:

   *  :ref:`Same-Host Migration With Future Reclamation` (*preferable if a same-host migration is needed*). |SAMEHOSTMIGRATIONFUTURE|

   *  :ref:`Same-Host Migration With Incremental Reclamation` (*if a same-host migration is needed but a same-host migration with future reclamation is not feasible*). |SAMEHOSTMIGRATIONINCREMENTAL|

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

   *  Running LOCKSS 1.x and LOCKSS 2.x together on the same host will degrade performance, and also cause the migration process to take longer.

   *  If your LOCKSS 1.x host is running an outdated operating system in the RHEL family such as CentOS Linux 7, you must first upgrade the OS to another operating system in the RHEL family before proceeding with a same-host migration.

Same-Host Migration
===================

|SAMEHOSTMIGRATION|

This :ref:`Migration Scenario` is available if a :ref:`New-Host Migration` is not feasible. This scenario has two subtypes: a :ref:`Same-Host Migration With Future Reclamation` (preferable if a same-host migration is needed) or a :ref:`Same-Host Migration With Incremental Reclamation` (if a same-host migration is needed but a same-host migration with future reclamation is not feasible).

Same-Host Migration With Future Reclamation
-------------------------------------------

|SAMEHOSTMIGRATIONFUTURE|

This :ref:`Migration Scenario` is preferable if a :ref:`Same-Host Migration` is needed. The primary requirement is that there is enough spare storage space on the LOCKSS 1.x host to hold the pre-existing copy of the preserved data under LOCKSS 1.x and a copy of it under LOCKSS 2.x simultaneously.

.. image:: laaws-migration-same-host-future-overview.png
   :align: center

Same-Host Migration With Incremental Reclamation
------------------------------------------------

|SAMEHOSTMIGRATIONINCREMENTAL|

This :ref:`Migration Scenario` is available if a :ref:`Same-Host Migration` is needed, but a :ref:`Same-Host Migration With Future Reclamation` is not feasible. It may be necessary if there is not enough spare storage space on the LOCKSS 1.x host to hold the pre-existing copy of the preserved data under LOCKSS 1.x and a copy of it under LOCKSS 2.x simultaneously. The process is largely the same as that for a :ref:`Same-Host Migration With Future Reclamation`, except for a step in :numref:`Configuring LOCKSS 1.x for Migration` (:ref:`Configuring LOCKSS 1.x for Migration`).

.. image:: laaws-migration-same-host-incremental-overview.png
   :align: center

This migration scenario is not eligible for a :ref:`Dry Run Migration`.

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

This guide is organized in consecutive sections (:numref:`Upgrading LOCKSS 1.x` through :numref:`Reconfiguring LOCKSS 2.x for Normal Operation`) representing the steps of the migration:

.. image:: laaws-migration-steps-start.png
   :align: center
   :alt: A diagram of seven consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The seven boxes are successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", "Running the Migrator" and "Reconfiguring LOCKSS 2.x for Normal Operation".

followed by some appendices.

In a number of places, the instructions differ
between a :ref:`New-Host Migration` and a :ref:`Same-Host Migration`, and you will find clearly marked sections for each, like in this example:

    .. tab-set::

       .. tab-item:: New-Host Migration
          :sync: newhost

          Example of instructions specific to a :ref:`New-Host Migration`.

       .. tab-item:: Same-Host Migration
          :sync: samehost

          Example of instructions specific to a :ref:`Same-Host Migration`.

In a few places, a single instruction step will apply only to one :ref:`Migration Scenario` or to a :ref:`Dry Run Migration`; in addition to text to this effect, this situation will be denoted by a visual chip, as in these examples:

    1. |NEWHOSTONLY| This step applies only to a :ref:`New-Host Migration`.

    2. |SAMEHOSTONLY| This step applies only to a :ref:`Same-Host Migration` (either a :ref:`Same-Host Migration With Future Reclamation` or a :ref:`Same-Host Migration With Incremental Reclamation`).

    3. |SAMEHOSTFUTUREONLY| This step applies only to a :ref:`Same-Host Migration With Future Reclamation`.

    4. |SAMEHOSTINCREMENTALONLY| This step applies only to a :ref:`Same-Host Migration With Incremental Reclamation`.

    5. |DRYRUNONLY| This step applies only to a :ref:`Dry Run Migration`.

    6. |ALLOTHERSCENARIOS| If a step applies to only one :ref:`Migration Scenario`, a counterpart that applies to all other scenarios may be denoted with this visual chip.

Many parts of this guide accompany you as you apply sections of the |MANUAL|. To help identify cross-references to this parallel source of instructions, the symbol |TAB| is used to denote |MANUAL| references, for example:

    See |TAB| Section 1.2.3 in the |MANUAL|.

---------------------------
Detailed Migration Overview
---------------------------

.. sidebar:: TL;DR

   *  The LOCKSS 1.x to 2.x migration tool is operated from the LOCKSS 1.x Web UI.

   *  During migration, continue to access content (ServeContent, proxy) using the 1.x host and port.

   *  During migration, additional AUs to be preserved and subscriptions should be added using the 2.x Web UI.

   *  During migration, changes to configuration, such as IP access lists and proxy settings, should be made to both the 1.x and 2.x systems.

The LOCKSS migration process provides a way to copy content and configuration from LOCKSS 1.x to LOCKSS 2.x. It requires that both the 1.x and the 2.x systems be running simultaneously, either on the same or on different hosts. The migrator is a 1.x component which talks to the 2.x REST services to store content, configuration, state information (such as agreement histories), and the metadata database (if applicable). It is operated from the LOCKSS 1.x Web user interface.

The set of archival units to copy is determined by selecting either all AUs or just those belonging to a single plugin. Migrating content takes significant time, and is highly dependent on content characteristics and environment (file size distribution, network vs. local storage, etc.). In some cases (e.g. GLN nodes), we expect it will take months to migrate all the content.

The migrator facilitate running both the 1.x and the 2.x systems in tandem, so that content collection, polling, and access are not interrupted significantly while migration proceeds. If performing a same-host migration, content may be incrementally deleted as it is moved, if necessary to reclaim disk space.

The migrator copies, and optionally verifies, content and state data for each AU. By default, the verification step does not compare copied content byte-for-byte, though this additional step can be switched on (but it will approximately double the time required to complete the migration).

The migrator migrates several AUs at a time. When an AU is being migrated, first it becomes "frozen" in 1.x so it will not crawl or poll; then its content is copied from 1.x to 2.x; then it is configured in 2.x; then it is deactivated (or deleted) from 1.x, at which point it again becomes eligible to crawl and poll in 2.x. During the migration process, the 1.x node continues to communicate with other nodes in the network; the 1.x node handles all the polling and voting traffic for AUs that have been migrated to 2.x, so as to give the impression of a single LOCKSS node to the rest of the network. Similarly, all content access (ServeContent, proxy) during the migration should be to the 1.x system, and requests corresponding to AUs that have been migrated to 2.x will be forwarded to 2.x as necessary, so as to give users the experience of a single LOCKSS node. (Note that this is experimental in LOCKSS 2.0-beta1.)

If you wish to add additional AUs to preserve, they should be added in the 2.x system. Similarly, new subscription should be added to the subscription manager on 2.x, but they will not take effect until migration is complete. Configuration data such as IP access lists and proxy settings are copied at the beginning of the migration process; if you need to make changes to them in the 1.x system during the migration, the same changes should be made in the 2.x system.

If you have set any configuration parameters in the Expert Config screen, this file is also copied at the beginning of migration, but each line is commented out to allow you to review which custom settings you wish to be in effect in the 2.x system.

----

.. rubric:: Footnotes

.. [#fn-key]

   Key for the diagrams in :numref:`Basic Migration Overview` (:ref:`Basic Migration Overview`):

   .. image:: laaws-migration-basic-key.png

.. [#fn-au]

   An **archival unit**, or **AU**, is a unit of preserved content in LOCKSS. Consisting of any number of versioned objects, an AU might be a volume of a journal, a single book and its assets, a given digitized collection, etc.
