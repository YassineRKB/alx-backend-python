#!/usr/bin/env python3
"""Module for make_multiplier"""
from typing import Callable
from functools import partial

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""

    multiply: Callable[[float], float] = partial(float.__mul__, multiplier)
    return multiply
