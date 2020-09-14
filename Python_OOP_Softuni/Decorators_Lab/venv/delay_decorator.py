import time

class deley_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        time.sleep(2)
        result = self.func(*args, **kwargs)
        return result


@deley_decorator
def say_hello():
    print('Hello')

say_hello()