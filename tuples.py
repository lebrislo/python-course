# Tuples: ordered, immutable, allows duplicate elements

# tuple item access
myTuple = ("Max", 28, "Boston")
myTuple[1]

# tuple item count
myTuple = ("a", "p", "p", "l", "e")
myTuple.count("p")

# tuple list conversion
myList = list(myTuple)
myTuple = tuple(myList)

# tuple unpacking
myTuple = ("Max", 28, "Boston")
name, age, city = myTuple

# tuple performance better than list
import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
