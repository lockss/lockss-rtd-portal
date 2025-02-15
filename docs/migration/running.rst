====================
Running the Migrator
====================

The next task is to run the migrator in the :guilabel:`Migration Settings` screen of your LOCKSS 1.x Web user interface.

Follow these steps:

1. To migrate all content, select :guilabel:`All plugins` from the :guilabel:`Select Plugins` dropdown menu. If you wish to migrate only a subset of the content, you may select a plugin and migrate just the archival units from that plugin.

2. Select your desired migration mode:

   *  To copy the selected plugin's AUs from LOCKSS 1.x to LOCKSS 2.x, select :guilabel:`Copy Content`.

   *  To copy the selected plugin's AUs from LOCKSS 1.x to LOCKSS 2.x and verify that each AU's URLs and state information were copied, select :guilabel:`Copy and Verify Content`.

   .. tip::

      To verify that already copied AUs match after the fact, you can alternatively select the :guilabel:`Verify Content` mode.

      .. COMMENT doesn't make sense except in dry run mode

3. *Optional.* To cause the verification step of the :guilabel:`Copy and Verify Content` or :guilabel:`Verify Content` modes to additionally perform byte-for-byte comparison of content data, select the :guilabel:`Full content compare` checkbox.

4. The :guilabel:`Skip already-copied AUs` checkbox is only useful in testing situations; the checkbox should remain selected.

5. Click the :guilabel:`Start Migration` button.

   .. tip::

      .. dropdown:: The migration takes a long time
         :name: running-patience
         :icon: light-bulb
         :animate: fade-in-slide-down

         The migration process takes a long time, proportional to the total content size, and impacted by system, network, and storage performance.

      .. dropdown:: The migration makes slow progress
         :name: running-progress
         :icon: light-bulb
         :animate: fade-in-slide-down

         There may be no apparent progress for a while during migration, don't worry. The Migration Control screen will display:

         1. Current activity.

         2. The next few AUs that will start migrating.

         3. The list of AUs that have finished migrating.

         4. The list of errors.

      .. dropdown:: Migration log files
         :name: running-logs
         :icon: light-bulb
         :animate: fade-in-slide-down

         The migrator writes debugging information to two LOCKSS 1.x log files :file:`/var/log/lockss/v2migration.txt` and :file:`/var/log/lockss/v2migration.err`.

      .. dropdown:: Stopping the migration in progress
         :name: running-aborting
         :icon: light-bulb
         :animate: fade-in-slide-down

         To stop the migration in progress, click the :guilabel:`Abort` button. It may take a moment for the migration to stop.
