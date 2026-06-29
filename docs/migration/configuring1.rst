.. include:: subst.rst

====================================
Configuring LOCKSS 1.x for Migration
====================================

.. image:: laaws-migration-steps-configuring1.png
   :align: center
   :alt: A diagram of eight consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first four boxes, successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host", "Installing LOCKSS 2.x", and "Configuring LOCKSS 2.x for Migration", are colored in light blue, indicating completed steps. The fifth box labeled "Configuring LOCKSS 1.x for Migration" is highlighted in yellow, indicating the step in progress. The last three boxes, successively labeled "Running the Migrator", "Reconfiguring LOCKSS 2.x for Normal Operation", and "Decommissioning LOCKSS 1.x", are not colored, indicating future steps.

The next task is to configure LOCKSS 1.x for migration in the :guilabel:`Migration Settings` screen of your LOCKSS 1.x Web user interface.

Your LOCKSS 2.x system will need to be running, and you will need to know the LOCKSS 2.x hostname, Web user interface username and password, and PostgreSQL database password, supplied when :ref:`Configuring LOCKSS 2.x for Migration`.

.. tip::

   This phase occurs in the :guilabel:`Migration Settings` screen of your LOCKSS 1.x Web user interface. Some of the fields in this screen are passwords related to your newly installed LOCKSS 2.x instance. Web browsers pop up dialogs offering to save these LOCKSS 2.x passwords, but you should decline, as they would overwrite the password you may have saved for the LOCKSS 1.x Web UI.

Follow these steps:

1. Log in to your LOCKSS 1.x Web user interface, and click on :guilabel:`Migration Settings` in the top-right navigation menu.

2. Complete the four fields in the :guilabel:`LOCKSS 2.x Target` section of the screen using the appropriate LOCKSS 2.x values:

   a. :guilabel:`Hostname`: Enter the hostname of your LOCKSS 2.x host:

      *  |NEWHOSTONLY| If you are doing a :ref:`New-Host Migration`, enter the LOCKSS 2.x hostname, for example :samp:`{lockss2.myuniversity.edu}`.

      *  |SAMEHOSTONLY| If you are doing a :ref:`Same-Host Migration`, enter the LOCKSS 2.x hostname:

         *  |LOCKSS1CONTAINER| In the unlikely event you are running LOCKSS 1.x as a Docker container, enter the fully qualified hostname, for example :samp:`{lockss.myuniversity.edu}`.

         *  |ALLOTHERSCENARIOS| Otherwise, simply enter ``localhost``.

   b. :guilabel:`Configuration Service Web UI Port`: The default Web UI port for the |CFGSVC|, ``24602``, should remain unchanged.

   c. :guilabel:`Web UI Username`: Enter the Web UI username for the LOCKSS 2.x instance.

   d. :guilabel:`Web UI Password`: Enter the Web UI password for the LOCKSS 2.x instance.

3. Click the :guilabel:`Load Configuration` button. The metadata database configuration will be queried from the LOCKSS 2.x instance and displayed in the :guilabel:`Metadata Database` section of the screen.

4. In the :guilabel:`Database Password` field, enter the password for the |POSTGRESQL|.

5. |DRYRUNONLY| If you are doing a :ref:`Dry Run Migration`, select the :guilabel:`Perform dry run migration` checkbox in the :guilabel:`Migration Options` section.

6.  |SAMEHOSTINCREMENTALONLY| **If, and only if,** you are doing a :ref:`Same-Host Migration With Incremental Reclamation`, select the :guilabel:`Delete each AU after migration` checkbox.

   .. caution::

      **Selecting this option causes content to be permanently deleted from your LOCKSS 1.x instance, gradually as the migration progresses.** This option should be used **if, and only if,** you are doing a :ref:`Same-Host Migration With Incremental Reclamation`, that is, a same-host migration with insufficient storage space to hold two copies of the content. You will receive a popup warning when you check this checkbox, which you need to acknowledge before you can continue. See :numref:`Same-Host Migration With Incremental Reclamation`.

7. Click on the :guilabel:`Next` button at the bottom of the :guilabel:`Migration Settings` screen to navigate to the :guilabel:`Migration Control` screen.
