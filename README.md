# Cache decorator
- Read the [guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md)  before start

You have a big array with data. You have to run a long runtime function
with this data. Data can be repeated.
To not re-run function with repeatable data, it will be good to store
results of completed runs.

У вас великий масив з даними. Вам потрібно запустити довгу функцію середовища виконання з цими даними. Дані можна повторювати. Щоб не запускати функцію повторно з повторюваними даними, було б добре зберігати результати завершених запусків.



Write decorator `cache` that stores results of completed runs with
different arguments, number of arguments can be also different.
If decorated function runs with repeating arguments it should return stored
result instead of calling function again. Decorator `cache` creating for 
decorating only functions that take **immutable** arguments.

Напишіть кеш декоратора, який зберігатиме результати завершених запусків з різними аргументами, кількість аргументів також може бути різною. Якщо декорована функція виконується з повторюваними аргументами, вона повинна повертати збережений результат, а не викликати функцію повторно. Кеш декоратора створюється лише для декорування функцій, які приймають незмінні аргументи.



Also note, that decorator `cache` should work correctly with few decorated
functions simultaneously and correctly return for every function separately.

Також зверніть увагу, що кеш декоратора повинен коректно працювати з кількома декорованими функціями одночасно та коректно повертати значення для кожної функції окремо.



Also `cache` should print `Getting from cache` when returns stored value and 
`Calculating new result` when run function with new arguments.

Також кеш повинен виводити: Отримання з кешу, коли повертається збережене значення, та Обчислення нового результату, коли функція виконується з новими аргументами.


Example:
```python
@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)

# Calculating new result 
# Calculating new result 
# Calculating new result 
# Getting from cache 
# Calculating new result 
# Getting from cache
```

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
