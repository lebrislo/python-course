# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import (
    accumulate,
    combinations,
    count,
    cycle,
    groupby,
    permutations,
    product,
    repeat,
)

# product: cartesian product of input iterables
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# permutations: all possible orderings of an input iterable
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1),(3, 1, 2), (3, 2, 1)]

# combinations: all possible combinations of an input iterable
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4),(3, 4)]

# accumulate: cumulative sum of an input iterable
a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))  # [1, 3, 6, 10]

# groupby: makes an iterator that returns consecutive keys and groups from the iterable
a = [1, 2, 3, 4]
group = groupby(a, lambda x: x < 3)
for key, value in group:
    print(key, list(value))  # True [1, 2] False [3, 4]


# cycle: cycle through an iterable
a = [1, 2, 3]
for i in cycle(a):
    print(i)  # 1 2 3 1 2 3 1 2 3 ...

# repeat: repeat an element
for i in repeat(1, 4):
    print(i)  # 1 1 1 1
