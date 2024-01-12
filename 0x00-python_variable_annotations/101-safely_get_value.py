#!/usr/bin/env python3
"""Module for type annotations"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Def = Union[T, None]
Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Returns the value safely"""
    if key not in dct:
        return default
    return dct[key]
