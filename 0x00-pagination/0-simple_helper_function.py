#!/usr/bin/env python3
""" Pagination Module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ This function returns tuple of size two containing
    a start index and an end index """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
