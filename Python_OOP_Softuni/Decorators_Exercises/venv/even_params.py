def even_parameters(func):
    def wrapper(*args):
        evens = [x for x in args if isinstance(x, int) and x % 2 == 0]
        if len(evens) != len(args):
            return f"Please use only even numbers!"
        return func(*args)
    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
