from functools import wraps

LOG_TYPES = {'FILE': 'FILE',
             'CMD': 'CMD'}

def log(type=LOG_TYPES['CMD']):
    def print_cmd(text):
        print(text)

    def print_file(text):
        with open('log.txt', 'a') as file:
            file.write(text)
            file.write('\n')

    def decorator(func):
        print_func = print_cmd
        if type == LOG_TYPES['FILE']:
            print_func = print_file

        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            print_func(f'--- Executing --- {func.__name__}() function returning {text}')
            func(*args, **kwargs)

        return wrapper
    return decorator

@log(LOG_TYPES['FILE'])
def say_test():
    return '!TEST!'

say_test()