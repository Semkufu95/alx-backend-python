#!/usr/bin/env python3
"""
A type annotated function sum_list that takes a list input_list of floats
as argument and returns theirs sum as floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' Adds a list of floats '''
    return float(sum(input_list))
