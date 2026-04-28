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

            .. compound::

               For example, you might use :program:`scp` on your LOCKSS 1.x host:

                  :samp:`scp /etc/lockss/config.dat {<username>}@{<lockss2host>}:{/path/to/lockss1_config_file.dat}`

               or something similar.

            If you are unable to copy the LOCKSS 1.x configuration file to your LOCKSS 2.x, you can still configure LOCKSS 2.x for migration, but you will be prompted to supply more information, which you will have to enter accurately from the corresponding LOCKSS 1.x values.

         b. .. compound::

               Ensure that the LOCKSS 1.x configuration file :samp:`{/path/to/lockss1_config_file.dat}` is readable by all on the LOCKSS 2.x host. For example, you can do this as ``root`` on the LOCKSS 2.x host with:

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

1. Perform |TAB| Section |CONFIGURE_CHAPTER|.1 (:external+lockss-manual:ref:`Gathering Configuration Information`) of the |MANUAL| normally, by gathering information about your LOCKSS 2.x host [#fn-same-host]_.

2. Perform a **modified** version of |TAB| Section |CONFIGURE_CHAPTER|.2 (:external+lockss-manual:ref:`Invoking configure-lockss`) of the |MANUAL|:

   a. :bdg-success:`new-host migration only`

      .. compound::

         First, if you are doing a :ref:`New-Host Migration`, double-check that you are in a shell console for your LOCKSS 2.x host, for example by typing:

         .. code-block:: shell

            hostname

         and verifying that the output is the expected name of your LOCKSS 2.x host.

   b. .. compound::

         Next, double-check that you are in a shell console acting as the ``lockss`` user by typing:

         .. code-block:: shell

            whoami

         and verifying that the output is ``lockss``.

   c. .. compound::

         Navigate to the |LOCKSS_INSTALLER_DIRECTORY|, symbolically:

         :samp:`cd {<LOCKSS_INSTALLER_DIR>}`

   d. .. compound::

         Run this command:

         .. code-block:: shell

            scripts/configure-lockss --migrate

.. note::

   This is as far as the review to evolve from 1.78/2.0-beta1 to 1.79/2.0-beta2 has gone for now. Anything beyond this point is definitely from the 1.78/2.0-beta1 guide.

2. Run the following command as the ``lockss`` user in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/configure-lockss -m

   which is short for:

   .. code-block:: shell

      scripts/configure-lockss --migrate

   This is almost the same as section 4.2 (:ref:`lockss-manual:invoking-configure-lockss`) of the :doc:`lockss-manual:index`, but with the additional ``--migrate`` option.

3. The first prompt, :guilabel:`Command to use to execute kubectl commands`, is the same as that from section 4.3 (:ref:`lockss-manual:Kubernetes Settings`) of the :doc:`lockss-manual:index`. If you are using the K3s Kubernetes environment that ships with LOCKSS 2.x, the proposed value is already correct; hit :kbd:`Enter` to accept it. Otherwise, enter the command needed to invoke :program:`kubectl` in your environment.

4. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a **new-host migration**, follow these steps:

         a. You will receive the following prompt:

            :guilabel:`Did you copy a LOCKSS 1.x config.dat file to this host?`

            *  If you enter :kbd:`Y` for "yes", you will then receive the following prompt:

               :guilabel:`Location of copied LOCKSS 1.x config.dat file`

               Enter the path of the copied LOCKSS 1.x configuration file, or hit :kbd:`Enter` to accept the default in square brackets (:file:`/tmp/v1config.dat`) if it matches the path you used.

            *  If you enter :kbd:`N` for "no", you will have to manually and accurately enter a number of values reflecting your LOCKSS 1.x configuration in the next step (instead of the values being imported directly from your copied LOCKSS 1.x configuration file).

         b. You will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. (If you answered :kbd:`N` in the previous step because you could not copy your LOCKSS 1.x configuration file to the LOCKSS 2.x host, there will be no imported values offered as defaults and you will have to manually enter the values reflecting your LOCKSS 1.x configuration.)

            These confirmation prompts are as follows:

            *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

            *  :guilabel:`IP address of this machine`

            *  :guilabel:`Initial subnet(s) for admin UI access`

            *  :guilabel:`LCAP protocol port`

            *  :guilabel:`Is this machine behind NAT?`

            *  :guilabel:`Mail relay for this machine`

            *  :guilabel:`Does the mail relay <mailhost> need a username and password?`

            *  :guilabel:`E-mail address for administrator`

            *  :guilabel:`Configuration URL`

            *  :guilabel:`Configuration proxy (host:port)`

            *  :guilabel:`Preservation group(s)`

            corresponding to these sections of the :doc:`lockss-manual:index`:

            *  Section 4.4 (:ref:`lockss-manual:Network Settings`)

            *  Section 4.5 (:ref:`lockss-manual:Mail Settings`)

            *  Section 4.6 (:ref:`lockss-manual:Preservation Network Settings`)

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a **same-host migration**, follow these steps:

         a. Data will be imported from the LOCKSS 1.x configuration file :file:`/etc/lockss/config.dat` directly, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

            *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

            *  :guilabel:`IP address of this machine`

            *  :guilabel:`Initial subnet(s) for admin UI access`

            *  :guilabel:`LCAP protocol port`

            corresponding to section 4.4 (:ref:`lockss-manual:Network Settings`) of the :doc:`lockss-manual:index`.

         b. You will receive the following prompt:

            :guilabel:`Temporary LOCKSS 2.x LCAP port`

            Enter an LCAP port different from the one used by LOCKSS 1.x, for use during migration, or hit :kbd:`Enter` to accept the suggested value in square brackets.

         c. You will be asked to confirm more configuration values. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

            *  :guilabel:`Is this machine behind NAT?`

            *  :guilabel:`Mail relay for this machine`

            *  :guilabel:`Does the mail relay <mailhost> need a username and password?`

            *  :guilabel:`E-mail address for administrator`

            *  :guilabel:`Configuration URL`

            *  :guilabel:`Configuration proxy (host:port)`

            *  :guilabel:`Preservation group(s)`

            corresponding to these sections from the :doc:`lockss-manual:index`:

            *  Section 4.5 (:ref:`lockss-manual:Mail Settings`)

            *  Section 4.6 (:ref:`lockss-manual:Preservation Network Settings`)

5. Follow the instructions from the following sections of the :doc:`lockss-manual:index`:

            *  Section 4.7 (:ref:`lockss-manual:Web User Interface Settings`)

            *  Section 4.8 (:ref:`lockss-manual:Storage Areas`)

            *  Section 4.9 (:ref:`lockss-manual:Database Settings`)

            *  Section 4.10 (:ref:`lockss-manual:LOCKSS Services`)

            *  Section 4.11 (:ref:`lockss-manual:Web Replay Settings`)

            *  Section 4.12 (:ref:`lockss-manual:Final Steps`)

------------------
Running LOCKSS 2.x
------------------

Now start the LOCKSS 2.x system. Follow these steps:

1. Run the following command as ``lockss`` in the :ref:`lockss-manual:LOCKSS Installer Directory`:

   .. code-block:: shell

      scripts/start-lockss -w

   which is short for:

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

         If you are doing a **new-host migration**, follow these steps:

         a. In a browser, go to the URL :samp:`http://{<lockss2.myuniversity.edu>}:24621/DaemonStatus`, where :samp:`{<lockss2.myuniversity.edu>}` represents the host name of your LOCKSS 2.x host. Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in.

         b. Click on :guilabel:`Admin Access Control` in the top-right menu.

         c. If needed, allow the IP address of your existing LOCKSS 1.x host by entering it or its subnet in :guilabel:`Allow Access`, then click the :guilabel:`Update` button.

         d. If your LOCKSS network uses LCAP SSL keystores for encrypted communication between nodes, see the :doc:`lcap-ssl` chapter.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a **same-host migration**, go to the URL :samp:`http://{<lockss.myuniversity.edu>}:24621/DaemonStatus` in a browser, where :samp:`{<lockss.myuniversity.edu>}` represents the host name of your LOCKSS host [#fn-same-host]_. Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in. Your LOCKSS 2.x system is now ready for the next phase.

----

.. only:: html

   .. rubric:: Footnotes

.. [#fn-same-host]

   |FN_SAME_HOST|
