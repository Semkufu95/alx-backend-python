#!/usr/bin/env python3
"""
A type annotated function sum_mixed_list that takes a list mxd_lst of
intergers and floats and returns their sum as float
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' sum of a list with any type '''
    return float(sum(mxd_lst))
