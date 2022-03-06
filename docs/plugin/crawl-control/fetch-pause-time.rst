================
Fetch Pause Time
================

Plugin Key
   ``au_def_pause_time``

Plugin Value Type
   :ref:`long-value`

Sample
   .. code-block:: xml

        <entry>
          <string>au_def_pause_time</string>
          <long>3000</long>
        </entry>

Description
   The minimum amount of time (in milliseconds) between two fetches of consecutive URLs in the crawl of an AU.

   The most common value in the Global LOCKSS Network is ``3000`` for no more frequently than every 3 seconds.
