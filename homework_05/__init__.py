"""
Домашнее задание: Пишем классы и плодим наследников
"""

from homework_05.base import Vehicle
from car import Car
from engine import Engine
from exceptions import NotEnoughFuel, LowFuelError, CargoOverload
from plane import Plane
__all__ = [
    "base",
    "car",
    "engine",
    "exceptions",
    "plane",
]