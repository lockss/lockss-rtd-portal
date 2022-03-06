==========
Crawl Pool
==========

Plugin Key
   ``plugin_fetch_rate_limiter_source``

Plugin Value Type
   :ref:`string-value`

Description
   A specification for how AUs are split into crawl pools. Only one new content crawl from a given crawl pool can happen at once. In the default crawl pool scheme, there is one crawl pool per plugin, but this plugin key can be used to define a new behavior.

   The possible values are:

   *  ``au``: Each AU has its own crawl pool.

   *  ``plugin``: The pool name is the :ref:`Plugin Identifier`.

   *  :samp:`key:{str}`: The pool name is the string :samp:`{str}`.

   *  :samp:`host:{urlparamkey}`: The pool name is the string ``host:`` followed by the value of the AU's parameter named :samp:`{urlparamkey}`. If there is no such parameter, or if the parameter is not of type :ref:`URL`, the default crawl pool scheme applies.

   *  :samp:`title_attribute:{auattrkey}` and :samp:`title_attribute:{auattrkey}:{dflt}`: The pool name is the string ``attr:`` is the value of the AU's attribute named :samp:`{auattrkey}`. When the attribute is unset, if the longer form is used then use :samp:`{dflt}` as the value instead; otherwise the default crawl pool scheme applies.
