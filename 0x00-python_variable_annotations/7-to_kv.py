#!/usr/bin/env python3
"""Module contains type-annotated function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function takes a sring and an int OR float as arguments and
    returns a tuple

    Args:
        k (str): the string
        v (int OR float): the int OR float

    Returns:
        tuple: the string and the square of the int OR float
    """
    return (k, float(v ** 2))
