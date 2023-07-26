import hashlib
import json
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def compute_key(args: tuple, kwargs: dict) -> str:
        key = hashlib.md5(
            json.dumps(args, sort_keys=True).encode("utf-8")
        ).hexdigest()
        key += hashlib.md5(
            json.dumps(kwargs, sort_keys=True).encode("utf-8")
        ).hexdigest()
        return key

    def wrapper(*args, **kwargs) -> Any:
        key = compute_key(args, kwargs)
        if key in cache:
            print("Getting from cache")
            return cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper
