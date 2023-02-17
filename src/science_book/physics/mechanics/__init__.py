r"""
.. currentmodule:: science_book.physics.mechanics

======================================================
The Mechanics Module (:mod:`science_book.physics.mechanics`)
======================================================

Constant acceleration
---------------------

.. autosummary::
    :toctree: generated

    calculate_freefall_time
    calculate_constant_acceleration
    calculate_velocity
    calculate_displacement
    calculate_velocity_change_time

.. autosummary::
    :toctree: generated/

    calculate_momentum
    calculate_kinetic_energy
    calculate_potential_energy

"""

from ._constant_acceleration import *
from ._mechanics import *

__all__ = [name for name in dir() if not name.startswith('_')]
