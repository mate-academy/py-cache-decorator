from typing import Callable


# def cache(func) -> Callable:
#     #sort list, just pull answer if already there
#     #else calculate answer and add to list
#     cache = {}
#
#     def cache_wrapper(*args, **kwargs):
#         # Use arguments as the cache key
#         key = args + tuple(kwargs.items())
#         if key in cache:
#             print("Getting from cache")
#             return cache[key]
#
#         print("Calculating new result")
#         result = func(*args, **kwargs)
#         cache[key] = result
#         # return result
#
#     return cache_wrapper
#
#
# @cache
# def long_time_func(a: int, b: int, c: int) -> int:
#     return (a ** b ** c) % (a * c)
#
#
# @cache
# def long_time_func_2(n_tuple: tuple, power: int) -> int:
#     return [number ** power for number in n_tuple]
#
#
# # print(long_time_func(1, 2, 3))
# # print(long_time_func(2, 2, 3))
# # print(long_time_func_2((5, 6, 7), 5))
# # print(long_time_func(1, 2, 3))
# # print(long_time_func_2((5, 6, 7), 10))
# # print(long_time_func_2((5, 6, 7), 10))
# # #
# # # Calculating new result
# # # Calculating new result
# # # Calculating new result
# # # Getting from cache
# # # Calculating new result
# # # Getting from cache
