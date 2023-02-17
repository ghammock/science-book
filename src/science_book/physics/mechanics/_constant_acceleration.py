"""Functions for calculating properties of objects undergoing constant acceleration

References
----------
- D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, 6th ed.
  New York, NY: Wiley, 2001. ISBN: 9780471320005
"""

import math

from science_book.physics.constants import g


def calculate_freefall_time(initial_height: float, gravity: float = g) -> float:
    r"""Calculates the time an object will spend in gravitational freefall.

    This function calculates the time an object spends in a uniform gravitational
    field with no air resistance or other external forces (i.e. no terminal velocity).

    Parameters
    ----------
    initial_height : float
        The height above the surface (in meters) from which the object is dropped.

    gravity : float, default = :data:`science_book.physics.constants.g`
        The gravitational acceleration toward the surface in m/s²

    Returns
    -------
    float
        The time, in seconds, that the object spends in gravitational freefall.

    Notes
    -----
    This corresponds to the classical Newtonian physics model where a body's position
    as a function of time (under constant acceleration) can be modeled as:

    .. math::
        \begin{equation}\label{x(t)}
            x(t) = x_0 + u_0 t + \frac{1}{2} a t^2
        \end{equation}

    Under freefall, the initial velocity, :math:`u_0`, is zero and the final position
    (relative to the initial height) is also zero (i.e.
    :math:`{\Delta}x = x_0 - x_{final} = x_0`).  The acceleration is a downward vector
    due only to gravity, meaning that :math:`a = -g`.  So the characteristic equation
    becomes:

    .. math::
        \begin{equation}\label{free_fall}
            x(t) = x_0 - \frac{1}{2} g t^2 = 0
        \end{equation}

    Rearranging, yields :math:`t = \pm \sqrt{\frac{2x_0}{g}}`.  The negative value is
    nonsensical, so it is ignored.

    Examples
    --------
    >>> # Standard Earth gravity
    >>> round(calculate_freefall_time(20), 4)
    2.0196

    >>> # Using gravity of Mars
    >>> round(calculate_freefall_time(20, gravity=3.72076), 4)
    3.2788
    """

    if initial_height < 0:
        raise ValueError("The initial height must be a positive value.")
    if gravity == 0 or gravity < 0:
        raise ValueError("The gravitational acceleration must be a positive value.")

    return math.sqrt(2.0 * initial_height / gravity)


def calculate_constant_acceleration(initial_velocity: float, final_velocity: float, displacement: float) -> float:
    r"""Calculates the acceleration required to change velocity over a given displacement

    This function calculates the acceleration required for a change in velocity
    (initial velocity - final velocity) over a specified displacement (i.e. the
    distance over which the velocity change occurs.)  The acceleration may be positive
    (representing an increase in velocity) or negative (representing a decrease in
    velocity).

    Parameters
    ----------
    initial_velocity : float
        The velocity at the start of the displacement interval in m/s.
    final_velocity : float
        The velocity at the end of the displacement interval in m/s.
    displacement : float
        The distance (in meters) over which the velocity change occurs.

    Returns
    -------
    float
        The magnitude of the acceleration (in m/s²) required for the velocity change
        over the specified distance.

    Notes
    -----
    An object's position as a function of time and under constant acceleration is:

    .. math::
        \begin{equation}
            x(t) = x_0 + u_0 t + \frac{1}{2} a t^2
        \end{equation}

    Recognizing that velocity under constant acceleration as a function of time is:

    .. math::
        \begin{equation}
            u(t) = u_0 + at
        \end{equation}

    Letting :math:`u(t) = u_{final}` and rearranging for :math:`t` yields:

    .. math::
        \begin{equation}
            t = \frac{u_{final} - u_0}{a}
        \end{equation}

    Letting :math:`x(t) = x_{final}` and substituting for :math:`t` yields:

    .. math::
        \begin{equation}
            x_{final} - x_0 =
                    u_0 \left( \frac{u_{final} - u_0}{a} \right)
                    + \frac{1}{2} a {\left( \frac{u_{final} - u_0}{a} \right)}^2
        \end{equation}

    Solving for :math:`a` and substituting :math:`\Delta x = x_{final} - x_0` results
    in the simplified equation:

    .. math::
        \begin{equation}\label{constant_acceleration}
            a = \frac{u_{final}^2 - u_0^2}{2 \Delta x}
        \end{equation}

    Examples
    --------

    Suppose a vehicle is travelling at 90 kph (25 m/s).  The driver brakes for 100 m to
    a speed of 54 kph (15 m/s).  The vehicle experiences a constant acceleration of
    -2 m/s².

    >>> calculate_constant_acceleration(25, 15, 100)
    -2.0

    The escape velocity of Earth is 11.2 km/s.  Over what distance must a spacecraft
    traverse assuming a constant 3g (approx. 29.4 m/s²) acceleration?

    >>> guess = 2.133e6  # meters
    >>> acc = calculate_constant_acceleration(0, 11_200, guess)
    >>> round(acc, 2)
    29.4

    References
    ----------
    - D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, 6th ed.
      New York, NY: Wiley, 2001. ISBN: 9780471320005
    """
    return (final_velocity**2 - initial_velocity**2) / (2 * displacement)


def calculate_velocity(initial_velocity: float, constant_acceleration: float, duration: float) -> float:
    r"""Calculates the velocity of an object under constant acceleration

    Parameters
    ----------
    initial_velocity : float
        The velocity at the start of the duration interval in m/s.
    constant_acceleration : float
        The acceleration, in m/s², constantly applied over the duration.
    duration : float
        The duration, in seconds, over which the acceleration is applied.

    Returns
    -------
    float
        The velocity of the object at the end of the time duration.

    Notes
    -----
    An object's velocity as a function of time and under constant acceleration is:

    .. math::
        \begin{equation}
            u(t) = u_0 + a t
        \end{equation}

    Examples
    --------

    Calculate the final velocity of an object with an initial velocity of 10 m/s
    undergoing a 2 m/s² constant acceleration over 15 seconds.

    >>> calculate_velocity(10, 2, 15)
    40

    References
    ----------
    - D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, 6th ed.
      New York, NY: Wiley, 2001. ISBN: 9780471320005
    """
    return initial_velocity + (constant_acceleration * duration)


def calculate_displacement(initial_velocity: float, constant_acceleration: float, duration: float) -> float:
    r"""Calculates the amount of displacement (travel) of an object under constant acceleration

    Parameters
    ----------
    initial_velocity : float
        The velocity at the start of the duration interval in m/s.
    constant_acceleration : float
        The acceleration, in m/s², constantly applied over the duration.
    duration : float
        The duration, in seconds, over which the acceleration is applied.

    Returns
    -------
    float
        The distance the object has traveled (:math:`\Delta x`) at the end of the
        time duration.

    Notes
    -----
    An object's displacement (:math:`\Delta x`) as a function of time and under constant
    acceleration is:

    .. math::
        \begin{equation}
            x(t) = x_0 + u_0 t + \frac{1}{2} a t^2
        \end{equation}

    Rearranging and letting :math:`\Delta x \equiv x(t) - x_0` yields

    .. math::
        \begin{equation}
            \Delta x = u_0 t + \frac{1}{2} a t^2
        \end{equation}

    Examples
    --------

    An object with an initial velocity of 10 m/s undergoing a 2 m/s² constant
    acceleration over 15 seconds travels 375 meters (and is travelling at 40 m/s at
    the end of 15 seconds).

    >>> calculate_displacement(10, 2, 15)
    375.0
    >>>
    >>> calculate_velocity(10, 2, 15)
    40

    References
    ----------
    - D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, 6th ed.
      New York, NY: Wiley, 2001. ISBN: 9780471320005
    """
    return (initial_velocity * duration) + (0.5 * constant_acceleration * duration**2)


def calculate_velocity_change_time(velocity_change: float, acceleration: float) -> float:
    r"""Calculates the time an object takes to change velocity

    Parameters
    ----------
    velocity_change : float
        The velocity change, :math:`\Delta u`, over the interval in m/s.
    acceleration : float
        The constant acceleration responsible for the velocity change in m/s².

    Returns
    -------
    float
        The time, in seconds, it takes to change velocity under the specified
        acceleration.

    Notes
    -----
    An object's velocity under constant acceleration as a function of time is:

    .. math::
        \begin{equation}
            u(t) = u_0 + at
        \end{equation}

    Letting :math:`u(t) = u_{final}` and rearranging for :math:`t` yields:

    .. math::
        \begin{equation}
            \begin{split}
                t &= \frac{u_{final} - u_0}{a} \\
                  &= \frac{\Delta u}{a}
            \end{split}
        \end{equation}

    Examples
    --------

    Suppose a vehicle is travelling at 90 kph (25 m/s).  The driver brakes to a speed
    of 54 kph (15 m/s) under a constant acceleration of -2 m/s².

    >>> calculate_velocity_change_time(10, -2)
    5.0

    References
    ----------
    - D. Halliday, R. Resnick, and J. Walker, *Fundamentals of Physics*, 6th ed.
      New York, NY: Wiley, 2001. ISBN: 9780471320005
    """
    return math.fabs(velocity_change) / math.fabs(acceleration)
