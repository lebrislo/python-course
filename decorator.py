# Function decorator
import functools


def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def print_name():
    print("Max")


print_name = start_end_decorator(print_name)
print_name()


def add_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@add_decorator
def add5(x):
    return x + 5


res = add5(10)
print(res)
print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(3)
def greet(name):
    print(f"Hello {name}")


greet("World")


# Class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()  # This is executed 1 times
say_hello()  # This is executed 2 times

# use cases: debug decorator, timer decorator, check arguments decorator
