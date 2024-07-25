==========================================
Configuring LOCKSS 2.0-beta1 for Migration
==========================================

The next task in the migration process is to configure LOCKSS 2.0-beta1 for migration.

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

1. Per section 4.1 (:ref:`lockss-manual:before-invoking-configure-lockss`) of the LOCKSS 2.0-beta1 System Manual, gather information about your LOCKSS 2.x host (which is a new host if doing a new-host migration or your LOCKSS 1.x host if doing a same-host migration).

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

      1. You will receive the following prompt:

         :guilabel:`Did you copy a LOCKSS 1.x config.dat file to this host?`

         Enter :kbd:`Y` for "yes" (unless you were not able to copy the LOCKSS 1.x configuration file from the LOCKSS 1.x host, in which case you will need FIXME).

      2. You will then receive the following prompt:

         :guilabel:`Location of copied LOCKSS 1.x config.dat file`

         Enter the path of the copied LOCKSS 1.x configuration file, or hit :kbd:`Enter` to accept the default in square brackets if it matches the path you used.

      3. Data will be imported from the LOCKSS 1.x configuration file, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

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

      1. Data will be imported from the LOCKSS 1.x configuration file, and you will be asked to confirm each configuration value. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

         *  :guilabel:`Fully qualified hostname (FQDN) of this machine`

         *  :guilabel:`IP address of this machine`

         *  :guilabel:`Initial subnet(s) for admin UI access`

         *  :guilabel:`LCAP protocol port`

         corresponding to section 4.4 (:ref:`lockss-manual:Network Settings`) of the LOCKSS 2.0-beta1 System Manual.

      2. You will receive the following prompt:

         :guilabel:`Temporary LOCKSS 2.x LCAP port`

         Enter an LCAP port different from the one used by LOCKSS 1.x, for use during migration, or hit :kbd:`Enter` to accept the suggested value in square brackets.

      3. You will be asked to confirm more configuration values. You can do so by simply hitting :kbd:`Enter` for each, to accept the imported value in square brackets. These confirmation prompts are as follows:

         *  :guilabel:`Is this machine behind NAT?`

         *  :guilabel:`Mail relay for this machine`

         *  :guilabel:`Does the mail relay <mailhost> need a username and password?`

         *  :guilabel:`E-mail address for administrator`

         *  :guilabel:`Configuration URL`

         *  :guilabel:`Configuration proxy (host:port)`

         *  :guilabel:`Preservation group(s)`

         corresponding to sections 4.5 (:ref:`lockss-manual:Mail Settings`) and 4.6 (:ref:`lockss-manual:Preservation Network Settings`) of the LOCKSS 2.0-beta1 System Manual.
