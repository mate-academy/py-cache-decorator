from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_resultados = {}

    def wrapper(*args, **kwargs) -> Any:
        chave = (args, tuple(sorted(kwargs.items())))

        if chave in cache_resultados:
            print("Getting from cache")
            return cache_resultados[chave]

        print("Calculating new result")
        resultado = func(*args, **kwargs)
        cache_resultados[chave] = resultado
        return resultado

    return wrapper
