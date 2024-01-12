#!/usr/bin/env python3
"""Module for make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""

    def multiply(floaty: float) -> float:
        """Returns the product of floaty and multiplier"""
        result = float(floaty * multiplier)
        return result
    return multiply
