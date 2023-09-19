def cache(func):
    store_result = {}

    def inner(*args):
        tuple_parames = args
        if tuple_parames in store_result.keys():
            print("Getting from cache")
            return store_result[tuple_parames]
        else:
            print("Calculating new result")
            store_result[tuple_parames] = func(*args)
            return store_result[tuple_parames]

    return inner


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
