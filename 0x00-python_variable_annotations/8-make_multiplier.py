#!/usr/bin/env python3
"""Module for make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier. using lamda function"""
    return lambda x: x * multiplier
