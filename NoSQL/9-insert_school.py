#!/usr/bin/env python3
"""
Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: Keyword arguments representing the document fields and values

    Returns:
        The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
