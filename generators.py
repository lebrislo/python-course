# Generators: more memory efficient than lists


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(list(firstn(10)))


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print(list(fibonacci(20)))
