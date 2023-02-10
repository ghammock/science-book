r"""
.. currentmodule:: sciguy.physics

==========================================
The Physics Module (:mod:`sciguy.physics`)
==========================================

This module is used for physics calculations.  It includes physical constants (the
:mod:`~sciguy.physics.constants` module) and functions to calculate phenomena such as
freefall, projectile motion, etc.

.. toctree::
    :caption: Submodules
    :maxdepth: 1
    :name: physics_module_contents

    constants
    mechanics
"""

from sciguy.physics import constants, mechanics

__all__ = [
    "constants",
    "mechanics",
]
