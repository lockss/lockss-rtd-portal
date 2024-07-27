====================
Running the Migrator
====================

.. warning::

   This page is under construction. LOCKSS 1.78 and LOCKSS 2.0-beta1 have not yet been released.

   .. image:: https://openmoji.org/php/download_asset.php?type=emoji&emoji_hexcode=1F6A7&emoji_variant=color
      :target: #
      :align: center
      :width: 256px
      :alt: Image of a road construction sign

The next task is to run the migrator, in the :guilabel:`Migration Control` screen of the LOCKSS 1.78 Web UI.

Follow these steps:

1. To migrate all content, select :guilabel:`All plugins` from the :guilabel:`Select Plugins` dropdown menu. If you wish to migrate only a subset of the content, you may select a plugin to migrate just the archival units from that plugin.

2. Select your desired migration mode:

   *  To copy the selected plugin's AUs from LOCKSS 1.78 to LOCKSS 2.0-beta1, select :guilabel:`Copy Content`.

   *  To copy the selected plugin's AUs from LOCKSS 1.78 to LOCKSS 2.0-beta1 and verify that each AU's URLs and state information were copied, select :guilabel:`Copy and Verify Content`.

   .. note::

      To verify that already copied AUs match after the fact, you can alternatively select the :guilabel:`Verify Content` mode.

      .. COMMENT doesn't make sense except in dry run mode

3. *Optional.* To cause the verification step of the :guilabel:`Copy and Verify Content` or :guilabel:`Verify Content` modes to additionally perform byte-for-byte comparison of content, select the :guilabel:`Full content compare` checkbox.

4. The :guilabel:`Skip already-copied AUs` checkbox is only useful in testing situations; the checkbox should remain selected.

5. Click the :guilabel:`Start Migration` button. (Click the :guilabel:`Abort` button to stop the migration in progress. It may take a moment for the migration to stop.)

.. tip::

   The migration process takes a long time, proportional to the total content size, and impacted by system, network, and storage performance.

.. tip::

   There may be no apparent progress for a while during migration, don't worry. The Migration Control screen will display:

   1. Current activity.

   2. The next few AUs that will start migrating.

   3. The list of AUs that have finished migrating.

   4. The list of errors.

.. tip::

   The migrator writes debugging information to two LOCKSS 1.x log files, :file:`/var/log/lockss/v2migration.txt` and :file:`/var/log/lockss/v2migration.err`.
