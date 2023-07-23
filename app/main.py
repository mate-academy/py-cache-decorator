def cache(func: None) -> None:
    func_results = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, frozenset(kwargs.items()))

        if key in func_results:
            print("Getting from cache")
            return func_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_results[key] = result
            return result

    return wrapper
