==============================================
Frequently Asked Questions about the Migration
==============================================

.. warning::

   This page is under construction. LOCKSS 1.78 and LOCKSS 2.0-beta1 have not yet been released.

   .. image:: https://openmoji.org/php/download_asset.php?type=emoji&emoji_hexcode=1F6A7&emoji_variant=color
      :target: #
      :align: center
      :width: 256px
      :alt: Image of a road construction sign

.. rubric:: Is commissioning a new host required to install LOCKSS 2.x?

No; see this :ref:`discussion of the pros and cons of commissioning a new host <new-host-recommended>`.

.. rubric:: Instead of migrating, could I install LOCKSS 2.x and let it recrawl all the content?

This is not a viable option. Migration is admittedly slow, but nowhere as slow as the crawl rate limits imposed by publisher and content provider Web sites. Additionally, not all of the content preserved in your current LOCKSS node will be available to recrawl.
