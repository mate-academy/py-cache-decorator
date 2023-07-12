def cache(func: None) -> None:
    cached_results = {}

    def wrapper(*args: None) -> None:
        if args in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[args] = result = func(*args)
        return cached_results
