# -*- coding: utf-8 -*-

from science_book.physics.constants import g


def calculate_momentum(mass: float, velocity: float) -> float:
    return mass * velocity


def calculate_kinetic_energy(mass: float, velocity: float) -> float:
    return 0.5 * mass * velocity**2


def calculate_potential_energy(mass: float, height: float, gravity: float = g) -> float:
    return mass * height * gravity
