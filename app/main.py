from typing import Callable


def cache(func: Callable) -> Callable:
    slownik = {}
    def wrapper(*args, **kwargs):
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
def add(a, b):
    return a + b

print(add(1, 2))  # Calculating new result
print(add(1, 2))  # Getting from cache
print(add(2, 3))  # Calculating new result










