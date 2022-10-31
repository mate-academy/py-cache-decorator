def cache(func: callable) -> callable:
    cache_memory = {}

    def wrapper(*args) -> float:
        if args in cache_memory:
            print("Getting from cache")
            return cache_memory[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_memory[args] = result

        return result
    return wrapper
