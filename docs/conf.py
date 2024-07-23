# Copyright (c) 2000-2024, Board of Trustees of Leland Stanford Jr. University
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# See https://github.com/readthedocs/sphinx_rtd_theme
import sphinx_rtd_theme

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

######## See https://about.readthedocs.com/blog/2024/07/addons-by-default/
import os
# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

# -- Project information -----------------------------------------------------

project = 'LOCKSS Documentation Portal'
copyright = '2000-2024, LOCKSS Program'
author = 'LOCKSS Program'

# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_title
html_title = project

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # See https://www.sphinx-doc.org/en/master/usage/extensions/index.html
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',

    # See https://sphinx-rtd-theme.readthedocs.io/
    'sphinx_rtd_theme',

    # See https://github.com/sphinx-contrib/email
    'sphinxcontrib.email',

    # See https://sphinx-design.readthedocs.io/
    'sphinx_design',

    # See https://github.com/missinglinkelectronics/sphinxcontrib-globalsubs
    'sphinxcontrib.globalsubs',
]

intersphinx_mapping = {
    'lockss': ('https://docs.lockss.org/en/latest/', None),
    'lockss-manual': ('https://docs.lockss.org/projects/manual/en/latest/', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
# See https://sphinx_rtd_theme.readthedocs.io/
#html_theme = 'sphinx_rtd_theme'
# See https://insipid-sphinx-theme.readthedocs.io/
html_theme = 'insipid'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# See https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
html_css_files = [
    'css/lockss.css',
]

# See https://github.com/readthedocs/readthedocs.org/issues/2569
master_doc = 'index'

# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_logo = 'images/lockss-docs-128x128.png'

# See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-prev_next_buttons_location
    'prev_next_buttons_location': 'both',
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-collapse_navigation
    #'collapse_navigation': False,
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-navigation_depth
    #'navigation_depth': -1,
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-style_external_links
    #'style_external_links': True,
    # See https://insipid-sphinx-theme.readthedocs.io/en/latest/configuration.html#theme-option-breadcrumbs
    'breadcrumbs': True,
    # See https://insipid-sphinx-theme.readthedocs.io/en/latest/configuration.html#theme-option-strip_section_numbers
    'strip_section_numbers': False,
}

# See https://insipid-sphinx-theme.readthedocs.io/en/0.4.2/configuration.html#theme-option-left_buttons
html_context = {
    'display_github': False,
}

# See https://insipid-sphinx-theme.readthedocs.io/en/0.4.2/configuration.html#confval-html_show_sourcelink
html_show_sourcelink = False

# See https://insipid-sphinx-theme.readthedocs.io/en/latest/configuration.html#configuration
html_permalinks_icon = '#'

# See https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#default-substitutions
# and https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-today_fmt
today_fmt = '%Y-%m-%d'

# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-smartquotes
smartquotes = False

# See https://insipid-sphinx-theme.readthedocs.io/en/0.4.2/configuration.html#example
html_use_index = False
html_domain_indices = False

html_extra_path = ['dev/apis/EXTRA']

