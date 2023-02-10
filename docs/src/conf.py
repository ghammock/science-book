# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#

import os
import re
import sys
from datetime import date

import sphinx_rtd_theme


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../../src"))

# pyproject_path = pathlib.Path(__file__).parent.parent.parent / "pyproject.toml"
# with open(str(pyproject_path), "rb") as pyproject_file:
#     pyproject = tomli.load(pyproject_file)
# pyproject = pyproject.get("project", {})
#
# release = pyproject.get("version", "0.0.0")

import sciguy  # noqa E402, Need to set the path first.

# -- Project information -----------------------------------------------------
# project = pyproject.get("name", "SciGuy")
# authors_list = cast("list[str]", pyproject.get("authors", []))

project = sciguy.__title__
authors_list = sciguy.__author__

author = ", ".join(authors_list)
release = sciguy.__version__
version = ".".join(release.split(".")[:3])
copyright = f"2023-{date.today().year}, Gary Hammock"  # noqa A001
language = "en"

print(f"{project} Version {version}")

# -- General configuration ---------------------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.imgconverter",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
today_fmt = "%Y-%B-%d"
add_module_names = False
templates_path = ["_templates"]
option_emphasise_placeholders = True
source_suffix = [".rst"]
source_encoding = "utf-8"
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# For the Read the Docs theme,
# :see: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    "sticky_navigation": True,
    "logo_only": False,
    "display_version": True,
    "style_external_links": True,
}

html_context = {
    "display_github": True,
    "github_user": "ghammock",
    "github_repo": "sciguy",
    "github_version": "dev",
    "conf_py_path": "/docs/src/",
}

html_last_updated_fmt = "%Y-%m-%d"
html_copy_source = False
html_show_sourcelink = False

# -- Options for LaTeX output ------------------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
# :see: https://tex.stackexchange.com/a/600712
# :see: https://groups.google.com/g/sphinx-users/c/XnJnQ2N1ACU/m/JYexaQPHAgAJ
latex_documents = [
    (
        "index",
        "sciguy.tex",
        "SciGuy Documentation",
        re.sub(r"\s*,\s*", r" \\and ", author),
        "manual",
        True,
    )
]
latex_engine = "lualatex"
latex_elements = {
    "fontpkg": r"""
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setromanfont{DejaVu Serif}
\setmonofont{Menlo}
""",
    "preamble": r"""
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\usepackage{newunicodechar}
\newfontfamily{\emojifont}{Noto Color Emoji}[Renderer=Harfbuzz]
\newunicodechar{📂}{{\emojifont 📂}}
\newunicodechar{📄}{{\emojifont 📄}}
""",
    "fncychap": r"\usepackage[Bjornstrup]{fncychap}",
    "printindex": r"\footnotesize\raggedright\printindex",
}
latex_toplevel_sectioning = None

# -- Options for the AutoDoc extension ---------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autoclass_content = "both"  # Includes __init__ docstring in class documentation
autodoc_default_options = {
    "members": True,
    "member-order": "alphabetical",
}
autodoc_typehints = "description"  # 'signature' (default), 'description', or 'none'

# -- Options for the AutoSectionLabel extension ------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
autosectionlabel_prefix_document = True

autosummary_generate = True

# -- Options for the ExtLinks extension --------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
extlinks = {
    "pypi": ("https://pypi.org/project/%s", "%s on PyPI"),
}

# -- Options for the InterSphinx extension -----------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- Options for the Napoleon extension --------------------------------------
# :see: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for the todo extension ------------------------------------------
todo_include_todos = True
