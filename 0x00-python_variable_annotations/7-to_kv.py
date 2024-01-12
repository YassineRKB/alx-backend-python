#!/usr/bin/env python3
"""Module for type annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of complex type"""
    result = (k, float(v**2))
    return result
