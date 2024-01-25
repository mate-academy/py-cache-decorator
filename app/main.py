from typing import Callable, Any


from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_values = []
    result_values = []
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_values:
            print("Getting from cache")
            for i in range(len(cache_values)):
                if key == cache_values[i]:
                    return result_values[i]

        else:
            result = func(*args, **kwargs)
            cache_values.append(key)
            print("Calculating new result")
            result_values.append(result)
            return result

    return wrapper
