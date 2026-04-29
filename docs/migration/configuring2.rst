.. include:: subst.rst

====================================
Configuring LOCKSS 2.x for Migration
====================================

.. image:: laaws-migration-steps-configuring2.png
   :align: center
   :alt: A diagram of seven consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first three boxes, successively labeled "Upgrading LOCKSS 1.x", "Preparing the LOCKSS 2.x Host" and "Installing LOCKSS 2.x", are colored in light blue, indicating completed steps. The fourth box labeled "Configuring LOCKSS 2.x for Migration" is highlighted in yellow, indicating the step in progress. The last three boxes, successively labeled "Configuring LOCKSS 1.x for Migration", "Running the Migrator" and "Reconfiguring LOCKSS 2.x for Normal Operation", are not colored, indicating future steps.

The next task in the migration process is to configure LOCKSS 2.x for migration on your LOCKSS 2.x host [#fn-same-host]_.

---------------------------------------
Importing Configuration From LOCKSS 1.x
---------------------------------------

The first part of this task is to make your LOCKSS 1.x configuration file (and if applicable, the LCAP SSL keystores of your LOCKSS 1.x instance) available to your LOCKSS 2.x instance.

Follow these steps:

1. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a :ref:`New-Host Migration`:

         a. Copy the LOCKSS 1.x configuration file from :file:`/etc/lockss/config.dat` on your LOCKSS 1.x host to some file path on your LOCKSS 2.x host, symbolically represented as :samp:`{/path/to/lockss1_config_file.dat}`. Although you can use any path on your LOCKSS 2.x host, we recommend :file:`/tmp/v1config.dat`.

            For example, you might use :program:`scp` on your LOCKSS 1.x host:

            :samp:`scp /etc/lockss/config.dat {<username>}@{<lockss2host>}:{/path/to/lockss1_config_file.dat}`

            or something similar.

            If you are unable to copy the LOCKSS 1.x configuration file to your LOCKSS 2.x, you can still configure LOCKSS 2.x for migration, but you will be prompted to supply more information, which you will have to enter accurately from the corresponding LOCKSS 1.x values.

         b. Ensure that the LOCKSS 1.x configuration file :samp:`{/path/to/lockss1_config_file.dat}` is readable by all on the LOCKSS 2.x host. For example, you can do this as ``root`` on the LOCKSS 2.x host with:

            :samp:`chmod +r {/path/to/lockss1_config_file.dat}`

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a :ref:`Same-Host Migration`, the LOCKSS 2.x configuration script will find the LOCKSS 1.x configuration file directly at :file:`/etc/lockss/config.dat`, so you do not need to do anything in this step.

2. If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes, see the :doc:`lcap-ssl` appendix for additional instructions in this spot.

.. _Running configure-lockss --migrate:

---------------------------------------------
Running :program:`configure-lockss --migrate`
---------------------------------------------

The second part of this task is to run the :program:`configure-lockss` tool with the special ``--migrate`` option on your LOCKSS 2.x host [#fn-same-host]_.

This will proceed largely as described in |TAB| Chapter |CONFIGURE_CHAPTER| (:external+lockss-manual:doc:`configuring`) of the |MANUAL|, **but with some notable exceptions described below**:

1. Follow the instructions in |TAB| Section |CONFIGURE_CHAPTER|.1 (:external+lockss-manual:ref:`Gathering Configuration Information`) of the |MANUAL|.

2. Follow these steps (**modified** from Section |CONFIGURE_CHAPTER|.2 of the |MANUAL|):

   a. :bdg-success:`new-host migration only`

      First, if you are doing a :ref:`New-Host Migration`, double-check that you are in a shell console for your LOCKSS 2.x host, for example by typing:

      .. code-block:: shell

         hostname

      and verifying that the output is the expected name of your LOCKSS 2.x host.

   b. Next, double-check that you are in a shell console acting as the ``lockss`` user by typing:

      .. code-block:: shell

         whoami

      and verifying that the output is ``lockss``.

   c. Navigate to the |LOCKSS_INSTALLER_DIRECTORY|, symbolically:

      :samp:`cd {<LOCKSS_INSTALLER_DIR>}`

   d. Run this command:

      .. code-block:: shell

         scripts/configure-lockss --migrate

      .. tip::

         Some of the questions asked by :program:`configure-lockss` will have a suggested or default value, displayed in square brackets; either type the desired value and then hit :kbd:`Enter`, or just hit :kbd:`Enter` to accept the value in square brackets.

3. Follow the instructions in |TAB| Section |CONFIGURE_CHAPTER|.3 (:external+lockss-manual:ref:`Kubernetes Settings`) of the |MANUAL|.

4. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a :ref:`New-Host Migration`, follow these steps:

         a. You will receive the following prompt:

            :guilabel:`Did you copy a LOCKSS 1.x config.dat file to this host?`

            Enter :kbd:`Y` for "yes" or :kbd:`N` for "no", or hit :kbd:`Enter` to accept the default in square brackets.

            *  If you enter :kbd:`Y` for "yes", you will then receive the following prompt:

               :guilabel:`Location of copied LOCKSS 1.x config.dat file`

               Enter the path of the copied LOCKSS 1.x configuration file, symbolically represented as :samp:`{/path/to/config.dat}` above, or hit :kbd:`Enter` to accept the default in square brackets (:file:`/tmp/v1config.dat`).

            *  If you enter :kbd:`N` for "no", you will have to manually and accurately enter a number of values reflecting your LOCKSS 1.x configuration (instead of the values being imported directly from your copied LOCKSS 1.x configuration file).

         b. Follow the instructions in the following sections in the |MANUAL|:

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.1 (:external+lockss-manual:ref:`Hostname`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.2 (:external+lockss-manual:ref:`IP Address`)

         c. You will then receive the following message:

            .. code-block:: text

               The following values were imported from your LOCKSS 1.0 configuration.
                 In normal circumstances they should be accepted as is.

            Follow the instructions in the following sections in the |MANUAL|:

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.3 (:external+lockss-manual:ref:`Initial UI Subnet`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.4 (:external+lockss-manual:ref:`LCAP Port`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.5 (:external+lockss-manual:ref:`Network Address Translation`)

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a :ref:`Same-Host Migration`, follow these steps:

         a. You will receive this message:

            ``Found /etc/lockss/config.dat``

            confirming that the LOCKSS 1.x configuration file was detected.

         b. You will then receive the following message:

            .. code-block:: text

               The following values were imported from your LOCKSS 1.0 configuration.
                 In normal circumstances they should be accepted as is.

            Follow the instructions in the following sections of the |MANUAL|:

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.1 (:external+lockss-manual:ref:`Hostname`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.2 (:external+lockss-manual:ref:`IP Address`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.3 (:external+lockss-manual:ref:`Initial UI Subnet`)

            *  |TAB| Section |CONFIGURE_CHAPTER|.4.4 (:external+lockss-manual:ref:`LCAP Port`)

         c. After the :guilabel:`LCAP protocol port` prompt, you will receive the following prompt:

            :guilabel:`Temporary LOCKSS 2.x LCAP port`

            Enter an LCAP port different from the one used by LOCKSS 1.x, for use during migration, or hit :kbd:`Enter` to accept the suggested value in square brackets.

         d. Follow the instructions in |TAB| Section |CONFIGURE_CHAPTER|.4.5 (:external+lockss-manual:ref:`Network Address Translation`) of the |MANUAL|.

5. Follow all instructions from the following sections of the |MANUAL|:

            *  |TAB| Section 4.5 (:external+lockss-manual:ref:`Mail Settings`)

            *  |TAB| Section 4.6 (:external+lockss-manual:ref:`Preservation Network Settings`)

            *  |TAB| Section 4.7 (:external+lockss-manual:ref:`Web User Interface Settings`)

            *  |TAB| Section 4.8 (:external+lockss-manual:ref:`Storage Area Settings`)

            *  |TAB| Section 4.9 (:external+lockss-manual:ref:`Database Settings`)

            *  |TAB| Section 4.10 (:external+lockss-manual:ref:`Stack Component Settings`)

            *  |TAB| Section 4.11 (:external+lockss-manual:ref:`Web Replay Settings`)

            *  |TAB| Section 4.12 (:external+lockss-manual:ref:`Final Steps of configure-lockss`)

------------------
Running LOCKSS 2.x
------------------

Now start the LOCKSS 2.x system. Follow these steps:

1. Run the following command on your LOCKSS 2.x host [#fn-same-host]_ (still as the ``lockss`` user, still in the :external+lockss-manual:ref:`LOCKSS Installer Directory`):

   .. code-block:: shell

      scripts/start-lockss --wait

   If the startup process goes well, you will see:

   .. code-block:: text

      LOCKSS services are ready; AUs may still be loading.

   and control will be returned to the command line.

   .. tip::

      During this first startup, hundreds of megabytes of container images will be downloaded, which can take many minutes on a slow network.

2. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a :ref:`New-Host Migration`, follow these steps:

         a. In a browser, go to the URL :samp:`http://{<lockss2host>}:24602/DaemonStatus`, where :samp:`{<lockss2host>}` represents the host name of your LOCKSS 2.x host (for example ``lockss2.myuniversity.edu``). Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in.

         b. Click on :guilabel:`Admin Access Control` in the top-right menu.

         c. If needed, allow the IP address of your existing LOCKSS 1.x host by entering it or its subnet in :guilabel:`Allow Access`, then click the :guilabel:`Update` button.

         d. If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes, see the :doc:`lcap-ssl` chapter.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a :ref:`Same-Host Migration`, go to the URL :samp:`http://{<lockss2host>}:24602/DaemonStatus`, where :samp:`{<lockss2host>}` represents the host name of your LOCKSS 2.x host [#fn-same-host]_ (for example ``lockss2.myuniversity.edu``). Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in. Your LOCKSS 2.x system is now ready for the next phase.

----

.. rubric:: Footnotes

.. [#fn-same-host]

   |FN_SAME_HOST|
