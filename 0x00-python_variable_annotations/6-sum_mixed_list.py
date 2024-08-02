#!/usr/bin/env python3
"""Module contains type-annotated function"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function takes a list of integers and floats and
    returns their sum as a float

    Args:
        mxd_list (list): the list of integers and floats to be summed

    Returns:
        float: the sum of the integers and floats
    """
    return float(sum(mxd_list))
