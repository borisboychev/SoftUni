from functools import wraps

def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, *kwargs) * times

        return wrapper

    return decorator


""""Test Code"""


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
