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
import os
import sys
from importlib.metadata import version as package_version

sys.path.insert(0, os.path.abspath('../appium'))


# -- Project information -----------------------------------------------------

project = 'Appium Python Client'
copyright = '2020-2026, Appium'
author = 'Appium'

# The full version, including alpha/beta/rc tags
release = package_version('Appium-Python-Client')

language = 'en'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'sphinx.ext.napoleon', 'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_title = 'Appium Python Client'
html_theme_options = {'github_url': 'https://github.com/appium/python-client'}

# The publishing workflow supplies the version served at this URL.
if docs_version := os.getenv('APPIUM_DOCS_VERSION'):
    html_theme_options.update(
        navbar_start=['navbar-logo', 'version-switcher'],
        switcher={'json_url': 'https://appium.github.io/python-client-sphinx/switcher.json', 'version_match': docs_version},
        check_switcher=False,
    )

add_module_names = False

autodoc_default_options = {
    'exclude-members': 'T',
}
