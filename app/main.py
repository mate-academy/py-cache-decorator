from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    resultados = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        chave = (args, tuple(sorted(kwargs.items())))

        if chave in resultados:
            print("Getting from cache")
            return resultados[chave]

        print("Calculating new result")
        resultado = func(*args, **kwargs)
        resultados[chave] = resultado

        return resultado

    return wrapper


@cache
def long_time_func(
    base: int,
    expoente: int,
    potencia: int
) -> int:
    return (base ** expoente ** potencia) % (base * potencia)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    numeros = []

    for number in n_tuple:
        numeros.append(number ** power)

    return numeros


long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)
