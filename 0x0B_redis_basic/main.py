#!/usr/bin/env python3
from exercise import Cache, replay


if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache)
