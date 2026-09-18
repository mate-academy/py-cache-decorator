from typing import Callable


def cache(func):
    results = {}  # cache unique to each decorated function
    
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))  # hashable key
        
        if key in results:
            print("Getting from cache")
            return results[key]
        
        print("Calculating new result")
        result = func(*args, **kwargs)
        results[key] = result
        return result
    
    return wrapper
