def cache(func: any) -> any:
    result_runs = {}

    def wrapper(*args: int) -> any:

        if args not in result_runs.keys():
            result_runs[args] = func(*args)
            print("Calculating new result")
            return result_runs[args]

        print("Getting from cache")
        return result_runs[args]

    return wrapper
