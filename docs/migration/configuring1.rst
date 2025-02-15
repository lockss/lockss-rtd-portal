====================================
Configuring LOCKSS 1.x for Migration
====================================

The next task is to configure LOCKSS 1.x for migration in the :guilabel:`Migration Settings` screen of your LOCKSS 1.x Web user interface.

Your LOCKSS 2.x system will need to be running, and you will need to know the LOCKSS 2.x hostname [#fnsamehost]_, Web user interface username and password, and PostgreSQL database password, supplied when configuring the LOCKSS 2.x system.

.. important::

   This phase occurs in the :guilabel:`Migration Settings` screen of your LOCKSS 1.x Web user interface. Some of the fields in this screen are passwords related to your newly installed LOCKSS 2.x instance. Web browsers pop up dialogs offering to save these LOCKSS 2.x passwords, but you should decline, as they would overwrite the password you may have saved for the LOCKSS 1.x Web UI.

Follow these steps:

1. In your LOCKSS 1.x Web user interface, click on :guilabel:`Migration Settings` in the navigation side panel.

2. Complete the first four fields in the :guilabel:`Migration Target` section of the form and enter the LOCKSS 2.x values gathered earlier:

   a. :guilabel:`Target Hostname`: Enter the hostname of your LOCKSS 2.x host (``localhost`` for a **same-host migration**, a host name like ``lockss2.myuniversity.edu`` for a **new-host migration**).

   b. :guilabel:`Target Configuration Service Port`: The default port ``24621`` should remain unchanged.

   c. :guilabel:`Username`: Enter the Web UI username supplied to the LOCKSS 2.x system.

   d. :guilabel:`Password`: Enter the Web UI password supplied to the LOCKSS 2.x system.

3. Click the :guilabel:`Load Configuration` button. The Metadata Database configuration will be queried from the LOCKSS 2.x system and displayed.

4. :guilabel:`Database Password`: Enter the PostgreSQL database password supplied to the LOCKSS 2.x system.

5. `Optional.` In the :guilabel:`Migration Options` section, select the :guilabel:`Perform dry run migration` checkbox if you want to **only test** migration from LOCKSS 1.x to LOCKSS 2.x without permanent changes to your LOCKSS 1.x system.

6. `Optional.` If you are performing a **same-host migration with insufficient total storage space** on the host for two copies of the preserved content, select the :guilabel:`Delete AUs after migration` checkbox.

   .. caution::

      **Selecting this option will permanently delete content from your LOCKSS 1.x system, gradually during the migration as it progresses.** This should only be used if you are doing a **same-host migration with insufficient total disk space**, meaning there is not enough total disk space for two copies of the preserved content -- one copy in your LOCKSS 1.x instance and one copy in your LOCKSS 2.x instance. It is not recommended if you are doing a **new-host migration**, or a **same-host migration with sufficient total disk space**.

7. Click on the :guilabel:`Next` button to navigate to the Migration Control screen.

----

.. only:: html

   .. rubric:: Footnotes

.. [#fnsamehost]

   If your :ref:`Migration Scenario` is a **same-host migration**, your LOCKSS 1.x host and your LOCKSS 2.x host are the same host.
