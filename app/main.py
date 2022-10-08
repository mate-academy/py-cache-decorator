def cache(func) -> None:
    result_runs = {}

    def wrapper(*args):
        run_func = func(*args)
        result_func = {args: run_func}
        if (args, run_func) not in result_runs.items():
            result_runs.update(result_func)
            return print(f"Calculating new result {result_func[args]}")
        else:
            for key in result_runs.keys():
                if key == args:
                    return print(f"Getting from cache {result_runs[key]}")

    return wrapper


@cache
def long_time_func(a, b, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple, power):
    return [number ** power for number in n_tuple]


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
