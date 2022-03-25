======================
LOCKSS Plugin Concepts
======================

-------------
LOCKSS Plugin
-------------

A **LOCKSS plugin** is a bundle of descriptors, rules and code loaded into the LOCKSS software, describing how to harvest and process a preservation target.

A preservation target might be an individual Web site, or a family of related Web sites (for instance all Web sites powered by the same content publishing platform), or a corpus of Web-accessible resources discovered through some interface (for example an OAI-PMH server, or a service with an API).

-------------
Archival Unit
-------------

In almost all cases, the preservation target is preserved in plugin-defined chunks called **archival units** (or **AUs** for short).

What these chunks are depends on the situation, but generally the goal is to split the preservation target into chunks of manageable size that are expected to become unchanging eventually, for instance time-bound chunks. For example, in a LOCKSS plugin for a preservation target that consists of serial publications, an AU could be equated with one volume or one year of one publication.

-------------------------------
Plugin Configuration Parameters
-------------------------------

A LOCKSS plugin leaves placeholders in rules and code called :doc:`../identification/plugin-parameters`. An AU is identified by a plugin and values for each of the plugin's configuration parameters. When the parameter values for an AU are substituted for the placeholders in the plugin's rules and code, the result is rules and code suited for that specific AU.

Typical plugin parameters include a URL prefix or URL fragment (e.g. base URL, directory name...), an identifier (e.g. ISSN of a journal, ISBN of a book, publication code, database identifier of an object...), a year or a date range, a part number (e.g. volume number, numbered subdivision...), and more.

-------------
Plugin Format
-------------

A LOCKSS plugin is expressed as a mapping from keys to values. Except for rare exceptions that are built into the LOCKSS software, LOCKSS plugins consist of an XML file containing these key-value pairs, accompanied by optional Java class files (compiled Java code), bundled together in a JAR file (a Zip file of Java class files and associated metadata).

-------------------------
Plugin Feature Categories
-------------------------

This guide groups plugin components into conceptual categories, which are introduced briefly in subsections below and have a dedicated section each in this guide:

*  :ref:`Identification Features`: features related to the identification, versioning and parameterization of the plugin.

*  :ref:`Crawl Control Features`: features related to the definition and behavior of content crawls.

*  :ref:`Crawl Validation Features`: features related to content validation in the context of a crawl.

*  :ref:`Poll Control Features`: features that influence the operation of the LOCKSS audit and repair protocol.

*  :ref:`Hash Filtering Features`: features related to content canonicalization for inter-node comparison purposes.

*  :ref:`Metadata Extraction Features`: features related to the extraction and interpretation of metadata from preserved content.

*  :ref:`Web Replay Features`: features related to supporting the replay of Web content.

*  :ref:`Inheritance Features`: features related to sharing similar behavior among a set of plugins.

*  :ref:`Miscellaneous Features`.

-----------------------
Identification Features
-----------------------

All plugins define a number of identifying aspects:

*  **Plugin identifier**: a unique identifier for the plugin.

*  **Plugin name**: a user-friendly name for the plugin.

*  **Plugin version**: the plugin's version number.

*  **Plugin configuration parameters**: a list of configuration parameter descriptors, defining the placeholders in use in the plugin's rules and code.

*  **AU name**: a rule to generate a default name for each AU based on the plugin name and the plugin parameters, in the event the AU does not have a name in the AU inventory.

Optionally:

*  **Required daemon version**: the release number of the earliest version of the LOCKSS software that supports all the features required by the plugin.

The :doc:`../identification/index` chapter covers these plugin aspects.

----------------------
Crawl Control Features
----------------------

The following plugin aspects can be involved in controlling how content is crawled:

*  **Start URLs**: one or more URLs from which the crawl of an AU begins.

*  **Crawl seed**: in lieu of a list of start URLs, code called a crawl seed can compute the starting points of the crawl of an AU, for instance by interacting with an API.

*  **Permission URLs**: one or more URLs giving the LOCKSS software permission to crawl an AU, if permission is not given on the start URLs.

*  **Per-host permission path**: path where permission statement may be found on hosts not listed in start URLs or Permission URLs. Useful for sites such as Internet Archive that have banks of similar hosts with unpredictable names.

*  **Permitted host pattern**: pattern rules to allow collection from hosts that cannot explicitly grant permission, for example CDN hosts used to distribute standard components used by web sites such as Javascript libraries.

*  **Crawl rules**: sequential rules determining if a URL discovered during the crawl of an AU should in turn be fetched as part of the AU or not.

*  **Crawl window**: a crawl window controls what times of day or days of the week crawls against the preservation target are allowed; by default an AU is eligible to crawl at any time.

*  **Recrawl interval**: the amount of time before an AU that has previously been crawled successfully is eligible to attempt crawling again.

*  **Refetch depth**: number of links away from the start URL(s) that will be fetched by normal crawls. Deep crawls may be used to cause all URLs in an AU to be refetched (subject to If-Modified-Since).

*  **Fetch pause time**: the minimum amount of time between two fetches of consecutive URLs in the crawl of an AU.

*  **Crawl rate limiter**: fine grained control of the maximum rate at which URLs may be fetched, based on media type, URL pattern, day of week or time of day.

*  **Crawl pool**: controls the number of simultaneous crawls that may be running against any one host or platform.

*  **Response handler**: custom action taken when fetching a URL results in certain error conditions or HTTP response codes.

*  **URL normalizer**: code that normalizes URL variants into canonical URLs.

*  **Link extractor**: media type-specific code that extracts or extrapolates URLs from the collected content, to allow the crawler to follow links. Link extractors are built in for most standard media types that contain links (html, css, pdf, etc.); plugins may supply link extractors for additional media types or extend the built in extractors to handle additional constructs.

*  **Content filter**: code that filters content before a link extractor is run. Supplements the crawl rules in cases where more context it needed to determine whether a link should be followed.

*  **URL fetcher**: custom code to fetch URLs, for cases that require a more elaborate interaction than a single GET.

*  **URL consumer**: custom code to store collected URLs in the repository.  E.g., for sites that redirect permanent URLs to one-time URLs, to store the content at the permanent URL, or to adapt to sites undergoing HTTP to HTTPS transitions

The :doc:`../crawl-control/index` chapter covers these plugin aspects.

-------------------------
Crawl Validation Features
-------------------------

A plugin can optionally define aspects that help verify that the crawl is obtaining the content it is supposed to:

*  **Redirect to login URL pattern**: determines whether an HTTP redirect returned by the site is actually a redirect to a login page.

*  **Login page checker**: determines if a URL fetched successfully (HTTP 200) is in fact a login page or some other undesirable substitute for the intended content.

*  **Content validator**: code that determines if certain URLs pass a validation test, most often a media type check or format validation test.

*  **Substance patterns**: pattern rules to check that at least one URL processed during the crawl of an AU is substantive (non-trivial), for example to verify that at least one substantive object was processed rather than just tables of contents.

*  **Substance predicate**: code that determines whether a collected URL has substantive content. Alternative to substance patterns, allows programmatic substance determination.

The :doc:`../crawl-validation/index` chapter covers these plugin aspects.

---------------------
Poll Control Features
---------------------

These plugin elements include:

*  **Exclude URLs**: patterns for URLs that should not be included in polls.

*  **Poll result weight**: patterns for URLs to allow some disagreements to influence the results more than others.

*  **Repair from publisher when too close**: instructs the poller to fetch a new copy of files from the origin site when too-few peers agree on the content.

*  **Repair from peer if missing**: patterns for URLs that should be fetched from a peer, when the poller detects that they're missing.

The :doc:`../poll-control/index` chapter covers these plugin aspects.

-----------------------
Hash Filtering Features
-----------------------

Many plugins designed to harvest and preserve Web-native content need to go to some lengths to enable comparison of (hashes of) content between the nodes in a LOCKSS network, because fetching a given URL is likely to result in non-identical results from node to node, or from fetch to fetch on the same node. This is due to a raft of causes: advertising banners, personalization ("You are logged in as...", "Downloaded by..."), time-variable content (current date, news ticker), location-variable content (CDN URLs, institution-dependent integration with a link resolver), related content widgets ("You may also be interested in..."), reverse citations and pingbacks ("This page has been referenced by..."), tracking data and watermarking embedded in the content, temporary system messages ("The site will be down for maintenance from..."), and more. Some of these variations now appear outside HTML in media types like PDF or Microsoft PowerPoint files.

To canonicalize content before comparison between nodes in the LOCKSS audit and repair protocol, a plugin can define a **hash filter** for each affected media type. The LOCKSS plugin framework offers a variety of utility classes specifically for **HTML** and **PDF** filtering, as part of its general content filtering framework.

See the :doc:`../hash-filtering/index` chapter for more details.

----------------------------
Metadata Extraction Features
----------------------------

The LOCKSS plugin framework enables the extraction of metadata from ingested content, through an extensible metadata extraction framework; a plugin can optionally define:

*  **Article iterator**: code that traverses the AU and enumerates all the logical items (journal articles, electronic books, electronic theses and dissertations, repository objects...) found in it, as bundles of related URLs.

*  **Article metadata extractor**: code that extracts metadata from the logical items enumerated by the article iterator using file metadata extractors, and that post-processes and stores the extracted metadata in the LOCKSS metadata database.

*  **File metadata extractor**: code that extracts metadata from files with a given media type.

The :doc:`../metadata-extraction/index` chapter covers these plugin aspects.

-------------------
Web Replay Features
-------------------

A plugin can define optional elements that are applied by the embedded ServeContent Web replay engine:

*  **Link rewriter**: code used by the built-in ServeContent replay engine that changes intra-site links or other URLs to point back to the ServeContent host. Link rewriters are built in for most standard media types that contain links (html, css, javascript, etc.); plugins may supply link rewriters for additional media types or extend the built in rewriters to handle additional constructs.

*  **Rewrite HTML meta tags**: pattern that determines which HTML meta tags have values that should be rewritten during web replay.  Some tags (e.g., citation URLs) should not be rewritten to point back to the ServeContent host.

The :doc:`../web-replay/index` chapter covers these plugin aspects.

--------------------
Inheritance Features
--------------------

Commonalities among a set of similar plugins may be abstracted out in to a parent plugin, to reduce duplication. Each child plugin inherits all the elements of the parent plugin.

*  **Parent plugin**: names the parent plugin from which this plugin should inherit elements.

*  **Parent plugin version**: the version number of the parent plugin, to guard against changed to a parent inadvertently changing the behavior of a child plugin.

The :doc:`../inheritance/index` chapter covers these plugin aspects.

----------------------
Miscellaneous Features
----------------------

*  **Feature version map**: associates version strings with several of the plugin elements. For polling-related elements such as hash filters, the version is used to determine which other peers a peer may invite into polls - the plugin's polling version must be the same across all peers participating in a poll. For metadata extractors and substance checker patterns, the version is used to detect when a change in the plugin may require content to be reprocessed.

*  **Feature URLs**: provides information to allow the Open URL resolver to locate articles, issue ToCs, etc.

*  **Bulk content**: declares that the AUs managed by the plugin are not organized semantically (e.g, they may span publications). Affects metadata extraction.

*  **Archive file types**: specifying the types of archive files (zip, tar, etc.) in this plugin's AUs whose members will be individually accessible. Usually used with bulk content plugins to index metadata for archive members.

*  **AU config user message**: text displayed when a user adds one or more AUs managed by this plugin. Typically used when a site requires crawlers to register with them.

*  **Plugin notes**: commentary displayed along with a plugin's definition in the UI.

-------------------
Minimalistic Plugin
-------------------

A simple plugin will likely have at minimum:

*  Identifying aspects, including configuration parameters.

*  Start URLs, and optionally permission URLs.

*  Crawl rules.

If extracting metadata from the preserved content into the LOCKSS metadata database is desired, the plugin will also need:

*  Metadata extraction elements, including an article iterator.

If the preserved content consists of non-static HTML Web pages, it will likely need:

*  Hash filters.

Use of other aspects is situation-dependent, varying in need based on characteristics and behavior of the preservation target. This guide gives some guidance about when certain components are needed and to what purpose.

------------------------------------------------------
Plugin Compatibility Between LOCKSS 1.x and LOCKSS 2.x
------------------------------------------------------

Conceptually, LOCKSS plugins are the same in the classic LOCKSS system (LOCKSS 1.x) and in the rearchitected LOCKSS system (LOCKSS 2.x), although future features will only be developed for the rearchitected LOCKSS system without being backported to the classic LOCKSS system, as the classic system becomes deprecated.
