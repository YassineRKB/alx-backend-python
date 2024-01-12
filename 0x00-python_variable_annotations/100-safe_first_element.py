#!/usr/bin/env python3
"""Module for duck typing an iterable object"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list"""
    if not lst:
        return None
    return lst[0]
