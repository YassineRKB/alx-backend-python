#!/usr/bin/env python3
"""Module for element length"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their length"""
    return [(i, len(i)) for i in lst]
