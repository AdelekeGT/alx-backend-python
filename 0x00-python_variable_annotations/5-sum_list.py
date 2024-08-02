#!/usr/bin/env python3
"""Module contains a type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function takes a list of floats and returns their sum as a float

    Args:
        input_list (list): the list of floats to be summed

    Returns:
        float: the sum of the floats
    """
    return float(sum(input_list))
