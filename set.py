# Set: unordered, mutable, no duplicates

# create set
mySet = {1, 2, 3, 4, 5, 5, 5}  # duplicate 5 will be ignored

# set remove
mySet.remove(4)  # throws an error if item not found
mySet.discard(5)  # doesn't throw an error if item not found

# set pop
mySet = {1, 2, 3, 4, 5}
mySet.pop()  # remove random item from set

# set union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
u = odds.union(evens)  # combine two sets

# set intersection
u = odds.intersection(evens)  # returns empty set

setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3, 8, 9}

# set difference
u = setA.difference(setB)  # returns 4 and 5

# set symmetric difference
u = setA.symmetric_difference(setB)  # returns 4, 5, 8, 9

# set subset
setC = {1, 2, 3}
setD = {1, 2, 3, 4, 5}
setC.issubset(setD)  # returns True

# set disjoint
setC = {1, 2, 3}
setD = {4, 5, 6}
setC.isdisjoint(setD)  # returns True

# frozen set
a = frozenset([1, 2, 3, 4])  # immutable set
