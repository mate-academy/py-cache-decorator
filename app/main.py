def cache(func: callable) -> Callable:
    results = {}

    def wrapper(*args) -> Any:
        if args in results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
        return results[args]

    return wrapper
