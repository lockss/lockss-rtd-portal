.. include:: subst.rst

================================================
Appendix: Instructions for Users of LOCKSS Nodes
================================================

This guide is primarily aimed at system administrators of LOCKSS nodes; **this appendix is aimed at users of LOCKSS nodes**, describing important information about using the LOCKSS node during and after the migration.

:numref:`Migration Overview` (:ref:`Migration Overview`) provides a general idea of what the migration from LOCKSS 1.x to 2.x looks like:

*  An initially empty LOCKSS 2.x instance is installed and configured, and the migration process is set up. At this stage, you continue to interact with the LOCKSS 1.x instance only, as normal.

*  Then the |PRINCIPAL| begins, during which the LOCKSS 2.x instance is gradually populated with the data preserved in the LOCKSS 1.x instance, while the latter is gradually depleted. During this phase, the LOCKSS 1.x and 2.x instances work in tandem to provide LOCKSS functionality. You will largely interact with the LOCKSS 1.x instance, **with some exceptions**; see :numref:`Using LOCKSS During the Migration` (:ref:`Using LOCKSS During the Migration`).

*  Finally, the LOCKSS 1.x instance is taken out of commission, and the LOCKSS 2.x instance takes over, providing all LOCKSS functionality. From this point on, you will interact with the LOCKSS 2.x instance.

---------------------------------
Using LOCKSS During the Migration
---------------------------------

Web User Interface During the Migration
=======================================

During the |PRINCIPAL|, a given archival unit (AU) is available in either the LOCKSS 1.x instance or the LOCKSS 2.x instance (except for the time when it is its turn to go through the migration process, during which it is temporarily unavailable in both). If you wish to interact with the AU in the Web user interface (UI), such as looking at its state or causing crawls or polls in the debug panel, you will need to use either the LOCKSS 1.x Web UI or the LOCKSS 2.x Web UI accordingly, depending on where the AU is active.

Deleting AUs During the Migration
=================================

During the |PRINCIPAL|, should the need to delete AUs that have been migrated to the LOCKSS 2.x instance arise, **wait until after the migration is complete before deleting such AUs**.

Subscription Manager During the Migration
=========================================

During the |PRINCIPAL|, **do not use the subscription manager in LOCKSS 1.x, use the subscription manager in LOCKSS 2.x**. However, please note that changes to subscription information will not take effect until the migration is complete.

--------------------------------
Using LOCKSS After the Migration
--------------------------------

Once the migration is completed, the LOCKSS 1.x is taken out of commission and you will interact with the LOCKSS 2.x instance only.

Rather than all functionality under one monolithic roof as in LOCKSS 1.x, LOCKSS 2.x functionality is split up into multiple services:

*  The LOCKSS Repository Service, responsible for object storage at a low level.

*  The LOCKSS Configuration Service, for example where you might add AUs and interact with the subscription manager.

*  The LOCKSS Crawler Service, responsible for Web crawls.

*  The LOCKSS Poller Service, responsible for polling and voting, as well as the ServeContent Web replay engine and the OpenURL resolver.

*  The LOCKSS Metadata Service, responsible for metadata extraction jobs and metadata queries.

The first three are always running; the other two depend on which functionality is needed and configured on the node.

The Web user interface (UI) is therefore also split into corresponding pieces, each on its own port number; see :external+lockss-manual:ref:`Network Ports` in the |MANUAL|. The layout of the LOCKSS 2.x Web UIs is intentionally similar to that of LOCKSS 1.x, with minor exceptions:

*  The top-left corner of the each screen now has a list of LOCKSS services that have been configured, so you can navigate to each, and the service you are currently interacting with is labeled at the top of each screen. (Please note that navigating from one service UI to another may require entering your username and password for each.)

*  A few areas of functionality may have a local instance decorated with the word :guilabel:`local` to distinguish it from the one that is considered the primary instance for the node as a whole. For example:

   *  If you select :guilabel:`Expert Config`, you will be taken to an expert config screen managed by the LOCKSS Configuration Service, and configuration values entered there will apply to the node as a whole, but if you select the :guilabel:`local` instance of :guilabel:`Expert Config`, you will be taken to an expert config screen applying only to the service you are currently interacting with.

   *  If you select :guilabel:`Crawl Status`, you will be taken to a screen managed by the LOCKSS Crawler Service, and see the status of Web crawls for the node. But the LOCKSS Configuration Service needs a little Web crawling functionality, to crawl plugin registries. In its UI, if you select the :guilabel:`local` instance of :guilabel:`Crawl Status`, you will be taken to a screen that functions the same way but applies only to plugin regsitry crawls.

LOCKSS 2.x is programmable via REST APIs. However, a LOCKSS 2.x node can also be configured to run the LOCKSS SOAP Compatibility Service so client requests using the legacy SOAP APIs can continue to work while new tools using the REST APIs are deployed.

Note that the LOCKSS Repository Service and the LOCKSS SOAP Compatibility Service do not have Web UIs of their own.

For more information about LOCKSS 2.x, see the |MANUAL|.
