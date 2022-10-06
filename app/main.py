def cache(func: callable) -> None:
    """
    This decorator check if arguments were used before.
    If yes, it takes results from stored dictionary, where arguments are keys
    and values are results.
    """
    stored_results = {}

    def wrapper(*args: float) -> float:
        if args in stored_results:
            print("Getting from cache")
            return stored_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            stored_results[args] = result
            return result
    return wrapper
