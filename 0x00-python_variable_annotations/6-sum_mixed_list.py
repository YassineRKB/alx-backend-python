#!/usr/bin/env python3
"""Module for summing floats and integers"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats and integers."""
    result = float(sum(mxd_lst))
    return result
