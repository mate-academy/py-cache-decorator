def cache(func: any) -> any:
    result_runs = {}

    def wrapper(*args: int) -> any:
        run_func = func(*args)
        result_func = {args: run_func}
        if (args, run_func) not in result_runs.items():
            result_runs.update(result_func)
            print("Calculating new result")
        else:
            for key in result_runs.keys():
                if key == args:
                    print("Getting from cache")
        return run_func
    return wrapper
