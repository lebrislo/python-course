# Dictionary: key-value pairs, unordered, mutable

# delete dictionary item
myDict = {"name": "Max", "age": 28, "city": "New York"}
del myDict["name"]

# dictoionary copy
myDict = {"name": "Max", "age": 28, "city": "New York"}
newDict = myDict.copy()
# or newDict = dict(myDict) but not newDict = myDict because it will point to the same dictionary

# dictionary merge
myDict = {"name": "Max", "age": 28}
myDict2 = {"name": "Mary", "age": 27}
myDict.update(myDict2)


# dictionary tuple keys
myTuple = (7, 8)
myDict = {myTuple: 15}
# doesn't work with list because list is mutable
