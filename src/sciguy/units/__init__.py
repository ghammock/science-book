"""Physical units of measurement.

sciguy expressly endorses the SI unit system.  In this system, there are seven
standard units of measurement (which are derived using physical constants).  These
seven base units and the quantity they measure are:

1. second (s) - time,
2. meter or metre (m) - length,
3. kilogram (kg) - mass,
4. ampere (A) - electric current,
5. kelvin (K) - temperature,
6. mole (mol) - amount of substance, and
7. candela (cd) - luminous intensity

SI prefixes are provided for indicating order-of-magnitude of a base unit.

This module is heavily influenced by the constants module of SciPy.  Special thanks to
those contributors.
"""


import math

from sciguy.physics.constants import atomic_mass as _atomic_mass
from sciguy.physics.constants import speed_of_light, standard_gravity


__all__ = [
    "Pa",
    "angstrom",
    "arcmin",
    "arcminute",
    "arcsec",
    "arcsecond",
    "astronomical_unit",
    "atm",
    "atmosphere",
    "atomic_mass",
    "atto",
    "au",
    "bar",
    "barrel",
    "bbl",
    "cc",
    "centi",
    "cubic_centimeter",
    "day",
    "deci",
    "degree",
    "degree_fahrenheit",
    "deka",
    "exa",
    "exbi",
    "femto",
    "fermi",
    "fluid_ounce",
    "fluid_ounce_imp",
    "fluid_ounce_us",
    "fluid_oz",
    "foot",
    "fps",
    "g_c",
    "gallon",
    "gallon_imp",
    "gallon_us",
    "gibi",
    "giga",
    "gram",
    "hecto",
    "hour",
    "inch",
    "julian_year",
    "kibi",
    "kilo",
    "kilogram",
    "kmh",
    "lb",
    "lbm",
    "light_year",
    "liter",
    "litre",
    "mebi",
    "mega",
    "meter",
    "metre",
    "metric_ton",
    "micro",
    "micron",
    "mil",
    "mile",
    "milli",
    "minute",
    "mmHg",
    "mph",
    "nano",
    "ounce",
    "oz",
    "pa",
    "parsec",
    "pascal",
    "pebi",
    "peta",
    "pico",
    "pound",
    "psi",
    "quecto",
    "quetta",
    "radian",
    "ronna",
    "ronto",
    "second",
    "slug",
    "stone",
    "tebi",
    "tera",
    "ton",
    "torr",
    "u",
    "week",
    "yard",
    "year",
    "yobi",
    "yocto",
    "yotta",
    "zebi",
    "zepto",
    "zero_celsius",
    "zetta",
]

###########################################################
# SI Prefixes
# See: https://en.wikipedia.org/wiki/Metric_prefix
###########################################################

# N.B.: Using symbols here would clutter the namespace with a lot of single character
# variable names, so don't do it.

quetta = 1e30
ronna = 1e27
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24
ronto = 1e-27
quecto = 1e-30

###########################################################
# Binary prefixes
# See: https://en.wikipedia.org/wiki/Metric_prefix
###########################################################

# N.B. As stated above, using symbols here would clutter the namespace with a lot of
# single character variable names, so don't do it.

kibi = 2**10
mebi = 2**20
gibi = 2**30
tebi = 2**40
pebi = 2**50
exbi = 2**60
zebi = 2**70
yobi = 2**80

###########################################################
# Time units (relative to second)
###########################################################

second = 1
minute = 60.0
hour = 60 * minute
day = 24 * hour
week = 7 * day
year = 365 * day
julian_year = 365.25 * day

###########################################################
# Angular units (relative to radians)
###########################################################

radian = 1
degree = math.pi / 180
arcmin = arcminute = degree / 60
arcsec = arcsecond = arcmin / 60

###########################################################
# Length units (relative to meter)
###########################################################

meter = metre = 1
inch = 0.0254  # US customary unit
foot = 12 * inch  # US customary unit
yard = 3 * foot  # US customary unit
mile = 5280 * foot  # US customary unit
mil = inch / 1000
fermi = 1e-15
angstrom = 1e-10
micron = 1e-6
au = astronomical_unit = 149_597_870_700.0
light_year = julian_year * speed_of_light
parsec = au / arcsec

###########################################################
# Mass units (relative to kilogram)
###########################################################

# US customary conversion factor to make sure |1 lbm| == |1 lbf|
# as used in Newton's second law (F = ma).
g_c = standard_gravity / foot  # lbm⋅ft/lbf⋅s²

kilogram = 1
gram = 1e-3
metric_ton = 1e3
lb = lbm = pound = 0.453_592_37  # avoirdupois
slug = g_c * lbm  # lbf⋅s²/ft ≅ 14.59390 kg
oz = ounce = pound / 16
stone = 14 * pound
ton = 2000 * pound
u = atomic_mass = _atomic_mass

###########################################################
# Pressure units (relative to Pascal)
###########################################################

pa = Pa = pascal = 1
atm = atmosphere = 101_325
bar = 1e5
torr = mmHg = atm / 760
psi = pound * standard_gravity / inch**2

###########################################################
# Volume units (relative to meter³)
###########################################################

liter = litre = 1e-3
cc = cubic_centimeter = 1e-6
gallon = gallon_us = 231 * inch**3  # US
gallon_imp = 4.546_09e-3  # UK/Imperial gallon
fluid_ounce = fluid_ounce_us = fluid_oz = gallon / 128  # US
fluid_ounce_imp = gallon_imp / 160  # UK/Imperial fluid oz.
bbl = barrel = 42 * gallon_us  # Typically used for oil/petroleum products

###########################################################
# Speed units (relative to meter per second or m/s)
###########################################################

kmh = 1000.0 / hour
mph = mile / hour
fps = foot / second

###########################################################
# Temperature units (relative to kelvin)
###########################################################

zero_celsius = 273.15
degree_fahrenheit = 5.0 / 9.0  # Not for linear conversion, used for incremental differences.
