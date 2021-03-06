from typing import Union

import matplotlib.pyplot as plt
import numpy as np

from ..geomesh.vector import Vector
from .basecharge import Charge
from ..geomesh.point import Point


class PointCharge(Charge, Point):
    R = 0.01  # effective radius of the charge for plot

    def __new__(cls, *args):
        self = super(PointCharge, cls).__new__(cls, args[1])
        self.__init__(*args)
        return self

    def __init__(self, *args):
        """
        Construct a charge by specifying its location and magnitude.
        :param loc: the location of the point
        """
        Charge.__init__(self, args[0])

    @property
    def coulomb(self):
        return self.rho

    @coulomb.setter
    def coulomb(self, coulomb: Union[int, float]):
        self.rho = coulomb

    def force_on(self, other: "PointCharge", **kwargs) -> Vector:
        """
        The force, generated by self, on another charge

        :param other: another Charge
        :return: The force between self and other
        """
        vec = other.location - self.location
        distance = vec.norm
        direction = vec.unit

        return self.coulomb * other.coulomb * self.k * direction / (distance ** 2)

    def potential_at(self, r: Vector):
        """
        Electric potential at location x
        :param r: location where the potential evaluated
        :return:
        """
        return self.k * self.coulomb / (self.location - r).norm

    def e_field_intensity(self, r: Vector, **kwargs) -> Vector:
        """
        The electric field intensity at point r due to self which is located at self.loc

        :param r: the point where the e-field intensity is evaluated
        :return: The e-field intensity, located at r, generated by self
        """
        vec = r - self.location
        distance = vec.length
        direction = vec.unit

        intensity = self.k * self.coulomb / (distance ** 2)

        return intensity * direction

    def plot(self):
        """
        plot the charge
        :return:
        """
        color = "b" if self.coulomb < 0 else "r" if self.coulomb > 0 else "k"

        r = 0.1 * (np.sqrt(np.fabs(self.coulomb)) / 2.0 + 1.0)
        fig = plt.figure()
        ax = fig.gca(projection="3d")

        fig, ax = plt.subplots(1, 1)
        circle = plt.Circle(*self.location, r, color=color, zorder=10)
        ax.add_artist(circle)
