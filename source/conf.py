# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "testph"
copyright = "2023, Matteo Di Cristofaro"
author = "Matteo Di Cristofaro"

# The full version, including alpha/beta/rc tags
release = "1.0.0"

master_doc = "index"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinxcontrib.bibtex", "myst_parser", "sphinx_design", "sphinx_copybutton"]

bibtex_bibfiles = ["bibliography.bib"]
bibtex_reference_style = "author_year"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Set custom CSS and JS files

html_css_files = ["https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css"]
html_js_files = ["https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js", "main.js"]
#html_css_files = ['https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css',]
#html_js_files = ['https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js','main.js',]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Set theme options
html_theme_options = {
    "repository_url": "https://catlism.github.io/",
    "use_sidenotes": True,
    "show_toc_level": 2,
    "show_nav_level": 1,

}

html_title = "CATLISM | Online Companion"
