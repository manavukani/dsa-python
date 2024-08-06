# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper


# @timer # this is decorator -> passes through timer before execution
# def example_function(n):
#     time.sleep(n)

# example_function(2)

# ---------------------------------------------------------------
# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ", ".join(str(arg) for arg in args)
#         kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
#         if not args and not kwargs:
#             print(
#                 f"calling: {func.__name__} with 0 args and 0 kwargs"
#             )
#         else:
#             print(
#                 f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}"
#             )
#         return func(*args, **kwargs)

#     return wrapper


# @debug
# def hello():
#     print("hello")


# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}")


# hello()
# greet("chai", greeting="hanji ")



# ---------------------------------------------------------------
# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

import time

def cache(func):
    cache_value = {}
    print("cache values: ",cache_value)
    def wrapper(*args):
        if args in cache_value:
            print("result found in cache values: ", end="")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))
