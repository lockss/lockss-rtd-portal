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


# -- Project information -----------------------------------------------------

project = 'LOCKSS Documentation Portal'
copyright = '2000-2022, LOCKSS Program'
author = 'LOCKSS Program'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # See https://github.com/readthedocs/sphinx_rtd_theme
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs',
]

intersphinx_mapping = {
    'lockss': ('https://lockss.readthedocs.io/en/latest/', None),
    'lockss-manual': ('https://lockss.readthedocs.io/projects/manual/en/latest/', None)
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
# See https://sphinx-rtd-theme.readthedocs.io/
html_theme = 'sphinx_rtd_theme'

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

# See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-prev_next_buttons_location
    'prev_next_buttons_location': 'none',
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-collapse_navigation
    'collapse_navigation': False,
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-navigation_depth
    'navigation_depth': -1,
    # See https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#confval-style_external_links
    'style_external_links': True,
}

# See https://sphinx-tabs.readthedocs.io/
sphinx_tabs_disable_tab_closing = True

# See https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#default-substitutions
# and https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-today_fmt
today_fmt = '%Y-%m-%d'

# See https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-smartquotes
smartquotes = False
