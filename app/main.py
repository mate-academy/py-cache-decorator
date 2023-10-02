def cache(func: callable) -> callable:
    store_result = {}

    def inner(*args) -> tuple:
        tuple_parames = args
        if tuple_parames in store_result.keys():
            print("Getting from cache")
            return store_result[tuple_parames]
        print("Calculating new result")
        store_result[tuple_parames] = func(*args)
        return store_result[tuple_parames]

    return inner
