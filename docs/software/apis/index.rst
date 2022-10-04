=========
REST APIs
=========

The API of each LOCKSS REST service is described in a Swagger 2.0 specification,
which can be found relative to the root of the component's Git repository in the file
:file:`src/main/resources/swagger/swagger.yaml`. The specification can be used as input into another tool, for instance Swagger Codegen,
to produce clients and server stubs in a variety of languages and frameworks, and documentation. This guide contains HTML renderings of each specification generated with the
`sphinxcontrib.openapi <https://github.com/sphinx-contrib/openapi>`_ Sphinx extension.

.. toctree::

   LOCKSS Repository Service REST API <laaws-repository-service.html#http://>
   LOCKSS Configuration Service REST API <laaws-configuration-service#http://>
   LOCKSS Poller Service REST API <laaws-poller-service#http://>
   LOCKSS Metadata Extraction Service REST API <laaws-metadata-extraction-service#http://>
   LOCKSS Metadata Service REST API <laaws-metadata-service#http://>
