#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls to a method in the database"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__name__
        count_key = f"{key}_count"
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Returns the callable that will be called"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Returns the method wrapped by this method call"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


class Cache:
    def __init__(self):
        """Construct a new Cache instance with the given arguments"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data in the given database
        and return it as a string"""
        key = str(uuid.uuid4())
        if isinstance(data, (str, bytes)):
            self._redis.set(key, data)
        elif isinstance(data, (int, float)):
            self._redis.set(key, str(data))
        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """ Get the value of the given key from the given function"""
        data = self._redis.get(key)
        if data is not None:
            if fn is not None:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> str:
        """ Returns the string representation
        of the given key in the given format"""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Returns the value of the given key in the given"""
        return self.get(key, fn=int)


def replay(c: Cache):
    """Retrieving lists"""
    r = c._redis
    key = c.store.__qualname__
    inputs_key = f"{key}:inputs"
    outputs_key = f"{key}:outputs"

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    call_count = len(inputs)

    print(f"{key} was called {call_count} times:")

    for input_data, output_data in zip(inputs, outputs):
        input_args = eval(input_data.decode("utf-8"))
        output_key = output_data.decode("utf-8")
        print(f"{key}{input_args} -> {output_key}")
