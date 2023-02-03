import typing


def cache(func: typing.Callable) -> typing.Callable:
    cache_func = {}

    def inner(*args) -> typing.Any:

        if ((args), (func.__name__)) in cache_func:
            print("Getting from cache")

        else:
            print("Calculating new result")
            complited_func = func(*args)
            key_for_func = ((args), (func.__name__))
            cache_func[key_for_func] = complited_func
        return cache_func[(args), (func.__name__)]

    return inner
