import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("json/person.json", "w") as file:
    json.dump(person, file, indent=2)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("Max", 27)
userJSON = json.dumps(user.__dict__)
print(userJSON)
