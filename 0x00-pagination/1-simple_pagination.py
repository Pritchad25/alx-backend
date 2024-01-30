#!/usr/bin/env python3
""" Pagination Module"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """A function that takes two integer arguments page and page_size.
    And returns a tuple of size two containing a start index and an end index
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10):
        """A method that takes two integer arguments page with default value 1
        and page_size with default value 10 if the input arguments are out of
        range for the dataset and returns an empty list.
        """
        assert isinstance(page, int) and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset) or end <= 0:
            return []
        return dataset[start:end]
