=====================================
Configuring LOCKSS 1.78 for Migration
=====================================

.. note::

   Many Web browsers pop up dialogs offering to save passwords entered as part of this UI screen. But these various passwords are about the LOCKSS 2.x host. You should decline saving these passwords in your browser, as they would overwrite the password you may have saved for the LOCKSS 1.x host.

The next task is to configure LOCKSS 1.78 for migration on your LOCKSS 1.x host.

Your LOCKSS 2.0-beta1 system will need to be running, and you will need to know the LOCKSS 2.x hostname, Web UI username and password, and PostgreSQL database password, supplied when configuring the LOCKSS 2.x system.

Follow these steps:

1. In your LOCKSS 1.78 Web user interface, click on :guilabel:`Migration Settings` in the navigation side panel.

2. Complete the first four fields in the :guilabel:`Migration Target` section of the form and enter the LOCKSS 2.x values gathered earlier:

   a. :guilabel:`Target Hostname`

      *  If you are doing a new-host migration, enter the hostname of your LOCKSS 2.x host, for instance ``lockss2.myuniversity.edu``.

      *  If you are doing a same-host migration, the default value ``localhost`` should remain unchanged.

   b. :guilabel:`Target Configuration Service Port`

      The default port ``24621`` should remain unchanged.

   c. :guilabel:`Username`

      Enter the Web UI username supplied to the LOCKSS 2.x system.

   d. :guilabel:`Password`

      Enter the Web UI password supplied to the LOCKSS 2.x system.

3. Click the :guilabel:`Load Configuration` button. The Metadata Database configuration will be queried from the LOCKSS 2.x system and displayed.

4. :guilabel:`Database Password`

   Enter the PostgreSQL database password supplied to the LOCKSS 2.x system.

5. `Optional.` In the :guilabel:`Migration Options` section, select the :guilabel:`Perform dry run migration` checkbox if you want to **only test** migration from LOCKSS 1.x to LOCKSS 2.x without permanent changes to your LOCKSS 1.x system.

6. `Optional.` If you are performing a same-host migration and there is **insufficient total storage space** on the host for two copies of the preserved content, select the :guilabel:`Delete AUs after migration` checkbox.

   .. caution::

      **Selecting this option will permanently delete content from your LOCKSS 1.x system.** This should only be used if you need to reclaim the disk space as the migration is running in a same-host migration.

7. Click on the :guilabel:`Next` button to navigate to the Migration Control screen.
