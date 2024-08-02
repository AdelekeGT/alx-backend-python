#!/usr/bin/env python3
"""Module contains a type-annotated function"""


def concat(str1: str, str2: str) -> str:
    """
    Function takes two strings and returns a concatenated string

    Args:
        str1 (str): first string
        str2 (str): second string

    Returns:
        str: the concatenated string
    """
    return str1 + str2
