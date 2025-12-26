from typing import Callable, Any


def cache(func: Callable) -> Callable:
    # This dictionary is local to the 'func' being decorated,
    # ensuring isolation between different decorated functions.
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Create a unique, hashable key representing the specific call.
        # We include kwargs by converting the items to a sorted tuple.
        cache_key = (args, tuple(sorted(kwargs.items())))

        if cache_key in storage:
            print("Getting from cache")
            return storage[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[cache_key] = result
        return result

    return wrapper
