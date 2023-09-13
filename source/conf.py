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

project = "catlism_oc"
copyright = "2023, Matteo Di Cristofaro"
author = "Matteo Di Cristofaro"

# The full version, including alpha/beta/rc tags
release = "v1.0.1"

master_doc = "index"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

#pygment_style = ["github-dark"]
extensions = [
    "sphinxcontrib.bibtex",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_git",
    "sphinxcontrib.asciinema",
    "sphinxext.remoteliteralinclude",
    "sphinx_favicon",
    "sphinxcontrib.lastupdate",
    #"sphinx_tippy",
]

favicons = [
    "logo-16x16.png",
    "logo-32x32.png",
    "logo.svg",
]

# Set option to enable use of Figures syntax in markdown https://myst-parser.readthedocs.io/en/v0.16.0/syntax/optional.html?highlight=figures#markdown-figures
myst_enable_extensions = ["colon_fence", "strikethrough"]

bibtex_bibfiles = ["../../catlism_bib/bibliography.bib"]
bibtex_reference_style = "author_year"
bibtex_default_style = "alpha"

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

html_css_files = ["custom.css","https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"]
html_js_files = [
    "https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js",
    "main.js",
]
# html_css_files = ['https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css',]
# html_js_files = ['https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js','main.js',]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# Set theme options, drawn from booktheme conf.py
# https://github.com/executablebooks/sphinx-book-theme/blob/master/docs/conf.py
html_theme_options = {
    "repository_url": "https://github.com/catlism/catlism.github.io/",
    "repository_branch": "main",
    "use_sidenotes": True,
    #"use_source_button": True,
    "show_toc_level": 2,
    "show_nav_level": 1,
    # "home_page_in_toc": True,
    "pygment_light_style": "colorful",
    "pygment_dark_style": "monokai",
    "extra_footer": "<div>Built with <a href='https://github.com/executablebooks/sphinx-book-theme'>Sphinx book theme</a></div><div><a href='https://catlism.github.io/privacy.html'>Privacy</a></div>",
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/catlism/catlism.github.io/",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
    ],
}

html_title = "CATLISM | Online Compendium"

html_sidebars = {
    "**": ["navbar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]
}

# Make the website default to dark theme
html_context = {
    "default_mode": "dark"
}

sphinxcontrib_asciinema_defaults = {
    'theme': 'monokai',
    'preload': 1,
    'font-size': '25px',
#    'path': 'path/to/castdir'
}