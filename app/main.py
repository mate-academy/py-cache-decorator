def cache(func: callable) -> callable:
    result = {}

    def inner(*args) -> tuple:
        parameters = args
        if parameters in result.keys():
            print("Getting from cache")
            return result[parameters]
        else:
            print("Calculating new result")
            result[parameters] = func(*args)
            return result[parameters]

    return inner


@cache
def long_time_func(num_1: int, num_2: int, num_3: int) -> int:
    return (num_1 ** num_2 ** num_3) % (num_1 * num_3)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
