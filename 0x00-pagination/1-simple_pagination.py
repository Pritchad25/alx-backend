#!/usr/bin/env python3
""" Pagination Module"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class that paginates a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Function that returns the Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """ Function that returns the tuple of size two containing
        start index, end index """
        pass
