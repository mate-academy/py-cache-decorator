from typing import Callable, Any


def cache(func: Callable) -> Callable:
    slownik = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in slownik:
            print("Getting from cache")
            return slownik[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            slownik[key] = result
            return result

    return wrapper


@cache
def add(apples: int, bananas: int) -> int:
    return apples + bananas


print(add(1, 2))  # Calculating new result
print(add(1, 2))  # Getting from cache
print(add(2, 3))  # Calculating new result
