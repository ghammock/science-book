"""
SciGuy
======

An open-source, freely-available package to help everyday users with science
calculations.
"""

import sys

from sciguy.__version__ import __version__


if sys.version_info < (3, 8):
    raise ImportError("The sciguy package does not support Python 3.7 or older.")

__title__ = "sciguy"
__summary__ = "A package to help everyday users with science calculations"
__author__ = "Gary Hammock <ghammock79@gmail.com>"
__copyright__ = "Copyright © 2023, Gary Hammock"

__all__ = ["__author__", "__copyright__", "__summary__", "__title__", "__version__"]
