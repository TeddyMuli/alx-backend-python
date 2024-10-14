#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and apply any necessary changes.
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Use mypy to validate the following piece of code and apply any necessary changes.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
