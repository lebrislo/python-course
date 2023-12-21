# Lists : ordered, mutable, allows duplicate elements

# sort without changing the original list
myList = [4, -9, 5, 1, -3, 10]
newList = sorted(myList)
print(myList)
print(newList)

# dupicate list
myList = [0] * 5
print(myList)

# list slicing
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [start:end:step]
newList = myList[1:6:2]
print(newList)

# list copy
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = myList[:]
# or newList = myList.copy() but not newList = myList because it will point to the same list
print(newList)

# reverse list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = myList[::-1]  # reverse list or newList = myList.reverse()

# list comprehension
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newList = [i * i for i in myList]  # square each element in the list
