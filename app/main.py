def cache(func: list) -> str:
    add_func = []

    def wrapps(*args, **kwargs) -> str:
        perfom_func = func(*args, **kwargs)
        if perfom_func not in add_func:
            print("Calculating new result")
            add_func.append(perfom_func)
        else:
            print("Getting from cache")
        return perfom_func
    return wrapps
