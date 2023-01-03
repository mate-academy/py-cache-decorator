def cache(func: list) -> str:
    add_func = {}

    def wrapps(*args, **kwargs) -> str:
        if args in add_func:
            print("Getting from cache")
        else:
            perfom_func = func(*args, **kwargs)
            add_func[args] = perfom_func
            print("Calculating new result")
        return add_func[args]
    return wrapps
