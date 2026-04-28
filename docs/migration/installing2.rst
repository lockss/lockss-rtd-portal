=====================
Installing LOCKSS 2.x
=====================

.. image:: laaws-migration-steps-installing2.png
   :align: center
   :alt: A diagram of seven consecutive arrow-shaped boxes, representing from left to right the steps of the migration workflow from LOCKSS 1.x to LOCKSS 2.x. The first two boxes, successively labeled "Upgrading LOCKSS 1.x" and "Preparing the LOCKSS 2.x Host", are colored in light blue, indicating completed steps. The third box labeled "Installing LOCKSS 2.x" is highlighted in yellow, indicating the step in progress. The last four boxes, successively labeled "Configuring LOCKSS 2.x for Migration", "Configuring LOCKSS 1.x for Migration", "Running the Migrator" and "Reconfiguring LOCKSS 2.x for Normal Operation", are not colored, indicating future steps.

The next task in the migration process is to install LOCKSS |UPGRADE_TO_PATCH|, the latest version of LOCKSS |UPGRADE_TO_MINOR|, on your LOCKSS 2.x host [#fn-same-host]_.

The process depends on your :ref:`Migration Scenario`:

.. |INSTALL_CHAPTER| replace:: 2

.. tab-set::

   .. tab-item:: New-Host Migration
      :sync: newhost

      If you are doing a :ref:`New-Host Migration`, follow all instructions in Chapter |INSTALL_CHAPTER| (:external+lockss-manual:doc:`installing/index`) of the :external+lockss-manual:doc:`index` on your LOCKSS 2.x host:

      *  Section |INSTALL_CHAPTER|.1 (:external+lockss-manual:doc:`installing/user`)

      *  Section |INSTALL_CHAPTER|.2 (:external+lockss-manual:doc:`installing/downloading`)

      *  Section |INSTALL_CHAPTER|.3 (:external+lockss-manual:doc:`installing/running`)

   .. tab-item:: Same-Host Migration
      :sync: samehost

      If you are doing a :ref:`Same-Host Migration`, follow the instructions in the following sections of the :external+lockss-manual:doc:`index` on your LOCKSS 1.x host [#fn-same-host]_:

      *  Section |INSTALL_CHAPTER|.1.1 (:external+lockss-manual:ref:`Establishing a root Session`)

      *  Section |INSTALL_CHAPTER|.2 (:external+lockss-manual:doc:`installing/downloading`)

      *  Section |INSTALL_CHAPTER|.3 (:external+lockss-manual:doc:`installing/running`)

      Note that Section |INSTALL_CHAPTER|.1.2 is not performed in this scenario.

----

.. only:: html

   .. rubric:: Footnotes

.. [#fn-same-host]

   If your :ref:`Migration Scenario` is a :ref:`Same-Host Migration`, your LOCKSS 1.x host and your LOCKSS 2.x host are the same host.
