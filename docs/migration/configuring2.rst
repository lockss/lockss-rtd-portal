==========================================
Configuring LOCKSS 2.0-beta1 for Migration
==========================================

The next task in the migration process is to configure LOCKSS 2.0-beta1 for migration on your LOCKSS 2.x host.

-------------------------------------------
Importing the LOCKSS 1.x Configuration File
-------------------------------------------

First, you will need to make the LOCKSS 1.x configuration file available to the LOCKSS 2.x configuration script. This depends on your :ref:`Migration Scenario`:

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a new-host migration, you need to copy the LOCKSS 1.x configuration file :file:`/etc/lockss/config.dat` from your LOCKSS 1.x host to somewhere on your LOCKSS 2.x host, for example using :program:`scp`. The LOCKSS 2.x configuration script will later prompt you for the path of this file on the LOCKSS 2.x host (by default, :file:`/tmp/v1config.dat`).

      If you are not able to copy the LOCKSS 1.x configuration file to the LOCKSS 2.x host, you can still configure LOCKSS 2.x for migration, but you will be prompted to supply more information.

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a same-host migration, the LOCKSS 2.x configuration script will find the LOCKSS 1.x configuration file :file:`/etc/lockss/config.dat` directly, so you do not need to do anything here.

---------------------------------------------
Running :program:`configure-lockss --migrate`
---------------------------------------------

The second part of this phase is to run the :program:`configure-lockss` tool with the special ``--migrate`` option. This will proceed largely as described in chapter 4 (:doc:`lockss-manual:configuring`) of the LOCKSS 2.0-beta1 System Manual, **but with a number of notable differences described here.** Follow these steps:

1. Per section 4.1 (:ref:`lockss-manual:Configuration Prerequisites`) of the LOCKSS 2.0-beta1 System Manual, gather information about your LOCKSS 2.x host (which is a new host if doing a new-host migration or your LOCKSS 1.x host if doing a same-host migration).

2. Run the following command as the ``lockss`` user in the LOCKSS 2.x installation directory:

   .. code-block:: shell

      scripts/configure-lockss --migrate

   This is almost the same as section 4.2 (:ref:`lockss-manual:invoking-configure-lockss`) of the LOCKSS 2.0-beta1 System Manual, but with the additional ``--migrate`` option.

3. The first prompt, :guilabel:`Command to use to execute kubectl commands`, is the same as that from section 4.3 (:ref:`lockss-manual:Kubernetes Settings`) of the LOCKSS 2.0-beta1 System Manual. If you are using the K3s Kubernetes environment that ships with LOCKSS 2.x, the proposed value is already correct; hit :kbd:`Enter` to accept it. (Otherwise, enter the command needed to invoke :program:`kubectl` in your environment.)

4. This step depends on your :ref:`Migration Scenario`:

   .. tab-set::

      .. tab-item:: New-Host Migration
         :sync: newhost

         If you are doing a new-host migration, follow these steps:

         a. You will receive the following prompt:

            :guilabel:`Did you copy a LOCKSS 1.x config.dat file to this host?`

            *  If you enter :kbd:`Y` for "yes", you will then receive the following prompt:

               :guilabel:`Location of copied LOCKSS 1.x config.dat file`

               Enter the path of the copied LOCKSS 1.x configuration file, or hit :kbd:`Enter` to accept the default in square brackets if it matches the path you used.

            *  If you enter :kbd:`N` for "no", you will have to manually enter a number of values reflecting your LOCKSS 1.x configuration in the next step (instead of the values being imported directly from your copied LOCKSS 1.x configuration file).

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

            corresponding to sections 4.4 (:ref:`lockss-manual:Network Settings`) through 4.6 (:ref:`lockss-manual:Preservation Network Settings`) of the LOCKSS 2.0-beta1 System Manual.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         If you are doing a same-host migration, follow these steps:

         a. Data will be imported from the LOCKSS 1.x configuration file, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

            *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

            *  :guilabel:`IP address of this machine`

            *  :guilabel:`Initial subnet(s) for admin UI access`

            *  :guilabel:`LCAP protocol port`

            corresponding to section 4.4 (:ref:`lockss-manual:Network Settings`) of the LOCKSS 2.0-beta1 System Manual.

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

            corresponding to sections 4.5 (:ref:`lockss-manual:Mail Settings`) and 4.6 (:ref:`lockss-manual:Preservation Network Settings`) of the LOCKSS 2.0-beta1 System Manual.

5. Follow the instructions from sections 4.7 (:ref:`lockss-manual:Web User Interface Settings`) through 4.12 (:ref:`Final Steps`) of the LOCKSS 2.0-beta1 System Manual.

------------------------
Running LOCKSS 2.0-beta1
------------------------

Now start the LOCKSS 2.0-beta1 system. Follow these steps:

1. Run the following command:

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

         a. In a browser, go to the URL :samp:`http://{<lockss2.myuniversity.edu>}:24621/DaemonStatus`, where :samp:`{<lockss2.myuniversity.edu>}` represents the host name of your LOCKSS 2.x host. Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in.

         b. Click on :guilabel:`Admin Access Control` in the top-right menu.

         c. If needed, allow the IP address of your existing LOCKSS 1.x host by entering it or its subnet in :guilabel:`Allow Access`, then click the :guilabel:`Update` button.

      .. tab-item:: Same-Host Migration
         :sync: samehost

         In a browser, go to the URL :samp:`http://{<lockss2.myuniversity.edu>}:24621/DaemonStatus`, where :samp:`{<lockss2.myuniversity.edu>}` represents the host name of your LOCKSS 2.x host. Log in using the Web user interface username and password you specified during the configuration process. If the red warning "This LOCKSS box is still starting" is shown, wait a moment and hit refresh until it is gone and you can log in. Your LOCKSS 2.x system is now ready for the next step.
