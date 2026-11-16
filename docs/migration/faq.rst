==============================================
Frequently Asked Questions about the Migration
==============================================

.. rubric:: General Questions
   :heading-level: 2

.. rubric:: Is commissioning a new host required to install LOCKSS 2.x?
   :name: Is commissioning a new host required to install LOCKSS 2.x?

No, but it is recommended. See :ref:`Why is a new-host migration recommended? <Why is a new-host migration recommended?>` in :numref:`New-Host Migration` (:ref:`New-Host Migration`).

.. rubric:: Instead of migrating, could I install LOCKSS 2.x and let it recrawl all the content?
   :name: Instead of migrating, could I install LOCKSS 2.x and let it recrawl all the content?

This is not a viable option. Migration may be slow, but nowhere as slow as the crawl rate limits imposed by publisher and content provider Web sites. Additionally, not all of the content preserved in your current LOCKSS node will be available to recrawl.

.. rubric:: Troubleshooting
   :heading-level: 2

.. rubric:: In a same-host migration with containerized LOCKSS 1.x, what to do if I get the message "Could not connect to database" when I click "Next" in the Migration Settings screen?

In a same-host migration with containerized LOCKSS 1.x, you need to allow the IP address of the LOCKSS 1.x container access to your LOCKSS 2.x system. Please refer to the dedicated section for this in :numref:`Running LOCKSS 2.x` (:ref:`Running LOCKSS 2.x`): in step (2), select the section for a same-host migration, and follow the instruction in step (b).

.. rubric:: What should I do if LOCKSS 1.x restarts during the primary migration phase?
   :name: What should I do if LOCKSS 1.x restarts during the primary migration phase?

.. COMMENT FIXME

*This section is under construction.*

.. rubric:: What should I do if LOCKSS 2.x restarts during the primary migration phase?
   :name: What should I do if LOCKSS 2.x restarts during the primary migration phase?

.. COMMENT FIXME

*This section is under construction.*
