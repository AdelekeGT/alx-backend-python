#!/usr/bin/env python3
"""Module contains type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function takes a float as argument and returns a function
    that multiplies a float by the multiplier

    Args:
        multiplier (float): the float to multiply by

    Returns:
        function: the function that multiplies a float by the multiplier
    """
    def multiplier_fn(n: float) -> float:
        return n * multiplier
    return multiplier_fn
