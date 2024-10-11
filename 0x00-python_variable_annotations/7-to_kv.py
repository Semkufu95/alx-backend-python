#!/usr/bin/env python3
"""
A type annotated function to_kv that takes a string 'k' and an int OR float 'v'
as arguments and returns a single tuple.
The first element of the string is 'k'.
The second element is the square of the int/float v
and should be annotated as float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' funtion returning a tuple of k and v '''
    return k, v ** 2
