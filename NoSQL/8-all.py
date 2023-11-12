#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection. Returns an empty list if no documents are found.
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
