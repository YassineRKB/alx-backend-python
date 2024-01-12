#!/usr/bin/env python3
"""Module for summing floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats."""
    result = float(sum(input_list))
    return result
