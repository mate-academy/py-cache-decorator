def cache(func: callable) -> callable:
    cached_results = {}

    def inner(*args: any) -> any:
        if args in cached_results.keys():
            print("Getting from cache")
            return cached_results[args]
        print("Calculating new result")
        cached_results.update({args: func(*args)})
        return cached_results[args]

    return inner
