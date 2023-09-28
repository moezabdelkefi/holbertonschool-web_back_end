import csv
from typing import List
from math import ceil

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int, total_items: int) -> tuple:
        """
        Calculate the start and end indices for a given page and page size.

        Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
        total_items (int): The total number of items in the dataset.

        Returns:
        tuple: A tuple containing the start index (inclusive) and end index (exclusive).
        Returns (None, None) if page or page_size is invalid.
        """
        if page < 1 or page_size <= 0 or total_items <= 0:
            return None, None

        start_index = (page - 1) * page_size
        end_index = min(start_index + page_size, total_items)

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "Page size must be a positive integer."
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_items = len(self.dataset())

        start_index, end_index = self.index_range(page, page_size, total_items)
        if start_index is None or end_index is None:
            return []

        return self.dataset()[start_index:end_index]
    