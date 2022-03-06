===========
PDF Filters
===========

.. note::

   This page is under construction.

Increasingly, some content providers generate PDF files dynamically, making each fetch of the same URL slightly different, just like HTML pages in many cases. To allow the nodes in a LOCKSS network to canonicalize PDF files for comparison purposes, the LOCKSS software contains a PDF processing and filtering framework that can be used as building blocks to construct PDF filters [#fnpdfbox]_.

The interface of this framework and general tools are in the ``org.lockss.pdf`` package, with an implementation based on `Apache PDFBox <https://pdfbox.apache.org/>`_ 1.8 in the ``org.lockss.pdf.pdfbox`` package.

*Under construction.*

----

.. rubric:: Footnotes

.. [#fnpdfbox]

   Additionally, there is legacy code based on (pre-Apache) `PDFBox <https://sourceforge.net/projects/pdfbox/>`_ 0.7.3 which is **deprecated**, and an experimental library based on Apache PDFBox 2.0 which is in active development.
