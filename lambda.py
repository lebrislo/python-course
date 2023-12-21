# Lambda:

add10 = lambda x: x + 10
print(add10(5))  # 15

mult = lambda x, y: x * y
print(mult(2, 7))  # 14

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D_sorted)  # [(1, 2), (5, -1), (10, 4), (15, 1)]

points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)  # [(5, -1), (15, 1), (1, 2), (10, 4)]

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))  # [2, 4, 6, 8, 10]

# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))  # [2, 4, 6]

# reduce(func, seq)
from functools import reduce

a = [1, 2, 3, 4]
prod_a = reduce(lambda x, y: x * y, a)
print(prod_a)  # 24
