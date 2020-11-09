"""
Coulomb's Law states that the force F between two point charges Q1 and Q2 is:

(1) Along the line joining them
(2) Directly proportional to the product Q1Q2 of the charges
(3) Inversely proportional to the square of the distance R between them
"""

from typing import Tuple
from typing import Union

import numpy as np

from ..math.vector import Vector


class Charge(object):
    def __init__(self, q: Union[int, float], r: Union[Vector, np.ndarray]):
        """
        Construct a charge by specifying its location and magnitude.
        :param q:
        :param r:
        """
        if len(r) != 3:
            raise ValueError("Location Vector must be 3 element ndarray or an instance of Vector.")

        if isinstance(r, np.ndarray):
            self._loc = Vector(r[0], r[1], r[2])
        else:
            self._loc = r

        self._mag = q

    @property
    def loc(self):
        return self._loc

    @loc.setter
    def loc(self, r: Union[Vector, np.ndarray]):
        self._loc = r

    @property
    def mag(self):
        return self._mag

    @mag.setter
    def mag(self, q: Union[int, float]):
        self._mag = q

    def force_on(self, other: "Charge") -> Tuple[float, Vector, Vector]:
        """
        The force, generated by self, on another charge
        :param other: another Charge
        :return:
        The magnitude of the force and the direction vector defined by two location vectors
        """
        r = (self.loc - other.loc).mag
        k = 9.0E9
        force = k * self.mag * other._mag / (r * r)
        return force, self.loc, other.loc
