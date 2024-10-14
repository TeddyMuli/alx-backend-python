#!/usr/bin/env python3
"""
Given the parameters and the return values, add type annotations to the function
Hint: look into TypeVar
"""
from typing import TypeVar, Mapping, Optional, Any



T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """
    Given the parameters and the return values, add type annotations to the function
    Hint: look into TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
