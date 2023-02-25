import typing


def cache(func: typing.Callable) -> typing.Callable:
    stored_values = {}

    def wrapper(*args) -> typing.Any:
        if args in stored_values:
            print("Getting from cache")
        else:
            stored_values[args] = func(*args)
            print("Calculating new result")
        return stored_values[args]
    return wrapper
