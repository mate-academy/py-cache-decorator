from typing import Any


def cache(func: callable) -> callable:
    _cache = {}

    def some_inputs(*inputs: Any) -> str:
        if func.__name__ not in _cache:
            _cache[func.__name__] = {}
        if inputs not in _cache[func.__name__]:
            _cache[func.__name__][inputs] = func(*inputs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return _cache[func.__name__][inputs]

    return some_inputs
