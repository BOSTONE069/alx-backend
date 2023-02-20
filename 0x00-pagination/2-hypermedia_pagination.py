#!/usr/bin/env python3
"""
    Simple pagination.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
        Returns the range of indexes for a given page.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:  # sourcery skip: identity-comprehension
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Returns a page of data.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.dataset() is None:
            return []

        indexRange = index_range(page, page_size)
        return self.dataset()[indexRange[0]:indexRange[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        # sourcery skip: inline-immediately-returned-variable
        """
            Returns info about dataset.
        """
        data = self.get_page(page, page_size)
        dataSet = self.__dataset
        lenSet = len(dataSet) if dataSet else 0

        totalPages = math.ceil(lenSet / page_size) if dataSet else 0
        page_size = len(data) if data else 0

        prevPage = page - 1 if page > 1 else None
        nextPage = page + 1 if page < totalPages else None

        hyperMedia = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }

        return hyperMedia
