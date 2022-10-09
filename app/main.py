def cache(func: any) -> any:
    result_runs = {}

    def wrapper(*args: int) -> any:

        if args not in result_runs.keys():
            run_func = func(*args)
            result_func = {args: run_func}
            result_runs.update(result_func)
            print("Calculating new result")
            return run_func
        else:
            print("Getting from cache")
            return result_runs[args]

    return wrapper
