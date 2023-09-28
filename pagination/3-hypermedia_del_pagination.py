#!/usr/bin/env python3
import csv
from typing import List, Dict


class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve a page of data from the indexed dataset with hypermedia 
        information.
        """
        assert isinstance(
            index, int) and index >= 0
        assert isinstance(
            page_size, int) and page_size > 0
        dataset = self.indexed_dataset()
        total_items = len(dataset)
        current_index = index if index is not None else 0

        if current_index >= total_items:
            return {
                "index": current_index,
                "next_index": current_index,
                "page_size": page_size,
                "data": [],
            }

        end_index = min(current_index + page_size, total_items)
        data = [dataset.get(i, []) for i in range(current_index, end_index)]
        next_index = end_index

        return {
            "index": current_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
